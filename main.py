from pypresence import Presence 
import random
import time

start = int(time.time())
client_id = "1059963819700531240"
RPC = Presence(client_id)
RPC.connect()

amount = 0.0000000

while True: #infinite loop
    RPC.update(
        large_image = "bitcoin", #name of your asset
        large_text = "Mining Bitcoins",
        details = "Mining...",
        state = f"Status: {amount:.7f} Mined",
        start = start,
        buttons = [{"label": "Coinbase", "url": "https://www.coinbase.com/"}, {"label": "Bitcoin Price", "url": "https://coinmarketcap.com/currencies/bitcoin/"}])
    time.sleep(15) #can be as low as 15, depends on how often you want to update
    amount += random.uniform(0.0000001, 0.0000010)
