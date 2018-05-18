import time
import pychromecast
import pychromecast.controllers.dashcast as dashcast

chromecasts = pychromecast.get_chromecasts()
print([cc.device.friendly_name for cc in chromecasts])

cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Lemon")
cast.wait()
d = dashcast.DashCastController()
cast.register_handler(d)
print(cast.device)

mc = cast.media_controller
mc.play_media('https://i.giphy.com/media/3YIqLjzw0DE6Kdzzzc/giphy.mp4', 'video/mp4')
mc.block_until_active()
time.sleep(20)
