from typedweb import Routes
from typedweb.routing.extensions import FileRoutes


def test_empty_fileroutes():
    assert (Routes() + FileRoutes("typedweb.openapi")) == (
        Routes() + FileRoutes("typedweb.routing")
    )
