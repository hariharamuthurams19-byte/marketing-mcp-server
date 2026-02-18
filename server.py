from mcp.server import FastMCP

# Create MCP server
mcp = FastMCP("Marketing MCP Server")

# Define tool
@mcp.tool()
async def ab_test_analyzer(headline_a: str, headline_b: str):
    """
    Analyze A/B test headlines.
    """
    return {
        "headline_a": headline_a,
        "headline_b": headline_b,
        "analysis": f"Comparing '{headline_a}' vs '{headline_b}'."
    }

# This exposes FastAPI app for Render
app = mcp.app
