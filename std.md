# setup memory: Counter mem start/Upbit/DownCounter mem start/Downbit/Unbit
# 0+ * 0- * * |000..
{thermbits}.>+>++>>->-->.
# load unbit
{lunb}.[<++>].
# unload unbit
{ulunb}.[<+>].
# For 0123 if slot is 0/0 1/+ 2/- or 3/* then break
{skpdcmem}.[>3]>.
# Add to UpCounter * takes you to 0 / adds 0 after cursor
{add0b4}.</>>.
{add+b4}.</>+>.
{add-b4}.</>->.
{add*b4}.</>++>.
{uAdd}.*[>3] {add+b4} {skpdcmem} >.
# setup graph memory
# A graph is a complex data type
{stpgm}. .
{stp}.{thermbits}{stpgm}. setup func def
# GOAL: Never encapsulate a function call {stp{stp}} is illegal.
{main}.{stp}. functional call



