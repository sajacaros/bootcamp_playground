def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError('Strands must be of equal length.')
    return sum([True if strand1[idx] != strand2[idx] else False for idx, _ in enumerate(strand1)])
