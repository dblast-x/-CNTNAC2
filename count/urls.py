from django.urls import path
from . import views


app_name = "count"
urlpatterns = [
    path("orders/", views.orders_view, name="orders"),
    path("new_item/", views.new_item_view, name="new_item"),
]
