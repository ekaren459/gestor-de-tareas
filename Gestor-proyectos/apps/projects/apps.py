from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.projects'

    def ready(self):
        # Import signals to register audit logging
        try:
            from . import signals  # noqa: F401
        except Exception:
            pass
