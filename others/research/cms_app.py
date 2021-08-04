from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ResearchApp(CMSApp):
    name = _("Research App")
    urls = ["research.urls"]
    app_name = "research"

apphook_pool.register(ResearchApp)