#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
""" This is Django ORM
>>> from posts.models import Post
>>> p = Post()
>>> p 
<Post: Post object (None)>
>>> p.title = "My First Post!" 
>>> p.save()
>>> p
<Post: Post object (1)>
>>> p.print()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Post' object has no attribute 'print'
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
>>> exit()
"""