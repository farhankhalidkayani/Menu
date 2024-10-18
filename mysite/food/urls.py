from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("<int:pk>/", views.detail.as_view(), name="detail"),
    path("add/", views.add_item.as_view(), name="add_item"),
    path("edit/<int:item_id>", views.edit_item, name="edit_item"),
    path("delete/<int:item_id>", views.delete_item, name="delete_item"),
]
