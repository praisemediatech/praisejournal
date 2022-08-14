from django.urls import path
from .views import HomeView, BlogList, TagList, CatList, PostDetailView
from .import views

urlpatterns = [
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='single_post'),
    path('blog/<category>/', CatList.as_view(), name='catlist'),
    path('blog/tag/<tag>/', TagList.as_view(), name='taglist'),
    path('', HomeView.as_view(), name='index'),
    path('blog/', BlogList.as_view(), name='blog_list'),
    path('blog/<str:pk>/single-blog/comment-reply/', views.commentReply, name='comment_reply'),
]