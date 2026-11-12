def dummy_function(a: str = "Dummy"):
    if a == "Dummy":
        return "Hello from dummy_function!"
    else:
        raise ValueError("a is not Dummy")


def dummy_function_2(a: str = "Dummy"):
    if a == "Dummy":
        return "Hello from dummy_function_2!"
    else:
        raise ValueError("a is not Dummy")