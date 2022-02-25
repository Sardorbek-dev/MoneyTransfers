from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Transfer
from .filters import TransferFilter

# Create your views here.
class TransferListView(ListView):
    model = Transfer
    template_name = 'transfer_list.html'
    # sorting by ID
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TransferFilter(self.request.GET, queryset=self.get_queryset())
        return context

class TransferCreateView(CreateView):
    model = Transfer
    template_name = 'transfer_new.html'
    fields = ('title', 'description','pul_yuboriladigan_davlatni_tanlang', 'transfer_pul_birligini_tanlang', 'transfer_turi', 'qaysi_shahar_yoki_viloyat_yubormoqchisiz', 'price',)

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
    fields = ['title', 'description', 'pul_yuboriladigan_davlatni_tanlang', 'transfer_pul_birligini_tanlang', 'transfer_turi', 'qaysi_shahar_yoki_viloyat_yubormoqchisiz', 'price',]
    template_name = 'transfer_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def get_success_url(self):
    #     messages.success(
    #         self.request, 'Your post has been updated successfully.')
    #     return reverse_lazy('transfer_list')


class TransferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transfer
    template_name = 'transfer_delete.html'
    success_url = reverse_lazy('transfer_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
