from django.shortcuts import render, render_to_response # funcoes de renderizacao dos templates
from investidores.forms import DesejoForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from investidores.models import Desejo


def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = DesejoForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = DesejoForm() # An unbound form

    return render(request, 'desejo.html', {
        'form': form,
    })
    
    

class IndexView(generic.ListView):
    template_name = 'desejos/index.html'
    context_object_name = 'latest_poll_list'

    '''
    def get_queryset(self):
        """Return the last five published polls."""
        return Desejo.objects.all()
    '''
    