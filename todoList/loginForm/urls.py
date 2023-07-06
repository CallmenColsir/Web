from django.urls import path
from . import views as l_view

urlpatterns = [
    path("login", l_view.login_form, name="login-form"),
    path('register', l_view.register_form, name="register-form"),
    path('logout', l_view.logout_form, name="logout-form"),
]
