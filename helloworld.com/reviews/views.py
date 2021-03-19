from django.shortcuts import render, get_object_or_404,redirect
from .models import Review

def review_list(request):
    context = {
      'review_list': Review.objects.all().order_by('-created_at'),
    }
    return render(request, 'reviews/review_list.html', context)

def review_detail(request,pk):
    context = {
      'review': get_object_or_404(Review,pk=pk)
    }
    return render(request, 'reviews/review_detail.html', context)

def review_create(request):
    form = ReviewCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_list')

    context = {
      'form': form
    }
    return render(request, 'reviews/review_form.html', context)


def review_create(request):
    return render(request, 'reviews/review_form.html')


def review_create_send(request):
  name = request.POST.get('store_name')
  print('送信されたデータ→ {}' .format(name))
  return redirect('review_list')