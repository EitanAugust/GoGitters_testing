import logging


logging.basicConfig(filename="arrayfunctions.log",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class ArrayFunc:

    def __init__(self, array):
        self.array = array
        self.max_diff = None
        self.sum_list = None
        self.min_max = None

    def calc_max_diff(self):
        '''Function to find the maximum magnitude difference between
        consecutive elements in a numerical list

        :param self: class that is initialized containing an array
        :raises ValueError: if the numerical list input is of length
         less than 2
        :raises TypeError: if a non-numerical list is given
        :raises ImportError: if a required package was not loaded
        '''

        diff_var = []
        try:
            for i in range(0, len(self.array)-1):
                diff_var.append(self.array[i+1] - self.array[i])

            if abs(max(diff_var)) > abs(min(diff_var)):
                self.max_diff = max(diff_var)
            elif abs(max(diff_var)) < abs(min(diff_var)):
                self.max_diff = min(diff_var)
            elif max(diff_var) == min(diff_var):
                self.max_diff = max(diff_var)
            else:
                self.max_diff = [min(diff_var), max(diff_var)]

            logging.info('Function completed without errors')

        except ValueError:
            print('Numerical list must be at least of length 2')
            logging.warning('Found max diff is of type None')
            self.max_diff = None
        except TypeError:
            print('Only numerical lists accepted')
            logging.warning('Found max diff is of type None')
            self.max_diff = None
        except ImportError:
            # This file does not use any non-standard python
            # packages like numpy
            print('Missing package... or basic python installation')
            logging.debug('Required package is not installed')
            self.max_diff = None

    def calc_sum_list(self):
        '''Function to find the sum of all elements in a list

        :param self: class that is initialized containing an array
        :raises ValueError: if infinity is in the input array
        :raises TypeError: if list is empty or contains non-numericals
        :raises ImportError: if a required package was not loaded
        '''
        import numpy as np
        try:
            if(float('inf') in self.array or float('-inf') in self.array):
                raise ValueError
            if(len(self.array) == 0):
                raise TypeError
            self.sum_list = np.sum(self.array)
            logging.info('Function completed without errors')

        except ImportError:
            print('Missing Numpy')
            logging.debug('numpy is not installed')
            self.sum_list = None
        except TypeError:
            print('Only numerical lists are accepted')
            logging.warning('sum is None')
            self.sum_list = None
        except ValueError:
            print('Input contains inappropriate value')
            logging.warning('sum is None')
            self.sum_list = None

    def calc_min_max(self):
        """Finds the minimum and maximum values of a numerical list.

        :param self: class that is initialized containing an array
        :raises ImportError: if numpy is not installed
        :raises TypeError: if a non-numerical list is given
        :raises ValueError: if a numerical list is not of at least length 2
        """
        try:
            import numpy as np
            min_val = np.amin(self.array)
            max_val = np.amax(self.array)
            self.min_max = (min_val, max_val)

            logging.info('Function was completed successfully.')

        except ImportError:
            print('Missing package: numpy')
            logging.debug('Required package numpy is not installed')
            self.min_max = None
        except TypeError:
            print('Only numerical lists accepted')
            logging.warning('Min/max is not numerical list')
            self.min_max = None
        except ValueError:
            print('Numerical list must be at least of length 1')
            logging.warning('Min/max not length 1')
            self.min_max = None
