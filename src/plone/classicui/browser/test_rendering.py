from Products.Five import BrowserView


class TestRenderingRedirectView(BrowserView):
    def __call__(self):
        self.request.response.redirect(
            f"{self.context.absolute_url()}/@@test-rendering"
        )


class TestRenderingView(BrowserView):
    def __call__(self):
        self.request.set("disable_plone.rightcolumn", 1)
        self.request.set("disable_plone.leftcolumn", 1)
        return super().__call__()
