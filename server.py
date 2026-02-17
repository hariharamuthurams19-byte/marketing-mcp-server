from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Marketing MCP Server")

TOOLS = [
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

@app.get("/")
def root():
    return {"server": "Marketing MCP Server"}

@app.get("/.well-known/mcp.json")
def mcp_manifest():
    return {
        "schema_version": "1.0",
        "name": "Marketing MCP Server",
        "description": "Marketing tools for analytics and audits",
        "tools": TOOLS
    }

class ToolRequest(BaseModel):
    tool: str
    input: Dict[str, Any]

@app.post("/run")
def run_tool(request: ToolRequest):
    if request.tool == "ab-test-analyzer":
        return {
            "result": f"Compared {request.input}"
        }

    return {"error": "Tool not found"}
