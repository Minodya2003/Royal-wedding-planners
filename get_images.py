import urllib.request, ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_id(query):
    url = f"https://unsplash.com/napi/search/photos?query={query.replace(' ', '+')}&per_page=1"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    res = urllib.request.urlopen(req, context=ctx).read()
    data = json.loads(res)
    return data["results"][0]["id"]

print("corporate:", get_id("conference"))
print("school:", get_id("graduation"))
print("private:", get_id("birthday cake"))
