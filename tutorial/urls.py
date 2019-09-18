from django.conf.urls import url
from django.contrib import admin

from blog.views import PostListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view()),
]
