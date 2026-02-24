from module import isdigit
import sys

def run_all_tests():
    tests = [
        ("23", True),
        ("a123", False),
        ("123a", False),
        (123, True)
    ]

    for i, (input_string, expected) in enumerate(tests):
        if one_test_success(input_string, expected):
            print(f"Test {i}: Pass!")
        else:
            print(f"Test {i}: Fail")
            one_or_more_failures = True

def one_test_success(input, expected):
    try:
        actual = isdigit(input)
        print(f"Expected: {expected}, Got: {actual}")
        assert(actual == expected)
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)