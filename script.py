from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
import pynput
from pynput.keyboard import Key, Controller
from tomlkit import key
keyboard = Controller()
print("""
░██████╗██╗░░░██╗██████╗░░██████╗░█████╗░██████╗░██╗██████╗░███████╗  ████████╗░█████╗░
██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝╚█████╗░██║░░╚═╝██████╔╝██║██████╦╝█████╗░░  ░░░██║░░░██║░░██║
░╚═══██╗██║░░░██║██╔══██╗░╚═══██╗██║░░██╗██╔══██╗██║██╔══██╗██╔══╝░░  ░░░██║░░░██║░░██║
██████╔╝╚██████╔╝██████╦╝██████╔╝╚█████╔╝██║░░██║██║██████╦╝███████╗  ░░░██║░░░╚█████╔╝
╚═════╝░░╚═════╝░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝  ░░░╚═╝░░░░╚════╝░

██████╗░░█████╗░██╗███╗░░██╗██████╗░░█████╗░███╗░░██╗ 
██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██╔══██╗████╗░██║ 
██████╦╝███████║██║██╔██╗██║██████╦╝███████║██╔██╗██║ 
██╔══██╗██╔══██║██║██║╚████║██╔══██╗██╔══██║██║╚████║ 
██████╦╝██║░░██║██║██║░╚███║██████╦╝██║░░██║██║░╚███║ 
╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝ 
""")
name = input("tiktok id: ")

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id=f"@{name}")


# Define how you want to handle specific events via decorator


@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    total_donations = 0
    total_donations += 1

    # Define handling an event via "callback"
client.add_listener("comment", on_comment)


@client.on("gift")
async def on_gift(event):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            print(
                f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")
            keyboard.press(Key.up)
            keyboard.release(Key.up)
    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")
        keyboard.press(Key.up)
        keyboard.release(Key.up)
if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
