#Admin page for website
from website.models import UserProfile, Summer
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'fb_username', 'year','is_alum')
    list_filter = ['is_alum','year', 'is_social_member']
    
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Summer)