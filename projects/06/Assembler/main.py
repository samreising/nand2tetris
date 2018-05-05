from parser import Parser
from code import Code
from symboltable import SymbolTable
import sys


class Main:
    def main():
        filename = sys.argv[1]
        output = open(filename.split('.')[0] + '.hack', 'w')

        firstPass = Parser(filename)
        symbolTable = SymbolTable()
        rom_address = 0
        ramAddress = 16

        # First pass adds L_COMMANDs and ROM addresses to symbol table
        while firstPass.hasMoreCommands():
            firstPass.advance()
            command = firstPass.commandType()
            if command == 'A_COMMAND' or command == 'C_COMMAND':
                rom_address += 1
            elif command == 'L_COMMAND':
                symbolTable.addEntry(firstPass.symbol(), rom_address)

        # When A_COMMAND is encountered:
        #   if symbol is a digit write it to file
        #   if symbol is not a digit, look it up in the symbol table. If it's there, write the address
        #   if symbol is not a digit, look it up in the symbol table. If it is not there, add it then write the address
        secondPass = Parser(filename)
        while secondPass.hasMoreCommands():
            secondPass.advance()
            command = secondPass.commandType()
            symbol = secondPass.symbol()
            if command == 'A_COMMAND' and symbol:
                if symbol.isdigit():
                    output.write('0' + '{0:015b}'.format(int(symbol)) + '\n')
                elif symbolTable.contains(symbol):
                    symbolAddress = symbolTable.getAddress(symbol)
                    output.write('0' + '{0:015b}'.format(int(symbolAddress)) + '\n')
                else:
                    symbolTable.addEntry(symbol, ramAddress)
                    ramAddress += 1
                    symbolAddress = symbolTable.getAddress(symbol)
                    output.write('0' + '{0:015b}'.format(int(symbolAddress)) + '\n')
            else:
                dest = Code.dest(secondPass.dest())
                jump = Code.jump(secondPass.jump())
                comp = Code.comp(secondPass.comp())
                if comp != None:
                    output.write('111' + comp + dest + jump + '\n')

        output.close()

    if __name__ == "__main__":
        main()