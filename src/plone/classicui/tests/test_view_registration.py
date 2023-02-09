from plone.classicui.testing import PLONE_CLASSICUI_INTEGRATION_TESTING

import unittest


class TestViewRegistration(unittest.TestCase):
    """Test that plone.classicui is properly registering views."""

    layer = PLONE_CLASSICUI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

    def test_registered_views_with_class(self):
        """Test if plone.classicui is installed."""
        for name in (
            "main_template",
            "test-rendering",
        ):
            view = self.portal.restrictedTraverse(name)

            # The view is an instance of
            # Products.Five.browser.metaconfigure.SimpleViewClass
            # based on the class specified in zcml.
            # This class is the second in the method resolution order.
            zcml_class = view.__class__.mro()[1]

            self.assertIn(
                "plone.classicui",
                zcml_class.__module__,
                f"View {name} not registered properly",
            )
