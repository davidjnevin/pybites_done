import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    line_count = 0
    lines = poem.split("\n")
    for line in lines:
        dedented = textwrap.dedent(line).strip()

        if not dedented:
            line_count = 0
            continue
        else:
            line_count += 1
        new_line = "" if line_count == 1 else (" " * INDENTS)
        print(new_line + dedented)
