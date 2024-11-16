from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students_list, name='students'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('teams/', views.teams_list, name='teams'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('programs/', views.programs_list, name='programs'),
    path('programs/<int:program_id>/', views.program_detail, name='program_detail'),
    path('categories/', views.category_list, name='categories'),
    path('stages/', views.stage_list, name='stages'),
    path('stages/<int:stage_id>/', views.stage_detail, name='stage_detail'),
    path('images/', views.display_images, name='images'),
    path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
