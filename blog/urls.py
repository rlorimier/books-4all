from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.newpost, name='newpost'),
    path('post/<int:pk>/', views.details, name='details'),
    path('post/<int:pk>/edit/', views.editpost, name='editpost'),
    path('post/about/', views.about, name='about'),
    path('accounts/', include('allauth.urls')),
    path('post/<int:pk>/comment/', views.addcomment, name='addcomment'),
]
