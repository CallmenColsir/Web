from django.urls import path
from . import views as t_view

urlpatterns = [
    path("home", t_view.home_page, name="home-page"),
    path("add", t_view.add_items, name="add-items"),
    path("delete/<int:pk>", t_view.delete_items, name="delete-items"),
]
