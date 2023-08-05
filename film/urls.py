from django.urls import path
from film import views

urlpatterns = [
    path('detail/<int:id>/', views.DetailView.as_view(), name="detail"),
    path('actors/', views.ActorView.as_view(), name="actors"),
    path('actor_detail/<int:id>/', views.ActorDetailView.as_view(), name="actor_detail"),
    path('delete-comment/<int:id>/', views.DeleteCommentView.as_view(), name = "delete-comment" ),
    path('user_views/', views.UserViewsView.as_view, name="user_views"),
]