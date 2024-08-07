# Thermo

Thermo is a language designed to be a superset of BrainFuck. Thermo is designed to use only either 2-bit or 64-bit numbers as a Language for coding a Turing Machine. The Standard 2-bit number only has 3 numeric values; 0, 1 and -1. * is a special numeric symbol which happens as a result of adding to 1 or subtracting from -1, then subtracting or adding with + or - again would send it to 0.   

## Supported Operators

- @ means allocate 64 bit number and read in 64 bit pointer address at the current cell
- ! means copy pointer address buffer into current cell and allocate a 64 bit number at the cell (also reads in cell pointer)
- ~ means deallocate memory address in pointer address buffer
- & means read in current cell into pointer address buffer
- | means jump to pointer address' cell
- * takes you to cell 0 
- ** skips to the next cell with value * or 0 if not found
- / adds a cell with value 0 after the current cell
- \\{x} copies a 64 bit number x into the current cell
- $ copies the number in the current cell to a copy value buffer
- ^ copies the number in the copy value buffer into the current cell
- , prints the number in the current copy value buffer to the terminal in ASCII
- ; prints the number in the current copy value buffer to the terminal
- () are the same as [] expect () loops until the value in the function operand buffer = 0
- %% encapsulates math operations done on the function operand buffer, +-$^,; are allowed in between %% 

- <>+-[] are the other supported bf operations

## Example of 2-Bit Math

0++ = * / *+ = 0 / 0-- = * / *- = 0 / 0- = - / 0+ = + / +- = 0 / -+ = 0 /
