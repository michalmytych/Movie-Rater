from django.core.management.utils import get_random_secret_key


def save_generated_key():
    with open('secrets.py', 'w') as secrets_file:
        KEY = get_random_secret_key()
        declaration = f'DJANGO_SECRET_KEY = "{KEY}"'
        secrets_file.write(declaration)

save_generated_key()        