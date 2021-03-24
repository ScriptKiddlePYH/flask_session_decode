#index.html
#!/usr/bin/env python3
import sys
import zlib
from base64 import b64decode
from flask.sessions import session_json_serializer
from itsdangerous import base64_decode

def decryption(payload):
    payload, sig = payload.rsplit(b'.', 1)
    payload, timestamp = payload.rsplit(b'.', 1)

    decompress = False
    if payload.startswith(b'.'):
        payload = payload[1:]
        decompress = True

    try:
        payload = base64_decode(payload)
    except Exception as e:
        raise Exception('Could not base64 decode the payload because of '
                         'an exception')

    if decompress:
        try:
            payload = zlib.decompress(payload)
        except Exception as e:
            raise Exception('Could not zlib decompress the payload before '
                             'decoding the payload')

    return session_json_serializer.loads(payload)

if __name__ == '__main__':
    s = ".eJxNkEFvgmAMhv_K0rMHQHYx8TADEk3aRYKQ9mIUUSh8LgGM5jP-930zy7Jr3_R52vcBu1NfDTXMxv5aTWDXHGH2gLcDzIADtKxxQFEZkEWf9eyhEWW78kVXd9Rj42Yh2dRIkdZcSMe29DDLVbJyKtraz2QbULHuOFsa1kVHCVtJckNFXlOBU8mWNavUaNctma0v0cL87LLNnalTzHhK7gZWvLE9O2fqnOsObexJ9vGOzisG5_CcQDn0p9341VaXfy-QUhQHGDl9sQklWbaYkCFtQ9a8oSC-i5YOFd_ZrG4OFfJm_sI1Zn-u_kiU-OnmN7nsjQtgrIYRJnAdqv5VG_gePL8BIVdt1g.YFqwsg.NmpTxs5MdLFCPOt5ItoGwfjM54w; path=/; domain=5d7c6405-5d4e-46fb-bd67-465fc901999f.node3.buuoj.cn; HttpOnly"
    print(decryption(s.encode()))
