import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
base_url = "https://api.exaroton.com/v1"


async def main():
    resp = await api_request("/servers/", "GET", {})
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Returns a list of servers that your account can access.

Example response:
{
   "success":true,
   "error":null,
   "data":[
      {
         "id":"EwYiY9IAMtQBTb6U",
         "name":"example",
         "address":"example.exaroton.me",
         "motd":"Welcome to the server of example!",
         "status":0,
         "host":null,
         "port":null,
         "players":{
            "max":20,
            "count":0,
            "list":[]
         },
         "software":{
            "id":"kb4p09ABvLjxzedx",
            "name":"Vanilla",
            "version":"1.16.5"
         },
         "shared":false
      }
   ]
}
'''

