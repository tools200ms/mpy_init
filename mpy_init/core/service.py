from mpy_init.utils.parser_errors import ServiceEmptyNameError, ServiceNameDoesNotStartWithLetterError, \
    ServiceInvalidNameError


class Service:
    @staticmethod
    def validateName(name: str):
        # always ensure that validateName is not empty value
        if not name:
            raise ServiceEmptyNameError()

        if not name[0].isalpha():
            raise ServiceNameDoesNotStartWithLetterError()

        if not all(c.isalnum() or c == '_' or c == '-' for c in name):
            raise ServiceInvalidNameError(name)

        return True
