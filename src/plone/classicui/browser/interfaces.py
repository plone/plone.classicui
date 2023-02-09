from zope.interface import Attribute
from zope.interface import Interface


class IMainTemplate(Interface):
    """Interface to the view that generated the main_template"""

    macros = Attribute("Macros")
    template_name = Attribute("Template name")
