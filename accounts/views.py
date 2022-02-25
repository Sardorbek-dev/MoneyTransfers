from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from articles.models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.
class UserEditForm(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('article_list')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()  # fetch all categoris from backend
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])


        context['page_user'] = page_user

        return context

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('article_list')
    fields = ('bio', 'telegram_url', 'instagram_url', 'facebook_url')

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile_page.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)