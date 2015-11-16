from datetime import datetime
import hashlib
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class UrlMaker(models.Model):
    author = models.ForeignKey(User)
    long_url = models.URLField()
    short_url = models.CharField(max_length=100)
    time_made = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    instance = kwargs.get("instance")
    created = kwargs.get("created")
    if created:
        Profile.objects.create(user=instance)


class UrlRecord(models.Model):
    long_url = models.TextField()
    short_url = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User)
    time_made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.long_url

    @property
    def hits(self):
        return self.urlcounter_set.all().count()


class UrlCounter(models.Model):
    record = models.ForeignKey(UrlRecord)

    def __str__(self):
        return self.long_url


def shortener(long_url):
    input_data = "{}{}".format(long_url, datetime.now().strftime("%f"))
    url_code = bytes(input_data, encoding="ascii")
    m = hashlib.md5()
    m.update(url_code)
    short_url_code = m.hexdigest()
    short_url = "tk" + short_url_code[:8]
    return short_url


@receiver(pre_save, sender=UrlRecord)
def url_record_pre_save(sender, **kwargs):
    instance = kwargs.get("instance")
    instance.short_url = shortener(instance.long_url)

