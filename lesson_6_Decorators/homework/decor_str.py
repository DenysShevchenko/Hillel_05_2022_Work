import functools


def reverse_string(func):
    @functools.wraps(func)
    def wrapper():

        results_func = func()
        if not isinstance(results_func, str):
            results_func = None
        return results_func

    return wrapper


@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year():
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
