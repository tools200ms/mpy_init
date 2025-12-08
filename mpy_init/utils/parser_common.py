from mpy_init.lib.messages import ServiceErrorMsg
from mpy_init.utils.parser_errors import MultipleValueError


class Validate:
    @staticmethod
    def serviceName(name: str) -> True:
        """
        Validates if the given service name follows the required naming rules.

        Args:
            name (str): Service name to validate.

        Returns:
            bool: True if validation passes.

        Raises:
            ServiceEmptyNameError: If name is empty.
            ServiceInvalidNameError: If name contains invalid characters.
            ServiceNameDoesNotStartWithLetterError: If name doesn't start with a letter.
        """
        # ensure that the name is not an empty value
        if not name:
            raise ValueError(ServiceErrorMsg.MISSING_NAME)

        if not all(c.isalpha() or c.isdigit() or c == '_' or c == '-' for c in name):
            raise ValueError(ServiceErrorMsg.INVALID_NAME)

        if not name[0].isalpha():
            raise ValueError(ServiceErrorMsg.ILLEGAL_NAME)

        return True


class ParserCommon:
    @staticmethod
    def normalize_servicename(srv_name:str):
        Validate.serviceName(srv_name)
        # label name to lowercase:
        return srv_name.lower()

    @staticmethod
    def split_servicenames_to_list(value: str) -> list:
        """Split string into list by space, comma and semicolon separators"""
        value = value.replace(',', ' ').replace(';', ' ')
        list = []
        error_list = MultipleValueError()

        for srv_name in value.split():
            try:
                srv_name = ParserCommon.normalize_servicename(srv_name)

                # Skip duplicate service names
                if srv_name in list:
                    raise ValueError(ServiceErrorMsg.REDEFIN_NAME)

                list.append(srv_name.lower())

            except ValueError as srvname_err:
                error_list.addFailedValue(srvname_err)

        if error_list.hasErrors():
            raise error_list.strip()

        return list

