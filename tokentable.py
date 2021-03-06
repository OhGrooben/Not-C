#Author : Craig Clephane 
#Last edited : 10/03/2019

#File which contains all the names of tokens, as well as symbols and keywords. 

#Must remain the same order - do NOT change without authors permission 
TokenEOF, TokenMultiply, TokenDivide, TokenMod, TokenAdd,       \
TokenSubtract, TokenNegate, TokenNOT, TokenLss, TokenLeq,       \
TokenGTR, TokenGEQ, TokenEQ, TokenNeg, TokenAssign,             \
TokenAND, TokenOR, TokenIF, TokenELSE, TokenWHILE,              \
TokenPrint, TokenPutc, TokenLparen, TokenRparen, TokenLbrace,   \
TokenRbrace, TokenSemi, TokenComma, TokenIdent, TokenInteger,   \
TokenString, TokenINT, TokenSTRING, TokenEOL = range(34)

#Must remain the same order - do NOT change without authors permission 
all_syms = ['End_of_File', 'OMulti', 'ODivide','OMod', 'OAdd', 
            'OSub', 'ONeg', 'ONot', 'OLess','OLessequal',
            'OGreater','OperationGreaterequal', 'OperationEqual', 'ONotequal', 'Oassign',
            'OAnd', 'Oor', 'KeywordIF', 'KeywordELSE', 'KeywordWHILE', 
            'KeywordPRINT', 'KeywordPutc', 'LeftParen', 'RightPaaren', 'LeftBrace', 
            'RightBrace', 'SemiColon', 'Comma', 'Identifier', 'Integer', 
            'String', 'KeywordInt', 'KeywordSTRING', 'EOL']


#changed comparaters to "compare" rather then "Operator"
categories = ['EOF', 'Operator', 'Operator', 'Operator', 'Operator',
              'Operator', 'Operator', 'Operator', 'Operator', 'Operator',
              'Operator', 'Operator', 'Operator', 'Operator', 'Assignment',
              'Operator', 'Operator', 'Function', 'Function', 'Function', 
              'Function', 'Punctuator', 'Punctuator', 'Punctuator', 'Punctuator',
              'Punctuator','StatementTerminator','Comma','Variable','Variable',            ##comma added by peter for a unique priority in parse tree.
              'Variable', 'Operator', 'Operator', 'EOL']
    
#translation table from front end to back end. WIP.
translation = ['End_of_File', 'OMulti', 'ODivide','OMod', 'OAdd', 
            'OSub', 'ONeg', 'ONot', 'OLess','OLessequal',
            'OGreater','OperationGreaterequal', 'OperationEqual', 'ONotequal', 'Oassign',
            'OAnd', 'Oor', 'KeywordIF', 'KeywordELSE', 'KeywordWHILE', 
            'KeywordPRINT', 'KeywordPutc', 'LeftParen', 'RightPaaren', 'LeftBrace', 
            'RightBrace', 'SemiColon', 'Comma', 'Identifier', 'Integer', 
            'String', 'KeywordInt', 'KeywordSTRING', 'EOL']


Symbols = { '{': TokenLbrace,
            '}': TokenRbrace,
            '(': TokenLparen,
            ')': TokenRparen,
            '+': TokenAdd,
            '-': TokenSubtract,
            '*': TokenMultiply,
            '%': TokenMod,
            ';': TokenSemi,
            ',': TokenComma }

#Keywords of the complier
keyWords = { 'if': TokenIF,
             'else':TokenELSE,
             'print': TokenPrint,
             'putc': TokenPutc,
             'while': TokenWHILE, 
             'Int': TokenINT,
             'String': TokenSTRING}

