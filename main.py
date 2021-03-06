#Author : Craig Clephane
#Last edited : 22/03/2019

#Main file for !C compiler.

#Imported files
import LexicalAnalysis as lex
import symtable
import parseTreeGeneration as treeGen
import optimiser as icOpt
import compile as ncCompile
import semantics as sem
import sys

# Reads source file, checks for arguments from commandline
outputFilename = "output.asm"
sourceFilename = ""

if len(sys.argv) < 2:
    print("Error (not-c): No input file provided. Usage: python3 main.py sourceFile outputFile")
    print("\t\tsourceFile: required, input file containing code for the source program")
    print("\t\toutputFile: optional, output file containing generated assembly code for target program. Default: output.asm")
    exit()
else:
    sourceFilename = sys.argv[1]
lex.file = open(sourceFilename, "r")
Idname =""

TokArrayLine = []
Buffer = treeGen.TreeGen();#tree gen class setup.

while True:
    tokenStream  =  lex.getToken()     #Grabs the token stream, which includes the type of token, column, line and variable if present.
    token        =  tokenStream[0]     #Grabs token.
    Line         =  tokenStream[1]     #Grabs line.
    Column       =  tokenStream[2]     #Grabs column.

    #Prints token visually, comment over when needed.
    print ("%5d  %10d %-20s %-14s" % (Line, Column,lex.tokentable.categories[tokenStream[0]], lex.tokentable.all_syms[tokenStream[0]]), end='')

    if token == lex.tokentable.TokenInteger: print("  %5d" % (tokenStream[3]))
    elif token == lex.tokentable.TokenString: print(' "%s"' % (tokenStream[3]))
    elif token == lex.tokentable.TokenIdent: print("  %s" % (tokenStream[3]))
    else: print("")

    if len(tokenStream)>3:Buffer.add(lex.tokentable.categories[tokenStream[0]],lex.tokentable.translation[tokenStream[0]], Line, tokenStream[3])     ##adds token to tree gen buffer.
    else: Buffer.add(lex.tokentable.categories[tokenStream[0]],lex.tokentable.all_syms[tokenStream[0]], Line)

    #Grabs END OF LINE Token, appends over filestream to output this.
    if lex.endOfLine == True:
        lex.endOfLine = False
        tokenStream = lex.tokentable.TokenEOL, Line, Column
        print ("%5d  %10d %-20s %-14s" % (Line, Column,lex.tokentable.categories[tokenStream[0]], lex.tokentable.all_syms[tokenStream[0]]), end='')
        print ("\n")
        Buffer.add(lex.tokentable.categories[tokenStream[0]],lex.tokentable.all_syms[tokenStream[0]], Line)

    #Ends loop if 'TokenEOF' is detected.
    if token == lex.tokentable.TokenEOF:
        tokenStream = lex.tokentable.TokenEOL, Line, Column##Adds EOL token before EOL to fix EOF bug.
        Buffer.add(lex.tokentable.categories[tokenStream[0]],lex.tokentable.all_syms[tokenStream[0]], Line)
        break

#Example of printing table, remove when needed
symtable.printTable()


'''
##PETERS NOTES:
all tree generation is done in above while loop. And all done withen the Buffer object.
to access trees simply use Buffer.retrieve(n) or Buffer.GeneratedTree[n] this will retrieve the root node for line 'n'
all other nodes for a tree are stored as a refrence in the form node.lhn EXAMPLE:

node=Buffer.retrieve(2)
Buffer.GeneratedTree[2]==node: True

Level1Node = node.lhn
Level2Node = node.lhn.rhn

an empty node will return None


BELOW CODE IS JUST FOR TESTING


''' 

print("\n\nGENERATED TREES: ")

for Node in Buffer.GeneratedTrees:
   print ("\nLine: ",Node.line)
   Node.PrintTree()


i = 0
for Node in Buffer.GeneratedTrees:
    print("\nSemantic analysis for line: " , Node.line)
    sem.eval(Buffer.GeneratedTrees[i], Node.line)
    i = i + 1
   
symtable.printTable() 

icOpt.icOptimise(Buffer)

# Call compile.py
if len(sys.argv) >= 3:
    outputFilename = sys.argv[2]
ncCompile.buildProgram(Buffer.GeneratedTrees, symtable.symbol_table, outputFilename)
