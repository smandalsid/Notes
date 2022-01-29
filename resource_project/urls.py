"""resource_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resources.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('user_login/', user_login, name="user_login"),
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('admin_login/', admin_login, name="admin_login"),
    path('admin_home/',admin_home, name="admin_home"),
    path('logout/',Logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('password_change/',password_change,name='password_change'),
    path('profile_edit/',profie_edit,name='profile_edit'),
    path('notes_upload/',notes_upload,name='notes_upload'),
    path('view_my_notes/',view_my_notes,name='view_my_notes'),
    path('delete_my_notes/<int:pid>/',delete_my_notes,name='delete_my_notes'),
    path('view_users',view_users,name='view_users'),
    path('delete_user/<int:pid>/',delete_user,name='delete_user'),
    path('pending_notes/',pending_notes,name='pending_notes'),
    path('verified_notes/',verified_notes,name='verified_notes'),
    path('rejected_notes/',rejected_notes,name='rejected_notes'),
    path('assign_status/<int:pid>/',assign_status,name='assign_status'),
    path('all_notes/',all_notes,name='all_notes'),
    path('delete_note/<int:pid>',delete_note,name='delete_note'),
    path('all_notes_user/',all_notes_user,name='all_notes_user'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
