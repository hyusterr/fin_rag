set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/p0033.osil"
write problem temp/p0033.osil.lp
presolve
write transproblem temp/p0033.osil_trans.lp
set heur emph def
read temp/p0033.osil_trans.lp
optimize
validatesolve "3089" "3089"
read temp/p0033.osil.lp
optimize
validatesolve "3089" "3089"
quit
