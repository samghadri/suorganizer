from .models import Tag, StartUp
from django.shortcuts import get_object_or_404, render
# from django.http.response import HttpResponse
# from django.template import loader, RequestContext


def tag_list(request):
    return render(request, 'organizer/tag_list.html',
                        {'tag_list': Tag.objects.all()})
    # tag_list = Tag.objects.all()
    # template = loader.get_template('organizer/tag_list.html')
    # context = RequestContext(request,{'tag_list': tag_list})
    # output = template.render(context)
    # return HttpResponse(output)


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request,'organizer/tag_detail.html', {'tag':tag})
    # template = loader.get_template('organizer/tag_detail.html')
    # context = RequestContext(request,{'tag': tag})
    # return HttpResponse(template.render(context))

def startup_list(request):
    return render(request, 'organizer/startup_list.html',
                        {'startup_list': StartUp.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(StartUp, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html',
                            {'startup':startup})
