from . import views
from .views import ArticleView, ArticleDetailView, SharePostView, CommentView, ArticleByTagView
from django.urls import path
from .feeds import LastestPostsFeed


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
    path('blog', ArticleView.as_view(), name='blog'),
    path('blog/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('share/<slug:slug>/', SharePostView.as_view(), name='share_post'),
    path('comment/<slug:slug>/', CommentView.as_view(), name='send_comment'),
    path('appointment', views.appointment, name='appointment'),
    path('tags/<slug:slug>', ArticleByTagView.as_view(), name='tag_list'),
    path('blog/feed', LastestPostsFeed(), name='post_feed')
]