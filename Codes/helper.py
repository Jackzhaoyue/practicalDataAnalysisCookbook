import time             
import numpy as np
import sklearn.metrics as mt                          

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('The method {0} took {1:2.2f} sec to estimate.' \
              .format(method.__name__, te-ts))
        return result

    return timed

def split_data(data, y, x = 'All', test_size = 0.33):
    # dependent variable and all the independent
    variables = {'y': y}

    if x == 'All':
        allColumns = list(data.columns)
        allColumns.remove(y)

        variables['x'] = allColumns
    else:
        if type(x) != list:
            print('The x parameter has to be a list...')
            sys.exit(1)
        else:
            variables['x'] = x

    # create a variable to flag the training sample
    data['train']  = np.random.rand(len(data)) < (1 - test_size) 

    # split the data into training and testing
    train_x = data[data.train] [variables['x']]
    train_y = data[data.train] [variables['y']]
    test_x  = data[~data.train][variables['x']]
    test_y  = data[~data.train][variables['y']]

    return train_x, train_y, test_x, test_y

def printModelSummary(actual, predicted):
    print('Overall accuracy of the model is {0:.2f}'\
        .format(
            (actual == predicted).sum() / \
            len(actual) * 100))
    print(mt.classification_report(actual, predicted))