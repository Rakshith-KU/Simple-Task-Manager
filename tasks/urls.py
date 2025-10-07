from django.urls import path
from . import views
from . import views_auth

urlpatterns = [
    # Task management
    path('', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_create'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('toggle/<int:task_id>/', views.task_toggle_status, name='task_toggle_status'),

    # Authentication
    path('signup/', views_auth.signup_view, name='signup'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
]
