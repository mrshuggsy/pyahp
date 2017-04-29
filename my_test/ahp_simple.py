"""Simple test script for basic AHP functionality outside of the module/API"""

weights = {'-2': 1/9.0, '-1': 1/3.0, '0': 1, '1': 3, '2': 9}
crits = []
opts = []

# Capture all the critera
print('Please input all the criteria (-1 to stop).')
while True:
    crit = input('Please input a criteria: ')
    if '-1' in crit:
        break
    crits.append(crit)
    print('Current criteria: {0}'.format(crits))
print('All AHP criteria: {0}'.format(crits))

# Capture all the options
print('Please input all the options (-1 to stop).')
while True:
    opt = input('Please input an option: ')
    if '-1' in opt:
        break
    opts.append(opt)
    print('Current options: {0}'.format(opts))
print('All AHP options: {0}'.format(opts))

# Rank the criteria
rank_sentinal = 1
rank_crits = dict()
print(weights)
for crit_r in crits:
    rank_crits[crit_r] = dict()
    for crit_c in crits[:rank_sentinal]:
        if crit_r == crit_c:
            rnk_val = 1
        else:
            rnk_val = weights[input('Please enter a weight relation for {0} vs {1}: '.format(
                crit_r, crit_c
            ))]
        rank_crits[crit_r][crit_c] = rnk_val
        try:
            rank_crits[crit_c][crit_r] = 1/rnk_val
        except KeyError:
            rank_crits[crit_c] = {crit_r: 1/rnk_val}
print('Criteria Rankings: {0}'.format(rank_crits))

# Rank the options within a criteria
rank_sentinal = 1
rank_opts = dict()
for opt in opts:
    rank_opts[opt] = dict()
    for crit_r in crits:
        rank_opts[opt][crit_r] = dict()
        for crit_c in crits[:rank_sentinal]:
            if crit_r == crit_c:
                rnk_val = 1
            else:
                rnk_val = weights[input('Please enter a weight relation for {0} vs {1}: '.format(
                    crit_r, crit_c
                ))]
            rank_crits[crit_r][crit_c] = rnk_val
            try:
                rank_crits[crit_c][crit_r] = 1/rnk_val
            except KeyError:
                rank_crits[crit_c] = {crit_r: 1/rnk_val}
    print('For criteria {0}, Option Rankings: {1}'.format(opt, rank_opts[opt]))
print('All option rankings: {0}'.format(rank_opts))

#

