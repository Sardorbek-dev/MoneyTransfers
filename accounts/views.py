from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfilePageForm, EditProfilePage
from articles.models import Profile
from .models import CustomUser
from transfers.models import TransferComment

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
    success_url = reverse_lazy('article_list')
    template_name = 'registration/edit_account.html'

    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()  # fetch all categoris from backend
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        page_user_comment = TransferComment.objects.all
        print('Here:', page_user_comment)


        context['page_user'] = page_user
        context['page_user_comment'] = page_user_comment

        return context

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('article_list')
    form_class = EditProfilePage

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

