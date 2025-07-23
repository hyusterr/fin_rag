set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/MANN_a9.clq.lp"
write problem temp/MANN_a9.clq.lp.rlp
presolve
write transproblem temp/MANN_a9.clq.lp_trans.rlp
set heur emph def
read temp/MANN_a9.clq.lp_trans.rlp
optimize
validatesolve "16" "16"
read temp/MANN_a9.clq.lp.rlp
optimize
validatesolve "16" "16"
quit
