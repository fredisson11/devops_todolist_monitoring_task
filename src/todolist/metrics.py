from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from django.http import HttpResponse

get_requests_counter = Counter('http_get_requests_total', 'Total number of GET requests')
post_requests_counter = Counter('http_post_requests_total', 'Total number of POST requests')

def metrics_view(request):
    if request.method == 'GET':
        get_requests_counter.inc()
    elif request.method == 'POST':
        post_requests_counter.inc()
    
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)