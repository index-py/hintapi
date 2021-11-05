import time
from pathlib import Path as FilePath

from typing_extensions import Annotated

from hintapi import HTTPException, HttpRoute, HintAPI, required_method
from hintapi.parameters.field_functions import Path
from hintapi.openapi import OpenAPI


def homepage():
    """
    Homepage
    """
    return "hello, hintapi"


def exc():
    raise Exception("For get debug page.")


def message():
    """
    Message

    For testing server send event response
    """

    def message_gen():
        for i in range(5):
            time.sleep(app.state.wait_time)
            yield {"id": i, "data": "hello"}

    return message_gen()


def sources(filepath: Annotated[str, Path()]):
    """
    Return source files
    """
    realpath = FilePath(".") / filepath.lstrip("./")
    if realpath.exists() and realpath.is_file():
        return realpath
    else:
        raise HTTPException(404)


app = HintAPI(
    debug=True,
    routes=[
        HttpRoute("/", homepage),
        HttpRoute("/exc", exc),
        HttpRoute("/message", message),
        HttpRoute("/sources/{filepath:any}", sources) @ required_method("GET"),
    ],
)
app.router << "/docs" // OpenAPI().routes
app.state.wait_time = 1
