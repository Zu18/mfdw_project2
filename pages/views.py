from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . models import Page
from .forms import ContactForm

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


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(),
                                                  'submitted': submitted})







