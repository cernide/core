# isort: skip_file

from django.apps import AppConfig


class StreamsConfig(AppConfig):
    name = "core.streams"
    verbose_name = "Streams"

    def ready(self):
        from core.common import conf

        conf.validate_and_setup()

        import core.common.options.conf_subscriptions  # noqa
