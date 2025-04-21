INSTRUCTION = """
You will generate the python code to generate the test cases, which follows the format:
---
```python
import random

random.seed(42)

def generate_input_values():
    # Your code here
    return [input_values]

def solution(input_values):
    # Your code here
    return output_value

def generate_test_case():
    input_values = generate_input_values()
    expected_output = solution(input_values)
    return {
        "input": input_values,
        "expected_output": expected_output
    }

def generate_test_cases(n):
    for i in range(n):
        input_values = generate_test_case()
        output_value = solution(*input_values)

        input_values_str = (", ".join(map(str, input_values))).replace("'", '"')
        output_value_str = str(output_value).replace("'", '"')

        with open(f"\{i\}_in.txt", "w") as f:
            f.write(input_values_str)
        
        with open(f"\{i\}_out.txt", "w") as f:
            f.write(output_value_str)

if __name__ == "__main__":
    n = 5  # Number of test cases
    generate_test_cases(n)
```
---
There should be no explanation or comments in the code."""