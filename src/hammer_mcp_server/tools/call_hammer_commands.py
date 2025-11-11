from fastmcp.tools.tool import ToolResult

from ..utils.hammer_utils import (
    execute_hammer_command_for_tool,
    lifecycle_environment_create,
    lifecycle_environment_delete,
    organization_create,
    organization_delete,
    organization_update,
)


def register_hammer_commands(mcp):
    @mcp.tool(
        description="Execute a hammer CLI command with any arguments and return its output. Use "
        "this ONLY when the user explicitly wants to execute a command on the MCP server's "
        "environment. A leading 'hammer' is NOT required in the command.",
        tags=("hammer", "cli", "command", "local"),
        annotations={
            "title": "Execute Hammer CLI Command",
            "readOnlyHint": False,
            "destructiveHint": True,  # Hammer can be destructive
            "idempotentHint": False,
            "openWorldHint": False,
        },
    )
    async def execute_hammer(command: str) -> ToolResult:
        return await execute_hammer_command_for_tool(command)

    @mcp.tool(
        description="Create a new lifecycle environment in Foreman. Requires organization name, "
        "new lifecycle environment name, and the name of the prior lifecycle environment.",
        tags=("hammer", "lifecycle-environment", "create", "destructive"),
        annotations={
            "title": "Execute Hammer CLI Lifecycle Environment Create",
            "readOnlyHint": False,
            "destructiveHint": True,
            "idempotentHint": False,
            "openWorldHint": False,
        },
    )
    async def execute_hammer_lifecycle_environment_create(
        organization_name: str,
        lifecycle_environment_name: str,
        prior_lifecycle_environment_name: str = "Library",
    ) -> ToolResult:
        command = lifecycle_environment_create(
            organization_name,
            lifecycle_environment_name,
            prior_lifecycle_environment_name,
        )
        return await execute_hammer_command_for_tool(command)

    @mcp.tool(
        description="Delete a lifecycle environment in Foreman. Requires organization name and lifecycle environment name.",
        tags=("hammer", "lifecycle-environment", "delete", "destructive"),
        annotations={
            "title": "Execute Hammer CLI Lifecycle Environment Delete",
            "readOnlyHint": False,
            "destructiveHint": True,
            "idempotentHint": False,
            "openWorldHint": False,
        },
    )
    async def execute_hammer_lifecycle_environment_delete(
        organization_name: str, lifecycle_environment_name: str
    ) -> ToolResult:
        command = lifecycle_environment_delete(
            organization_name, lifecycle_environment_name
        )
        return await execute_hammer_command_for_tool(command)

    @mcp.tool(
        description="Create a new organization in Foreman/Katello with the given name.",
        tags=("hammer", "organization", "create", "destructive"),
        annotations={
            "title": "Execute Hammer CLI Organization Create",
            "readOnlyHint": False,
            "destructiveHint": True,
            "idempotentHint": False,
            "openWorldHint": False,
        },
    )
    async def execute_hammer_organization_create(name: str) -> ToolResult:
        command = organization_create(name)
        return await execute_hammer_command_for_tool(command)

    @mcp.tool(
        description="Update an existing organization in Foreman/Katello. Can update name and/or description.",
        tags=("hammer", "organization", "update", "destructive"),
        annotations={
            "title": "Execute Hammer CLI Organization Update",
            "readOnlyHint": False,
            "destructiveHint": True,
            "idempotentHint": False,
            "openWorldHint": False,
        },
    )
    async def execute_hammer_organization_update(
        name: str, new_name: str = "", description: str = ""
    ) -> ToolResult:
        command = organization_update(name, new_name, description)
        return await execute_hammer_command_for_tool(command)

    @mcp.tool(
        description="Delete an organization from Foreman/Katello.",
        tags=("hammer", "organization", "delete", "destructive"),
        annotations={
            "title": "Execute Hammer CLI Organization Delete",
            "readOnlyHint": False,
            "destructiveHint": True,
            "idempotentHint": False,
            "openWorldHint": False,
        },
    )
    async def execute_hammer_organization_delete(name: str) -> ToolResult:
        command = organization_delete(name)
        return await execute_hammer_command_for_tool(command)
