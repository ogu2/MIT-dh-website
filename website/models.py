from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
	'''Requires facebook username to pull current fb image and
	possibly other user data'''
	user=models.ForeignKey(User,unique=True)
	fb_username=models.CharField(max_length=50)
	course=models.CharField(max_length=50)
	year=models.IntegerField()
	phone_number=models.CharField(max_length=20)
	url=models.URLField(blank=True)
	home_town=models.CharField(max_length=250,blank=True)
	short_bio=models.CharField(max_length=250,blank=True)
	is_alum=models.BooleanField()
	is_social_member=models.BooleanField()
	
	def __unicode__(self):
		return str(self.user.first_name)+' '+str(self.user.last_name)+' ('+str(self.user.username)+') , '+str(self.year)
