from ..utils.hammer_utils import (
    execute_hammer_command_for_resource,
    lifecycle_environment_create,
    lifecycle_environment_delete,
    lifecycle_environment_info,
    lifecycle_environment_list,
    organization_create,
    organization_delete,
    organization_info,
    organization_list,
    organization_update,
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
        name="Generate Hammer CLI Lifecycle Environment List Command",
        description="Generates a hammer command for listing lifecycle environments. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-list",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_list() -> str:
        return f"hammer {lifecycle_environment_list()}"

    @mcp.resource(
        name="Execute Hammer CLI Lifecycle Environment List Command",
        description="Executes the hammer command to list lifecycle environments and returns the output.",
        uri="hammer://execute-lifecycle-environment-list",
        mime_type="text/plain",
    )
    async def execute_hammer_lifecycle_environment_list() -> str:
        return await execute_hammer_command_for_resource(lifecycle_environment_list())

    @mcp.resource(
        name="Generate Hammer CLI Lifecycle Environment Info Command",
        description="Generates a hammer command for getting lifecycle environment information. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-info/{organization_name}/{lifecycle_environment_name}",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_info(
        organization_name: str, lifecycle_environment_name: str
    ) -> str:
        return f"hammer {lifecycle_environment_info(organization_name, lifecycle_environment_name)}"

    @mcp.resource(
        name="Execute Hammer CLI Lifecycle Environment Info Command",
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
        name="Generate Hammer CLI Lifecycle Environment Create Command",
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
        name="Generate Hammer CLI Lifecycle Environment Delete Command",
        description="Generates a hammer command for deleting a lifecycle environment. Does not execute the command.",
        uri="hammer://generate-lifecycle-environment-delete/{organization_name}/{lifecycle_environment_name}",
        mime_type="text/plain",
    )
    async def generate_hammer_lifecycle_environment_delete(
        organization_name: str,
        lifecycle_environment_name: str,
    ) -> str:
        return f"hammer {lifecycle_environment_delete(organization_name, lifecycle_environment_name)}"

    @mcp.resource(
        name="Generate Hammer Organization List Command",
        description="Generates a hammer command for listing organizations. Does not execute the command.",
        uri="hammer://generate-organization-list",
        mime_type="text/plain",
    )
    async def generate_hammer_organization_list() -> str:
        return f"hammer {organization_list()}"

    @mcp.resource(
        name="Execute Hammer CLI Organization List Command",
        description="Executes the hammer command to list organizations and returns the output.",
        uri="hammer://execute-organization-list",
        mime_type="text/plain",
    )
    async def execute_hammer_organization_list() -> str:
        return await execute_hammer_command_for_resource(organization_list())

    @mcp.resource(
        name="Generate Hammer Organization Info Command",
        description="Generates a hammer command for getting organization information. Does not execute the command.",
        uri="hammer://generate-organization-info/{name}",
        mime_type="text/plain",
    )
    async def generate_hammer_organization_info(name: str) -> str:
        return f"hammer {organization_info(name)}"

    @mcp.resource(
        name="Execute Hammer CLI Organization Info Command",
        description="Executes the hammer command to get organization information and returns the output.",
        uri="hammer://execute-organization-info/{name}",
        mime_type="text/plain",
    )
    async def execute_hammer_organization_info(name: str) -> str:
        return await execute_hammer_command_for_resource(organization_info(name))

    @mcp.resource(
        name="Generate Hammer Organization Create Command",
        description="Generates a hammer command for creating an organization. Does not execute the command.",
        uri="hammer://generate-organization-create/{name}",
        mime_type="text/plain",
    )
    async def generate_hammer_organization_create(name: str) -> str:
        return f"hammer {organization_create(name)}"

    @mcp.resource(
        name="Generate Hammer Organization Update Command",
        description="Generates a hammer command for updating an organization. Does not execute the command.",
        uri="hammer://generate-organization-update/{name}/{new_name}/{description}",
        mime_type="text/plain",
    )
    async def generate_hammer_organization_update(
        name: str, new_name: str = "", description: str = ""
    ) -> str:
        return f"hammer {organization_update(name, new_name, description)}"

    @mcp.resource(
        name="Generate Hammer Organization Delete Command",
        description="Generates a hammer command for deleting an organization. Does not execute the command.",
        uri="hammer://generate-organization-delete/{name}",
        mime_type="text/plain",
    )
    async def generate_hammer_organization_delete(name: str) -> str:
        return f"hammer {organization_delete(name)}"
