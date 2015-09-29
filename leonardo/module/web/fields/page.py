from django_select2.fields import AutoModelSelect2Field

from django_select2.widgets import *

from ..models import PageColorScheme, PageTheme, Page


class Field(AutoModelSelect2Field):
    empty_values = [u'']


class PageSelectField(Field):
    queryset = Page.objects
    search_fields = ['title__icontains', ]

    def label_from_instance(self, obj):
        """
        Coerces ``value`` to a Python data type.
        """
        return obj.tree_label


class PageColorSchemeSelectField(Field):
    queryset = PageColorScheme.objects
    search_fields = ['label__icontains', 'name__icontains']


class PageThemeSelectField(Field):
    queryset = PageTheme.objects
    search_fields = ['label__icontains', 'name__icontains']
