from plone.app.layout.viewlets.common import ViewletBase
from plone.base.interfaces import ISearchSchema
from plone.registry.interfaces import IRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.component import getUtility


class SearchBoxViewlet(ViewletBase):
    index = ViewPageTemplateFile("searchbox.pt")

    def update(self):
        super().update()

        context_state = getMultiAdapter(
            (self.context, self.request), name="plone_context_state"
        )

        registry = getUtility(IRegistry)
        search_settings = registry.forInterface(ISearchSchema, prefix="plone")
        self.livesearch = search_settings.enable_livesearch
        self.show_images = search_settings.search_show_images

        folder = context_state.folder()
        self.folder_path = "/".join(folder.getPhysicalPath())
