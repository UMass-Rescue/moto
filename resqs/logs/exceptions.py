from __future__ import unicode_literals
from resqs.core.exceptions import JsonRESTError


class LogsClientError(JsonRESTError):
    code = 400


class ResourceNotFoundException(LogsClientError):
    def __init__(self, msg=None):
        self.code = 400
        super(ResourceNotFoundException, self).__init__(
            "ResourceNotFoundException", msg or "The specified log group does not exist"
        )


class InvalidParameterException(LogsClientError):
    def __init__(self, msg=None):
        self.code = 400
        super(InvalidParameterException, self).__init__(
            "InvalidParameterException", msg or "A parameter is specified incorrectly."
        )


class ResourceAlreadyExistsException(LogsClientError):
    def __init__(self):
        self.code = 400
        super(ResourceAlreadyExistsException, self).__init__(
            "ResourceAlreadyExistsException", "The specified log group already exists"
        )


class LimitExceededException(LogsClientError):
    def __init__(self):
        self.code = 400
        super(LimitExceededException, self).__init__(
            "LimitExceededException", "Resource limit exceeded."
        )
