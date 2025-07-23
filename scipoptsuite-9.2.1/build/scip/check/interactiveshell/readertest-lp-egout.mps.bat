set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/egout.mps"
write problem temp/egout.mps.lp
presolve
write transproblem temp/egout.mps_trans.lp
set heur emph def
read temp/egout.mps_trans.lp
optimize
validatesolve "568.1007" "568.1007"
read temp/egout.mps.lp
optimize
validatesolve "568.1007" "568.1007"
quit
