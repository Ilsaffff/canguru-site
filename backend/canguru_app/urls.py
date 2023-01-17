from django.urls import path
from . import views


app_name = 'canguru_app'
urlpatterns = [
    path('canguru/create/', views.UserCreateView.as_view())
]
