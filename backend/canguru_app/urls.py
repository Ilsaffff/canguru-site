from django.urls import path
from . import views

app_name = 'canguru_app'
urlpatterns = [
    path('user/create/', views.UserCreateView.as_view()),
    path('all/', views.UsersListView.as_view()),
    path('user/detail/<int:pk>', views.UserDetatilView.as_view())
]
