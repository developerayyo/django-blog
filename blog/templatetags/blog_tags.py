from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

# custom tags
# simple tag to retrieve the total post published on the blog
register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


# inclusion tag to display latest posts in the sidebar of the blog
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# custom tag to display the most commented posts
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


# custom filter to enable md syntax for blog posts.
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
