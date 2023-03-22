from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("view/", views.view, name="view"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"),
path("<int:id>", views.index, name="index"),
]
