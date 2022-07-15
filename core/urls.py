"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from habits import views as habits_views


urlpatterns = [
    path('', habits_views.home, name="home"),
    # for django-registration-redux
    path('accounts/', include('registration.backends.simple.urls')), 
    path('admin/', admin.site.urls),
    path('habits/', habits_views.habits_list, name='habits_list'),
    path('habits/add/', habits_views.add_habit, name='add_habit'),
    path('habits/<int:pk>/edit/', habits_views.edit_habit, name='edit_habit'),
    path('habits/<int:pk>/delete/', habits_views.delete_habit, name='delete_habit'),
    path('habits/<int:pk>/entry/', habits_views.add_entry, name='add_entry'),
    path('habits/<int:pk>/detail/', habits_views.habit_detail, name='habit_detail'),
]


#debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]