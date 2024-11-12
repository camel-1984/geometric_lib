import circle  # noqa: F401
import square  # noqa: F401
import triangle  # noqa: F401

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "area-square": 1,
    "area-triangle": 3,
    "perimeter-circle": 1,
    "perimeter-square": 1,
    "perimeter-triangle": 3
}


def calc(fig, func, size):
    assert fig in figs, "Unknown figure"
    assert func in funcs, "Unknown function"

    expected_size = sizes.get(f"{func}-{fig}")
    if len(size) != expected_size:
        raise TypeError(
            f"Expected {expected_size} arguments for "
            f"{fig} {func}, got {len(size)}"
        )

    return eval(f'{fig}.{func}(*{size})')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, "
                    f"available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, "
                     f"available are {funcs}:\n")

    expected_size = sizes.get(f"{func}-{fig}", 1)

    if expected_size == 1:
        size = [int(input("Input a single size value:\n"))]
    else:
        while len(size) != expected_size:
            size_input = input(
                f"Input {expected_size} figure "
                f"sizes separated by space:\n"
            )
            size = list(map(int, filter(None, size_input.split(' '))))

    try:
        result = calc(fig, func, size)
        print(f"{func} of {fig} with size {size} is {result}")
    except (AssertionError, TypeError, ValueError) as e:
        print(f"Error: {e}")
