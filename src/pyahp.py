""" This is an implementation of the Analytic Hierarchy Process (AHP)
    in Python
"""
import math

class AHP(object):
    """ This class implements the AHP data structure and provides
        operations for the AHP analysis
    """

    def __init__(self, criteria=None, alternatives=None, weights=None):
        self.criteria = list(criteria) if criteria else []
        self.alternatives = list(alternatives) if alternatives else []
        if weights:
            self.weights = dict(weights)
        else:
            self.weights = {'-2': 1/9.0, '-1': 1/3.0, '0': 1, '1':3, '2':9}

        self.criteria_ranks = dict()
        self.alternative_ranks = dict()

    def add_criteria(self, *criteria):
        """Adds criteria to the AHP analysis"""
        for crit in criteria:
            self.criteria.append(crit)


    def _rank_items(self, items):
        pass


    def _get_rank_input(self, item1, item2, criteria=None):
        if criteria:
            # Should do something different if we're ranking within the context of some criteria
            pass

        if item1 == item2:
            this_ranking = '0'
        else:
            this_ranking = None

        while this_ranking not in self.weights:
            print('What is the relation of {0} vs. {1}?'.format(
                item1, item2
            ))

            this_ranking = input()
            if this_ranking not in self.weights:
                print('Invalid relation. Possible relations: {0}'.format(
                    self.weights.keys()
                ))

        return self.weights[this_ranking]


    def _set_rank_value(self, item1, item2, value):
        pass


    def _make_weights_str(self):
        temp_str = ''
        for weight in self.weights:
            temp_str += "'" + weight + "'" + '=' + \
                        str(round(self.weights[weight], ndigits=3)) + ' | '
        return temp_str[0:-3]


    def rank_criteria(self):
        """Goes through the ranking process for the criteria from a blank ranking matrix"""
        ranking_sentinel = 0
        for criteria in self.criteria:
            self.criteria_ranks[criteria] = dict()

        for crit_row in range(len(self.criteria)):
            print('Possible relations: {0}'.format(self._make_weights_str()))
            ranking_sentinel += 1

            for crit_col in range(0, ranking_sentinel):
                rank_val = self._get_rank_input(self.criteria[crit_row], self.criteria[crit_col])
                self.criteria_ranks[self.criteria[crit_row]][self.criteria[crit_col]] = rank_val
                self.criteria_ranks[self.criteria[crit_col]][self.criteria[crit_row]] = 1/rank_val

        for row in self.criteria_ranks:
            print(self.criteria_ranks[row])


    def print_criteria_matrix(self):
        """Method to pretty-print the matrix of criteria rankings"""
        for row in self.criteria_ranks:
            row_str = str(row)
            print(row_str)


if __name__ == '__main__':
    COMP = AHP()
    COMP.add_criteria('Color', 'Weight', 'Cost')
    COMP.rank_criteria()
    COMP.print_criteria_matrix()
