# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response ,redirect
from django.core.context_processors import request
from website.models import UserProfile, Summer,ContactMessages
from website.forms import ContactForm
from django.template import RequestContext

import random

def index(request):
    return HttpResponse("habari dh")

def home(request):
  uid = request.session.get('user')
  args={}
  if uid is None:
    members=UserProfile.objects.filter(is_alum=False, is_social_member=False)
    args['members']=members
    
    try:
        args['alerts']=request.session['alerts']
        del request.session['alerts']
    except:
        args['alerts']=None
        
    x=Summer.objects.all()
    if x:
        random.shuffle(x)
        args['summer']=x[0]
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

def contact(request):
    return render_to_response('devel.html') #contact.html

def members(request):
    args={}
    membs=UserProfile.objects.filter(is_alum=False, is_social_member=False).order_by('?')[:1].get()
    args['members']=membs
    return render_to_response('members.html',args) #members.html

def summer(request):
    '''Template extends members'''
    args={}
    membs=Summer.objects.filter(userp__is_alum=False, userp__is_social_member=False).order_by('?')[:1].get()
    args['members']=membs
    return render_to_response('summer.html',args)

def devel(request):
    return render_to_response('devel.html')

def contact_us(request):
    user = None
    if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
        ContactMessages(processed=False,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
                ).save()
        request.session['alerts'] = ['Contact message has been successfully sent']
        return redirect('home')
        
    else:
      form = ContactForm()

    return render_to_response(
    'contact_us.html',
    {
      'form': form,
      'months': range(1, 12),
      'years': range(2011, 2036),
    },
    context_instance=RequestContext(request)

  )
