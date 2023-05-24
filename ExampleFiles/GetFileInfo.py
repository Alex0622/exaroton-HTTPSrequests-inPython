import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
serverID = "Insert your server ID here"
base_url = "https://api.exaroton.com/v1"
path = "server.properties"



async def main():
    resp = await api_request(f"/server/{serverID}/files/info/{path}/", "GET", {})
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Get file information.

Example response:
{
    "success": true, 
    "error": null, 
    "data": {
        "path": "/server.properties", 
        "name": "server.properties", 
        "isTextFile": true, 
        "isConfigFile": true, 
        "isDirectory": false, 
        "isLog": false, 
        "isReadable": false, 
        "isWritable": false, 
        "size": 1266, 
        "children": null
    }
}
'''