from django.shortcuts import render
from django.views import generic

from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(hidden = False)


class PostView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
