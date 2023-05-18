def parting(xs, parts):
    part_len = [xs[i:i + parts] for i in range(0, len(xs), parts)]
    return part_len
