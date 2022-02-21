from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Transfer

# Create your views here.
class TransferListView(ListView):
    model = Transfer
    template_name = 'transfer_list.html'

class TransferCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Transfer
    template_name = 'transfer_new.html'
    fields = ('title', 'description', 'price', 'photo', 'author',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class TransferDetailView(DetailView):
    model = Transfer
    template_name = 'transfer_detail.html'

class TransferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transfer
    fields = ['title', 'description', 'price', 'photo', 'author',]
    template_name = 'transfer_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TransferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transfer
    template_name = 'transfer_delete.html'
    success_url = reverse_lazy('transfer_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
