from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dash,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('influencers',views.influencers_dash,name='influencers'),
    path('influencers_stats',views.influ_view,name='influencers_stats'),
    path('influencers_stats01',views.influ_view01,name='influencers_stats01'),
    path('faqs_link',views.faqs,name='faqs_link'),
    path('logout/',views.logout,name='logout'),
    
]
