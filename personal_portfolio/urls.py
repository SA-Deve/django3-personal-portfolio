from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home/',views.home,name='home'),
    path('projects/', views.project, name='project'),
    path('detail/<int:project_id>', views.detail, name='detail')
]
