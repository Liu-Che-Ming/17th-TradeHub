from django.urls import path

from . import views

app_name = "inventory"


urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("create", views.create, name="create"),
    path("delete/<int:id>", views.delete, name="delete"),
]