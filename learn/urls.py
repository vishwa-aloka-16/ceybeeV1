from . import views
from django.urls import path

urlpatterns = [
    path('', views.showLearn, name='learn'),
    path('blog/<int:blog_id>/', views.showLearnBlog, name='blog'),
    ]