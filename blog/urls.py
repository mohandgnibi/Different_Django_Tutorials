from django.urls import path

from .views import (BlogListView, 
                    BlogDetailView, 
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeletView
)

app_name = "blog"
urlpatterns = [
    # Create a blog post.
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    # Display a single post.
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    # Update post.
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    # Delete post.
    path("post/<int:pk>/delete/", BlogDeletView.as_view(), name='post_delete'),
    # Home Page, display all post.
    path("", BlogListView.as_view(), name="home"),
]
