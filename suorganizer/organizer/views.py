from .models import Tag
from django.shortcuts import get_object_or_404, render
# from django.http.response import HttpResponse
# from django.template import loader, RequestContext



def homepage(request):
    return render(request, 'organizer/tag_list.html',
                        {'tag_list': Tag.objects.all()})
    # tag_list = Tag.objects.all()
    # template = loader.get_template('organizer/tag_list.html')
    # context = RequestContext(request,{'tag_list': tag_list})
    # output = template.render(context)
    # return HttpResponse(output)


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request,'organizer/tag_detail.html',
                                {'tag':tag})

    # template = loader.get_template('organizer/tag_detail.html')
    # context = RequestContext(request,{'tag': tag})
    # return HttpResponse(template.render(context))
