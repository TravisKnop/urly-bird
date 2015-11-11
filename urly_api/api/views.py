from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import View, ListView, CreateView
from api.models import UrlRecord, UrlCounter


@property
def get_long_url(long_url):
    print(long_url)
    return long_url


class UrlListView(ListView):
    model = UrlRecord


class UrlRedirectView(View):

    def get(self, request, short_url):
        url = UrlRecord.objects.get(short_url=short_url)
        UrlCounter.objects.create(record=url)
        return HttpResponseRedirect(url.long_url)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


