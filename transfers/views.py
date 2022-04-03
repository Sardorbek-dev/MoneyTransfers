from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core import serializers
import json



from .models import Transfer, TransferComment, get_uz_strings, get_ger_strings, get_usa_strings
from .filters import TransferFilter
from .forms import TransferCommentForm, TransferForm
from articles.models import Profile
from accounts.models import CustomUser

# Create your views here.
def like(request, pk):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        transfer = get_object_or_404(Transfer, id=id)
        if transfer.likes.filter(id=request.user.id).exists():
            transfer.likes.remove(request.user)
            transfer.like_count -= 1
            result = transfer.like_count
            transfer.save()
        else:
            transfer.likes.add(request.user)
            transfer.like_count += 1
            result = transfer.like_count
            transfer.save()

        return JsonResponse({'result': result, })

        return HttpResponseRedirect(transfer.get_absolute_url())

def status_change(request, pk):
    print( 'transfer: ',pk)
    if request.POST.get('action') == 'post':
        result = ''
        id = request.POST.get('postId')
        print( 'transfer2: ',id)

        transfer = get_object_or_404(Transfer, id=id)

        if transfer.status_transfer:
            transfer.status_transfer = False
            result = transfer.status_transfer
            transfer.save()
        else:
            transfer.status_transfer = True
            result = transfer.status_transfer
            transfer.save()

        return JsonResponse({'result': result, })

        return HttpResponseRedirect(transfer.get_absolute_url())


# def LikeView(request, pk):
#     transfer = get_object_or_404(Transfer, id=request.POST.get('transfer_id'))  # Attrs of Form ==> id=request.POST.get('article_id') FROTNEND--> article_id = name="article_id"
#     liked = False
#     if transfer.likes.filter(id=request.user.id).exists():
#         transfer.likes.remove(request.user)
#         liked = False
#     else:
#         transfer.likes.add(request.user)
#         liked = True

#     return HttpResponseRedirect(transfer.get_absolute_url()) # reverse('article_list', args=[str(pk)]) args=[str(pk)]) --> primary key of the article, which by user liked

# def ReputationView(request, pk):
#     transfer = get_object_or_404(Transfer, id=request.POST.get('transfer_id'))  # Attrs of Form ==> id=request.POST.get('article_id') FROTNEND--> article_id = name="article_id"
#     reputation = False

#     if transfer.reputations.filter(id=request.user.id).exists():
#         transfer.reputations.remove(request.user)
#         reputation = False

#     else:
#         transfer.reputations.add(request.user)
#         reputation = True
#     return HttpResponseRedirect(reverse('transfer_list')) # reverse('article_list', args=[str(pk)]) args=[str(pk)]) --> primary key of the article, which by user liked

def ReputationView(request, pk):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postId'))
        transfer = get_object_or_404(Transfer, id=id)
        if transfer.reputations.filter(id=request.user.id).exists():
            transfer.reputations.remove(request.user)
            transfer.reputation_count -= 1
            result = transfer.reputation_count
            transfer.save()
        else:
            transfer.reputations.add(request.user)
            transfer.reputation_count += 1
            result = transfer.reputation_count
            transfer.save()

        return JsonResponse({'result': result, })

        return HttpResponseRedirect(transfer.get_absolute_url())


def TransferViewView(request, pk):

    transfer = get_object_or_404(Transfer, id=request.POST.get('transfer_id'))  # Attrs of Form ==> id=request.POST.get('article_id') FROTNEND--> article_id = name="article_id"
    # Field 'id' expected a number but got <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x00000186219C2770>>. Debug fixed!!!
    if request.user.id is None:
        transfer_view = False
    else:
        transfer.views.add(request.user)
        transfer_view = True

    return HttpResponseRedirect(transfer.get_absolute_url()) # reverse('article_list', args=[str(pk)]) args=[str(pk)]) --> primary key of the article, which by user liked

class TransferListView(ListView):
    paginate_by = 5
    model = Transfer
    template_name = 'transfer_list.html'
    # sorting by ID
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TransferFilter(self.request.GET, queryset=self.get_queryset()) # or => Transfer.objects.all()
        context['filter_status_active'] = Transfer.objects.filter(status_transfer=True)
        context['search_users'] = serializers.serialize("json", Profile.objects.all(), fields=["user", "user_image"], use_natural_foreign_keys=True)
        context['profiles'] = Profile.objects.all()
        context['users'] = CustomUser.objects.all()
        filtered_transfers = context['filter']

        if len(filtered_transfers.qs) > 10:
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
        else:
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

            return HttpResponseRedirect(transfer.get_absolute_url()) #redirect to transfer detail page

    else:
        transfer_comment_form = TransferCommentForm()

    context = {
        'transfer': transfer,
        'transfer_comment_form': transfer_comment_form,
        'page_obj': page_obj,
    }

    return render(request, 'transfer_detail.html', context)



class TransferCreateView(CreateView):
    form_class = TransferForm
    template_name = 'transfer_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        uz_strings = get_uz_strings()
        ger_strings = get_ger_strings()
        usa_strings = get_usa_strings()

        json_uz_strings = json.dumps(uz_strings)
        json_ger_strings = json.dumps(ger_strings)
        json_usa_strings = json.dumps(usa_strings)

        context['json_uz_strings'] = json_uz_strings
        context['json_ger_strings'] = json_ger_strings
        context['json_usa_strings'] = json_usa_strings
        return context

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Your transfer has been successfully created.')
        return reverse_lazy('transfer_list')

class TransferDetailView(DetailView):
    model = Transfer
    template_name = 'transfer_detail.html'
    form = TransferCommentForm()

    def get_context_data(self, *args, **kwargs):
        context = super(TransferDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Transfer, id=self.kwargs['pk'])
        #print('stuffT:', stuff.author_id)# for loop all Articles with pk key, if doesnt exit, get 404
        total_likes = stuff.total_likes()  # from model 'total_likes' function
        total_reputations = stuff.total_reputations() # Delete!!!!!!!!
        total_views = stuff.total_views()
        page_user_transfer = Transfer.objects.filter(author_id=stuff.author_id)
        page_user_comment = TransferComment.objects.filter(author_id=stuff.author_id)

        liked = False
        reputation = False
        view = False


        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        if stuff.reputations.filter(id=self.request.user.id).exists():
            reputation = True

        if stuff.views.filter(id=self.request.user.id).exists():
            view = True

        # Users who have liked transfers of current user
        if page_user_transfer.count() != 0:
            userLike = []
            userReputation = []
            for eachTransfer in page_user_transfer:

                for user in eachTransfer.likes.all():
                    userLike.append(user)

                for user in eachTransfer.reputations.all():
                    userReputation.append(user)

            context['userLike'] = userLike
            context['userReputation'] = userReputation
            context['page_user_transfer'] = page_user_transfer
        else:
            context['userLike'] = 0
            context['userReputation'] = 0

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


        context['profile'] = Profile.objects.all()
        context['page_user_transfer'] = page_user_transfer
        context['page_user_comment'] = page_user_comment
        context['total_views'] = total_views
        context['liked'] = liked
        context['reputation'] = reputation
        context['view'] = view

        context['form'] = self.form
        return context

class TransferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transfer
    fields = ['title', 'description', 'location', 'moneyCurrency', 'transferArt', 'whichLocation', 'price',]
    template_name = 'transfer_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        update_uz_strings = get_uz_strings()
        update_ger_strings = get_ger_strings()
        update_usa_strings = get_usa_strings()

        update_json_uz_strings = json.dumps(update_uz_strings)
        update_json_ger_strings = json.dumps(update_ger_strings)
        update_json_usa_strings = json.dumps(update_usa_strings)

        context['update_json_uz_strings'] = update_json_uz_strings
        context['update_json_ger_strings'] = update_json_ger_strings
        context['update_json_usa_strings'] = update_json_usa_strings
        return context

    def get_success_url(self):
        messages.success(self.request, 'Your transfer has been successfully updated.')
        transfer_id = self.kwargs['pk']
        return reverse_lazy('transfer_detail', kwargs={'pk': transfer_id})

class TransferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transfer
    template_name = 'transfer_delete.html'
    success_url = reverse_lazy('transfer_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Your transfer has been successfully deleted.')
        return reverse_lazy('transfer_list')
