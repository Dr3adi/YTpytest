from enum import Enum


class GlobalErrorMessanges(Enum):
    WRONG_STATUS_CODE = 'Полученный статус-код отличается от ожидаемого'
    WRONG_ELEMET_COUNT = 'Ожидаемое количество одличается от ожидаемого'