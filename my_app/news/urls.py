from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name = 'news_home'),
    path('create', views.create, name = 'create'),
    path('<int:pk>', views.NewDetailView.as_view(), name = 'blog-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name = 'blog-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name = 'blog-delete')
]