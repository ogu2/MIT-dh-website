# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("habari dh")

def home(request):
  uid = request.session.get('user')
  if uid is None:
    return render_to_response('index.html')
  else:
    return render_to_response('user.html', {'user': User.objects.get(pk=uid)})

def sign_in(request):
    return HttpResponse("habari dh")

def sign_out(request):
    return HttpResponse("habari dh")

def register(request):
    return HttpResponse("habari dh")
