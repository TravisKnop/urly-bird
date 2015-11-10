from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from api.shortener import shortener


class Profile(models.Model):
    user = models.OneToOneField(User)
    credit_card = models.CharField(max_length=20, blank=True)
    weight = models.FloatField(null=True)

    def __str__(self):
        return "{}'s profile".format(self.user.username)


@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    instance = kwargs.get("instance")
    created = kwargs.get("created")
    if created:
        Profile.objects.create(user=instance)


class UrlRecord(models.Model):
    long_url = models.TextField()
    short_url = models.CharField(max_length=100, blank=True)

    @property
    def hits(self):
        return self.urlcounter_set.all().count()


class UrlCounter(models.Model):
    record = models.ForeignKey(UrlRecord)


@receiver(pre_save, sender=UrlRecord)
def url_record_post_save(sender, **kwargs):
    instance = kwargs.get("instance")
    instance.short_url = shortener(instance.long_url)