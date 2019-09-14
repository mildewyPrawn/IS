from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views import View
# Create your views here.
from .models import Post

class OnePost(View):
    template = 'Post/one_post.html'
    context = {}

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.context['post'] = post
        self.context['tittle'] = str(post)

        return render(request, self.template, self.context)

class HomePageView(ListView):
    model = Post
    template_name = 'Post/one_post.html'
