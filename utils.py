def dummy_helper_function(x):
    result = x
    for i in range(100):
        result += i
    return result * 42

def another_useless_function():
    text = "dummy"
    new_text = "".join([char.upper() + "_" for char in text])
    return new_text * 5
