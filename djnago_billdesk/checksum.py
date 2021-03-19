try:
    from django.conf import settings
    CHECKSUM_KEY = settings.CHECKSUM_KEY
except Exception:
    CHECKSUM_KEY = ''
import hmac
import hashlib

# nonce = 1
# customer_id = 123456
# API_SECRET = 'thekey'
# api_key = 'thapikey'
#
# message = '{} {} {}'.format(nonce, customer_id, api_key)

class Checksum:
    def get_checksum(self,message):
        signature = hmac.new(bytes(CHECKSUM_KEY, 'latin-1'), msg=bytes(message, 'latin-1'),
                             digestmod=hashlib.sha256).hexdigest().upper()
        return signature
    def verify_checksum(self,message):
        l_index = message.rindex('|')
        to_be_verified = message[l_index+1:]
        my_checksum = self.get_checksum(message[:l_index])#+settings.CHECKSUM_KEY
        if my_checksum == to_be_verified:
            return True
        else:
            return False