from django.shortcuts import render, get_object_or_404,redirect
from .models import Review
from .forms import ReviewCreateForm
from django.views import generic
from django.urls import reverse_lazy

class ReviewList(generic.ListView):
    model = Review
# def ReviewList(generic.ListView):
    # context = {
    #   'review_list': Review.objects.all().order_by('-created_at'),
    # }
    # return render(request, 'reviews/review_list.html', context)

class ReviewDetail(generic.DetailView):
    model = Review
# def review_detail(request,pk):
#     context = {
#       'review': get_object_or_404(Review,pk=pk)
#     }
#     return render(request, 'reviews/review_detail.html', context)

class ReviewCreate(generic.CreateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')
# def review_create(request):
#     form = ReviewCreateForm(request.POST or None)
        
#     #入力内容に問題がない場合は、保存してリダイレクト
#     if request.method == 'POST' and  form.is_valid():
#         form.save()
#         return redirect('reviews:review_list')
            
#     #問題があれば、入力画面のテンプレートファイルに
#     #エラーメッセージ入りのformオブジェクトを渡す
#     context = {
#         'form': form,
#     }
#     return render(request, 'reviews/review_form.html', context)

class ReviewUpdate(generic.UpdateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')
# def review_update(request,pk):
#     review = get_object_or_404(Review, pk=pk)
#     form = ReviewCreateForm(request.POST or None, instance=review)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('reviews:review_list')

#     context = {
#         'form': form
#     }
#     return render(request, 'reviews/review_form.html', context)

class ReviewDelete(generic.DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list]')

# def review_delete(request,pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.method == 'POST':
#         form.delete()
#         return redirect('reviews:review_list')

#     context = {
#         'review': review
#     }
#     return render(request, 'reviews/review_confirm_delete.html', context)



        

