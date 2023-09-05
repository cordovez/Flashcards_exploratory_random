     
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

class WriteFile(ABC):
    """ This abstract class take a filename string and a another class,
    assigned to 'writer'.
    
    The __init__ method creates an instance of the 'writer' assigned as 'formatter'
    
    The instance 'write' method takes formatter.format() passed from the 'writer' class, now called 'formatter' to write to file.
    """
    def __init__(self, filename, writer):
        # self.fh = open(filename, 'w')
        self.filename = filename
        self.formatter = writer()
        
    def write(self, text: Any):
        """ 
        The csv file expects a list, the log file expects a string
        """
        # self.fh.write(self.formatter.format(text))
        # self.fh.write('/n')
        with open(self.filename, 'a') as fh:
            fh.write(self.formatter.format(text))
            fh.write('\n')   
        
    # def closes(self):
    #     self.fh.close()

class CSVFormatter:
    """The parent class expects a format method
    """
    def __init__(self):
        self.delim = ","
    
    def format(self, this_list: list):
        new_list = []
        for element in this_list:
            if self.delim in element:
                new_list.append(f"{element}")
            else:
                new_list.append(element)
        return self.delim.join(new_list)
    
class LogFormatter:
    """The parent class expects a format method
    """ 
    def format(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        return f"{date_str} {this_line}"
    
write_csv = WriteFile('composition_data.csv', CSVFormatter)
write_log = WriteFile("composition_log.txt", LogFormatter)

write_csv.write(["Juan", "Guayaquil", "1969", "54"])
write_csv.write(["Owen", "Dublin", "1978", "45"])

write_log.write("This is the first log message of the composition model")
write_log.write("This is the second log message of the composition model")
