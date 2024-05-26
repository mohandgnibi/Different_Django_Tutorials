from django.urls import path

from .views import homePageView

urlpatterns = [
    # Home page
    path('', homePageView, name='home')
]