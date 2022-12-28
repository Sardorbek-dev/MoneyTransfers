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
        
        # Users who have liked transfers of current user
        if page_user_transfer.count() != 0:
            userLike = []
            userReputation = []
            for eachTransfer in page_user_transfer:

                for user in eachTransfer.likes.all():
                    userLike.append(user)

                for user in eachTransfer.reputations.all():
                    userReputation.append(user)
            
            userLike_counted = {}
            for i in userLike:
                userLike_counted[i] = userLike.count(i)

            userReputation_counted = {}
            for i in userReputation:
                userReputation_counted[i] = userReputation.count(i)

            like_counter = 0
            for user, total_likes in userLike_counted.items():
                like_counter = like_counter + total_likes

            reputation_counter = 0
            for user, total_reputations in userReputation_counted.items():
                reputation_counter = reputation_counter + total_reputations

            context['userLike'] = userLike_counted
            context['userReputation'] = userReputation_counted
            context['like_counter_total'] = like_counter
            context['reputation_counter_total'] = reputation_counter
        else:
            context['userLike'] = 0
            context['userLike_test_total'] = 0
            context['like_counter_total'] = 0
            context['reputation_counter_total'] = 0

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

