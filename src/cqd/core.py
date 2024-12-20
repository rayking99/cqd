def cqd(obj):
    # ANSI color codes
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    attributes = dir(obj)
    for attr in attributes:
        if attr.startswith("__") and attr.endswith("__"):  # Dunder methods
            print(f"{BLUE}{attr}{RESET}")
        elif attr.startswith("_"):  # Protected attributes
            print(f"{YELLOW}{attr}{RESET}")
        else:  # Public attributes or methods
            print(f"{GREEN}{attr}{RESET}")
