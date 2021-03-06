# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

import os


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class GearPost(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='gearimages/', default='/ION/static/images/imgnotfound.png')
    price = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        os.rmdir(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(Document, self).delete(*args, **kwargs)


class PhotoPost(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='IOPimages/')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=GearPost)
def delete_gearpost(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo.delete(False)

@receiver(pre_delete, sender=PhotoPost)
def delete_photopost(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo.delete(False)
