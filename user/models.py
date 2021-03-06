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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
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


class Image(models.Model):
    name = models.CharField(max_length = 50)
    picture = ImageField(blank = True, manual_crop = '1080x1080')
    caption = HTMLField()
    posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_det = models.ForeignKey(Profile, on_delete=models.CASCADE)

    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def is_liked(self):
        pass

        
    @classmethod
    def update_caption(self, caption):
        update_img = cls.objects.filter(id = id).update(caption = caption)
        return update_img

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id).all()
        return image

    @classmethod
    def get_profile_pic(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images

    @property
    def count_comments(self):
        comments = self.comments.count()
        return comments

    @property
    def count_likes(self):
        likes = self.likes.count()
        return likes


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['posted']
