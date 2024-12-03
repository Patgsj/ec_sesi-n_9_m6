from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from books.models import Book

@receiver(post_save, sender=User)
def assign_development_permission(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Book)
        development_permission = Permission.objects.get(
            content_type=content_type,
            codename='development'
        )
        instance.user_permissions.add(development_permission)
