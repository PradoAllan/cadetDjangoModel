from django.urls import path

# Class APIView para melhor personalização:
from . import views

urlpatterns = [
    path('', views.UserAPIView.as_view(), name='cadet-list'),
    path('<int:pk>/', views.UserIdAPIView.as_view(), name='cadet-retrieve'),
    path('roles/', views.RoleAPIView.as_view(), name='roles-list'),
    path('roles/<int:pk>/', views.RoleIdAPIView.as_view(), name='roles-retrieve')
]

# Com esse código, foi usado uma funcção api_view. Funciona bem, mas geralmente, queremos criar uma classe APIView 
# para manipularmos melhor os métodos e personalizar da maneira que queremos os endpoints.
# from .views import cadetView, RolesView

# urlpatterns = [
#     path('cadets/', cadetView, name="cadet"),
#     path('roles/', RolesView, name="roles")
# ]
