set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/p0548.mps"
write problem temp/p0548.mps.opb
presolve
write transproblem temp/p0548.mps_trans.opb
set heur emph def
read temp/p0548.mps_trans.opb
optimize
validatesolve "8691" "8691"
read temp/p0548.mps.opb
optimize
validatesolve "8691" "8691"
quit
