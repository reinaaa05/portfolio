from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Video, Comment,Category
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import CommentCreateForm, VideoSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class VideoList(generic.ListView):
    model = Video
    paginate_by = 9
    def get_queryset(self):
        queryset = super().get_queryset()
        form = VideoSearchForm(self.request.GET or None)
        if form.is_valid():
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                queryset = queryset.filter(Q(title__icontains=key_word) | Q(title__icontains=key_word))
            
        return queryset

class VideoCategoryList(generic.ListView):
    model = Video

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category)

class VideoDetail(generic.DetailView):
    model = Video

class VideoCreate(LoginRequiredMixin,generic.CreateView):
    model = Video
    fields = ['title','thumbnail', 'file', 'category'] #'__all__'
    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super(VideoCreate,self).form_valid(form)
    success_url = reverse_lazy('videos:video_list')

class VideoUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Video
    fields = ['title','thumbnail', 'file', 'category'] #'__all__'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.writer != self.request.user:
            raise PermissionDenied('権限がありません')
        return super(VideoUpdate, self).dispatch(request, *args, **kwargs)
    success_url = reverse_lazy('videos:video_list')

class VideoDelete(LoginRequiredMixin,generic.DeleteView):
    model = Video
    success_url = reverse_lazy('videos:video_list')


class CommentCreate(LoginRequiredMixin,generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        video_pk = self.kwargs['pk']
        video = get_object_or_404(Video, pk=video_pk)
        comment = form.save(commit=False)
        comment.target = video
        comment.save()
        return redirect('videos:video_detail', pk=video_pk)

class UserDetail(generic.DetailView):
    model = Video
    template_name = 'videos/user_detail.html'