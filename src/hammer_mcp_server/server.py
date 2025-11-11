import logging

import click
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_context
from fastmcp.settings import LOG_LEVEL
from fastmcp.utilities.logging import configure_logging

from .resources import register_resources
from .tools import register_tools


def normalize_log_level(_ctx, _param, value):
    """Standardize log level input to uppercase."""
    if value:
        value = value.upper()
    return value


@click.command()
@click.option(
    "--port",
    default=8080,
    help="Port to listen on for HTTP",
    envvar="PORT",
    show_default=True,
)
@click.option(
    "--host",
    default="127.0.0.1",
    help="Host to listen on for HTTP",
    envvar="HOST",
    show_default=True,
)
@click.option(
    "--log-level",
    default="INFO",
    help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    callback=normalize_log_level,
    show_default=True,
)
@click.option(
    "--transport",
    default="streamable-http",
    help="Transport protocol to use (streamable-http, stdio)",
    show_default=True,
)
@click.pass_context
def main(
    ctx: click.Context,
    host: str,
    port: int,
    log_level: LOG_LEVEL,
    transport: str,
) -> int:
    """Run the Hammer MCP server."""

    # Default loggers
    logging.basicConfig(level=log_level)
    configure_logging(level=log_level)
    # Global logger for the MCP server
    logger = logging.getLogger("hammer_mcp_server")
    logger.setLevel(log_level)

    mcp = FastMCP(name="Hammer MCP Server")

    register_tools(mcp, get_context)
    register_resources(mcp, get_context)

    if transport == "stdio":
        mcp.run(transport="stdio", show_banner=False)
    else:
        mcp.run(
            transport="streamable-http",
            host=host,
            port=port,
            show_banner=False,
            log_level=log_level,
        )

    ctx.exit(0)
