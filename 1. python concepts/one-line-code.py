print(' '.join(x for i, x in enumerate(sorted(input().split())) if (i + 1) % 3 == 0 and int(x) % 3 == 0))
