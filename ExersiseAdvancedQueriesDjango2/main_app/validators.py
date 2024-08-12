from django.core.exceptions import ValidationError


class RangeValueValidator:
    def __init__(self, start, end, message=None):
        self.start = start
        self.end = end
        self.__message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = f"The rating must be between {self.start:.1f} and {self.end:.1f}"

    def __call__(self, value: int):
        if not self.start <= value <= self.end:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.RangeValueValidator',
            [self.start, self.end],
            {'message': self.message},
        )
