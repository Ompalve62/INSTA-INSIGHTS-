from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dash,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('influencers',views.influencers_dash,name='influencers'),
    path('influencers_stats',views.influ_view,name='influencers_stats'),

]
