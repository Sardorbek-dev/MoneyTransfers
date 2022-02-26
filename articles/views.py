from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import AddArticleForm
from django.http import HttpResponseRedirect

from .models import Article, Comment, Category
from .forms import CommentForm

# Create your views here.

def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))  # Attrs of Form ==> id=request.POST.get('article_id') FROTNEND--> article_id = name="article_id"
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(article.get_absolute_url()) # reverse('article_list', args=[str(pk)]) args=[str(pk)]) --> primary key of the article, which by user liked


def article_detail_comment(request, pk):

    article = Article.objects.get(id=pk)
    comments = Comment.objects.filter(article=article, reply=None).order_by('-id')

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            reply_id = request.POST.get('comment_id') #Form ==> id=request.POST.get('comment_id') FROTNEND--> comment_id = name="comment_id"
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
                new_comment = Comment.objects.create(article=article, author=request.user, comment=comment, reply=comment_qs)
            else:
                new_comment = Comment.objects.create(article=article, author=request.user, comment=comment, reply=comment_qs)

            new_comment.save()

            return HttpResponseRedirect(article.get_absolute_url()) #redirect to article detail page

    else:
        comment_form = CommentForm()

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'article_detail.html', context)


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() # fetch all categoris from backend
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)

        # # Total likes
        # stuff = Article.objects.all() # for loop alle Article with pk key, if doesnt exit, get 404
        #
        # print('stuff:', )
        # # for itemm in staff:
        #     print('Here', itemm)
        #total_likes = staff.total_likes() # from model 'total_likes' function
        # context['total_likes'] = total_likes

        context['cat_menu'] = cat_menu

        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()  # fetch all categoris from backend
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_posts = Article.objects.filter(category=cats.replace('-', ' ')) # ==> category is the same name in our Article model name "category = models.CharField(max_length=200, default='coding')"
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    form_class = AddArticleForm
    template_name = 'article_new.html'
    # fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    #form_class = AddArticleForm
    template_name = 'category_new.html'
    fields = ('name',)
    # fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # to know which user create a category

    def test_func(self):
        return self.request.user.is_superuser

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    form = CommentForm()

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        # Total likes
        stuff = get_object_or_404(Article, id=self.kwargs['pk'])  # for loop all Articles with pk key, if doesnt exit, get 404
        total_likes = stuff.total_likes()  # from model 'total_likes' function
        #print('stuff:', stuff)

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        context['form'] = self.form
        return context


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'summary', 'body', 'photo',]
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
