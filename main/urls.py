from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^samplerate$', views.samplerate, name='samplerate'),
    url(r'^testing$', views.testing, name='testing')
]