from django.urls import path
from blog import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_new/', views.CreatePostView.as_view(), name='post_new'),
    path('post_edit/<int:pk>', views.PostUpdateView.as_view(), name='post_edit'),
    path('post_remove/<int:pk>/', views.PostDeleteView.as_view(), name='post_remove'),
    path('draft_list/', views.DraftListView.as_view(), name='draft_list'),
    path('add_comment_to_post/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment_approve/<int:pk>/', views.comment_approve, name='comment_approve'),
    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('post_publish/<int:pk>/', views.post_publish, name='post_publish'),
]

