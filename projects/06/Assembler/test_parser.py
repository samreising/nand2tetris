import unittest
from parser import Parser
import sys

class Test_Parser(unittest.TestCase):
    # creates setup for tests
    def setUp(self):
        self.file = 'MaxL.asm'
        self.parser = Parser(self.file)
        self.test = []

    # should return False when there are no more commands
    def test_hasMoreCommands(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
        assert self.parser.hasMoreCommands() == False

    # should return program with comments stripped
    def test_hasMoreCommands(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.currentLine != '':
                self.test.append(self.parser.currentLine)
        assert self.test[0] == '@0'  # @0
        assert self.test[1] == 'D=M'  # D=M
        assert self.test[2] == '@1'  # @1
        assert self.test[3] == 'D=D-M'  # D=D-M
        assert self.test[4] == '@10'  # @10
        assert self.test[5] == 'D;JGT'  # D;JGT
        assert self.test[6] == '@1'  # @1
        assert self.test[7] == 'D=M'  # D=M
        assert self.test[8] == '@12'  # @12
        assert self.test[9] == '0;JMP'  # 0;JMP
        assert self.test[10] == '@0'  # @0
        assert self.test[11] == 'D=M'  # D=M
        assert self.test[12] == '@2'  # @2
        assert self.test[13] == 'M=D'  # M=D
        assert self.test[14] == '@14'  # @14
        assert self.test[15] == '0;JMP'  # 0;JMP


    # should return corresponding command type
    def test_commandType(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            command = self.parser.commandType()
            if command:
                self.test.append(command)
        assert self.test[0] == 'A_COMMAND'  # @0
        assert self.test[1] == 'C_COMMAND'  # D=M
        assert self.test[2] == 'A_COMMAND'  # @1
        assert self.test[3] == 'C_COMMAND'  # D=D-M
        assert self.test[4] == 'A_COMMAND'  # @10
        assert self.test[5] == 'C_COMMAND'  # D;JGT
        assert self.test[6] == 'A_COMMAND'  # @1
        assert self.test[7] == 'C_COMMAND'  # D=M
        assert self.test[8] == 'A_COMMAND'  # @12
        assert self.test[9] == 'C_COMMAND'  # 0;JMP
        assert self.test[10] == 'A_COMMAND'  # @0
        assert self.test[11] == 'C_COMMAND'  # D=M
        assert self.test[12] == 'A_COMMAND'  # @2
        assert self.test[13] == 'C_COMMAND'  # M=D
        assert self.test[14] == 'A_COMMAND'  # @14
        assert self.test[15] == 'C_COMMAND'  # 0;JMP


    # should return appropriate symbol or decimal xxx for A_COMMAND or L_COMMAND
    def test_symbol(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            symbol = self.parser.symbol()
            if symbol:
                self.test.append(symbol)
        assert self.test[0] == '0'  # @0
        assert self.test[1] == '1'  # @1
        assert self.test[2] == '10'  # @10
        assert self.test[3] == '1'  # @1
        assert self.test[4] == '12'  # @12
        assert self.test[5] == '0'  # @0
        assert self.test[6] == '2'  # @2
        assert self.test[7] == '14'  # @14


    # Should return the correct dest mnemonic for C_COMMAND
    def test_dest(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            dest = self.parser.dest()
            if dest:
                self.test.append(dest)
        assert self.test[0] == 'D'  # D=M
        assert self.test[1] == 'D'  # D=D-M
        assert self.test[2] == 'D'  # D=M
        assert self.test[3] == 'D'  # D=M
        assert self.test[4] == 'M'  # M=D

    # Should return the correct comp mnemonic for C_COMMAND
    def test_comp(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            comp = self.parser.comp()
            if comp:
                self.test.append(comp)
        assert self.test[0] == 'M'  # D=M
        assert self.test[1] == 'D-M'  # D=D-M
        assert self.test[2] == 'D'  # D;JGT
        assert self.test[3] == 'M'  # D=M
        assert self.test[4] == '0'  # 0;JMP
        assert self.test[5] == 'M'  # D=M
        assert self.test[6] == 'D'  # M=D
        assert self.test[7] == '0'  # 0;JMP

    # Should return the correct jump mnemonic for C_COMMAND
    def test_jump(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            jump = self.parser.jump()
            if jump:
                self.test.append(jump)
        assert self.test[0] == 'JGT'  # D;JGT
        assert self.test[1] == 'JMP'  # 0;JMP
        assert self.test[2] == 'JMP'  # 0;JMP

if __name__ == '__main__':
    unittest.main()