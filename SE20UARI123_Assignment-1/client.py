#client
import asyncio
import websockets

async def client():
    async with websockets.connect("ws://143.110.242.113:9000") as websocket:
        message = await websocket.recv()
        print(f"Received message from server: {message}")
        reply = "Hello from the client!"
        await websocket.send(reply)

asyncio.get_event_loop().run_until_complete(client())
