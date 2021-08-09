# Information about this repository.
This repository contains files that give you an example of how to do HTTPS requests using the exaroton API and Python. You can check the exaroton API documentation [here](https://developers.exaroton.com/).

# How to use "GET" in HTTPS requests using Python?
First of all you need to add your API token in the python file. Other files require a server ID to get logs, RAM, or other options of that server.
After adding your API token and (in case that it's needed) your server ID, you can simply execute the Python file.

# How to use "POST" in HTTPS requests using Python?
All files require your API token and server ID in order to work.
If you want to change the server RAM, you need to open the [ChangeServerRAM-example.py](https://github.com/Alex0622/exaroton-HTTPSrequests-inPython/blob/main/Example%20files/ChangeServerRAM-example.py) file and change the "ram" parameter to the new amount of RAM (in GB) that you want, now you just need to execute the file. 

![image](https://user-images.githubusercontent.com/70553543/128785913-d181071b-9f47-4710-906c-6b4f6bfaa5d7.png)

If you want to execute a Minecraft command you can open the [ExecuteServerCommand-example.py](https://github.com/Alex0622/exaroton-HTTPSrequests-inPython/blob/main/Example%20files/ExecuteServerCommand-example.py) file and change the "command" parameter to the one that you want to execute, then just execute the Python file.

![image](https://user-images.githubusercontent.com/70553543/128786179-3bf443c3-032b-4dfd-8f34-1041a89e11b2.png)




# How to get your API token on exaroton?
You can find your API token on your [exaroton account settings](https://exaroton.com/account/).
![image](https://user-images.githubusercontent.com/70553543/114220742-9bb56f80-9929-11eb-815f-fb64be29bc54.png)


# How to get your server ID?
You can see your server ID on the ["Servers"](https://exaroton.com/servers/) page below the server name or any server page on the left below the server name. The server ID starts with a #:

![image](https://user-images.githubusercontent.com/70553543/114220991-e9ca7300-9929-11eb-8961-6266419f26cf.png)

Note: you don't need to add the # on your serverID.
