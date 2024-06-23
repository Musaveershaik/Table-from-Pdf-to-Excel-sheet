import camelot

# Provide the full path to the file
file_path = 'Path of your pdf file'
tables = camelot.read_pdf(file_path, pages='1')
print(tables)

# Export the tables to CSV file at the desired location
output_path = 'file sve location'
tables.export(output_path, f='csv', compress=True)
tables[0].to_csv(output_path)  # to a csv file
print(tables[0].df)  # to a df
