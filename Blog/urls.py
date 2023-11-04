from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage, name='home'),
    path('blogDetails/<slug>', views.blog_details),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.LogOut, name='logout'),
]
