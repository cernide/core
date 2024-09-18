# isort: skip_file

from django.apps import AppConfig


class APIsConfig(AppConfig):
    name = "core.apis"
    verbose_name = "APIs"

    def ready(self):
        from core.common import conf
        from core.common import auditor
        from core.orchestration import executor, operations
        from core.common import query

        conf.validate_and_setup()
        query.validate_and_setup()
        operations.validate_and_setup()
        executor.validate_and_setup()
        auditor.validate_and_setup()

        import core.db.signals.runs  # noqa
        import core.db.signals.versions  # noqa
        import core.db.signals.bookmarks  # noqa
        import core.db.signals.stats  # noqa

        import core.common.options.conf_subscriptions  # noqa
        from core.common.events import auditor_subscriptions  # noqa
        from core.db.administration import register  # noqa
