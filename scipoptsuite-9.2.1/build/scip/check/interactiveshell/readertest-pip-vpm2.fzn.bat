set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/vpm2.fzn"
write problem temp/vpm2.fzn.pip
presolve
write transproblem temp/vpm2.fzn_trans.pip
set heur emph def
read temp/vpm2.fzn_trans.pip
optimize
validatesolve "13.75" "13.75"
read temp/vpm2.fzn.pip
optimize
validatesolve "13.75" "13.75"
quit
