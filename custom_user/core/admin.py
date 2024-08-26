from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','profile_pic','is_active','is_staff','is_superuser','last_login')
    add_fieldsets = (
        ( 
            None,
         {
        'classes':('wide',),
        'fields':('email','username','password1','password2','profile_pic'),
    },
   ),
  )

admin.site.register(CustomUser,CustomUserAdmin)
