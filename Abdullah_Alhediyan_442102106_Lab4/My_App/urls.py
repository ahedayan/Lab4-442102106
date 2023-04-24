from django.urls import path
from . import views

urlpatterns = [
    path("", views.view1, name="view1"),
    path("<int:number>", views.view2, name="view2"),
    path("taxrate", views.view3, name="view3"),

]