from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_comment$', views.user_comment, name='user_comment')
]
