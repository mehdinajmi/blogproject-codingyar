from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list_view, name='post_list_view'),
    path('', views.PostListView.as_view(), name='post_list_view'),
    # path('<int:pk>/', views.post_detail_view, name='post_detail_view'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail_view'),
    # path('create/', views.add_post_view, name='add_create'),
    path('create/', views.AddPostView.as_view(), name='add_create'),
    # path('<int:pk>/update/', views.update_view, name='post_update'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    # path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]