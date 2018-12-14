class ToDict:
    def to_dict(self):
        return self.__dict__.copy()
    
    def __repr__(self):
        return str(self.__dict__)
