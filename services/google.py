## Shorty
## Copyright 2011 Andrea Stagi
## See LICENSE

## @url goo.gl
class Google(Service):

    def shrink(self, bigurl):
        resp = request('http://goo.gl/api/url', {'url': bigurl}, post_data = 'toolbar')
        data = resp.read()
        jdata = json.loads(data)
        if 'short_url' not in jdata:
            raise ShortyError(data)
        else:
            return jdata['short_url']

    def qrcode(self, url):
        if not url.startswith('http://goo.gl/'):
            url = self.shrink(url)
        qrdata = request(url + '.qr').read()
        return qrdata

