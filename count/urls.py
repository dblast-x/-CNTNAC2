from django.urls import path
from . import views


app_name = "count"
urlpatterns = [
    path("", views.orders_view, name="home"),
    path("new_item/", views.new_item_view, name="new_item"),
    path("delete_item/", views.delete_view, name="delete"),
    path("order_log/", views.order_log, name="order_log"),
]
