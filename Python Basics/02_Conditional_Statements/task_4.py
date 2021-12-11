number = float(input())
measure_unit_input = input()
measure_unit_output = input()

if measure_unit_input == 'm' and measure_unit_output == 'cm':
    print(f"{number * 100:.3f}")
elif measure_unit_input == 'm' and measure_unit_output == 'mm':
    print(f"{number * 1000:.3f}")

elif measure_unit_input == 'cm' and measure_unit_output == 'mm':
    print(f"{number * 10:.3f}")
elif measure_unit_input == 'cm' and measure_unit_output == 'm':
    print(f"{number * 0.01:.3f}")

elif measure_unit_input == 'mm' and measure_unit_output == 'cm':
    print(f"{number * 0.1:.3f}")
elif measure_unit_input == 'mm' and measure_unit_output == 'm':
    print(f"{number * 0.001:.3f}")