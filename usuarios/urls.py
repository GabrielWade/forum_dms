from django.urls import path
from usuarios.views import login


urlpatterns = [
    path("login", login, name="login"),
]
