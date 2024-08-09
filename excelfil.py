# import xlsxwriter module     
import xlsxwriter     
      
book = xlsxwriter.Book('Example2.xlsx')     
sheet = book.add_sheet()     
       
# Rows and columns are zero indexed.     
row = 0    
column = 0    
      
content = ["Parker", "Smith", "John"]     
      
# iterating through the content list     
for item in content :     
      
    # write operation perform     
    sheet.write(row, column, item)     
      
    # incrementing the value of row by one with each iterations.     
    row += 1    
          
book.close()     