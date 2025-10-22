# JP Morgan Payments API Documentation MCP Server

A Model Context Protocol (MCP) server for accessing JP Morgan Payments API documentation.

This MCP server provides tools to search Payments API documentation, fetch specific pages, and discover related content.

## Features

- **Read Documentation**: Fetch and convert API documentation pages to markdown format
- **Search Documentation**: Find relevant documentation using the API search API
- **Related Content**: Discover related pages for a given documentation URL

## Prerequisites

- Python 3.10 or newer
- Package manager: `uv` (recommended) or `pip`
- For development: Git and Node.js (for MCP Inspector)

## Installation

### Using uv (Recommended)

1. Install uv if you haven't already:
   ```bash
   pip install uv
   ```

2. Clone the repository and install the package:
   ```bash
   git clone <repository-url>
   cd mcp-for-api-documentation
   uv venv
   uv pip install -e .
   ```

### Using pip

```bash
pip install git+<repository-url>
```

## Usage

### Command Line

Run the MCP server directly from the command line:

```bash
jpmc.mcp-for-api-documentation
```

Or using the Python module:

```bash
python -m jpmc.mcp-for-api-documentation.server
```

### Local Testing

#### MacOS/Linux

Run the standalone MCP server:
```bash
uv --directory <path-to-project> run jpmc.mcp-for-api-documentation
```

With MCP Inspector:
```bash
npx @modelcontextprotocol/inspector uv --directory <path-to-project> run jpmc.mcp-for-api-documentation
```

#### Windows

```powershell
# Set up Python environment
cd <path-to-project>
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install "markdownify>=1.1.0" "mcp[cli]>=1.11.0" "pydantic>=2.10.6" "httpx>=0.27.0" "loguru>=0.7.0" "beautifulsoup4>=4.12.0"

# Run server standalone
python -m jpmc.mcp-for-api-documentation.server

# Or with MCP Inspector
npx @modelcontextprotocol/inspector python -m jpmc.mcp-for-api-documentation.server
```

## Integration with MCP Clients

Configure the MCP server in your MCP client (e.g., Copilot in VS Code or IntelliJ):

Note: you may need to adjust the command and it args based on your environment and installation method. For example,
(1) use the absolute path for "uv", or use "python" directly if "uv" is not available.
(2) in a corp network behind proxy, you may need to set up a "HTTP_PROXY" in the "env" section.

```json
{
  "mcpServers": {
    "jpmc.mcp-for-api-documentation": {
      "command": "uv",
      "args": [
        "--directory", 
         "<path-to-this-py-project>", 
        "run",
         "jpmc.mcp-for-api-documentation"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

## Available Tools

The server provides the following tools for accessing JP Morgan Payments API documentation:

### search_documentation

Searches across all API documentation using the official Search API.

**Parameters:**
```python
search_documentation(
    search_phrase: str,  # The phrase to search for
    limit: int = 10      # Maximum number of results (optional, default: 10)
) -> list[dict]          # Returns a list of matching document references
```

### read_documentation

Fetches and converts a specific API documentation page to markdown format.

**Parameters:**
```python
read_documentation(
    url: str            # URL of the documentation page to read
) -> str                # Returns markdown-formatted content
```

### related

Provides related content recommendations for a specific API documentation page.

**Parameters:**
```python
related(
    url: str             # URL of the documentation page to get recommendations for
) -> list[dict]          # Returns a list of related document references
```

## Example Queries, Prompts, or Instructions for LLM

```
Look up checkout-related documents, citing the sources
```
```
Find documentation about payment methods
```

```
Get related pages for https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/consumer-profile-management/payment-methods
```

```
I want to add a product to the merchant catalog, can you help me format the API request?
```
```
I want to setup a checkout intent session, can you help me format the API request?
```
```
I want to create a payment link, help me format the API request.
```
```
I am a merchant developer, I want to create a jpmc checkout setup intent call, using python. my merchant id is 451207-smoke-tests-orb-diu.
```


## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest tests/
```

### Environment Variables

- `HTTP_PROXY` / `HTTPS_PROXY`: Proxy server for HTTP requests (optional)
- `FASTMCP_LOG_LEVEL`: Logging level (default: WARNING)

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE) files for details.
