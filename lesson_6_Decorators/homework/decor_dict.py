import functools


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            kwargs[target_key] = replace_with
            return func(*args, **kwargs)

        return wrapper

    return decorator


@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
