import esp
import espnow
import network

# Enable ESPNOW
esp.osdebug(None)
esp.check_fw()

# Enable WiFi in station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Enable ESPNOW peer-to-peer mode
espnow.init()

# Set up a callback to receive ESPNOW data
def espnow_rx_callback(mac, data):
  print('Received ESPNOW data from MAC:', mac)
  print('Data:', data)

espnow.set_rx_cb(espnow_rx_callback)

# Send ESPNOW data to a peer
def send_espnow_data(data, peer_mac):
  espnow.send(peer_mac, data)

# Set up a peer with the given MAC address
def add_espnow_peer(peer_mac):
  espnow.add_peer(peer_mac)
  print('Successfully added a peer with MAC:', peer_mac)

# Set the ESPNOW channel
def set_espnow_channel(channel):
  espnow.set_channel(channel)

# Set the ESPNOW power level
def set_espnow_power(power):
  espnow.set_power(power)

#To use this code, you will need to first enable ESPNOW on your ESP32 or ESP8266 device, and then set up a WiFi connection in station mode. Next, you can initialize ESPNOW in peer-to-peer mode and set up a callback function to receive ESPNOW data.

#You can then use the send_espnow_data function to send ESPNOW data to a peer, and the add_espnow_peer function to set up a peer with a specific MAC address. You can also use the set_espnow_channel and set_espnow_power functions to set the ESPNOW channel and power level, respectively.

#I hope this helps! Let me know if you have any questions.
  