set display verblevel 0
set timing enabled FALSE
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/SOS/sparse2.lp"
optimize
write statistics temp/sparse2.lp_r1.stats
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/SOS/sparse2.lp"
optimize
write statistics temp/sparse2.lp_r2.stats
quit
