from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, login_view, logout_view, register_view, profile_view, SearchResultsView, TagPostListView, CommentCreateView, CommentUpdateView, CommentDeleteView

)


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("search/", SearchResultsView.as_view(), name="search-results"),
    path("tags/<str:tag_name>/", TagPostListView.as_view(), name="posts-by-tag"),
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

]

# ["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"] 
# tags/<slug:tag_slug>/", "PostByTagListView.as_view 
# comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/
#  PostByTagListView.as_view()