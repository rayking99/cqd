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


def cqd2(obj):
    # ANSI color codes
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    attributes = dir(obj)
    for attr in attributes:
        try:
            # Get the attribute value and its type
            attr_value = getattr(obj, attr)
            attr_type = type(attr_value).__name__

            if attr.startswith("__") and attr.endswith("__"):  # Dunder methods
                print(f"{BLUE}{attr:<30} : {attr_type}{RESET}")
            elif attr.startswith("_"):  # Protected attributes
                print(f"{YELLOW}{attr:<30} : {attr_type}{RESET}")
            else:  # Public attributes or methods
                print(f"{GREEN}{attr:<30} : {attr_type}{RESET}")
        except Exception:
            # Handle cases where attribute access might be restricted
            print(f"{attr:<30} : <unable to access>")
