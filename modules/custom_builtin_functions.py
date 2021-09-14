from functools import reduce


class CustomBuiltinFuntions:
    '''
    Class with custom definitions of built-in functions.
    '''
    # len_counter: Class attribute to count the times _get_len was evoked. 
    len_counter = 0

    def _get_len(self, a=None, b=None):
        # Increments the len_counter attribute on each call.
        self.len_counter += 1
        return self.len_counter+1


if __name__ == '__main__':

    input_list = input('Enter list of Elements Saperated by space = ').split() or [0]
    if not ['0'] == input_list:
        list_length = reduce(CustomBuiltinFuntions()._get_len, input_list)
    else:
        # Reduce function not reducing ['0']
        list_length = 1

    print('Length of the list = ', list_length)




    
