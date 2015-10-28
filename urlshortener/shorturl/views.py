from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from shorturl.models import Homepage


class HomeView(TemplateView):
r    template_name = "base.html"
