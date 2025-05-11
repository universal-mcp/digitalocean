
from universal_mcp.servers import SingleMCPServer
from universal_mcp.integrations import AgentRIntegration
from universal_mcp.stores import EnvironmentStore

from universal_mcp_digitalocean.app import DigitaloceanApp

env_store = EnvironmentStore()
integration_instance = AgentRIntegration(name="digitalocean", store=env_store)
app_instance = DigitaloceanApp(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()


