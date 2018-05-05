import unittest
from parser import Parser
from code import Code
import sys

class Test_Code(unittest.TestCase):
    # creates setup for tests
    def setUp(self):
        self.file = 'MaxL.asm'
        self.parser = Parser(self.file)
        self.test = []

    # Should return the correct binary code for dest mnemonic
    def test_dest(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            dest = self.parser.dest()
            if dest:
                self.test.append(Code.dest(dest))
        assert self.test[0] == '010'  # D=M
        assert self.test[1] == '010'  # D=D-M
        assert self.test[2] == '010'  # D=M
        assert self.test[3] == '010'  # D=M
        assert self.test[4] == '001'  # M=D

    # Should return the correct binary code for comp mnemonic
    def test_comp(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            comp = self.parser.comp()
            if comp:
                self.test.append(Code.comp(comp))
        assert self.test[0] == '1110000'  # D=M
        assert self.test[1] == '1010011'  # D=D-M
        assert self.test[2] == '0001100'  # D;JGT
        assert self.test[3] == '1110000'  # D=M
        assert self.test[4] == '0101010'  # 0;JMP
        assert self.test[5] == '1110000'  # D=M
        assert self.test[6] == '0001100'  # M=D
        assert self.test[7] == '0101010'  # 0;JMP

    # Should return the correct binary code for jump mnemonic
    def test_jump(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            jump = self.parser.jump()
            if jump:
                self.test.append(Code.jump(jump))
        assert self.test[0] == '001'  # D;JGT
        assert self.test[1] == '111'  # 0;JMP
        assert self.test[2] == '111'  # 0;JMP

if __name__ == '__main__':
    unittest.main()