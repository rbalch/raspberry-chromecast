import pychromecast
import pychromecast.controllers.youtube as yt
import time


chromecasts = pychromecast.get_chromecasts()
casts = [cc for cc in chromecasts if cc.cast_type == 'cast']
print('Casts founds: {c}'.format(c=len(casts)))


print('Claiming casts...')
for cast in casts:
    print('-->', cast.device.friendly_name)
    cast.wait()
    cast.quit_app()

print('Waiting for running apps to die...')
time.sleep(10)


youTubeId = 'zJ7hUvU-d2Q'
print('Telling casts to track [{id}]'.format(url=youTubeId))


for cast in casts:
    print('--> {d} : {u}'.format(d=cast.device.friendly_name, u=youTubeId))
    yt = yt.YouTubeController()
    cast.register_handler(yt)
    yt.play_video(youTubeId)

time.sleep(10)
