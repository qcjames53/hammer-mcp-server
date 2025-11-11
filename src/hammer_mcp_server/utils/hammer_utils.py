import asyncio
import shlex

from fastmcp.tools.tool import ToolResult

from hammer_mcp_server.utils.content_utils import build_tool_result


def build_success_structured_content(
    command: str, output: str, returncode: int
) -> dict:
    """Build structured content for a successful hammer command execution."""
    return {
        "message": f"Hammer command executed successfully: hammer {command}",
        "command": f"hammer {command}",
        "output": output,
        "returncode": returncode,
    }


def build_failure_structured_content(
    command: str, output: str, error: str, returncode: int
) -> dict:
    """Build structured content for a failed hammer command execution."""
    return {
        "message": f"Hammer command failed: hammer {command}",
        "command": f"hammer {command}",
        "output": output,
        "error": error,
        "returncode": returncode,
    }


async def execute_hammer_command_for_tool(command: str) -> ToolResult:
    process = await asyncio.create_subprocess_exec(
        "hammer",
        *shlex.split(command),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await process.communicate()

    # Decode output
    stdout_text = stdout.decode("utf-8") if stdout else ""
    stderr_text = stderr.decode("utf-8") if stderr else ""

    if process.returncode == 0:
        return build_tool_result(
            build_success_structured_content(command, stdout_text, process.returncode)
        )
    else:
        return build_tool_result(
            build_failure_structured_content(
                command, stdout_text, stderr_text, process.returncode
            )
        )


async def execute_hammer_command_for_resource(command: str) -> str:
    process = await asyncio.create_subprocess_exec(
        "hammer",
        *shlex.split(command),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        return stdout.decode("utf-8")
    else:
        return f"error: Hammer CLI command failed with error: {stderr.decode('utf-8')}"


def lifecycle_environment_list() -> str:
    return "lifecycle-environment list"


def lifecycle_environment_info(
    organization_name: str, lifecycle_environment_name: str
) -> str:
    return f"lifecycle-environment info --organization {shlex.quote(organization_name)} --name {shlex.quote(lifecycle_environment_name)}"


def lifecycle_environment_create(
    organization_name: str,
    lifecycle_environment_name: str,
    prior_lifecycle_environment_name: str,
) -> str:
    return f'lifecycle-environment create --organization {shlex.quote(organization_name)} --name {shlex.quote(lifecycle_environment_name)} --prior {shlex.quote(prior_lifecycle_environment_name)} --description "Created by Hammer MCP Server"'


def lifecycle_environment_delete(
    organization_name: str, lifecycle_environment_name: str
) -> str:
    return f"lifecycle-environment delete --organization {shlex.quote(organization_name)} --name {shlex.quote(lifecycle_environment_name)}"
