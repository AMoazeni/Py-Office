import csv

def CSVParse(*args, **kwargs):
  ''' csv_open(str 'csv_path') returns a Python Dictionary{} and accepts a local .CSV file path.

      Sample Use:
      List of columns - "csv_data['columns'][0]"
      List of rows - "csv_data['rows']"
      First row - "csv_data['rows'][0]"
      First item of first row - "csv_data['rows'][0][0]"
  '''

  # Initialize
  print('', end='\n\n')
  csv_data={}
  rows=[]
  columns=[]
  index=0

  # Function Block
  try:
    with open(args[0], newline='') as csvfile:
      csv_reader = csv.reader(csvfile)

      for row in csv_reader:
        if index==0:
          columns.append(row)
        else:
          rows.append(row)
        index+=1
        #print(', '.join(row))

      csv_data['columns'] = columns
      csv_data['rows'] = rows

    return csv_data

  # Error Handler
  except BaseException as e:
    error_msg = 'Error: \n' + str(e)
    print(error_msg, end='\n\n')
    return error_msg

  # Clean up block
  finally:
    pass
