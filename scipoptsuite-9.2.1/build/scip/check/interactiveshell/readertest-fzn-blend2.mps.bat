set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/blend2.mps"
write problem temp/blend2.mps.fzn
presolve
write transproblem temp/blend2.mps_trans.fzn
set heur emph def
read temp/blend2.mps_trans.fzn
optimize
validatesolve "7.598985" "7.598985"
read temp/blend2.mps.fzn
optimize
validatesolve "7.598985" "7.598985"
quit
