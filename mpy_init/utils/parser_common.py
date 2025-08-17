from mpy_init.utils.parser_error_list import LabelValueErrorList
from mpy_init.utils.validator import Validators
from mpy_init.utils.validator_errors import ValidationError


class ParserCommon:
    @staticmethod
    def split_servicenames_to_list(self, value: str) -> list:
        """Split string into list by space, comma and semicolon separators"""
        value = value.replace(',', ' ').replace(';', ' ')
        list = []
        error_list = LabelValueErrorList()

        for srv_name in value.split():
            try:
                Validators.validateName(srv_name)

                list.append(srv_name.lower())
            except ValidationError as srvname_err:
                error_list.append(srvname_err)

        if error_list.hasErrors():
            raise error_list

        return list

