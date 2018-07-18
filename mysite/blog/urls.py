from django.urls import path, include
from django.conf.urls import url
from blog import views

app_name = 'blog'
# urlpatterns = [
#     path('', views.PostListView.as_view(), name='post_list'),
#     path('about/', views.AboutView.as_view(), name='about'),
#     path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
#     path('post/new/', views.CreatePostView.as_view(), name='post_new'),
#     path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
#     path('post/<int:pk>/remove/', views.DeletePostView.as_view(), name='post_remove'),
#     path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
#     path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
#     path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
#     path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
#     path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
# ]

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.DeletePostView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]