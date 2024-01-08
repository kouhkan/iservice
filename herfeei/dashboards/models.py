from django.db import models

from herfeei.common.models import BaseModel


class Rule(BaseModel):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=128)
    slug = models.SlugField(max_length=32, unique=True, allow_unicode=True, db_index=True)
    details = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FaqCategory(BaseModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, unique=True, db_index=True, allow_unicode=True)
    icon = models.CharField(max_length=512, null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ Category"
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.title


class Faq(BaseModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, unique=True, db_index=True, allow_unicode=True)
    details = models.TextField()
    category = models.ForeignKey(FaqCategory, on_delete=models.CASCADE, related_name="faq")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Contact(BaseModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, db_index=True, unique=True, allow_unicode=True)
    icon = models.ImageField(upload_to="icons/contacts/", null=True, blank=True)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.title
