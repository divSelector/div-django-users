# div_django_users

This is a template for a basic allauth users app. It has a custom model with email for username.
It prevents not-superuser staff users from abusing the admin page (to some capacity).
It has stock templates and static files for the class based generic auth views.
It's a starting point.

## Quick start

1. Add "users" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        'users',
    	'allauth',
    	'allauth.account',
    	'allauth.socialaccount'
    ]

2. Include the polls URLconf in your project urls.py like this::

    urlpatterns = [
        path('users/', include('users.urls')),
        path('users/', include('allauth.urls')),
        path('admin/', admin.site.urls),
    ]

3. You will need these settings in your settings.py

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For development

    STATIC_ROOT = BASE_DIR / 'static'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = []

    SITE_ID = 1  # Required by Django-allauth
    LOGIN_REDIRECT_URL = '/'  # URL to redirect the user after login
    LOGIN_URL = "/users/login"

    AUTH_USER_MODEL = 'users.User'
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
    ACCOUNT_EMAIL_VERIFICATION = 'none'      # Require email verification for new accounts


4. Run `python manage.py migrate` to create the user model.
5. Run `python manage.py createsuperuser` to create a superuser to login.

6. Start the development server and visit http://127.0.0.1:8000/admin/

