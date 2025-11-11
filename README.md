# Hammer MCP Server

A Model Context Protocol (MCP) server implementation that enables LLMs to interact with Hammer CLI.

## Installation

1. Install hammer locally:
```bash
sudo dnf install rubygem-hammer_cli rubygem-hammer_cli_foreman ruby-devel gcc make
sudo gem install hammer_cli_katello
hammer --help
```
2. Set up your `~/.hammer/cli_config.yml` as shown (change hostname):
```
:modules:
  - hammer_cli_foreman
  - hammer_cli_katello

:foreman:
  :enable_module: true
  :host: 'https://<foreman hostname>'
  :verify_ssl: false
  :username: admin
  :password: changeme

:katello:
  :enable_module: true

:log_dir: '~/.hammer/log'
:log_level: 'debug'
```
3. Fetch your CA cert and install (change hostname):
```bash
hammer --fetch-ca-cert https://<foreman hostname>
sudo install ~/.hammer/certs/<foreman hostname>_443.pem /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust
hammer --help
```
4. Make sure your hammer binary is authenticated and can run normal hammer commands.
5. Install dependencies
```bash
uv sync
```

## Usage
Run the server with:

```bash
uv run hammer-mcp-server
```

Or with custom options:

```bash
uv run hammer-mcp-server --transport streamable-http --log-level DEBUG
```

## Development

Install development dependencies:

```bash
uv sync --group dev
```

Format and lint code:

```bash
uv run ruff check .
uv run ruff format .
```

MCP Inspector:
```bash
sudo dnf install nodejs
npx @modelcontextprotocol/inspector
```
Connect to `http://localhost:8080/mcp` using" Streamable HTTP".