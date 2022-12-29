class RequestOperateResourceLockedError(Exception):
    ...


class IncorrectInstanceStatus(Exception):
    ...


class NotStopError(IncorrectInstanceStatus):
    ...


class RequestError(Exception):
    ...
