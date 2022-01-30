from django.db import models

from django.db.models.signals import pre_save


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,related_name='parent_category', null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    