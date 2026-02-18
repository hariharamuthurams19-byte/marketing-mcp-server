from mcp.server.fastapi import create_mcp_app
from mcp.server import Server

# Create MCP server
server = Server(
    name="Marketing MCP Server",
    description="Marketing tools for analytics and audits"
)

# Define tool
@server.tool()
async def ab_test_analyzer(headline_a: str, headline_b: str) -> dict:
    """
    Analyze A/B test headlines.
    """
    return {
        "headline_a": headline_a,
        "headline_b": headline_b,
        "analysis": f"Comparing '{headline_a}' vs '{headline_b}'."
    }

# Create FastAPI app
app = create_mcp_app(server)
