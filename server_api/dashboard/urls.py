from django.conf.urls import url, include
from .views import dashboard, articles
from . import views

urlpatterns = [
    url(r'test/', dashboard, name='dashboard'),
    # url(r'articles/(2003)', articles, name='articles'),
    # url(r'articles/([0-9]{4})', articles, name='articles'),
    url(r'articles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', articles, name='articles'),
    url(r'users/', include([
        url(r'(?P<user_id>\d+)', views.UserInfo.as_view()),
        url(r'', views.UserPage.as_view()),
    ])),
    url(r'books/', views.UserTest.as_view()),
    url(r'template/', views.Temp.as_view(), name='temp'),
    url(r'list/', views.UserListView.as_view(), name='listview')
]
