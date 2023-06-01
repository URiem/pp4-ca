from django.contrib import admin
from .models import Logentry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Logentry)
class LogentryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'year', 'privacy')
    search_field = ['title', 'description']
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'year')
    summernote_fields = ('description')


# @admin.register(Country)
# class CountryAdmin(SummernoteModelAdmin):

#     list_display = ('title', 'slug')
#     search_field = ['title']
    # prepopulated_fields = {'slug': ('title',)}
    # list_filter = ('status', 'year')
    # summernote_fields = ('description')
