import network
import espnow
import esp

# Enable ESPNOW
esp.osdebug(None)
esp.check_fw()

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

# Enable ESPNOW peer-to-peer mode
e = espnow.ESPNow()
e.active(True)
e.init()

peer  = b'\xa0\x20\xa6\x14\x68\xc6'   # MAC address of receiver-peer
peer2 = b'\xff\xff\xff\xff\xff\xff'   # MAC address of receiver (Universal Receiver)
e.add_peer(peer)
#e.add_peer(peer2)

# Send ESPNOW data to a peer
def SEND():
    e.send(peer, "Starting...")       # Send to all peers
    for i in range(100):
        e.send(peer, str(i)*20, True)
        e.send(peer, b'end')
    print("Data Sent successfully.")

# Receive ESPNOW data from a peer
def RECV():
    while True:
            host, msg = e.recv()
            if msg:             # msg == None if timeout in recv()
                print(host, msg)
                if msg == b'end':
                    print("Data Received Successfully")
                    break
