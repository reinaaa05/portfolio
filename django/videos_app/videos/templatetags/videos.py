from videos.forms import VideoSearchForm
from django import template
from videos.models import Category

register = template.Library()

@register.inclusion_tag('videos/search_form.html')
def create_search_form(request):
    form = VideoSearchForm(request.GET or None)
    return {'form': form}

@register.inclusion_tag('videos/category_list.html')
def create_category_list():
    return {
        'category_list' : Category.objects.all(),
    }


@register.simple_tag
def url_replace(request, field, value):
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()