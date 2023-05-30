from django.shortcuts import render
from django.views import generic
from .models import Logentry
# from django.views.generic import TemplateView


# class StartPage(TemplateView):
#     """
#     A view that only loads the home page to begin with
#     """
#     template_name = "index.html"


class LogentryList(generic.ListView):
    model = Logentry
    queryset = Logentry.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
