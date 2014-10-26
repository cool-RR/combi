try:
    from functools import cmp_to_key
except ImportError:
    # Python 3.0 / 3.1
    def cmp_to_key(mycmp):
        """Convert a cmp= function into a key= function"""
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
            def __hash__(self):
                raise TypeError('hash not implemented')
        return K

