import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
serverID = "Insert your server ID here"
base_url = "https://api.exaroton.com/v1"
ram = {"ram" : 2} #Change the RAM here, e.g. {"ram": 3} to set the server RAM to 3GB.


async def main():
    resp = await api_request(f"/server/{serverID}/options/ram/", "POST", ram)
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Change the amount of RAM assigned to the server to the amount specified in the ram POST parameter (in GB).

Example response:
{
   "success":true,
   "error":null,
   "data":{
      "ram":2
   }
}
'''