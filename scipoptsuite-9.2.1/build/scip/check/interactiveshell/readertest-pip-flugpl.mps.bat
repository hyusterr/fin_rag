set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/flugpl.mps"
write problem temp/flugpl.mps.pip
presolve
write transproblem temp/flugpl.mps_trans.pip
set heur emph def
read temp/flugpl.mps_trans.pip
optimize
validatesolve "1201500" "1201500"
read temp/flugpl.mps.pip
optimize
validatesolve "1201500" "1201500"
quit
