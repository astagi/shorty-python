"""
MIT License
Copyright (c) 2009 Joshua Roesslein

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from urllib2 import urlopen, URLError, HTTPError

class ShortyError(Exception):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        repr(self.reason)

"""Wrap urlopen to raise shorty errors instead"""
def request(*args, **kargs):

    try:
        return urlopen(*args, **kargs)
    except URLError, e:
        raise ShortyError(e)

"""Base interface that all services implement."""
class Service(object):

    def shrink(bigurl):
        """Take a big url and make it smaller"""

        return None

    def expand(tinyurl):
        return None

"""Tinyurl.com"""
class Tinyurl(Service):

    @staticmethod
    def shrink(bigurl):
        resp = request('http://tinyurl.com/api-create.php?url=%s' % bigurl)
        return resp.readline()
        
