from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('home/',views.home,name='home'),
    path('detail/<int:blog_id>/',views.detail,name='detail')
]