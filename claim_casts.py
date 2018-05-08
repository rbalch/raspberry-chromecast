import pychromecast
import pychromecast.controllers.dashcast as dashcast
import socket
import time


chromecasts = pychromecast.get_chromecasts()
casts = [cc for cc in chromecasts if cc.cast_type == 'cast']


def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    s.close()
    print('IP Address selected [{ip}]...'.format(ip=ipAddr))
    return ipAddr


def getUrl(ip):
    return 'http://{ip}:8000'.format(ip=ip)


print('Claiming casts...')
for cast in casts:
    print('-->', cast.device.friendly_name)
    cast.wait()
    cast.quit_app()

print('Waiting for running apps to die...')
time.sleep(5)


url = getUrl(getIp())
print('Telling casts to track [{url}]'.format(url=url))


for cast in casts:
    d = dashcast.DashCastController()
    cast.register_handler(d)
    d.load_url(url)
