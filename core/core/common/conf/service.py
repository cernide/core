from core.common.conf.handlers.env_handler import EnvConfHandler
from core.common.conf.handlers.settings_handler import SettingsConfHandler
from core.common.conf.option_service import OptionService
from core.common.options.option import OptionStores


class ConfService(OptionService):
    def setup(self):
        super().setup()
        self.stores[OptionStores.SETTINGS] = SettingsConfHandler()
        self.stores[OptionStores.ENV] = EnvConfHandler()
