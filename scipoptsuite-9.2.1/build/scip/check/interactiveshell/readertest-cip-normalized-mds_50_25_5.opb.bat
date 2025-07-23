set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/PseudoBoolean/normalized-mds_50_25_5.opb"
write problem temp/normalized-mds_50_25_5.opb.cip
presolve
write transproblem temp/normalized-mds_50_25_5.opb_trans.cip
set heur emph def
read temp/normalized-mds_50_25_5.opb_trans.cip
optimize
validatesolve "3" "3"
read temp/normalized-mds_50_25_5.opb.cip
optimize
validatesolve "3" "3"
quit
