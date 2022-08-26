from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

from . import views
from .views import LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
    path('create/', LeadCreateView.as_view(), name="create"),
    path('delete/<int:pk>/', views.lead_delete, name="delete"),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name="update"),
    path('<int:pk>/', LeadDetailView.as_view(), name="detail"),
]

# urlpatterns = [
#     path('', views.lead_list, name="index"),
#     path('create/', views.lead_create, name="create"),
#     path('delete/<int:pk>/', views.lead_delete, name="delete"),
#     path('update/<int:pk>/', views.lead_update, name="update"),
#     path('<int:pk>/', views.lead_detail, name="detail"),
# ]
