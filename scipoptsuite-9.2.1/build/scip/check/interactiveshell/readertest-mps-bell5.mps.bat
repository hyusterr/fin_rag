set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/bell5.mps"
write problem temp/bell5.mps.mps
presolve
write transproblem temp/bell5.mps_trans.mps
set heur emph def
read temp/bell5.mps_trans.mps
optimize
validatesolve "8966406.49" "8966406.49"
read temp/bell5.mps.mps
optimize
validatesolve "8966406.49" "8966406.49"
quit
