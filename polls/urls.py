from django.urls import path
from . import views


urlpatterns = [
    path('<int:question_id>/results/', views.results, name='results'),
]
