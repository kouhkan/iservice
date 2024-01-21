from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from herfeei.common.models import BaseModel
from herfeei.users.models import BaseUser


class Expert(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="expert")
    category = models.ForeignKey("services.ServiceCategory", on_delete=models.CASCADE)
    province = models.ForeignKey("services.Province", on_delete=models.CASCADE)
    city = models.ForeignKey("services.City", on_delete=models.CASCADE)
    license = models.ImageField(upload_to="experts/licenses/", null=True, blank=True)
    bad_background = models.BooleanField(default=False)
    bad_background_license = models.ImageField(upload_to="experts/bad_backgrounds/", null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


class AvailableTimeExpert(BaseModel):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name="available")
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.expert}"


class Warranty(BaseModel):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE, related_name="warranty")

    def __str__(self):
        return f"{self.expert}"


class Sample(BaseModel):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name="samples")
    category = models.ForeignKey("services.ServiceCategory", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="experts/samples/")
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.expert}"


class Bookmark(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="bookmark")
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=Expert)
def change_user_role(sender, instance, **kwargs):
    instance.user.role = BaseUser.UserRole.EXPERT
    instance.user.save()
