from django.views.generic import TemplateView
from django.utils.translation import ugettext as _
from django.shortcuts import render


# class SampleView(TemplateView):
#     template_name = "web/sample-view.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         return context


def bad_request(request):
    return render(request, 'web/400.html', status=400)


def permission_denied(request):
    return render(request, 'web/403.html', status=403)


def page_not_found(request):
    return render(request, 'web/404.html', status=404)


def server_error(request):
    return render(request, 'web/500.html', status=500)
