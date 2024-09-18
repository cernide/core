from django.apps import AppConfig


class DBConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "core.db.pgsql.db"
    verbose_name = "DB"
