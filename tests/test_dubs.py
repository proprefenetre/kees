import time
from contextlib import contextmanager


def _remove_dubs(lst):
    words = [w.split() for w in lst]
    uniques = []
    keys = set()
    for word in words:
        if len(word) > 1:
            keys.add(word[-1])
            uniques.append(word)
    for word in [w for w in words if len(w) == 1]:
        if word[0] not in keys:
            uniques.append(word)
    return [' '.join(w) for w in uniques]


def _get_uniques(words):
    """ remove translation if the same translation occurs with a determiner """
    words = [w.split() for w in words]
    det = []
    no_det = []
    for w in words:
        if len(w) < 2:
            no_det.append(w)
        else:
            det.append(w)
    for x in no_det:
        if x[0] not in [v[1] for v in det]:
            det.append(x[0])
        else:
            continue
    return [' '.join(d) for d in det]


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("{}: {}".format(label, end - start))


# uniques does not produce the right output on this list:
words = ['the dog', 'the cat', 'le chat', 'le chien', 'schaap', 'held', 'dog',
         'cat', 'chien', 'chat']

with timethis('uniques'):
    print(_get_uniques(words))      

with timethis('dubs'):
    print(_remove_dubs(words))      # faster

print()

with open('enable1.txt', 'r', encoding='ascii') as f:
    words = [w.strip() for w in f.readlines()]
    div = len(words) // 2
    pairs = [' '.join([a, b]) for a, b in zip(words[:div], words[div:])]
    pairs.extend(words[:div])

    for z in range(5):
        with timethis('uniques'):
            x = _get_uniques(pairs)     # takes ages (never seen it finish)
            print(x[:10])

        with timethis('dubs'):
            y = _remove_dubs(pairs)     # takes around 0.3 seconds 
            print(y[:10])
