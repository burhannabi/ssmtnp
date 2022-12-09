from django.apps import AppConfig


class HumanResourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'human_resource'
    verbose_name = 'Human Resource(HR)'

    def signals(self):
        import human_resource.signals