from django.conf.urls import url

from . import views,testdb,search
urlpatterns = {
    url(r'^index/$', views.index),
    url(r'^lalala/$', views.lalala),
    url(r'^testdb/$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^computer/<int:num>', views.computer1),



}