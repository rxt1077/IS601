from django.shortcuts import render
from django.utils import timezone
from .models import Contact
from datetime import datetime
import json
from django.http import JsonResponse

def parse_date(get_params, key, default):
    """
    Try to pull a date out of the query parameters, returning the default value
    on any errors.
    """
    if key in get_params:
        try:
            return datetime.fromisoformat(get_params[key])
        except ValueError:
            return default
    else:
        return default

def main(request):
    start = parse_date(request.GET, 'start',
        datetime.fromisoformat('1970-01-01T00:00:00+00:00'))
    end = parse_date(request.GET, 'end', timezone.now())
    contacts = Contact.objects.filter(time__gte=start).filter(time__lte=end)

    # Build a list of nodes based on the contact reports
    nodes = {}
    for contact in contacts:
        nodes[contact.source_name] = {
            'lat': float(contact.source_lat),
            'lon': float(contact.source_lon),
        };
        nodes[contact.contact_name] = {
            'lat': float(contact.contact_lat),
            'lon': float(contact.contact_lon),
        };

    context = {
        'start': start,
        'end': end,
        'contacts': contacts,
        'nodes_json': json.dumps(nodes), # pass the list of nodes as a JSON string 
    }
    return render(request, 'main/main.html', context)
