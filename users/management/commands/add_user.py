from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Создаем новую группу «Менеджер продуктов»
        product_manager_group = Group.objects.create(name='Product manager')

        # Получаем разрешения на добавление и изменение продуктов
        add_product_permission = Permission.objects.get(codename='add_product')
        change_product_permission = Permission.objects.get(codename='change_product')

        # Назначаем разрешения группе
        product_manager_group.permissions.add(add_product_permission, change_product_permission)

        # Создаем новую группу «Модератор продуктов»
        product_moderator_group = Group.objects.create(name='Product moderator')

        # Получаем разрешения на публикацию и удаление продуктов
        can_unpublish_product_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_product_permission = Permission.objects.get(codename='delete_product')

        # Назначаем разрешения группе
        product_moderator_group.permissions.add(delete_product_permission, can_unpublish_product_permission)

        User = get_user_model()
        user = User.objects.create(
            username="Petrov Petr",
            email='petrov@webstore.ru',
            first_name='Petr',
            last_name='Petrov'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        User = get_user_model()
        user = User.objects.create(
            username="Ivanov Ivan",
            email='ivanov@webstore.ru',
            first_name='Ivan',
            last_name='Ivanov'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        User = get_user_model()
        user = User.objects.create(
            username="Vasiljev Vasilij",
            email='vasiljev@webstore.ru',
            first_name='Vasilij',
            last_name='Vasiljev'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        User = get_user_model()
        user = User.objects.create(
            username="Sergjev Sergey",
            email='sergejev@webstore.ru',
            first_name='Sergey',
            last_name='Sergjev'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        # Менеджеры продуктов
        user = CustomUser.objects.get(email='petrov@webstore.ru')
        product_manager_group = Group.objects.get(name='Product manager')
        user.groups.add(product_manager_group)

        user = CustomUser.objects.get(email='ivanov@webstore.ru')
        product_manager_group = Group.objects.get(name='Product manager')
        user.groups.add(product_manager_group)

        user = CustomUser.objects.get(email='vasiljev@webstore.ru')
        product_manager_group = Group.objects.get(name='Product manager')
        user.groups.add(product_manager_group)

        user = CustomUser.objects.get(email='sergejev@webstore.ru')
        product_manager_group = Group.objects.get(name='Product manager')
        user.groups.add(product_manager_group)

        # Модераторы продуктов
        user = CustomUser.objects.get(email='petrov@webstore.ru')
        product_manager_group = Group.objects.get(name='Product moderator')
        user.groups.add(product_manager_group)

        user = CustomUser.objects.get(email='ivanov@webstore.ru')
        product_manager_group = Group.objects.get(name='Product moderator')
        user.groups.add(product_manager_group)
