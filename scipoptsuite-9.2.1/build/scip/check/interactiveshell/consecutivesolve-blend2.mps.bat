set display verblevel 0
set timing enabled FALSE
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/blend2.mps"
optimize
write statistics temp/blend2.mps_r1.stats
read "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip"/check/"instances/MIP/blend2.mps"
optimize
write statistics temp/blend2.mps_r2.stats
quit
