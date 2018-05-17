from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r"^",
        TemplateView.as_view(template_name="ui_kit/index.html"),
        name="ui-kit-index"
    ),
]
