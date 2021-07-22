from django.urls import path
from .views import *

app_name = 'employer'

urlpatterns = [
    path( "list_employer/", EmployerListView.as_view(), name="empl_rest_lst"),
    path("list_level/<slug:slug_level>/", EmployerLevelListView.as_view(), name="empl_lvl_lst")
]

