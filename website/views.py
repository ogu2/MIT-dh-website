# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import request
from website.models import UserProfile
def index(request):
    return HttpResponse("habari dh")

def home(request):
  uid = request.session.get('user')
  args={}
  if uid is None:
    members=UserProfile.objects.filter(is_alum=False, is_social_member=False)
    args['members']=members
    return render_to_response('index.html',args)
  else:
    return render_to_response('user.html', {'user': User.objects.get(pk=uid)})

def sign_in(request):
    return HttpResponse("habari dh")

def sign_out(request):
    return HttpResponse("habari dh")

def register(request):
    return HttpResponse("habari dh")

def life(request):
    return render_to_response('life.html')

def contact_us(request):
    return render_to_response('devel.html') #contact.html

def members(request):
    args={}
    args['members']=UserProfile.objects.filter(is_alum=False, is_social_member=False)
    return render_to_response('members.html',args) #members.html

def devel(request):
    return render_to_response('devel.html')
