from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import plone.classicui


class PloneClassicUILayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plone.classicui)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.classicui:default")


PLONE_CLASSICUI_FIXTURE = PloneClassicUILayer()


PLONE_CLASSICUI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_CLASSICUI_FIXTURE,),
    name="PloneClassicUILayer:IntegrationTesting",
)
