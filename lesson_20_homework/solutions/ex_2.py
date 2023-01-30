from decimal import Decimal


class NumbersList(list):

    def _validate_values_numeric(self, values):
        for v in values:
            if not isinstance(v, (int, float, Decimal)):
                raise ValueError(f'Value can not be of type {type(v).__name__} only int, float or Decimal allowed')

    def __init__(self, args):
        self._validate_values_numeric(args)
        super().__init__(args)

    def append(self, __object):
        self._validate_values_numeric([__object])
        super().append(__object)

    def extend(self, __iterable) -> None:
        self._validate_values_numeric(__iterable)
        super().extend(__iterable)

    def __setitem__(self, key, value):
        self._validate_values_numeric([value])
        super().__setitem__(key, value)

    def __add__(self, other):
        self._validate_values_numeric(other)
        super().__add__(other)

    def __iadd__(self, other):
        self._validate_values_numeric(other)
        super().__add__(other)




nl = NumbersList([1, 2.0, 3])
print(nl)
# nl.extend(['str'])
# nl.append([])

nl += ['str']
print(nl)
