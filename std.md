# setup memory counter/downcounter/upbit/downbit/unbit
{stpbits}.>>+>->>. 
# increment unbit ("pc counter") call twice to qbit then unbit if using QLib vs RLib
{incunb}.[<+].
# clear RLib unbit
.[<++].
# setup graph memory
{stpgm}. .
{stp}.{stpbits}{stpgm}. setup func def
{main}.{{stp}}. functional call
 


