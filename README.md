# Deep-Research-Viz
A Tool to turn Deep Research Results into Compelling Instagram Posts

## Running Deep Research within Deep-Research-Viz

The `deep-research` project is included as a submodule in this repository.
Refer to `deep-research/README.md` to install and setup

## Install ADK

`pip install google-adk`

References: https://google.github.io/adk-docs/get-started/quickstart/

## (Development) Run MCP Inspector
To inspect and testing `deep-research` MCP Server, run:
```
cd deep-research
npx @modelcontextprotocol/inspector
```

Transport Type: 
- Streamable HTTP

URL:
- https://localhost:<port>/api/mcp

Configuration:
- Increase Maximum Time Out if requests timed out

### To-do-list
- [X] Set up deep-research MCP server
- [ ] MCP Client to integrate deep-research into ADK
- [ ] Media Manager Agent
- [ ] Visual & Post Agent