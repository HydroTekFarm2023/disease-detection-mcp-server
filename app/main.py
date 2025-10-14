from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")


@mcp.tool()
async def ping(name: str = "World") -> str:
    """A simple test tool that greets the user."""
    return f"Hello, {name}! The MCP server is working correctly."


if __name__ == "__main__":
    mcp.run()
