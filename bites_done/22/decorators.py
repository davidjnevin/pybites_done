from functools import wraps


def make_html(element):
    def inner(fn):
        def wrapped(*args, **kwargs):
            return f"<{element}>{fn(*args, **kwargs)}</{element}>"

        return wrapped

    return inner
