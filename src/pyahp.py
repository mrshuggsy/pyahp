""" This is an implementation of the Analytic Hierarchy Process (AHP)
    in Python
"""
# import math
import logging
logging.basicConfig(level=logging.INFO)


class AHP(object):
    """ This class implements the AHP data structure and provides
        operations for the AHP analysis
    """

    def __init__(self, criteria=None, alternatives=None, weights=None):
        self.criteria = list(criteria) if criteria is not None else []
        self.alternatives = list(alternatives) if alternatives is not None else []
        if weights is not None:
            self.weights = dict(weights)
        else:
            self.weights = {'-2': 1/9.0, '-1': 1/3.0, '0': 1, '1': 3, '2': 9}

        self.criteria_ranks = dict()
        self.alternative_ranks = dict()

    def add_criteria(self, *_criteria):
        """Adds one or more criteria to the AHP analysis"""
        for crit in _criteria:
            self.criteria.append(crit)

    def add_alternative(self, *_alternative):
        """Adds one or more alternatives to the AHP analysis"""
        for alt in _alternative:
            self.alternatives.append(alt)

    def _rank_items(self, items):
        pass

    def _get_rank_input(self, item1, item2, _criteria=None):
        if item1 == item2:
            this_ranking = '0'
        else:
            this_ranking = None

        if _criteria:
            rank_question_str = 'Within the context of {0}, '.format(_criteria) + \
                                'what is the relation of {0} vs. {1}?'.format(
                                    item1, item2
                                )
        else:
            rank_question_str = 'What is the relation of {0} vs. {1}?'.format(
                item1, item2
            )

        while this_ranking not in self.weights:
            print(rank_question_str)

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

    def rank_criteria(self, values=None):
        """Goes through the ranking process for the criteria from a blank ranking matrix"""
        ranking_sentinel = 0
        if values is not None:
            values.reverse()

        for criteria in self.criteria:
            self.criteria_ranks[criteria] = dict()

        for crit_row in range(len(self.criteria)):
            print('Possible relations: {0}'.format(self._make_weights_str()))
            ranking_sentinel += 1

            for crit_col in range(0, ranking_sentinel):
                if values is not None:
                    if crit_col == crit_row:
                        rank_val = self.weights['0']
                    else:
                        logging.info('Ranking %s vs. %s as %s: %s',
                                     self.criteria[crit_row],
                                     self.criteria[crit_col],
                                     values[0],
                                     self.weights[str(values[0])]
                                    )
                        rank_val = self.weights[str(values.pop())]
                        # TODO: Try/catch on the rank_val pop above
                else:
                    rank_val = self._get_rank_input(self.criteria[crit_row],
                                                    self.criteria[crit_col])
                self.criteria_ranks[self.criteria[crit_row]][self.criteria[crit_col]] = rank_val
                self.criteria_ranks[self.criteria[crit_col]][self.criteria[crit_row]] = 1/rank_val

    def rank_alternatives(self):
        """Goes through the ranking process for the alternatives within each criteria
           starting from a blank matrix"""
        ranking_sentinel = 0

        for this_criteria in self.criteria:
            self.alternative_ranks[this_criteria] = dict()
            for alt in self.alternatives:
                self.alternative_ranks[this_criteria][alt] = dict()

            for alt_row in range(len(self.alternatives)):
                print('Possble relations: {0}'.format(self._make_weights_str()))
                self.alternative_ranks[this_criteria][self.alternatives[alt_row]] = dict()
                ranking_sentinel += 1

                for alt_col in range(0, ranking_sentinel):
                    # TODO: Fix: _get_rank_input doesn't ask for rank during alternatives rankings
                    rank_val = self._get_rank_input(
                        self.alternatives[alt_row], self.alternatives[alt_row],
                        _criteria=this_criteria
                    )
                    print('Context: {0} | {1} vs. {2} = {3}'.format(
                        this_criteria,
                        self.alternatives[alt_row],
                        self.alternatives[alt_col],
                        rank_val
                    ))
                    # TODO: Fix alternatives rankings
                    self.alternative_ranks[this_criteria] \
                        [self.alternatives[alt_row]][self.alternatives[alt_col]] = rank_val
                    self.alternative_ranks[this_criteria] \
                        [self.alternatives[alt_col]][self.alternatives[alt_row]] = 1/rank_val

    def print_criteria_matrix(self):
        """Method to pretty-print the matrix of criteria rankings"""
        for row, crit in (self.criteria_ranks, self.criteria):
            temp_str = '{0}: '.format(crit) + self.criteria_ranks[row]
            print(temp_str)

    def print_alternatives_matrices(self):
        """Method to pretty-print the matrices of alternatives in the context of each
           criteria rankings"""
        for crit in self.criteria:
            print("For the '{0}' critiera:".format(crit))

            for opt in self.alternative_ranks[crit]:
                temp_str = '{0}: '.format(opt) + self.alternative_ranks[opt]
                print(temp_str)


if __name__ == '__main__':
    COMP = AHP()
    COMP.add_criteria('Color', 'Weight', 'Cost')
    COMP.add_alternative('Widget A', 'Widget B')
    COMP.rank_criteria(values=[2, -1, 1])
    COMP.rank_alternatives()
    COMP.print_criteria_matrix()
