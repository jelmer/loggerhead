from sqlobject import *

from turbogears.database import PackageHub

hub = PackageHub("loggerhead")
__connection__ = hub

# class YourDataClass(SQLObject):
#     pass

