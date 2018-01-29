from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from .forms import PostForm

# def post_list(request):
class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(request,self.template_name,
                    {'post_list':Post.objects.all()})


class PostCreate(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template_name,{'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form': bound_form})


@require_http_methods(['HEAD', 'GET'])
def post_detail(request, slug, year, month):
    post = get_object_or_404(Post,
                pub_date__year=year,
                pub_date__month=month,
                slug__iexact=slug)
    return render(request,'blog/post_detail.html',{'post': post})


class PostUpdate(View):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form_update.html'


    def get_object(self, year, month, slug):
        return get_object_or_404(self.model,
                                 pub_date__year=year,
                                 pub_date__month=month,
                                 slug=slug)

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        # post = get_object_or_404(self.model,
        #                          pub_date__year=year,
        #                          pub_date__month=month,
        #                          slug=slug)
        context = {'form':self.form_class(instance=post),'post':post}

        return render(request, self.template_name, context)


    def post(self,request, year, month, slug):
        post = self.get_object(year, month, slug)
        # post = get_object_or_404(self.model,
        #                          pub_date__year=year,
        #                          pub_date__month=month,
        #                          slug=slug)
        bound_form = self.form_class(request.POST,instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)

        else:
            context = {'form':bound_form,'post':post}
            return render(request, self.template_name, context)


class PostDelete(View):
    def get(self, request, year, month, slug):
        post = get_object_or_404(Post,
                                 pub_date__year=year,
                                 pub_date__month=month,
                                 slug__iexact=slug)
        return render(request, 'blog/blog_post_delete.html', {'post':post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(Post,
                                 pub_date__year=year,
                                 pub_date__month=month,
                                 slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')
