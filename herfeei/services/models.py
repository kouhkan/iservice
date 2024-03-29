from django.contrib.auth import get_user_model
from django.db import models
from treebeard.mp_tree import MP_Node

from herfeei.common.models import BaseModel


class Province(BaseModel):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64,
                            unique=True,
                            db_index=True,
                            allow_unicode=True)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64,
                            unique=True,
                            db_index=True,
                            allow_unicode=True)
    province = models.ForeignKey(Province,
                                 on_delete=models.CASCADE,
                                 related_name="city")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class ServiceCategory(MP_Node, BaseModel):

    class ServiceCategoryStatus(models.TextChoices):
        ENABLE = "ENABLE"
        DISABLE = "DISABLE"

    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128,
                            db_index=True,
                            unique=True,
                            allow_unicode=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to="categories/image/",
                              null=True,
                              blank=True)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=10,
                              choices=ServiceCategoryStatus.choices,
                              default=ServiceCategoryStatus.ENABLE)

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.title


class ServiceItem(BaseModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32,
                            db_index=True,
                            unique=True,
                            allow_unicode=True)
    start_range = models.PositiveIntegerField()
    end_range = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Service(BaseModel):
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.PROTECT,
                                 related_name="service")
    items = models.ManyToManyField(ServiceItem, related_name="prices")
    introduce = models.TextField()
    guide = models.TextField()
    rule = models.TextField()

    def __str__(self):
        return f"{self.category}"


class Question(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64,
                            unique=True,
                            db_index=True,
                            allow_unicode=True)
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.CASCADE,
                                 related_name="questions")
    step = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class QuestionItem(BaseModel):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="items")
    content = models.CharField(max_length=128)
    relation = models.ForeignKey(ServiceItem,
                                 on_delete=models.CASCADE,
                                 related_name="question_items")

    def __str__(self):
        return f"{self.content}"


class UserAnswer(BaseModel):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name="answers")
    answers = models.ManyToManyField(QuestionItem, related_name="questions")

    def __str__(self):
        return f"{self.user}"
