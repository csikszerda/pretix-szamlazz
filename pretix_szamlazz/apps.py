from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_szamlazz"
    verbose_name = "Pretix Szamlazz.hu Plugin"

    class PretixPluginMeta:
        name = gettext_lazy("Pretix Szamlazz.hu Plugin")
        author = "Patrick Chilton"
        description = gettext_lazy("Szamlazz.hu integration for Pretix")
        visible = True
        version = __version__
        category = "PAYMENT"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA
