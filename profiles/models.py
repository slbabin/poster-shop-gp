from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=32, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=255, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=255, null=True,
                                               blank=True)
    default_city = models.CharField(max_length=255, null=True, blank=True)
    default_county = models.CharField(max_length=255, null=True, blank=True)
    default_postcode = models.CharField(max_length=255, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
