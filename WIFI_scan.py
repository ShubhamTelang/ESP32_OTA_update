import network                               #Import wifi

net=network.WLAN(network.STA_IF)             #Load station interface
net.active(True)                             #Activate wifi
net.scan()                                   #Scan wifi
net.connect('Your ssid','Your password')     #connect esp to wifi
