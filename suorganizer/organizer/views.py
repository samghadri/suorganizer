from django.shortcuts import get_object_or_404, render,redirect
from django.core.urlresolvers import reverse_lazy
from .models import Tag, StartUp, NewsLink
from .forms import TagForm, StartUpForm, NewsLinkForm
from django.views.generic import View
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.http.response import HttpResponse
# from django.template import loader, RequestContext


class Taglist(View):
    page_kwarg = 'page'
    template_name = 'organizer/tag_list.html'
    paginate_by = 5

    def get(self, request):
        tags = Tag.objects.all()
        paginator = Paginator(tags,
                            self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_kwarg,
                        n=page.previous_page_number())
        else:
            prev_url = None

        if page.has_next():
            next_url = '?{pkw}={n}'.format(pkw=self.page_kwarg,
                        n=page.next_page_number())
        else:
            next_url = None

        context = {
            "is_paginated": page.has_other_pages(),
            "next_page_url": next_url,
            "paginator": paginator,
            "previous_page_url": prev_url,
            'tag_list': page}

        return render(request, self.template_name, context)
# def tag_list(request):
#     return render(request, 'organizer/tag_list.html',
#                         {'tag_list': Tag.objects.all()})
    # tag_list = Tag.objects.all()
    # template = loader.get_template('organizer/tag_list.html')
    # context = RequestContext(request,{'tag_list': tag_list})
    # output = template.render(context)
    # return HttpResponse(output)

# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             new_tag.save()
#             return redirect(new_tag)
#         else:
#             form = TagForm()
#         return render(request, 'organizer/tag_form.html', {'form':form})

class TagCreate(ObjectCreateMixin,View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    # def get(self, request):
    #     return render(request, self.template_name, {'form':self.form_class()})
    #
    # def post(self, request):
    #     bound_form = self.form_class(request.POST)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     else:
    #         return render(request, self.template_name,{'form':bound_form})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request,'organizer/tag_detail.html', {'tag':tag})
    # template = loader.get_template('organizer/tag_detail.html')
    # context = {'tag': tag}
    # return HttpResponse(template.render(context))


class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = 'organizer/tag_form_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy('organizer:organizer_tag_list')
    template_name = 'organizer/tag_confirm_delete.html'


class StartupList(View):
    page_kwarg = 'page'
<<<<<<< HEAD
    paginate_by  = 5 #items per page
=======
    paginate_by  = 1 #items per page
>>>>>>> 373d39fc627fd105dbf5742f92f96e6e5549813d
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = StartUp.objects.all()
        paginator = Paginator(startups, self.paginate_by)
<<<<<<< HEAD
        page = paginator.page(1)
        context = {'is_paginated': page.has_other_pages(),
                   'paginator': paginator,
                   'startup_list': page}
        return render(request, self.template_name, context)


class StartupCreate(ObjectCreateMixin, View):

    form_class = StartUpForm
    template_name = 'organizer/startup_form.html'

=======
        page_number = request.GET.get(self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_kwarg,
                        n=page.previous_page_number())
        else:
            prev_url = None

        if page.has_next():
            next_url = '?{pkw}={n}'.format(pkw=self.page_kwarg,
                        n=page.next_page_number())
        else:
            next_url = None
        context = {'is_paginated': page.has_other_pages(),
                   'next_page_url': next_url,
                   'paginator': paginator,
                   'previous_page_url': prev_url,
                   'startup_list': page}
        return render(request, self.template_name, context)


class StartupCreate(ObjectCreateMixin, View):

    form_class = StartUpForm
    template_name = 'organizer/startup_form.html'

>>>>>>> 373d39fc627fd105dbf5742f92f96e6e5549813d
    # def get(self, request):
    #     return render(request, self.template_name,{'form':self.form_class()})
    #
    # def post(self, request):
    #     bound_form = self.form_class(request.POST)
    #     if bound_form.is_valid():
    #         new_startup =  bound_form.save()
    #         return redirect(new_startup)
    #     else:
    #         return render(request, self.template_name, {'form':bound_form})

class StartUpUpdate(ObjectUpdateMixin, View):
    form_class = StartUpForm
    model = StartUp
    template_name = 'organizer/startup_form_update.html'

def startup_detail(request, slug):
    startup = get_object_or_404(StartUp, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html',
                            {'startup':startup})

class StartUpDelete(ObjectDeleteMixin, View):
    model = StartUp
    success_url = reverse_lazy('organizer:organizer_startup_list')
    template_name = 'organizer/startup_confirm_delete.html'

class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

    # def get(self, request):
    #     return render(request, self.template_name,{'form':self.form_class()})
    #
    # def post(self, request):
    #     bound_form = self.form_class(request.POST)
    #     if bound_form.is_valid():
    #         new_newslink = bound_form.save()
    #         return redirect(new_newslink)
    #     else:
    #         return render(request, self.template_name, {'form':bound_form})


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_update.html'

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        context = {'form':self.form_class(instance=newslink), 'newslink':newslink}
        return render(request, self.template_name, context )

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink,pk=pk)
        bound_form = self.form_class(request.POST,instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {'form':bound_form,'newslink':newslink}
            return render(request,self.template_name, context)

class NewsLinkDelete(View):
    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        return render(request, 'organizer/newslink_confirm_delete.html')

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        startup = newslink.startup.delete()
        return redirect(startup)
