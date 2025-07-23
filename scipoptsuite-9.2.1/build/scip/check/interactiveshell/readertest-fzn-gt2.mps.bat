set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/gt2.mps"
write problem temp/gt2.mps.fzn
presolve
write transproblem temp/gt2.mps_trans.fzn
set heur emph def
read temp/gt2.mps_trans.fzn
optimize
validatesolve "21166" "21166"
read temp/gt2.mps.fzn
optimize
validatesolve "21166" "21166"
quit
