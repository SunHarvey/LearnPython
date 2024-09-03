import asyncio
import websockets


async def send_messages(websocket, path):
    while True:
        message = input("Enter message to send: ")
        await websocket.send(message)
        print(f"Sent message: {message}")


start_server = websockets.serve(send_messages, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server started on port 8765")
asyncio.get_event_loop().run_forever()
