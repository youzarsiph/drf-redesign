""" Customizes template tags from DRF """

from django.template import Library
from django.urls import NoReverseMatch, reverse
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe


# Create your tags here.
register = Library()


@register.simple_tag
def optional_login(request):
    """Include a login snippet if REST framework's login view is in the URLconf."""

    try:
        login_url = reverse("rest_framework:login")

    except NoReverseMatch:
        return ""

    snippet = """
    <a class="dropdown-item" href="{href}?next={next}">
      <strong class="d-flex align-items-center gap-3">
        <i class="bi bi-box-arrow-in-right"></i>
        Login
      </strong>
    </a>"""

    snippet = format_html(
        snippet,
        href=login_url,
        next=escape(request.path),
    )

    return mark_safe(snippet)


@register.simple_tag
def optional_logout(request, user, csrf_token):
    """Include a logout snippet if REST framework's logout view is in the URLconf."""

    try:
        logout_url = reverse("rest_framework:logout")

    except NoReverseMatch:
        snippet = format_html(
            '<li class="dropdown-item">{user}</li>',
            user=escape(user),
        )
        return mark_safe(snippet)

    snippet = """
    <form method="post" action="{href}?next={next}">
      <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
    
      <button type="submit" class="dropdown-item">
        <strong class="d-flex align-items-center gap-3">
          <i class="bi bi-box-arrow-right"></i>
          Logout
        </strong>
      </button>
    </form>"""

    snippet = format_html(
        snippet,
        user=escape(user),
        href=logout_url,
        next=escape(request.path),
        csrf_token=csrf_token,
    )

    return mark_safe(snippet)
