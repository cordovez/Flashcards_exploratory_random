from enum import StrEnum

class Strings(StrEnum):
    E = "E"
    A = "A"
    D = "D"
    G = "G"
    B = "B"


class Guitar_Strings:
    def __init__(self, open_string, scale):
        """Determines the notes on a string based on the string selected from an Enum"""
        self.open_string = open_string
        self.scale = scale

    @property
    def open_string(self):
        return self._open_string
    
    @open_string.setter
    def open_string(self, new_string):
        self._open_string = new_string   
        
    
    @property
    def notes_on_strings(self):
        """A string illustrated with its notes"""

        NOTES = ["C", "C#/Db", "D", "D#/Eb", "E", "F", 
                 "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
        
        _string = []
        starting_note = self._open_string
        starting_position = NOTES.index(starting_note)
        _string.append(f"{starting_note} ]")
        
        position = starting_position
        
        for note in NOTES:
            position += 1
            position %= len(NOTES)
            if NOTES[position] in self.scale:
                if len(NOTES[position]) == 5:
                    _string.append(f"{NOTES[position]}|")
                else:
                    _string.append(f"--{NOTES[position]}--|")
            else:
                _string.append("-----|")
            
        
        return _string


