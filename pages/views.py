from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ContactUsForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contact.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser



