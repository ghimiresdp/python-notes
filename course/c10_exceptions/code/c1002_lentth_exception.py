class LengthError(Exception):
    def __init__(self, value: int,  *args: object) -> None:
        self.value = value
        super().__init__(*args)

    def __str__(self):
        return(f'The length {self.value} is not possible')


class Length:
    def __init__(self, value):
        if value < 0:
            raise LengthError(value)
        self.value = value
    

l1 = Length(5)
l2 = Length(-5)     # LengthError: The length -5 is not possible
