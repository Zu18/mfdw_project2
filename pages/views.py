from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . models import Page


def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_update': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/page.html', context)






