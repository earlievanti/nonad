# Assuming the above RangedInt class definition

R1 = "not_an_int"  # Example problematic input

try:
    print(f"Creating RangedInt with value: {R1} and max_value: 12")
    x2 = RangedInt(R1, 12)
    print(f"RangedInt created successfully: {x2.value}")
except ValueError as e:
    print(f"Caught an exception: {e}")
