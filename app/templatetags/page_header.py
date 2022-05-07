from django import template
from app.models import Category

register = template.Library()

@register.simple_tag()
def get_category(slug):
    return Category.objects.get(slug=slug)

@register.inclusion_tag('include/_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}