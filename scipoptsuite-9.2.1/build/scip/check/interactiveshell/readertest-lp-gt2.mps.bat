set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/gt2.mps"
write problem temp/gt2.mps.lp
presolve
write transproblem temp/gt2.mps_trans.lp
set heur emph def
read temp/gt2.mps_trans.lp
optimize
validatesolve "21166" "21166"
read temp/gt2.mps.lp
optimize
validatesolve "21166" "21166"
quit
