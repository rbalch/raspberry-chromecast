import argparse
import pychromecast
import pychromecast.controllers.dashcast as dashcast
import socket
import time


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    s.close()
    print('IP Address selected [{ip}]...'.format(ip=ipAddr))
    return ipAddr


def find_casts():
    chromecasts = pychromecast.get_chromecasts()
    casts = [cc for cc in chromecasts if cc.cast_type == 'cast']
    print('Casts founds: {c}'.format(c=len(casts)))
    return casts


def claim_casts(casts):
    print('Claiming casts...')
    for cast in casts:
        print('-->', cast.device.friendly_name)
        cast.wait()
        cast.quit_app()


def cast_url(cast, url):
    print('--> {d} : {u}'.format(d=cast.device.friendly_name, u=url))
    d = dashcast.DashCastController()
    cast.register_handler(d)
    d.load_url(url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Utility to claim all cast devices on the network and cast a url to them.")
    parser.add_argument('--url',
                        required=True,
                        help='Url for casts to track.')
    args = parser.parse_args()

    casts = find_casts()
    claim_casts(casts)
    print('Waiting for running apps to die...')
    time.sleep(10)
    print('Telling casts to track [{url}]'.format(url=args.url))
    for cast in casts:
        cast_url(cast, args.url)
    time.sleep(10)
