set heur emph off
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/PseudoBoolean/normalized-mds_10_4_3.opb"
write problem temp/normalized-mds_10_4_3.opb.cip
presolve
write transproblem temp/normalized-mds_10_4_3.opb_trans.cip
set heur emph def
read temp/normalized-mds_10_4_3.opb_trans.cip
optimize
validatesolve "2" "2"
read temp/normalized-mds_10_4_3.opb.cip
optimize
validatesolve "2" "2"
quit
