"""Build a book with Jupyter Notebooks and Sphinx."""

__version__ = "0.13.1"

# Select compatible event loop for Tornado
# Default value on Windows changed with python 3.8

import asyncio
import sys

if sys.platform == "win32" and sys.version_info.minor >= 8:
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )



# We connect this function to the step after the builder is initialized
def setup(app):

    app.add_config_value("use_jupyterbook_latex", True, "env")
    app.add_config_value("use_multitoc_numbering", True, "env")

    # Extensions
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
