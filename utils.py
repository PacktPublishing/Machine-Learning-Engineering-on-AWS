from os import get_terminal_size
from contextlib import contextmanager
from IPython import embed as debug


def draw_line():
    columns, _ = get_terminal_size()
    print("=" * columns)


@contextmanager
def block(label):
    draw_line()
    print(f"[{label}]: START")
    draw_line()
    
    yield
        
    draw_line()
    print(f"[{label}]: END")
    draw_line()