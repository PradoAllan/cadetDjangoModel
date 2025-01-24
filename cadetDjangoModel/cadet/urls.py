from django.urls import path

# Class APIView para melhor personalização:
from . import views

urlpatterns = [
    path('', views.UserAPIView.as_view(), name='cadet-list'),
    path('<int:pk>/', views.UserIdAPIView.as_view(), name='cadet-retrieve'),
    path('roles/', views.RoleAPIView.as_view(), name='roles-list'),
    path('roles/<int:pk>/', views.RoleIdAPIView.as_view(), name='roles-retrieve'),
    path('work_experiences/', views.WorkExperienceAPIView.as_view(), name='work-experience'),
    path('work_experiences/<int:pk>/', views.WorkExperienceIdAPIView.as_view(), name='work-experience-id'),
    path('work_titles/', views.WorkTitleAPIView.as_view(), name='work-title'),
    path('work_titles/<int:pk>/', views.WorkTitleIdAPIView.as_view(), name='work-title-id'),
]

# urlpatterns = [
#     path('', views.UserAPIView.as_view(), name='user-list'),
#     path('<int:id>/', views.UserIdAPIView.as_view(), name='user-retrieve'),
#     path('roles/', views.RoleAPIView.as_view(), name='role-list'),
#     path('roles/<int:id>/', views.RoleIdAPIView.as_view(), name='role-retrieve'),
#     path('work_experiences/', views.WorkExperienceAPIView.as_view(), name='work-experience'),
#     path('work_experiences/<int:id>/', views.WorkExperienceIdAPIView.as_view(), name='work-experience-id'),
#     path('work_titles/', views.WorkTitleAPIView.as_view(), name='work-title'),
#     path('work_titles/<int:id>/', views.WorkTitleIdAPIView.as_view(), name='work-title-id'),
#     path('personal_projects/', views.UserPersonalProjectAPIView.as_view(), name='personal-project'),
#     path('personal_projects/<int:id>/', views.UserPersonalProjectIdAPIView.as_view(), name='personal-project-id'),
#     path('pratical_projects/', views.UserPraticalProjectAPIView.as_view(), name='pratical-project'),
#     path('pratical_projects/<int:id>/', views.UserPraticalProjectIdAPIView.as_view(), name='pratical-project-id'),
#     path('additional_projects/', views.AdditionalProjectAPIView.as_view(), name='additional-project'),
#     path('additional_projects/<int:id>/', views.AdditionalProjectIdAPIView.as_view(), name='additional-project-id'),
#     path('language_levels/', views.LanguageLevelAPIView.as_view(), name='language-level'),
#     path('language_levels/<int:id>/', views.LanguageLevelIdAPIView.as_view(), name='language-level-id'),
#     path('skills/', views.SkillAPIView.as_view(), name='skill'),
#     path('skills/<int:id>/', views.SkillIdAPIView.as_view(), name='skill-id'),
#     path('user_skills/', views.UserSkillAPIView.as_view(), name='user-skill'),
#     path('user_skills/<int:id>/', views.UserSkillIdAPIView.as_view(), name='user-skill-id'),
#     # path('intra/', views.UserIntraAPIView.as_view(), name='intra_id-list'),
#     # path('intra/<int:id>/', views.UserIntraIdAPIView.as_view(), name='intra_id-retrieve')
# ]

# Com esse código, foi usado uma funcção api_view. Funciona bem, mas geralmente, queremos criar uma classe APIView 
# para manipularmos melhor os métodos e personalizar da maneira que queremos os endpoints.
# from .views import cadetView, RolesView

# urlpatterns = [
#     path('cadets/', cadetView, name="cadet"),
#     path('roles/', RolesView, name="roles")
# ]
