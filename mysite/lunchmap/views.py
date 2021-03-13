from django.views import generic
from .models import Category, Shop

class IndexView(generic.ListView):
    model = Shop

class DetailView(generic.DetailView):
    model = Shop