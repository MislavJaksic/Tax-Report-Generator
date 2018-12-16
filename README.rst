## Tax Report Generator

### Inputs

Data, settings and command line arguments.  
Data is supplied using well formed, tidy Excel tables.  
Settings specify the tax report metadata.  
Command line arguments tell the program which tax reports you want to generate.  

### Outputs

Tax reports.  

### Command Line Parsing

Python's "argparse" is responsible for extracting arguments and mapping them to Excel file names.

### Pathfinding

Python's "os" makes sure that file paths are constructed correctly.

### Data Wrangling

Using "pandas" and "openpyxl" Excel tables are loaded, filtered and inserted into a data frame wrapper.  
I went to great lengths not to have "magic numbers" around the code.  
Most literal values, that is constants, are in settings files.

### Generating XML Reports

Using "lxml" XML template files are parsed and loaded into memory as XML trees.  
XML trees are then filled with data from the data frame wrapper.  
Data filled XML trees are then connected together to form a larger XML tree.  
In the end, the XML tree is serialised into a XML file.  
