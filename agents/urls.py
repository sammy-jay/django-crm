from django.urls import path

from . import views
from .views import AgentListView, AgentCreateView, AgentDetailView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='index'),
    path('create/', AgentCreateView.as_view(), name='create'),
    path('<int:pk>/', AgentDetailView.as_view(), name="detail"),
    # path('update/<int:pk>/', AgentUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', views.agent_delete, name="delete"),
]
