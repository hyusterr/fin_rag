set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/flugpl.mps"
write problem temp/flugpl.mps.rlp
presolve
write transproblem temp/flugpl.mps_trans.rlp
set heur emph def
read temp/flugpl.mps_trans.rlp
optimize
validatesolve "1201500" "1201500"
read temp/flugpl.mps.rlp
optimize
validatesolve "1201500" "1201500"
quit
