import django_filters

from django_filters import CharFilter
  
from . models import *

class BlogPostFilter(django_filters.FilterSet):
	title = CharFilter(field_name='title', lookup_expr='icontains')
	content = CharFilter(field_name='content', lookup_expr='icontains')
	class Meta:
		model = BlogPost
		fields = '__all__'
		exclude = ['likes', 'related_image', 'date_added']