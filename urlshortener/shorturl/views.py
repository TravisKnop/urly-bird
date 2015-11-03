from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View, ListView, CreateView
from shorturl.models import UrlRecord, UrlCounter

class UrlListView(ListView):
    model = UrlRecord
    template_name = "base.html"

class UrlRedirectView(View):

    def get(self, request, short_url):
        url = UrlRecord.objects.get(short_url=short_url)
        UrlCounter.objects.create(record=url)
        return HttpResponseRedirect(url.long_url)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"