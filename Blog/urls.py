from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage,name='home' ),
    path('blog_details/<pk>' ,views.blog_details ,name='blog-details'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.LogOut,name='logout'),
]