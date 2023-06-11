from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

# def create_group_with_permission(name, models: Tuple[Model, str]):
#     group = Group.objects.create(name=name)

#     for model, codename in models:
#         content_type = ContentType.objects.get_for_model(model)
#         permission = Permission.objects.get(content_type=content_type, codename=codename)

#     group.permissions.add(permission)
#     return group


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            **extra_fields
        )
        user.set_password(password)
        user.save()

        # self.add_primary_email(user)

        return user


    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        return user


    # @staticmethod
    # def add_primary_email(user):
    #     email = EmailAddress.objects.create(
    #         user_id=user.id, 
    #         email=user.email, 
    #         primary=True
    #     )
    #     email.save()
