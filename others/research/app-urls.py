from django.conf.urls import patterns, url

from research import views

urlpatterns = patterns('',
    url(r'^$', views.research_index, name='research'),
    url(r'^(?P<journal_id>\d+)/$', views.journal_detail, name='journal_detail'),
    url(r'^(?P<chapter_id>\d+)/$', views.chapter_detail, name='chapter_detail'),
)