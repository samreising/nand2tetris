// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
	@R0
	D=M 	// D = RAM[0]
	@n
	M=D 	// n = R0
	@product
	M=0 	// product = 0
	@R1
	D=M 	// D = RAM[1]
	@i
	M=D 	// i = R1

(LOOP)
	@i
	D=M
	@STOP
	D; JEQ 	// if i = 0 goto STOP

	@product
	D=M
	@n
	D=D+M
	@product
	M=D 	// product = product + n
	@i
	M=M-1 	//i = i - 1
	@LOOP
	0; JMP

(STOP)
	@product
	D=M
	@R2
	M=D 	// RAM[2] = product

(END)
	@END
	0; JMP