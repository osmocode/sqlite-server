
class ProxyException(Exception):
    """Base exception commig from Proxy"""
    pass


class ProxyIllegalStateException(ProxyException):
    """Invalid state for proxy"""
    def __init__(self, error: str) -> None:
        self.error = error
