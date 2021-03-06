from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserExtend(models.Model):
    user = models.OneToOneField(User,related_name="UserExtend")
    agentUsername = models.CharField(max_length=50)
    phi = models.IntegerField()
    location_lat = models.CharField(max_length=20)
    location_long = models.CharField(max_length=20)

    def get_achievements(self):
        return self.achievements_aux.all()

class Appel(models.Model):
    user = models.ForeignKey(User)

class Achievement(models.Model):
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=300)
    unlockers = models.ManyToManyField(UserExtend,through='AchievementUnlock', related_name="achievements_aux")

class AchievementUnlock(models.Model):
    userExtend = models.ForeignKey(UserExtend)
    achievement = models.ForeignKey(Achievement)
