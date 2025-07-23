# CMake generated Testfile for 
# Source directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check
# Build directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/scip/examples/Binpacking/check
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(examples-binpacking-build "/usr/local/lib/python3.10/dist-packages/cmake/data/bin/cmake" "--build" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build" "--config" "Release" "--target" "binpacking")
set_tests_properties(examples-binpacking-build PROPERTIES  RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;16;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;0;")
add_test(examples-binpacking-u20_00 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/binpacking" "-f" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/../data/u20_00.bpa" "-o" "9" "9")
set_tests_properties(examples-binpacking-u20_00 PROPERTIES  DEPENDS "examples-binpacking-build" PASS_REGULAR_EXPRESSION "Validation         : Success" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;37;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;0;")
add_test(examples-binpacking-u40_00 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/binpacking" "-f" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/../data/u40_00.bpa" "-o" "17" "17")
set_tests_properties(examples-binpacking-u40_00 PROPERTIES  DEPENDS "examples-binpacking-build" PASS_REGULAR_EXPRESSION "Validation         : Success" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;37;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;0;")
add_test(examples-binpacking-u60_00 "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/examples/binpacking" "-f" "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/../data/u60_00.bpa" "-o" "27" "27")
set_tests_properties(examples-binpacking-u60_00 PROPERTIES  DEPENDS "examples-binpacking-build" PASS_REGULAR_EXPRESSION "Validation         : Success" RESOURCE_LOCK "libscip" _BACKTRACE_TRIPLES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;37;add_test;/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/scip/examples/Binpacking/check/CMakeLists.txt;0;")
