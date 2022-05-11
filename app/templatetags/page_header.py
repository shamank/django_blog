from django import template
from app.models import Category, Comment

register = template.Library()

@register.simple_tag()
def get_category(slug):
    return Category.objects.get(slug=slug)

@register.inclusion_tag('include/_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}

@register.inclusion_tag('include/_comments.html')
def show_comments(slug):
    comments = Comment.objects.filter(post__slug=slug)
    return {"comments": comments}

# @register.inclusion_tag('include/_navigation.html')
# def show_categories():
#     categories = Category.objects.all()
#     return {"categories": categories}