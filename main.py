from pypresence import Presence 
import time

start = int(time.time())
client_id = "1059963819700531240"
RPC = Presence(client_id)
RPC.connect()

while True: #infinite loop
    RPC.update(
        large_image = "Mining Bitcoins", #name of your asset
        large_text = "",
        details = "Mining...",
        state = "",
        start = start,
        buttons = [{"label": "Bitcoin Price", "url": "https://coinmarketcap.com/currencies/bitcoin/"})
    time.sleep(15) #can be as low as 15, depends on how often you want to update
