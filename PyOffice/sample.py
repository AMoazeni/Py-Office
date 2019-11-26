from time import time as t

def SampleFunction(*args, **kwargs):
    
    ''' 
    Function Documentation Here.
    '''
    
    # Initialize
    func_name = 'SampleFunction'
    print(func_name, '[START]')
    time_start = t()
    data = {}
    error = 0
    error_msg = ''
    
    # SampleFunction Block
    try:
        if args:
            for i, arg in enumerate(args):
                print ('Input', i+1, ': ', arg)
        data['time_start'] = float(round(time_start, 4))
        data['time_ex'] = float(round(t() - time_start, 4))
        return data

    # Error Handler
    except BaseException as e:
        error = 1
        error_msg = str(e)
    
    # Clean up block
    finally:
        if error:
            print(func_name, '[ERROR]:', error_msg)
        else:
            print(func_name, '[OK] {0:.3f}s\n'.format(float(t() - time_start)))
        pass


