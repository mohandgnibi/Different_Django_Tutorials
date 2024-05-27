from django.urls import path

from .views import HomePageView, AboutPageView

app_name = "pages"
urlpatterns = [
    # About page
    path("about/", AboutPageView.as_view(), name="about"),
    # Home page
    path("", HomePageView.as_view(), name="home"),
]
