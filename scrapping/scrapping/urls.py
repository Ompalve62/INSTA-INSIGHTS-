"""scrapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dash,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('influencers',views.influencers_dash,name='influencers'),
    path('influencers_stats',views.influ_view,name='influencers_stats'),
    path('influencers_stats01',views.influ_view01,name='influencers_stats01'),
    path('faqs_link',views.faqs,name='faqs_link'),
    path('logout/',views.logout,name='logout'),
    path('filter_open',views.filter_popup,name='filter_open'),
    path('forgot',views.forgot,name='forgot'),
    path('privacy',views.privacy_policy,name='privacy')


]
