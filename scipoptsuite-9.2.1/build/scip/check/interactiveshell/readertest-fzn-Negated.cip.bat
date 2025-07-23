set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/Negated.cip"
write problem temp/Negated.cip.fzn
presolve
write transproblem temp/Negated.cip_trans.fzn
set heur emph def
read temp/Negated.cip_trans.fzn
optimize
validatesolve "1" "1"
read temp/Negated.cip.fzn
optimize
validatesolve "1" "1"
quit
