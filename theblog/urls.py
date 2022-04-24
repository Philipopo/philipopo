from django.urls import path
from . import views
from .views import AddPostView, AddPost2View, AddPost3View, AddPost4View, DeletePostView, DeletePost2View, DeletePost3View, DeletePost4View, CategoryListView, DeleteCategoryView, ArticleDetailView, Article2DetailView, Article3DetailView,  LikeView, AddCommentView

 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_post2/', AddPost2View.as_view(), name='add_post2'),
    path('add_post3/', AddPost3View.as_view(), name='add_post3'),
    path('add_post4/', AddPost4View.as_view(), name='add_post4'),



    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('article2/<int:pk>/remove', DeletePost2View.as_view(), name='delete_post2'),
    path('article3/<int:pk>/remove', DeletePost3View.as_view(), name='delete_post3'),
    path('article4/<int:pk>/remove', DeletePost4View.as_view(), name='delete_post4'),

    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('category/<int:pk>/delete', DeleteCategoryView.as_view(), name='delete-category'),



    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article2/<int:pk>', Article2DetailView.as_view(), name='article2-detail'),
    path('article3/<int:pk>', Article3DetailView.as_view(), name='article3-detail'),


    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),


    path('like/<int:pk>',   LikeView, name='like_post'),

]