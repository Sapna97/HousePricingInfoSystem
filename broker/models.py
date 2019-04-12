from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pictures/', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Adv(models.Model):
    broker=models.ForeignKey('broker.Profile',on_delete=models.CASCADE, related_name='advs')
    title=models.CharField(max_length=500)
    bath=models.IntegerField()
    balcony=models.IntegerField()
    bedrooms=models.IntegerField()
    area_sqft=models.FloatField()
    area_type=models.CharField(max_length=100)
    hk=models.IntegerField()
    location=models.CharField(max_length=500)

    def __str__(self):
        return self.title