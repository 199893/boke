from django.conf.urls import url
from . import views

app_name='comment'
urlpatterns = [
    url(r'^commit/(\d+)/$',views.commitcomment,name='commit')
]
