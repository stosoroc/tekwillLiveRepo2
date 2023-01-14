from decimal import Decimal, ROUND_UP, ROUND_DOWN, ROUND_CEILING, ROUND_HALF_DOWN, ROUND_HALF_UP

number = Decimal('1.333')
print(number)


other_number = Decimal(1.32)
print(other_number)
other_number = Decimal(1.32).quantize(Decimal('1.000'), ROUND_UP)
print(other_number)
other_number = Decimal(1.32).quantize(Decimal('1.0'), ROUND_DOWN)
print(other_number)
other_number = Decimal(1.32).quantize(Decimal('1.00000'), ROUND_HALF_DOWN)
print(other_number)
other_number = Decimal(1.35).quantize(Decimal('1.00000'), ROUND_HALF_DOWN)
print(other_number)
other_number = Decimal(1.35).quantize(Decimal('1.00000'), ROUND_HALF_UP)
print(other_number)
other_number = Decimal(1.32).quantize(Decimal('1'), ROUND_CEILING)
print(other_number)

print(other_number.to_integral())