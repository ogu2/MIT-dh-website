from django.conf.urls import patterns, include, url

urlpatterns = patterns('website.views',
    url(r'^$', 'home',name='home'),
    url(r'^$', 'sign_out',name='sign_out'),
    url(r'^$', 'sign_in',name='sign_in'),
    url(r'^$', 'register',name='register'),
    url(r'^contact_us$', 'contact_us', name='contact_us'),
    url(r'^members$','members',name='members'),
    url(r'^life$','life',name='life'),
    url(r'^devel$','devel', name='devel'),
    url(r'^summer$','summer', name='summer'),
)

