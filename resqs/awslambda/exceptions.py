from botocore.client import ClientError
from resqs.core.exceptions import JsonRESTError


class LambdaClientError(ClientError):
    def __init__(self, error, message):
        error_response = {"Error": {"Code": error, "Message": message}}
        super(LambdaClientError, self).__init__(error_response, None)


class CrossAccountNotAllowed(LambdaClientError):
    def __init__(self):
        super(CrossAccountNotAllowed, self).__init__(
            "AccessDeniedException", "Cross-account pass role is not allowed."
        )


class InvalidParameterValueException(LambdaClientError):
    def __init__(self, message):
        super(InvalidParameterValueException, self).__init__(
            "InvalidParameterValueException", message
        )


class InvalidRoleFormat(LambdaClientError):
    pattern = r"arn:(aws[a-zA-Z-]*)?:iam::(\d{12}):role/?[a-zA-Z_0-9+=,.@\-_/]+"

    def __init__(self, role):
        message = "1 validation error detected: Value '{0}' at 'role' failed to satisfy constraint: Member must satisfy regular expression pattern: {1}".format(
            role, InvalidRoleFormat.pattern
        )
        super(InvalidRoleFormat, self).__init__("ValidationException", message)


class PreconditionFailedException(JsonRESTError):
    code = 412

    def __init__(self, message):
        super(PreconditionFailedException, self).__init__(
            "PreconditionFailedException", message
        )
