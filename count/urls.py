from django.urls import path
from . import views


app_name = "count"
urlpatterns = [
    path("", views.orders, name="home"),
    path("items/", views.list_items, name="items"),
    path("add_item/", views.add_item, name="add_item"),
    path("delete_item/", views.delete_item, name="delete"),
    # path("edit_item/", views.delete, name="delete"),
    path("order_log/", views.order_log, name="order_log"),
]
