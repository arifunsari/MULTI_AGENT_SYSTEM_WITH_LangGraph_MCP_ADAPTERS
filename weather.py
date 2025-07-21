from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather location."""
    return {
  "state": "California",
  "weather": {
    "temperature_celsius": 27,
    "humidity_percent": 60,
    "condition": "Partly Cloudy",
    "updated_at": "2025-07-21T17:30:00Z"
  }
}

if __name__=="__main__":
    mcp.run(transport="streamable-http")
