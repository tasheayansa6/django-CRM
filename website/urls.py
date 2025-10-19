from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_users, name='login'),  # make sure this exists
    path('logout/', views.logout_user, name='logout'),
    path('register/', views._user, name='register'),

]
