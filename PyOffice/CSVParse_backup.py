def CSVParse(*args, **kwargs):
    
    ''' csv_open(str 'csv_path') returns a Python Dictionary{} and accepts a local .CSV file path.
    
    Sample Use:
    List of columns - "csv_data['columns'][0]"
    List of rows - "csv_data['rows']"
    First row - "csv_data['rows'][0]"
    First item of first row - "csv_data['rows'][0][0]"
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
        error_msg = str(e)
    
    # Clean up block
    finally:
        if error:
            print(func_name, '[ERROR]:', error_msg)
        else:
            print(func_name, '[OK] {0:.3f}s\n'.format(float(t() - time_start)))
        pass

