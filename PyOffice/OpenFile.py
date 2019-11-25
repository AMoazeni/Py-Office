def OpenFile(*args, **kwargs):
    
    ''' csv_open(str 'csv_path') returns a Python Dictionary{} and accepts a local .CSV file path.
    
    Sample Use:
    List of columns - "csv_data['columns'][0]"
    List of rows - "csv_data['rows']"
    First row - "csv_data['rows'][0]"
    First item of first row - "csv_data['rows'][0][0]"
    '''
    
    # Initialize
    print('Running OpenFile function.', end='\n\n')
    path = args[0]
    file_data = {}
    index = 0
    error = 0
    
    # OpenFile Function Block
    try:
        with open(path, 'r') as file:
            
            
            file_data = {'Data': [],
                         'Extension': path.split('.')[-1],
                         'Length': 0,
                         'Name': path.split('/')[-1],
                         'Path': path
                        } 
            
            for line in file:
                file_data['Data'].append(line)
                
            file_data['Length'] = len(file_data[Data])
      
        return file_data

    # Error Handler
    except BaseException as e:
        error = 1
        error_msg = 'Error: \n' + str(e)
        print(error_msg, end='\n\n')
        return None
    
    # Clean up block
    finally:
        
        pass
