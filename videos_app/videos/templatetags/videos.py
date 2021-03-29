from videos.forms import VideoSearchForm
from django import template

register = template.Library()

@register.inclusion_tag('videos/search_form.html')
def create_search_form(request):
    form = VideoSearchForm()
    return {'form': form}

    