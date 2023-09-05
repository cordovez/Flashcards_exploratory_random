     
from abc import ABC, abstractmethod
from datetime import datetime

class WriteFile(ABC):
    """ An abstract class which is going to force all it's implementations
    to use the abstract method "write" but which sets the property filename
    and writes to a file with the "write_line" method. """
    
    @abstractmethod
    def write(self):
        return
    
    def __init__(self, filename):
        self.filename = filename
        
    def write_line(self, text):
        with open(self.filename, 'a') as fh:
            fh.write(text + '\n')


class DelimFile(WriteFile):
    """ Takes a filename property with extension, ex: data.csv, and the delimiter, ex: ',' 
    
    The method 'write' used with the instance takes a list property
    """
     
    def __init__(self, filename: str, delimiter: str):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter
        
    def write(self, this_list: list):
        line = self.delimiter.join(this_list)
        self.write_line(line)
    
class LogFile(WriteFile):
    """ Takes a filename property with extension, ex: log.txt 
    
    The method 'write' used with the instance takes a string

    """
    def write(self, this_line: str):
        dt = datetime.now()
        date_str = dt.strftime('%y-%m-%d %H%M')
        self.write_line(f'{date_str}  {this_line}')
 

# two files created by passing the filename:
log = LogFile("log.txt")
write_csv = DelimFile("data.csv", ",")

# implement the abstract method "write" for each file:
log.write("This is the first log message")
log.write("This is the second log message")
log.write("This is the third log message")

write_csv.write(["Juan", "Guayaquil", "1969", "54"])
write_csv.write(["Owen", "Dublin", "1978", "45"])

