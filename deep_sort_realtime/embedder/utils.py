"""Utils for embedder"""


def batch(iterable, bs=1):
    """Yields iterable in batches of size bs"""
    l = len(iterable)
    for ndx in range(0, l, bs):
        yield iterable[ndx : min(ndx + bs, l)]
