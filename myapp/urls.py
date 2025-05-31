from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.task_list,name='task_list'),
    path('task/create/',views.task_create,name='task_create'),
    path('task/edit/<int:pk>/',views.task_edit,name='task_edit'),
    path('task_delete/<int:pk>/',views.task_delete,name='task_delete'),
]
