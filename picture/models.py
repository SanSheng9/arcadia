from django.db import models

from arcadia import settings


class Picture(models.Model):
    name = models.CharField(max_length=255, blank=False, default='New picture')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False)

    def __str__(self):
        return f'ID {self.id}: {self.name}'

class UserPictureRelation(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    favourites = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}: {self.picture.name}'