set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/bell5.mps"
write problem temp/bell5.mps.fzn
presolve
write transproblem temp/bell5.mps_trans.fzn
set heur emph def
read temp/bell5.mps_trans.fzn
optimize
validatesolve "8966406.49" "8966406.49"
read temp/bell5.mps.fzn
optimize
validatesolve "8966406.49" "8966406.49"
quit
