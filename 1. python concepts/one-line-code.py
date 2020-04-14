print(' '.join(
    y for y in sorted(set([x for i, x in enumerate(input().split()) if (i + 1) % 3 == 0 and int(x) % 3 == 0]))))
