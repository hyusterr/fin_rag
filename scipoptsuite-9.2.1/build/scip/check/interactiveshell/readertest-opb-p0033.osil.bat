set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/p0033.osil"
write problem temp/p0033.osil.opb
presolve
write transproblem temp/p0033.osil_trans.opb
set heur emph def
read temp/p0033.osil_trans.opb
optimize
validatesolve "3089" "3089"
read temp/p0033.osil.opb
optimize
validatesolve "3089" "3089"
quit
