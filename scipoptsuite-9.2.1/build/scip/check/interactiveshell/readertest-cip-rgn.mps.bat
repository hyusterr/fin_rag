set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/rgn.mps"
write problem temp/rgn.mps.cip
presolve
write transproblem temp/rgn.mps_trans.cip
set heur emph def
read temp/rgn.mps_trans.cip
optimize
validatesolve "82.19999924" "82.19999924"
read temp/rgn.mps.cip
optimize
validatesolve "82.19999924" "82.19999924"
quit
