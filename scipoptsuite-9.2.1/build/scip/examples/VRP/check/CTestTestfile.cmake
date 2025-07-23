# CMake generated Testfile for 
# Source directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check
# Build directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/examples/VRP/check
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(examples-vrp-build "/usr/local/lib/python3.10/dist-packages/cmake/data/bin/cmake" "--build" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build" "--config" "Release" "--target" "vrp")
set_tests_properties(examples-vrp-build PROPERTIES  RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/CMakeLists.txt;18;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/CMakeLists.txt;0;")
add_test(examples-vrp-eil13 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/vrp" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/../data/eil13.vrp")
set_tests_properties(examples-vrp-eil13 PROPERTIES  DEPENDS "examples-vrp-build" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/CMakeLists.txt;38;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/CMakeLists.txt;0;")
add_test(examples-vrp-eil7 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/vrp" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/../data/eil7.vrp")
set_tests_properties(examples-vrp-eil7 PROPERTIES  DEPENDS "examples-vrp-build" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/CMakeLists.txt;38;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/VRP/check/CMakeLists.txt;0;")
