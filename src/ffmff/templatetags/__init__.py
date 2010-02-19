from django.template import add_to_builtins
from templatetags import smart_if

# until the standard if is smarter
add_to_builtins('templatetags.smart_if')
