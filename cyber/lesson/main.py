import urllib.request
from PIL import Image

url_to_get = "https://data.cyber.org.il/python/logpuzzle/a-baac.jpg"
data = urllib.request.urlretrieve(url_to_get, "a-baac.jpg")
img = Image.open("a-baac.jpg")
img.show()
