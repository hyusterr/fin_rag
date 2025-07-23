# Install script for directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/tmp2/yshuang/fin.rag/scip")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/soplex" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/array.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/basevectors.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/changesoplex.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/classarray.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/classset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/clufactor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/clufactor.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/clufactor_rational.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/clufactor_rational.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/cring.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/dataarray.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/datahashtable.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/datakey.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/dataset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/didxset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/dsvector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/dsvectorbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/dvector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/enter.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/exceptions.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/fmt.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/idlist.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/idxset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/islist.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/leave.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lpcol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lpcolbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lpcolset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lpcolsetbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lprow.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lprowbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lprowset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/lprowsetbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/mpsinput.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/nameset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/notimer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/random.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/rational.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/ratrecon.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/ratrecon.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/slinsolver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/slinsolver_rational.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/slufactor.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/slufactor.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/slufactor_rational.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/slufactor_rational.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/sol.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/solbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/solverational.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/solvereal.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/sorter.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxalloc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxautopr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxautopr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxbasis.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxbasis.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxboundflippingrt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxboundflippingrt.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxbounds.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxchangebasis.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdantzigpr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdantzigpr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdefaultrt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdefaultrt.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdefines.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdefines.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdesc.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdevexpr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxdevexpr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxequilisc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxequilisc.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxfastrt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxfastrt.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxfileio.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxfileio.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxgeometsc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxgeometsc.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxgithash.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxharrisrt.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxharrisrt.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxhybridpr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxhybridpr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxid.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxleastsqsc.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxleastsqsc.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxlp.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxlpbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxlpbase_rational.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxlpbase_real.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxmainsm.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxmainsm.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxout.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxpapilo.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxparmultpr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxparmultpr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxpricer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxquality.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxratiotester.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxscaler.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxscaler.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxshift.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsimplifier.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsolve.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsolver.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsolver.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxstarter.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxstarter.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsteepexpr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsteeppr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsteeppr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsumst.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxsumst.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxvecs.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxvectorst.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxvectorst.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxweightpr.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxweightpr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxweightst.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxweightst.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/spxwritestate.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/ssvector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/ssvectorbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/stablesum.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/statistics.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/statistics.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/svector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/svectorbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/svset.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/svsetbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/testsoplex.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/timer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/timerfactory.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/unitvector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/unitvectorbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/updatevector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/updatevector.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/usertimer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/validation.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/validation.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/vector.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/vectorbase.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/wallclocktimer.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex_interface.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/soplex/soplex/config.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex_interface.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/soplex/external/fmt" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/chrono.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/color.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/compile.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/core.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/format-inl.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/format.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/locale.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/os.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/ostream.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/posix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/printf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/fmt/ranges.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/soplex/external/zstr" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/zstr/zstr.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/soplex/src/soplex/external/zstr/strict_fstream.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex"
         RPATH "/tmp2/yshuang/fin.rag/scip/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/bin/soplex")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex"
         OLD_RPATH "::::::::::::::::::::::::::::::"
         NEW_RPATH "/tmp2/yshuang/fin.rag/scip/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/soplex")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libsoplex.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libsoplex-pic.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so.7.1.3.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so.7.1"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libsoplexshared.so.7.1.3.0"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libsoplexshared.so.7.1"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so.7.1.3.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so.7.1"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/lib/libsoplexshared.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libsoplexshared.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex/soplex-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex/soplex-targets.cmake"
         "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/soplex/src/CMakeFiles/Export/7b30a661feffd7bbb1d77d2bef836267/soplex-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex/soplex-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex/soplex-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/soplex/src/CMakeFiles/Export/7b30a661feffd7bbb1d77d2bef836267/soplex-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/soplex/src/CMakeFiles/Export/7b30a661feffd7bbb1d77d2bef836267/soplex-targets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/soplex" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/soplex/CMakeFiles/soplex-config.cmake"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/soplex-config-version.cmake"
    )
endif()

