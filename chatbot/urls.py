from django.urls import path
from . import views


urlpatterns = [
    path("chat", views.chat, name="chat"),
    path("register", views.register, name="register"),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("spanish/", views.spanish, name="spanish"),
    path("detector/", views.detector, name="detector"),
    path("image/",views.image, name="image"),

]
