from django.apps import AppConfig


class NewsConfig(AppConfig):  # App initializing
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Новости'
