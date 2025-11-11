"""Resources for Hammer MCP Server."""

from fastmcp import FastMCP

from .hammer_docs import register_hammer_docs
from .hammer_resources import register_hammer_resources


def register_resources(mcp: FastMCP):
    """Register all resources with the MCP server."""
    register_hammer_docs(mcp)
    register_hammer_resources(mcp)
