
from django.urls import path
from . import views

app_name = 'oud'

urlpatterns = [
    path("", views.oud_register, name="oud_register"),
    path("success/",views.show_success,name="success"),
    # path("success/", views.success, name="success"),
]