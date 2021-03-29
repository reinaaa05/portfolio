from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Video, Comment
from django.urls import reverse_lazy
from .forms import CommentCreateForm


class VideoList(generic.ListView):
    model = Video

class VideoCreate(generic.CreateView):
    model = Video
    fields = '__all__'
    success_url = reverse_lazy('videos:video_list')

class VideoDetail(generic.DetailView):
    model = Video

class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        video_pk = self.kwargs['pk']
        video = get_object_or_404(Video, pk=video_pk)
        comment = form.save(commit=False)
        comment.target = video
        comment.save()
        return redirect('videos:video_detail', pk=video_pk)