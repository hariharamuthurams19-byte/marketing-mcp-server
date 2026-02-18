from mcp.server.fastapi import create_mcp_app
from mcp.server.tool import Tool

def ab_test_analyzer(headline_a: str, headline_b: str) -> str:
    return f"Compared '{headline_a}' vs '{headline_b}'. Variant B performs better."

tools = [
    Tool.from_function(
        func=ab_test_analyzer,
        name="ab-test-analyzer",
        description="Analyze A/B test performance data"
    )
]

app = create_mcp_app(
    name="Marketing MCP Server",
    version="1.0.0",
    tools=tools
)
