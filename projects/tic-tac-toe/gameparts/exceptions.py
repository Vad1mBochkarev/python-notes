
class FieldIndexError(Exception):
    def __srt__(self):
        return "введено значение за границей возожности этой маленькой вселенной"
    

class CellOccupiedError(Exception):

    def __str__(self):
        return "занято нахуй"