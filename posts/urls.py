from django.urls import path

from .views import HomePageView

app_name = 'posts'
urlpatterns = [
    # Home page
    path('', HomePageView.as_view(), name='home'),
]
