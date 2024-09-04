from django.urls import path

from . import views

app_name = "purchase_orders"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("delete/many", views.delete_selected_purchase_orders, name="delete_selected"),
    path("show/<int:id>", views.show, name="show"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
]