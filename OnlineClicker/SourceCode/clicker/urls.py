from django.urls import path
from . import views
urlpatterns = [
    path('', views.create, name='create'),
    path('clicking', views.clicking, name='clicking')
]
