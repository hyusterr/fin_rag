set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/lseu.mps"
write problem temp/lseu.mps.cip
presolve
write transproblem temp/lseu.mps_trans.cip
set heur emph def
read temp/lseu.mps_trans.cip
optimize
validatesolve "1120" "1120"
read temp/lseu.mps.cip
optimize
validatesolve "1120" "1120"
quit
