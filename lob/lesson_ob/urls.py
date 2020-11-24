from django.urls import path

from . import views

from lesson_ob.views import (
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
]
