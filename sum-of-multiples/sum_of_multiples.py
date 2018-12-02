def sum_of_multiples(limit, multiples):
    space = list(range(1, limit))
    res = set()
    for num in space:
        for multiplier in multiples:
            if num % multiplier == 0:
                res.add(num)

    return sum(res)