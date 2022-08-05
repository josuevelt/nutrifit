from django.urls import path
from .views import LogueoView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", LogueoView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout")
]