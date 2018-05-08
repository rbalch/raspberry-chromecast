import time
import giphy_client
import random
from giphy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
q = 'tuesday' # str | Search query term or prhase.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

previous_image = None
max_offset = 30

while True:
    offset = random.randint(0, max_offset)
    x = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)

    if len(x.data) < 5:
        max_offset -= 1
        time.sleep(5)
    else:
        image = x.data[random.randint(0, len(x.data) - 1)].images.original.mp4

        if image != previous_image:
            previous_image = image
            with open('api.json', 'w') as f:
                print('write: {i}'.format(i=image))
                f.write(image)

        time.sleep(60 * 5)
