set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/rgn.mps"
write problem temp/rgn.mps.rlp
presolve
write transproblem temp/rgn.mps_trans.rlp
set heur emph def
read temp/rgn.mps_trans.rlp
optimize
validatesolve "82.19999924" "82.19999924"
read temp/rgn.mps.rlp
optimize
validatesolve "82.19999924" "82.19999924"
quit
