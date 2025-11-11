from ..utils.hammer_utils import (
    execute_hammer_command_for_resource,
    lifecycle_environment_create,
    lifecycle_environment_delete,
    lifecycle_environment_info,
    lifecycle_environment_list,
)


def register_hammer_resources(mcp):
    @mcp.resource(
        name="Hammer CLI Full Help",
        description="Prints help for all available hammer commands, subcommands, and actions.",
        uri="hammer://full-help",
        mime_type="text/plain",
    )
    async def hammer_full_help() -> str:
        return await execute_hammer_command_for_resource("full-help")

    @mcp.resource(
        name="Generate Hammer CLI Lifecycle Environment List",
        description="Generates a hammer command for listing lifecycle environments. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-list",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_list() -> str:
        return f"hammer {lifecycle_environment_list()}"

    @mcp.resource(
        name="Execute Hammer CLI Lifecycle Environment List",
        description="Executes the hammer command to list lifecycle environments and returns the output.",
        uri="hammer://execute-lifecycle-environment-list",
        mime_type="text/plain",
    )
    async def execute_hammer_lifecycle_environment_list() -> str:
        return await execute_hammer_command_for_resource(lifecycle_environment_list())

    @mcp.resource(
        name="Generate Hammer CLI Lifecycle Environment Info",
        description="Generates a hammer command for getting lifecycle environment information. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-info/{organization_name}/{lifecycle_environment_name}",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_info(
        organization_name: str, lifecycle_environment_name: str
    ) -> str:
        return f"hammer {lifecycle_environment_info(organization_name, lifecycle_environment_name)}"

    @mcp.resource(
        name="Execute Hammer CLI Lifecycle Environment Info",
        description="Executes the hammer command to get lifecycle environment information and returns the output.",
        uri="hammer://execute-lifecycle-environment-info/{organization_name}/{lifecycle_environment_name}",
        mime_type="text/plain",
    )
    async def execute_hammer_lifecycle_environment_info(
        organization_name: str, lifecycle_environment_name: str
    ) -> str:
        return await execute_hammer_command_for_resource(
            lifecycle_environment_info(organization_name, lifecycle_environment_name)
        )

    @mcp.resource(
        name="Generate Hammer CLI Lifecycle Environment Create",
        description="Generates a hammer command for creating a lifecycle environment. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-create/{organization_name}/{lifecycle_environment_name}/{prior_lifecycle_environment_name}",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_create(
        organization_name: str,
        lifecycle_environment_name: str,
        prior_lifecycle_environment_name: str,
    ) -> str:
        return f"hammer {lifecycle_environment_create(organization_name, lifecycle_environment_name, prior_lifecycle_environment_name)}"

    @mcp.resource(
        name="Generate Hammer CLI Lifecycle Environment Delete",
        description="Generates a hammer command for deleting a lifecycle environment. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-delete/{organization_name}/{lifecycle_environment_name}",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_delete(
        organization_name: str,
        lifecycle_environment_name: str,
    ) -> str:
        return f"hammer {lifecycle_environment_delete(organization_name, lifecycle_environment_name)}"
