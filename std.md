# Setup Memory: Counter Mem Start/Upbit(flag)/DownCounter Mem Start/Downbit(flag)/Unbit
# 0+__ *0-__ **|000..
{thermbits}.>+>++>>->-->.
# load/unload unbit
{lunb}.[<++>].
{ulunb}.[<+>].
# 0123 mean if slot is 0/0 1/+ 2/- or 3/* then break loop
{skp1bit}.>.
{skpcmem}.[>3].
{skpdcmem}.[>3]>.
{slwtmbtsmemjmp}.* {skpcmem} {skpdcmem} {skp1bit}.
# Add to UpCounter | * takes you to 0 | / adds 0 after cursor
{add0b4}.</>>.
{add+b4}.</>+>.
{add-b4}.</>->.
{add*b4}.</>++>.
{uAdd}.* {skpcmem} {add+b4} {skpdcmem} {skp1bit}.
# setup graph memory | A graph is a complex data type
{stpgm}. .
{stp}.{thermbits}{stpgm}. setup func def
# GOAL: Never encapsulate a function call {stp{stp}} is illegal.
{main}.{stp}. functional call



