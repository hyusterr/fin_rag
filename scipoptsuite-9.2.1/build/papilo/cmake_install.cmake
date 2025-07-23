# Install script for directory: /tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/papilo/CMakeConfig.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/Config.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo-config-version.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/core" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Components.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/ConstraintMatrix.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/MatrixBuffer.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Objective.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Presolve.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/PresolveMethod.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/PresolveOptions.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/ProbingView.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Problem.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/ProblemBuilder.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/ProblemFlag.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/ProblemUpdate.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Reductions.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/RowFlags.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/SingleRow.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Solution.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/SparseStorage.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/Statistics.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/SymmetryStorage.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/VariableDomains.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/core/postsolve" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/BoundStorage.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/PostsolveStorage.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/Postsolve.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/PostsolveStatus.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/PostsolveType.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/ReductionType.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/core/postsolve/SavedRow.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/interfaces" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/HighsInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/GlopInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/GurobiInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/ScipInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/SolverInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/SoplexInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/interfaces/RoundingsatInterface.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/io" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/BoundType.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/Message.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/MpsParser.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/MpsWriter.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/OpbParser.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/OpbWriter.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/ParseKey.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/Parser.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/SolParser.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/io/SolWriter.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/misc" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Alloc.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Array.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/compress_vector.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/DependentRows.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Flags.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/fmt.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Hash.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/MultiPrecision.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Num.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/NumericalStatistics.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/PrimalDualSolValidation.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/OptionsParser.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/VersionLogger.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/ParameterSet.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Signature.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/StableSum.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/String.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/tbb.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Timer.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Validation.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Vec.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/VectorUtils.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/Wrappers.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/verification" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/verification/ArgumentType.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/verification/CertificateInterface.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/verification/EmptyCertificate.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/verification/VeriPb.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/misc" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/misc/extended_euclidean.hpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/presolvers" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/CoefficientStrengthening.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/ConstraintPropagation.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/DominatedCols.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/DualFix.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/DualInfer.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/FixContinuous.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/FreeVarSubstitution.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/ImplIntDetection.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/ParallelColDetection.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/ParallelRowDetection.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/Probing.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/SimpleProbing.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/SimpleSubstitution.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/SimplifyInequalities.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/SingletonCols.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/SingletonStuffing.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/presolvers/Sparsify.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/external/fmt" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/chrono.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/color.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/compile.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/core.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/format-inl.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/format.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/locale.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/os.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/ostream.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/posix.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/printf.h"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/fmt/ranges.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/external/pdqsort" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/pdqsort/pdqsort.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/external/ska" TYPE FILE FILES
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/ska/bytell_hash_map.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/ska/flat_hash_map.hpp"
    "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/ska/unordered_map.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/papilo/external/lusol" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/src/papilo/external/lusol/clusol.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/cmake/Modules/FindQuadmath.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/CMakeFiles/papilo-config.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/papilo/cmake/Modules/FindTBB.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/libpapilo-core.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/libclusol.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo/papilo-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo/papilo-targets.cmake"
         "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/CMakeFiles/Export/c41162f1621fa7d28748f8ed52f66d7f/papilo-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo/papilo-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo/papilo-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/CMakeFiles/Export/c41162f1621fa7d28748f8ed52f66d7f/papilo-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/papilo" TYPE FILE FILES "/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/CMakeFiles/Export/c41162f1621fa7d28748f8ed52f66d7f/papilo-targets-release.cmake")
  endif()
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/tmp2/yshuang/fin.rag/scipoptsuite-9.2.1/build/papilo/test/cmake_install.cmake")

endif()

