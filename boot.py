import network
import machine
import settings
print("boot file")

import uasyncio as asyncio
import usocket as socket
import machine
async def handle_client(client):
    while True:
        data = await client.readline()
        if not data:
            machine.Pin(2, machine.Pin.OUT).value(1)  # Turn on LED 1
        else    
            print("Received:", data)
            await client.write(data)

async def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((settings.__IP__, 21))
    server_socket.listen(1)
    print("Server listening on port 8080")

    while True:
        client, addr = server_socket.accept()
        print("Connected by", addr)
        asyncio.create_task(handle_client(client))



# verify new firmware exit or not
if settings.__FIRMWARE_STATUS__ == settings.__NEW_FIRMWARE__:
    print("New firmware!")
    settings.__FIRMWARE_TOGGLE__ = not settings.__FIRMWARE_TOGGLE__
    print(settings.__FIRMWARE_TOGGLE__)
    
if settings.__FIRMWARE_MODE__ == settings.__F1__:
    print("Enter in F1!")
    # Open the files using 'with' to ensure proper closing
    #with open(settings.__F2__, "w") as into_file, open(settings.__F1__, "r") as get_file:
    #    into_file.write(get_file.read())
    settings.run(settings.__F1_NAME__) 

    
loop = asyncio.get_event_loop()
loop.create_task(server())
loop.run_forever()
