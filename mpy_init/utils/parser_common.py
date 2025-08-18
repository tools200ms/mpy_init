from mpy_init.utils.parser_error_list import LabelValueErrorList
from mpy_init.utils.validator import Validators
from mpy_init.utils.validator_errors import ValidationError, ValidatorsNameReDefinitionError


class ParserCommon:
    @staticmethod
    def normalize_servicename(srv_name:str):
        Validators.validateName(srv_name)
        # label name to lowercase:
        return srv_name.lower()

    @staticmethod
    def split_servicenames_to_list(value: str) -> list:
        """Split string into list by space, comma and semicolon separators"""
        value = value.replace(',', ' ').replace(';', ' ')
        list = []
        error_list = LabelValueErrorList()

        for srv_name in value.split():
            try:
                srv_name = ParserCommon.normalize_servicename(srv_name)

                # Skip duplicate service names
                if srv_name in list:
                    raise ValidatorsNameReDefinitionError(srv_name)

                list.append(srv_name.lower())

            except ValidationError as srvname_err:
                error_list.append(srvname_err)

        if error_list.hasErrors():
            raise error_list

        return list

