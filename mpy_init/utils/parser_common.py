
from mpy_init.utils.parser_errors import ValListError
from mpy_init.utils.precheck import PreCheck


class ParserCommon:
    @staticmethod
    def normalize_servicename(srv_name:str):
        PreCheck.serviceName(srv_name)
        # label name to lowercase:
        return srv_name.lower()

    @staticmethod
    def split_servicenames_to_list(value: str) -> list:
        """Split string into list by space, comma and semicolon separators"""
        value = value.replace(',', ' ').replace(';', ' ')
        list = []
        error_list = ValListError()

        for srv_name in value.split():
            try:
                srv_name = ParserCommon.normalize_servicename(srv_name)

                # Skip duplicate service names
                if srv_name in list:
                    raise ValError(ServiceErrorMsg.REDEFIN_NAME, srv_name)

                list.append(srv_name.lower())

            except ValueError as srvname_err:
                error_list.append(srvname_err)

        if error_list.hasErrors():
            raise error_list.strip()

        return list

