from django.urls import path

from .views import  BlogListView, BlogDetailView

app_name = 'blog'
urlpatterns = [
    # Display a single post.
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # Home Page display all post.
   path('', BlogListView.as_view(), name='home'),
]