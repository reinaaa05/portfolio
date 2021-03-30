from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Video, Comment
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import CommentCreateForm, VideoSearchForm


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

class VideoDetail(generic.DetailView):
    model = Video

class VideoCreate(generic.CreateView):
    model = Video
    fields = '__all__'
    success_url = reverse_lazy('videos:video_list')

class VideoUpdate(generic.UpdateView):
    model = Video
    fields = '__all__'
    success_url = reverse_lazy('videos:video_list')

class VideoDelete(generic.DeleteView):
    model = Video
    success_url = reverse_lazy('videos:video_list')

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
