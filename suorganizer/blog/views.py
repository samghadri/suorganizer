from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import View
from django.views.decorators.http import require_http_methods


# def post_list(request):
class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(request,self.template_name,
                    {'post_list':Post.objects.all()})


@require_http_methods(['HEAD', 'GET'])
def post_detail(request, slug, year, month):
    post = get_object_or_404(Post,
                pub_date__year=year,
                pub_date__month=month,
                slug__iexact=slug)
    return render(request,'blog/post_detail.html',{'post': post})
