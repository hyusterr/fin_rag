set display verblevel 0
set timing enabled FALSE
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/Cardinality/atm_5_25_1.cip"
optimize
write statistics temp/atm_5_25_1.cip_r1.stats
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/Cardinality/atm_5_25_1.cip"
optimize
write statistics temp/atm_5_25_1.cip_r2.stats
quit
