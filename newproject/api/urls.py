from django.urls import path
from .views import (
    get_projects, 
    create_project, 
    project_settings, 
    get_tasks, 
    create_task, 
    task_settings, 
    get_stages, 
    create_stage, 
    stage_settings
)

urlpatterns = [
    path('projects/', get_projects, name='get_projects'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/<int:id>', project_settings, name='project_settings'),
    
    path('tasks/', get_tasks, name='get_tasks'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:id>', task_settings, name='task_settings'),
    
    path('stages/', get_stages, name='get_stages'),
    path('stages/create/', create_stage, name='create_stage'),
    path('stages/<int:id>', stage_settings, name='stage_settings')
]