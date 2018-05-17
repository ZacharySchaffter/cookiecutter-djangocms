import logging
from django import template
from django.utils.translation import ugettext as _
from django.template.defaultfilters import stringfilter

log = logging.getLogger(__name__)

register = template.Library()

@register.inclusion_tag("ui/debug/debug_message.html", takes_context=True)
def debug_message(context, message):
    return {
        "debug": context["web_settings"]["debug"],
        "message": message
    }


@register.filter(name="json_loads")
@stringfilter
def json_loads(value):
    import json
    try:
        data = json.loads(value)
    except Exception as e:
        log.exception(e)
        data = None

    return data
