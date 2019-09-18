# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
