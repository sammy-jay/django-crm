from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('leads/', views.lead_list),
    path('leads/<int:pk>/', views.lead_detail),
]
