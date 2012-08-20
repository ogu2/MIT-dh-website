from django.conf.urls import patterns, include, url

urlpatterns = patterns('website.views',
    url(r'^$', 'home',name='home'),
    url(r'^$', 'sign_out',name='sign_out'),
    url(r'^$', 'sign_in',name='sign_in'),
    url(r'^$', 'register',name='register'),

)

