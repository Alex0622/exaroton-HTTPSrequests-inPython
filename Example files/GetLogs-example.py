import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
serverID = "Insert your server ID here"
base_url = "https://api.exaroton.com/v1"



async def main():
    resp = await api_request(f"/server/{serverID}/logs/", "GET", {})
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Returns the contents of the latest server log file. This data is cached and will not show the latest changes immediately while the server is running.

Example response:
{
   "success":true,
   "error":null,
   "data":{
      "content":"[16:14:36] [main/INFO]: Environment: authHost='https://authserver.mojang.com', accountsHost='https://api.mojang.com', sessionHost='https://sessionserver.mojang.com', servicesHost='https://api.minecraftservices.com', name='PROD'\n[16:14:37] [main/INFO]: Reloading ResourceManager: Default, bukkit\n[16:14:38] [Worker-Main-5/INFO]: Loaded 7 recipes\n[16:14:40] [Server thread/INFO]: Starting minecraft server version 1.16.5\n[16:14:40] [Server thread/INFO]: Loading properties\n[16:14:40] [Server thread/INFO]: This server is running Paper version git-Paper-444 (MC: 1.16.5) (Implementing API version 1.16.5-R0.1-SNAPSHOT)\n[16:14:40] [Server thread/INFO]: Using 4 threads for Netty based IO\n[16:14:40] [Server thread/INFO]: Server Ping Player Sample Count: 12\n[16:14:40] [Server thread/INFO]: Debug logging is disabled\n[16:14:40] [Server thread/INFO]: Default game type: SURVIVAL\n[16:14:40] [Server thread/INFO]: Generating keypair\n[16:14:40] [Server thread/INFO]: Starting Minecraft server on *:48249\n[16:14:40] [Server thread/INFO]: Using epoll channel type\n[16:14:40] [Server thread/INFO]: Server permissions file permissions.yml is empty, ignoring it\n[16:14:40] [Server thread/INFO]: Preparing level "world"\n[16:14:41] [Server thread/INFO]: Preparing start region for dimension minecraft:overworld\n[16:14:41] [Server thread/INFO]: Loaded 0 spawn chunks for world world\n[16:14:41] [Server thread/INFO]: Preparing spawn area: 0%\n[16:14:41] [Server thread/INFO]: Preparing spawn area: 0%\n[16:14:42] [Server thread/INFO]: Preparing spawn area: 11%\n[16:14:42] [Server thread/INFO]: Time elapsed: 1053 ms\n[16:14:44] [Server thread/INFO]: Starting GS4 status listener\n[16:14:44] [Server thread/INFO]: Thread Query Listener started\n[16:14:44] [Query Listener #1/INFO]: Query running on **.**.**.**:9898\n[16:14:44] [Server thread/INFO]: Running delayed init tasks\n[16:14:44] [Server thread/INFO]: Done (4.114s)! For help, type "help"\n[16:14:44] [Server thread/INFO]: Timings Reset\n[16:14:53] [User Authenticator #1/INFO]: UUID of player MonkeyPlayz is 2d2d446f-6e27-7420-7061-6e6963212d2d\n[16:14:53] [Server thread/INFO]: MonkeyPlayz joined the game\n[16:14:53] [Server thread/INFO]: MonkeyPlayz[/**.**.**.**:36932] logged in with entity id 483 at ([world]51.5113281, 33.8125, -0.0774191)\n[16:21:42] [Server thread/INFO]: MonkeyPlayz missed the ground whilst trying to escape Bat\n[16:28:07] [Server thread/WARN]: MonkeyPlayz was kicked for floating too long!\n[16:28:07] [Server thread/INFO]: MonkeyPlayz lost connection: Flying is not enabled on this server\n[16:28:07] [Server thread/INFO]: MonkeyPlayz left the game\n[16:34:37] [Server thread/INFO]: Stopping the server\n[16:34:37] [Server thread/INFO]: Stopping server\n[16:34:37] [Server thread/INFO]: Saving players\n[16:34:37] [Server thread/INFO]: Saving worlds\n"
   }
}
'''
