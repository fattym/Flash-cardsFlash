
from django.db import models

# Create your models here.
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
    bio = HTMLField()
    photo = ImageField(blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='followers')
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    
    def __str__(self):
        return self.bio

    def __str__(self):
        return self.user.username




class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_number_of_cards(self):
        '''
        Returns the number of cards in the decks related
        card_set
        '''
        return self.card_set.count()
    get_number_of_cards.short_description = 'Card Count'

class Card(models.Model):
    parentDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.front
