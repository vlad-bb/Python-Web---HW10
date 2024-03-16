from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="/"),
    path("<int:page>", views.main, name="root_paginate"),
]
