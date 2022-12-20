import network
import esp
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()   # For ESP8266

e = espnow.ESPNow()
e.active(True)
peer = b'\xff\xff\xff\xff\xff\xff'   # MAC address of peer's wifi interface dc:4f:22:10:ce:22
#e.add_peer(peer)

e.send(peer, "Starting...")       # Send to all peers
for i in range(100):
    e.send(peer, str(i)*20, True)
    e.send(peer, b'end')