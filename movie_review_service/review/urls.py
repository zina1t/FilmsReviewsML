from django.urls import path
from . import views  # Import views from the current review app

urlpatterns = [
    path('submit/', views.submit_review, name='submit_review'),  # Point to the correct view function
]
