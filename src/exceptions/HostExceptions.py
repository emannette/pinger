class MissingHostsException(Exception):
    """An exception thrown if no hosts are passed to the module via command line"""

    def __init__(self, message='No hosts were passed.'):
        self.message = message
        super().__init__(self.message)
