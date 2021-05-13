import network

ssid="ESP32"
password="password"
ap=network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid,password=password)
