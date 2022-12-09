"""issue_tracker URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import ProjectView, CreateProjectView, ProjectDetailView, UpdateProjectView, DeleteProjectView, \
    IssueListView, IssueView, CreateIssueView, UpdateIssueView, DeleteIssueView \


urlpatterns = [
    path('admin/', admin.site.urls),
    # Project urls
    path('', ProjectView.as_view(), name='project_list'),
    path('project/create/', CreateProjectView.as_view(), name='create_project'),
    path('project/detail/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/update/<int:pk>/', UpdateProjectView.as_view(), name='update_project'),
    path('project/delete/<int:pk>/', DeleteProjectView.as_view(), name='delete_project'),

    # Issue urls
    path('issue/list/', IssueListView.as_view(), name='issue_list'),
    path('issue/detail/<int:pk>/', IssueView.as_view(), name='issue_detail'),
    path('issue/create/<int:pk>', CreateIssueView.as_view(), name='create_issue'),
    path('issue/update/<int:pk>/', UpdateIssueView.as_view(), name='update_issue'),
    path('issue/delete/<int:pk>/', DeleteIssueView.as_view(), name='delete_issue'),
]