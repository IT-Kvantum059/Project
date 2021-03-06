from django.http import HttpResponse
from django.template import loader

def show_phones(request):
    template = loader.get_template('snakes.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)