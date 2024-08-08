from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Response


class AdFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='ad_time',
        lookup_expr='gte',
        widget=DateTimeInput(
            format='%y-%m-%dT',
            attrs={'type': 'datetime-local'},
        ))

    class Meta:
        model = Post
        fields = {'title': ['icontains']}


class UserResponseFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='response_time',
        lookup_expr='gte',
        widget=DateTimeInput(
            format='%y-%m-%dT',
            attrs={'type': 'datetime-local'},
        ))

    class Meta:
        model = Response
        fields = {'ad'}

    def __init__(self, *args, **kwargs):
        super(UserResponseFilter, self).__init__(*args, **kwargs)
        self.filters['ad'].queryset = Post.objects.filter(author__id=kwargs['request'])