from django.contrib import admin
from .models import Logentry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Logentry)
class LogentryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_field = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
