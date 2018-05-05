// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LOOPWHITE)
	@KBD
	D=M
	@DRAWBLACK
	D; JGT 	// if KBD > 0 goto DRAWBLACK
	@LOOPWHITE
	D; JEQ 	// if KBD = 0 goto LOOPWHITE

(DRAWBLACK)
	@SCREEN
	D=A
	@addr
	M=D 	// addr = 16384
	
	@8192
	D=A
	@n
	M=D 	// n = 8192, last SCREEN address

	@i
	M=0 	// i = 0

(BLACK)
	@i
	D=M
	@n
	D=M-D
	@LOOPBLACK
	D; JEQ 	// if i = n goto LOOPBLACK

	@addr
	A=M
	M=-1 	// RAM[addr] = 1111111111111111

	@i
	M=M+1 	// i = i + 1
	@addr
	M=M+1 	// addr = addr + 1
	@BLACK
	0; JMP 	// goto BLACK

(LOOPBLACK)
	@KBD
	D=M
	@LOOPBLACK
	D; JGT 	// if KBD > 0 goto LOOPBLACK
	@DRAWWHITE
	D; JEQ 	// if KBD = 0 goto DRAWWHITE

(DRAWWHITE)
	@SCREEN
	D=A
	@addr
	M=D 	// addr = 16384
	
	@8192
	D=A
	@n
	M=D 	// n = 8192, last SCREEN address

	@i
	M=0 	// i = 0

(WHITE)
	@i
	D=M
	@n
	D=M-D
	@LOOPWHITE
	D; JEQ 	// if i = n goto LOOPWHITE

	@addr
	A=M
	M=0 	// RAM[addr] = 1111111111111111

	@i
	M=M+1 	// i = i + 1
	@addr
	M=M+1 	// addr = addr + 1
	@WHITE
	0; JMP 	// goto WHITE

