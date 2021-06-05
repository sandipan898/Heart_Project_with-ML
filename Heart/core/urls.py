from django.urls import path
from . views import form_view, resault_view
urlpatterns = [
    path('',form_view, name="main_form"),
    path('resault/',resault_view, name="resault_views")
]