from django.urls import path
from . import views
urlpatterns = [
    path("",views.login),
    path('register',views.register),
    path('index',views.index),
    path('user_index/<pk>',views.user_index),
    path('add_post',views.add_post),
    path('logout',views.logout),
]