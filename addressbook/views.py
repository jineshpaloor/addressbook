from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from addressbook.forms import AddressForm
from addressbook.models import Address

def home(request):
    addresses = Address.objects.all()
    return render_to_response('home.html',
                              {'addresses': addresses},
                              context_instance=RequestContext(request))


@csrf_exempt
def add_address(request):
    if request.method == 'POST':
        print 'post :',request.POST
        form = AddressForm(data=request.POST)
        print 'form...',form
        if form.is_valid():
            form.save()
            addresses = Address.objects.all()
            html = render_to_string('contacts.html', {'addresses':addresses})
        else:
            print 'form is invalid'
            html = render_to_string('add_contact.html', {'form':form})

    else:
        form = AddressForm()
        html = render_to_string('add_contact.html', {'form':form})

    data = {'html': html}
    json = simplejson.dumps(data)
    return HttpResponse(json, mimetype='application/json')

