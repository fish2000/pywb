import itertools
import hmac
import time
import zlib
import time
import datetime
import re

def peek_iter(iterable):
    try:
        first = next(iterable)
    except StopIteration:
        return None

    return itertools.chain([first], iterable)


def split_prefix(key, prefixs):
    for p in prefixs:
        if key.startswith(p):
            plen = len(p)
            return (key[:plen], key[plen:])


def create_decompressor():
    return zlib.decompressobj(16 + zlib.MAX_WBITS)


class HMACCookieMaker:
    def __init__(self, key, name):
        self.key = key
        self.name = name


    def __call__(self, duration, extraId = ''):
        expire = str(long(time.time() + duration))

        if extraId:
            msg = extraId + '-' + expire
        else:
            msg = expire

        hmacdigest = hmac.new(self.key, msg)
        hexdigest = hmacdigest.hexdigest()

        if extraId:
            cookie = '{0}-{1}={2}-{3}'.format(self.name, extraId, expire, hexdigest)
        else:
            cookie = '{0}={1}-{2}'.format(self.name, expire, hexdigest)

        return cookie

        #return cookie + hexdigest


# Adapted from example at
class PerfTimer:
    def __init__(self, perfdict, name):
        self.perfdict = perfdict
        self.name = name

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        if self.perfdict is not None:
            self.perfdict[self.name] = str(self.end - self.start)


DATE_TIMESPLIT = re.compile('[^\d]')

def iso_date_to_datetime(string):
    """
    >>> iso_date_to_datetime('2013-12-26T10:11:12Z')
    datetime.datetime(2013, 12, 26, 10, 11, 12)

    >>> iso_date_to_datetime('2013-12-26T10:11:12Z')
    datetime.datetime(2013, 12, 26, 10, 11, 12)
     """

    nums = DATE_TIMESPLIT.split(string)
    if nums[-1] == '':
        nums = nums[:-1]

    dt = datetime.datetime(*map(int, nums))
    return dt

def datetime_to_timestamp(dt):
    """
    >>> datetime_to_timestamp(datetime.datetime(2013, 12, 26, 10, 11, 12))
    '20131226101112'
    """

    return dt.strftime('%Y%m%d%H%M%S')

def iso_date_to_timestamp(string):
    """
    >>> iso_date_to_timestamp('2013-12-26T10:11:12Z')
    '20131226101112'

    >>> iso_date_to_timestamp('2013-12-26T10:11:12')
    '20131226101112'
     """

    return datetime_to_timestamp(iso_date_to_datetime(string))




if __name__ == "__main__":
    import doctest
    doctest.testmod()
