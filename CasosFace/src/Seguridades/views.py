#from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.api import users

from Seguridades.models import Greeting

import urllib

def main_page(request):
    Seguridades_name = request.GET.get('Seguridades_name', 'default_seguridades')
    guestbook_key = Greeting.get_key_from_name(Seguridades_name)
    greetings_query = Greeting.all().ancestor(guestbook_key).order('-date')
    greetings = greetings_query.fetch(10)
    if users.get_current_user():
        url = users.create_logout_url(request.get_full_path())
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(request.get_full_path())
        url_linktext = 'Login'
    template_values = {
        'greetings': greetings,
        'Seguridades_name': Seguridades_name,
        'url': url,
        'url_linktext': url_linktext,
    }
    return render_to_response(request, 'Seguridades/main_page.html', template_values)

def sign_post(request):
    if request.method == 'POST':
        Seguridades_name = request.POST.get('Seguridades_name')
        guestbook_key = Greeting.get_key_from_name(Seguridades_name)
        greeting = Greeting(parent=guestbook_key)
    
        if users.get_current_user():
            greeting.author = users.get_current_user().nickname()
    
        greeting.content = request.POST.get('content')
        greeting.put()
        return HttpResponseRedirect('/?' + urllib.urlencode({'Seguridades_name': Seguridades_name}))
    return HttpResponseRedirect('/')
    