from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_group_to_new_user(sender, instance, created, **kwargs):
    if created:
        group_name = 'Читатели'
        try:
            group = Group.objects.get(name=group_name)
            instance.groups.add(group)
        except Group.DoesNotExist:
            print("Группа '{group_name}' не существует ")