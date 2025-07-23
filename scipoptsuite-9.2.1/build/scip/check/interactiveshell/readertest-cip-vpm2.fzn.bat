set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/vpm2.fzn"
write problem temp/vpm2.fzn.cip
presolve
write transproblem temp/vpm2.fzn_trans.cip
set heur emph def
read temp/vpm2.fzn_trans.cip
optimize
validatesolve "13.75" "13.75"
read temp/vpm2.fzn.cip
optimize
validatesolve "13.75" "13.75"
quit
