import network
import espnow

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
espnow.init()

peer = b'\xa0\x20\xa6\x14\x68\xc6'   # MAC address of sender-peer
peer2 = b'\xff\xff\xff\xff\xff\xff'  # MAC address of receiver (Universal Receiver)
espnow.add_peer(peer)
espnow.add_peer(peer2)

# Send ESPNOW data to a peer
def SEND(peer_send):
    e.send(peer_send, "Starting...")       # Send to all peers
    for i in range(100):
        e.send(peer_send, str(i)*20, True)
        e.send(peer_send, b'end')

SEND(peer2)


