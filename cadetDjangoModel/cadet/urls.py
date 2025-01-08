from django.urls import path

from .views import cadetView, RolesView

urlpatterns = [
    path('cadets/', cadetView, name="cadet"),
    path('roles/', RolesView, name="roles")
]
