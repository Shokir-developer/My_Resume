from django.urls import path

from my_portfolio.views import Home, BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('posts/', BlogListView.as_view(), name='blogs'),
    path('blogs/<str:slug>/', BlogDetailView.as_view(), name='blog-detail'),

]