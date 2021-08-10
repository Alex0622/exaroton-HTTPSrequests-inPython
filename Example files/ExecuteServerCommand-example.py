import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
serverID = "Insert your server ID here"
base_url = "https://api.exaroton.com/v1"
command = {"command": "say Hellow World!"} #Change the command to the one that you want to execute, e.g. {"command": "say This is a test"}


async def main():
    resp = await api_request(f"/servers/{serverID}/command/", "POST", command)
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Execute Minecraft commands.

Example response:
{
  "success": true,
  "error": null,
  "data": null
}
'''