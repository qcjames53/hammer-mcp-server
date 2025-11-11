"""Tools for Hammer MCP Server."""

from fastmcp import FastMCP

from .call_hammer_commands import register_hammer_commands


def register_tools(mcp: FastMCP):
    """Register all tools with the MCP server."""
    register_hammer_commands(mcp)
