# ESP32_OTA_update_using_MicroPython
This process will tell you how to connect esp32 to internet using wifi and update scripts, you can also update esp32 using Access Point method ie. without connecting to internet but wireless.

STEPS to send your code over the internet-
1) Go to shell connected to ESP32 port and type "import webrepl_setup" and complete the setup. 
2) Connect ESP32 to your desktop using USB cable and give commands present in WIFI_scan.py file in shell connected to ESP32 port.
3) This will activate WIFI of esp32 and connect it to a wifi by giving Username and password when giving command " net.connect('Your ssid','Your password') ".
4) After connecting to WIFI, open https://micropython.org/webrepl/.
5) Check if ip is correct and hit "connect".
6) It will ask for WEBREPL password, provide your password and hit enter, It should connect.
7) Then you can send your code file using options provided on right side.


STEPS to send your code over Wifi-
1) Go to shell connected to ESP32 port and type "import webrepl_setup" and complete the setup. 
2) Connect ESP32 to your desktop using USB cable and give commands present in WIFI_as_AP.py file in shell connected to ESP32 port.
3) This will activate WIFI of esp32 as an Access Point.
4) Connect your desktop to the wifi "ESP32".
5) After connecting to WIFI, open https://micropython.org/webrepl/.
6) Check if ip is correct and hit "connect".
7) It will ask for WEBREPL password, provide your password and hit enter, It should connect.
8) Then you can send your code file using options provided on right side.
