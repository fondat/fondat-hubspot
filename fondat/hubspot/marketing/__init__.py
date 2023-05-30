"""..."""

from .events import resource as events
from fondat.resource import resource


class MarketingResource:
    events = events


resource = MarketingResource()
