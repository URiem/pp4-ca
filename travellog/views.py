from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


class StartPage(TemplateView):
    """
    A view that only loads the home page to begin with
    """
    template_name = "index.html"
