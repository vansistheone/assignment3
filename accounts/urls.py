from django.urls import path
from . import views
from .views import home
from .views import *

urlpatterns = [
    path('', views.home, name='home'),  # This will be the homepage


    path('register/', views.register, name="register"),

    path('login/', views.login_view, name="login"),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('logout/', views.logout_view, name="logout"),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path('core-values/', core_values_admin, name='core_values_admin'),
    path('delete-core/<int:id>/', delete_core_value, name='delete_core_value'),

    path('programs/', programs_admin, name='programs_admin'),
    path('delete-program/<int:id>/', delete_program, name='delete_program'),

    path('team/', team_admin, name='team_admin'),
    path('delete-team/<int:id>/', delete_team, name='delete_team'),

    path('impact/', impact_admin, name='impact_admin'),
    path('delete-impact/<int:id>/', delete_impact, name='delete_impact'),

    path('mission/', mission_admin, name='mission_admin'),
    path('story/', story_admin, name='story_admin')
]
