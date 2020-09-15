from django import template
register = template.Library()

@register.simple_tag
def get_verbose_field_name(field):
    """
    Returns verbose_name for a field.
    """
    return field.verbose_name