from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"server": "Marketing MCP Server"}

@app.get("/.well-known/mcp.json")
def mcp_manifest():
    return {
        "schema_version": "1.0",
        "name": "Marketing MCP Server",
        "description": "Marketing tools for analytics and audits",
        "tools": [
            {
                "name": "ab-test-analyzer",
                "description": "Analyze A/B test performance data",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "headline_a": {"type": "string"},
                        "headline_b": {"type": "string"}
                    },
                    "required": ["headline_a", "headline_b"]
                }
            }
        ]
    }
