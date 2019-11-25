from time import time as t

def SampleFunction(*args, **kwargs):
    
    ''' 
    Function Documentation Here.
    '''
    
    # Initialize
    start_time = t()
    func_name = 'SampleFunction'
    data = {}
    error = 0
    error_msg = ''
    
    # SampleFunction Block
    try:
        if args:
            for arg in args:
                print (arg)
        data['start_time'] = start_time
        data['ex_time'] = t() - start_time
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
            print(func_name, '[OK]: {0:.3}s\n'.format(float(t() - start_time)))
        pass


