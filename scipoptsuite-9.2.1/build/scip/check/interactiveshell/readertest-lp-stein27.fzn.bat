set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/stein27.fzn"
write problem temp/stein27.fzn.lp
presolve
write transproblem temp/stein27.fzn_trans.lp
set heur emph def
read temp/stein27.fzn_trans.lp
optimize
validatesolve "18" "18"
read temp/stein27.fzn.lp
optimize
validatesolve "18" "18"
quit
