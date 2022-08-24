from django.urls import path

from . import views

app_name = "leads"

urlpatterns = [
    path('', views.lead_list, name="index"),
    path('create/', views.lead_create, name="create"),
    path('delete/<int:pk>/', views.lead_delete, name="delete"),
    path('<int:pk>/', views.lead_detail, name="detail"),
]
