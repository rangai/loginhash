from django.urls import path

from myhash import views

urlpatterns = [
    path("new/", views.hash_new, name="hash_new"),
]