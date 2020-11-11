from django.urls import path

from . import views

from lesson_ob.views import (
    registration_view,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('register/', registration_view, name="register"),
]
