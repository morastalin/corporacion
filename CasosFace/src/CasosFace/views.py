from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from Seguridades.models import Author, Book
from Seguridades.forms import AuthorForm

import datetime

def nuevo_author(request):
    if request.method == 'POST':
        formulario = AuthorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/list_author')
    else:
        formulario = AuthorForm()
    return render_to_response('current_datetime.html',{'formulario':formulario}, context_instance=RequestContext(request))

def current_datetime(request):
    ahora = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'fecha_actual': ahora})

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = " <html><body>In %s hour(s), it will be %s .</body></html> " % (offset, dt)
    return HttpResponse(html)

def listBook(request):
    lista = Book.all()
    #lista = 3
    return render_to_response('lista.html',{'lista':lista})

