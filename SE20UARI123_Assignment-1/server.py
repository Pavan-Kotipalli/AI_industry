import asyncio
import websockets

async def server(websocket, path):
    message = "Hello from the server!"
    await websocket.send(message)
    reply = await websocket.recv()
    print(f"Received reply from client: {reply}")

start_server = websockets.serve(server, "139.59.28.124", 9000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
