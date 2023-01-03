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
        large_image = "bitcoin",
        large_text = "Mining Bitcoins",
        details = "Mining...",
        state = f"Status: {amount:.7f} BTC Mined",
        start = start,
        buttons = [{"label": "Coinbase", "url": "https://www.coinbase.com/"}, {"label": "Bitcoin Price", "url": "https://coinmarketcap.com/currencies/bitcoin/"}])
    time.sleep(15)
    amount += random.uniform(0.0000001, 0.0000010)
