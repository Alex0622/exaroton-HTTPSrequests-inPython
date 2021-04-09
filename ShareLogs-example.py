import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
serverID = "Insert your server ID here"
base_url = "https://api.exaroton.com/v1"



async def main():
    resp = await api_request(f"/server/{serverID}/logs/share/", "GET", {})
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Returns the mclo.gs API response data.

Example response:
{
   "success":true,
   "error":null,
   "data":{
      "id":"zCcf8T5",
      "url":"https://mclo.gs/zCcf8T5",
      "raw":"https://api.mclo.gs/1/raw/zCcf8T5"
   }
}
'''