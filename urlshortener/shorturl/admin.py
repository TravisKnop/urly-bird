from django.contrib import admin

# Register your models here.
from shorturl.models import UrlRecord, UrlCounter, Profile

admin.site.register(UrlRecord)
admin.site.register(UrlCounter)
admin.site.register(Profile)