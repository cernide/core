from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = "core.background.scheduler"
    verbose_name = "Scheduler"

    def ready(self):
        import core.db.signals.runs  # noqa
        import core.db.signals.stats  # noqa
        import core.db.signals.stats  # noqa
        from core.common import auditor, conf
        from core.orchestration import executor, operations

        conf.validate_and_setup()
        operations.validate_and_setup()
        executor.validate_and_setup()
        auditor.validate_and_setup()

        import core.common.options.conf_subscriptions  # noqa
        from core.common.events import auditor_subscriptions  # noqa
