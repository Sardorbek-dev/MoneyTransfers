from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponseRedirect


from .models import Transfer, TransferComment
from .filters import TransferFilter
from .forms import TransferCommentForm


# Create your views here.

def LikeView(request, pk):
    transfer = get_object_or_404(Transfer, id=request.POST.get('transfer_id'))  # Attrs of Form ==> id=request.POST.get('article_id') FROTNEND--> article_id = name="article_id"
    liked = False
    if transfer.likes.filter(id=request.user.id).exists():
        transfer.likes.remove(request.user)
        liked = False
    else:
        transfer.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(transfer.get_absolute_url()) # reverse('article_list', args=[str(pk)]) args=[str(pk)]) --> primary key of the article, which by user liked




class TransferListView(ListView):
    paginate_by = 5
    model = Transfer
    template_name = 'transfer_list.html'
    # sorting by ID
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TransferFilter(self.request.GET, queryset=self.get_queryset())
        filtered_transfers = context['filter']
        paginator = Paginator(filtered_transfers.qs, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            filtered_transfers = paginator.page(page)
        except PageNotAnInteger:
            filtered_transfers = paginator.page(1)
        except EmptyPage:
            filtered_transfers = paginator.page(paginator.num_pages)
        context['filtered_transfers'] = filtered_transfers
        return context

def transfer_detail_comment(request, pk):

    transfer = Transfer.objects.get(id=pk)
    transfer_comments = TransferComment.objects.filter(transfer=transfer, reply=None)
    transferComment = TransferComment.objects.all()
    p = Paginator(transferComment, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    # Comment posted
    if request.method == 'POST':
        transfer_comment_form = TransferCommentForm(request.POST or None)
        if transfer_comment_form.is_valid():
            transfer_comment = request.POST.get('transfer_comment')
            reply_id = request.POST.get('comment_id') #Form ==> id=request.POST.get('comment_id') FROTNEND--> comment_id = name="comment_id"
            comment_qs = None
            if reply_id:
                comment_qs = TransferComment.objects.get(id=reply_id)
                new_transfer_comment = TransferComment.objects.create(transfer=transfer, author=request.user, transfer_comment=transfer_comment, reply=comment_qs)
            else:
                new_transfer_comment = TransferComment.objects.create(transfer=transfer, author=request.user, transfer_comment=transfer_comment, reply=comment_qs)

            new_transfer_comment.save()

            return HttpResponseRedirect(transfer.get_absolute_url()) #redirect to article detail page

    else:
        transfer_comment_form = TransferCommentForm()

    context = {
        'transfer': transfer,
        'transfer_comment_form': transfer_comment_form,
        'page_obj': page_obj,
    }

    return render(request, 'transfer_detail.html', context)



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
    form = TransferCommentForm()

    def get_context_data(self, *args, **kwargs):
        context = super(TransferDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Transfer, id=self.kwargs['pk'])  # for loop all Articles with pk key, if doesnt exit, get 404
        total_likes = stuff.total_likes()  # from model 'total_likes' function
        # print('stuff:', stuff)

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        context['form'] = self.form
        return context


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
