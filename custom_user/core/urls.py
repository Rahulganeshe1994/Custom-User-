from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserPasswordChangeForm



urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('password_change',auth_views.PasswordChangeView.as_view(template_name = 'core/password_change.html',form_class = UserPasswordChangeForm),name='password_change'),

    # path('password_change_done',auth_views.PasswordChangeView.as_view(template_name = 'core/password_change_done.html'))
]
