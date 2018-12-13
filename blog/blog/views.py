from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.paginator import Paginator
from blog.models import Post
from blog.forms import PostForm, CommentForm


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_ordering(self):
        if self.request.GET.get('views') == 'asc':
            return 'views'
        if self.request.GET.get('views') == 'desc':
            return '-views'
        if self.request.GET.get('date') == 'asc':
            return '-date'
        return 'date'

    def get_queryset(self):
        return Post.objects.filter(hidden=False).order_by(self.get_ordering())


class PostView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj

    def comments_list(self):
        paginator = Paginator(self.object.comment_set.all(), 10)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['comment_add_url'] = '/post/{}/comment_add'.format(context['post'].id)
        context['comments'] = self.comments_list
        return context


class CreatePost(LoginRequiredMixin, generic.CreateView):
    template_name = "post_add.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateComment(LoginRequiredMixin, generic.CreateView):
    template_name = "comment_add.html"
    form_class = CommentForm

    def get_initial(self):
        return {
            "post": self.kwargs['post_pk']
        }

    def get_success_url(self):
        return "/post/{}".format(self.kwargs['post_pk'])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
