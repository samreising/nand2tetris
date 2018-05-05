class Parser:

    def __init__(self, input):
        self.file = open(input, 'r')
        self.currentLine = None
        self.nextLine = None

    # Are there more commands in the input?
    def hasMoreCommands(self):
        self.currentLine = self.file.readline()
        if self.currentLine == '':
            return False
        else:
            return True

    # Reads the next command from the input and makes it the current command. Should be called only if hasMoreCommands() is true. Initially there is no current command.
    def advance(self):
        if self.hasMoreCommands:
            self.removeComments()
            self.currentLine.strip()

    # Returns the type of the current command:
    # A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
    # C_COMMAND for dest=comp;jump
    # L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol.
    def commandType(self):
        if '@' in self.currentLine.strip():
            return 'A_COMMAND'
        elif '=' in self.currentLine.strip() or ';' in self.currentLine.strip():
            return 'C_COMMAND'
        elif '(' in self.currentLine.strip() or ')' in self.currentLine.strip():
            return 'L_COMMAND'

    # Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). Should be called only when commandType() is A_COMMAND or L_COMMAND.
    def symbol(self):
        if self.commandType() == 'A_COMMAND' or self.commandType() == 'L_COMMAND':
            command = ""
            for char in self.currentLine:
                if char == '@' or char == '=' or char == '(' or char == ')':
                    continue
                else:
                    command += char
            return command.strip()

    # Returns the dest mnemonic in the current C-command (8 possibilities). Should be called only when commandType() is C_COMMAND
    def dest(self):
        if self.commandType() == 'C_COMMAND' and '=' in self.currentLine:
            dest =self.currentLine.split('=')[0].strip()
            return dest

    # Returns the comp mnemonic in the current C-command (28 possibilities). Should be called only when commandType() is C_COMMAND.
    def comp(self):
        if self.commandType() == 'C_COMMAND' and '=' in self.currentLine:
            comp = self.currentLine.split('=')[1].strip()
            return comp
        elif self.commandType() == 'C_COMMAND' and ';' in self.currentLine:
            comp = self.currentLine.split(';')[0].strip()
            return comp

    # Returns the jump mnemonic in the current C-command (8 possibilities). Should be called only when commandType() is C_COMMAND.
    def jump(self):
        if self.commandType() == 'C_COMMAND' and ';' in self.currentLine:
            jump = self.currentLine.split(';')[1].strip()
            return jump

    # Remove comments from code
    def removeComments(self):
        self.currentLine = self.currentLine.split('//')[0].strip()