# Property function returns an object that proxies the requests
# to set or access the attribute value through the methods specified.


class Silly:
    def __init__(self):
        """
        Initialize silly with a default value.
        """
        self._silly = "silly"

    def _get_silly(self):
        """
        Getting the value of proprty silly.
        """
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        """
        Setting the value of proprty silly.
        """
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly,
                     "This is a silly property")


class SillyUsingDecorator:
    """
    This class does the same thing as above but it is 
    implemented using decorators.
    """

    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly
