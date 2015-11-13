from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from hashlib import md5
import datetime

from django.views.generic import View, ListView, CreateView, DetailView
from api.models import UrlRecord, UrlCounter, UrlMaker, shortener


# url(r'^create_url/$', login_required(UrlCreationView.as_view()), name="url_create"),
class UrlCreationView(CreateView):
    model = UrlMaker
    fields = ["long_url", "author", "time_made", "short_url"]
    success_url = "/"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.user = self.request.user
        return super().form_valid(form)


# url(r'^$', UserUrlListView.as_view(), name="url_list"),
class UserUrlListView(ListView):
    model = UrlRecord
    template_name = "index.html"


class UrlDetailView(DetailView):
    model = UrlMaker


class UrlRedirectView(View):

    def get(self, request, short_url):
        url = UrlRecord.objects.get(short_url=short_url)
        UrlCounter.objects.create(record=url)
        return HttpResponseRedirect(url.long_url)


# url(r'^create_user/', UserCreateView.as_view(), name="create_user"),
class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/accounts/login"

