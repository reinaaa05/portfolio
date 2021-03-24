from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentCreateForm
from .models import Post, Comment,Category, Tag

class PostList(generic.ListView):
    model = Post
    ordering = '-created_at'

class PostCategoryList(generic.ListView):
    model = Post
    ordering = '-created_at'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category_list'] = Category.objects.all()
    #     context['tag_list'] = Tag.objects.all()
    #     return context

class PostTagList(generic.ListView):
    model = Post
    ordering = '-created_at'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return super().get_queryset().filter(tags=tag)


class PostDetail(generic.DetailView):
    model = Post

class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('blog:post_detail', pk=post_pk)