from rest_framework.exceptions import APIException


class ApplicationError(Exception):

    def __init__(self, message, extra=None):
        super().__init__(message)

        self.message = message
        self.extra = extra or {}


class DuplicateUsername(Exception):

    def __init__(self, message, extra=None):
        super().__init__(message)

        self.message = message
        self.extra = extra or {}


class OrderTimeException(APIException):

    def __init__(self, message, extra=None):
        super().__init__(message)
        self.message = message
        self.extra = extra


class CompleteEmailProfileException(APIException):

    def __init__(self, message, extra=None):
        super().__init__(message)
        self.message = message
        self.extra = extra


class OwnerOfOrderException(APIException):

    def __init__(self, message, extra=None):
        super().__init__(message)
        self.message = message
        self.extra = extra
