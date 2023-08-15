from __future__ import absolute_import, division, print_function, unicode_literals

from __future__ import absolute_import, division, print_function, unicode_literals

import sys

from wit import Wit

token = "UZUN2W2TQIFHG4YGAUNWM57SZT573HS7"

client = Wit(access_token=token)
client.interactive()