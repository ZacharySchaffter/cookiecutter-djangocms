import logging
from django.shortcuts import render


log = logging.getLogger(__name__)


def bad_request(request):
    return render(request, 'web/errors/400.html', status=400)


def permission_denied(request):
    return render(request, 'web/errors/403.html', status=403)


def page_not_found(request):
    return render(request, 'web/errors/404.html', status=404)


def server_error(request):
    return render(request, 'web/errors/500.html', status=500)
