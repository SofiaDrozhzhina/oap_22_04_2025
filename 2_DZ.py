class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.current_line = ''
        self.lines = []

    def add_word(self, word):
        if not self.current_line:
            self.current_line = word
        elif len(self.current_line) + 1 + len(word) <= self.width:
            self.current_line += ' ' + word
        else:
            self.lines.append(self.current_line)
            self.current_line = word

    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)
            self.current_line = ''
        for line in self.lines:
            print(line)
        self.lines = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.current_line = ''
        self.lines = []

    def add_word(self, word):
        if not self.current_line:
            self.current_line = word
        elif len(self.current_line) + 1 + len(word) <= self.width:
            self.current_line += ' ' + word
        else:
            self.lines.append(self.current_line)
            self.current_line = word

    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)
            self.current_line = ''
        for line in self.lines:
            print(line.rjust(self.width))
        self.lines = []



lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()




