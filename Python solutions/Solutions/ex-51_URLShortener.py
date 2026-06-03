import random
import string
class URLShortener:
    def __init__(self):
        self.urls = {}
    def shorten(self, long_url):
        short_code = ''.join(
            random.choices(
                string.ascii_letters +
                string.digits,
                k=6
            )
        )
        self.urls[short_code] = long_url
        return short_code
    def expand(self, short_code):
        return self.urls.get(
            short_code,
            "URL Not Found"
        )
shortener = URLShortener()
code = shortener.shorten(
    "https://www.google.com"
)
print("Short URL:", code)
print(
    "Original URL:",
    shortener.expand(code)
)