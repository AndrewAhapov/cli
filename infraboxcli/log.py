from colorama import Fore, init
init()

class Logger(object):
    def __init__(self):
        pass

    def _print(self, color, s):
        print("%s[infrabox] %s%s" % (color, s, Fore.RESET))

    def info(self, s):
        self._print(Fore.BLUE, s)

    def warn(self, s):
        self._print(Fore.YELLOW, s)

    def error(self, s):
        self._print(Fore.RED, s)

logger = Logger()
