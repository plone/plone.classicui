from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.base.utils import get_installer
from plone.classicui.testing import PLONE_CLASSICUI_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.classicui is properly installed."""

    layer = PLONE_CLASSICUI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if plone.classicui is installed."""
        self.assertTrue(self.installer.is_product_installed("plone.classicui"))

    def test_browserlayer(self):
        """Test that IPloneClassicUI is registered."""
        from plone.browserlayer import utils
        from plone.classicui.interfaces import IPloneClassicUI

        self.assertIn(IPloneClassicUI, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = PLONE_CLASSICUI_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("plone.classicui")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.classicui is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("plone.classicui"))

    def test_browserlayer_removed(self):
        """Test that IPloneClassicUI is removed."""
        from plone.browserlayer import utils
        from plone.classicui.interfaces import IPloneClassicUI

        self.assertNotIn(IPloneClassicUI, utils.registered_layers())
