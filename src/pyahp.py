""" This is an implementation of the Analytic Hierarchy Process (AHP)
    in Python
"""
import math

class AHP(object):
    """ This class implements the AHP data structure and provides
        operations for the AHP analysis
    """

    def __init__(self, criteria=None, alternatives=None, weights=None):
        self.criteria = dict(criteria) if criteria else None
        self.alternatives = dict(alternatives) if alternatives else None
        if weights:
            self.weights = dict(weights)
        else:
            self.weights = {'-2': 1/9.0, '-1': 1/3.0, '0': 1, '1':3, '2':9}

        self.criteria_ranks = dict(dict())
        self.alternative_ranks = dict(dict())

    def comp_criteria(self):
        """Goes through the ranking process for the criteria"""
        for crit_row in self.criteria:
            print('Possible relations: {0}'.format(self.weights.keys()))

            for crit_col in self.criteria:
                if crit_col == crit_row:
                    this_ranking = '0'
                else:
                    this_ranking = None

                while this_ranking not in self.weights:
                    print('What is the relation of {1} vs. {2}?'.format(
                        crit_row, crit_col
                    ))

                    this_ranking = input()
                    if this_ranking not in self.weights:
                        print('Invalid relation. Possible relations: {0}'.format(
                            self.weights.keys()
                        ))

                self.criteria_ranks[crit_row][crit_col] = this_ranking

        for row in self.criteria_ranks:
            print(row)
