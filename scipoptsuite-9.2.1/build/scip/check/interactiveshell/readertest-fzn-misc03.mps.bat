set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/misc03.mps"
write problem temp/misc03.mps.fzn
presolve
write transproblem temp/misc03.mps_trans.fzn
set heur emph def
read temp/misc03.mps_trans.fzn
optimize
validatesolve "3360" "3360"
read temp/misc03.mps.fzn
optimize
validatesolve "3360" "3360"
quit
