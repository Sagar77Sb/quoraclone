from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('', views.home_view, name='home'),
    path('question/new/', views.post_question_view, name='post_question'),
    path('question/<int:pk>/', views.question_detail_view, name='question_detail'),
    path('answer/<int:pk>/like/', views.like_answer_view, name='like_answer'),
]
