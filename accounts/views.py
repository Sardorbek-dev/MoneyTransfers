from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfilePageForm, EditProfilePage, ProfileFeedbackForm
from articles.models import Profile, ProfileFeedback
from django.http import HttpResponseRedirect, JsonResponse
from .models import CustomUser
from transfers.models import Transfer, TransferComment

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class AccountShowView(ListView):
    model = CustomUser
    template_name = 'registration/account_page.html'

class UserEditForm(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('transfer_list')
    template_name = 'registration/edit_account.html'

    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    form = ProfileFeedbackForm

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()  # fetch all categoris from backend
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        page_user_comment = TransferComment.objects.filter(author_id=page_user.id)
        page_user_transfer = Transfer.objects.filter(author_id=page_user.id)
        context['transfers_status_active'] = Transfer.objects.filter(status_transfer=True, author_id=self.kwargs['pk'])

        #Users who have liked transfers of current user
        if page_user_transfer.count() != 0:
            userLike = {}
            for eachTransfer in page_user_transfer:
                for user in eachTransfer.likes.all():
                    userLike[user.id] = user.first_name
            context['userLike'] = userLike
        else:
            context['userLike'] = 0

        # count all likes
        likes_array = []
        for eachtransfer in page_user_transfer:
            if eachtransfer.total_likes:
                likes_array.append(eachtransfer.total_likes())
                total_likes = 0
                for i in range(0, len(likes_array)):
                    total_likes = total_likes + likes_array[i];
                    total_likes
                context['total_likes'] = total_likes
            else:
                context['total_likes'] = 0
                print('False')

        # count all reputation
        reputations_array = []
        for eachtransfer in page_user_transfer:
            if eachtransfer.total_reputations:
                reputations_array.append(eachtransfer.total_reputations())
                total_reputations = 0
                for i in range(0, len(reputations_array)):
                    total_reputations = total_reputations + reputations_array[i];
                    total_reputations
                context['total_reputations'] = total_reputations
            else:
                context['total_reputations'] = 0

        context['page_user'] = page_user
        context['page_user_comment'] = page_user_comment
        context['page_user_transfer'] = page_user_transfer
        context['form'] = self.form
        return context

def send_feedback(request, pk):

    profile = Profile.objects.get(id=pk)
    transfer_contents = ProfileFeedback.objects.filter(profile=profile)
    #profileFeedbackContenProfileFeedbackt = ProfileFeedback.objects.all()
    # p = Paginator(ProfileFeedback, 5)
    # page_number = request.GET.get('page')
    # page_obj = p.get_page(page_number)

    # Comment posted
    if request.method == 'POST':
        profile_feedback_content_form = ProfileFeedbackForm(request.POST or None)
        if profile_feedback_content_form.is_valid():
            profile_feedback_content = request.POST.get('content')
            print('profile_feedback_content', profile_feedback_content)
            new_profile_feedback_content = ProfileFeedback.objects.create(profile=profile, author=request.user, content=profile_feedback_content)
            new_profile_feedback_content.save()

            return HttpResponseRedirect(reverse_lazy('user_profile', kwargs={'pk': pk})) #redirect to user profile page
    else:
        profile_feedback_content_form = ProfileFeedbackForm()

    context = {
        'profile': profile,
        'profile_feedback_content_form': profile_feedback_content_form,
    }

    return render(request, 'user_profile.html', context)

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('transfer_list')
    form_class = EditProfilePage

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

