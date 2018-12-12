class ToDict:
    def to_dict(self):
        return self.__dict__
    
    def __repr__(self):
        return str(self.__dict__)
