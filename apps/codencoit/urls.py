from django.urls import path
from .views import *



urlpatterns = [
    path('team-member/', TeamMemberList.as_view()),
    path('team-member/<int:pk>', TeamMemberDetail.as_view()),
    path('industries/', IndustryList.as_view()),
    path('industries/<int:pk>', IndustryDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>', ProjectDetail.as_view()),
]
