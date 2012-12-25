from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
	'''Requires facebook username to pull current fb image and
	possibly other user data'''
	user=models.ForeignKey(User,unique=True)
	fb_username=models.CharField(max_length=100,blank=True)
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

class Summer(models.Model):
	'''Just for use during REX
	TODO:rethink this'''
	userp=models.ForeignKey(UserProfile,unique=True)
	what_you_did=models.TextField()
	yGermanHouse=models.TextField()
	anything_else=models.TextField()
	Short_bio=models.TextField()
	
	def __unicode__(self):
		return str(self.userp.user.first_name)+' '+str(self.userp.user.last_name)+' summer'
	
class ContactMessages(models.Model):
	'''Stores contact messages till we write email fn to change to log mode'''
	name=models.CharField(max_length=250)
	email=models.EmailField()
	message=models.TextField()
	processed=models.BooleanField()
	timestamp=models.DateField(auto_now_add=True)
	
	def __unicode__(self):
		return str(self.name)+' '+str(self.timestamp)
