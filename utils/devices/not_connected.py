class NotConnected:
    def __bool__(self):
        return False


NOTCONNECTED = NotConnected()
