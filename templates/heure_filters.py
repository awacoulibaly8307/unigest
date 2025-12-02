from django import template

register = template.Library()

@register.filter
def to_minutes(horaire):
    """Convertit une heure 'HH:MM' en minutes totales."""
    try:
        h, m = str(horaire).split(":")
        return int(h) * 60 + int(m)
    except:
        return 0
