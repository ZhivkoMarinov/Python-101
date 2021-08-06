class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened  

    def is_inside(self, value):
        start_boundary = 0
        end_boundary = 0

        if self.start_opened:
            start_boundary += 1
        if self.end_opened:
            end_boundary += 1

        return self.start + start_boundary <= value <= self.end - end_boundary

    def stringify(self):
        start_symbol = '['
        end_symbol = ']'

        if self.start_opened:
            start_symbol = '('
        if self.end_opened:
            end_symbol = ')'

        return f"{start_symbol}{self.start}, {self.end}{end_symbol}"
