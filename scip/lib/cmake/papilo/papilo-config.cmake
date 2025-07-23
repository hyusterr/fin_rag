if(NOT TARGET papilo)
  include(${CMAKE_CURRENT_LIST_DIR}/papilo-targets.cmake)
endif()
set(PAPILO_IMPORTED_TARGETS papilo)
set(PAPILO_FOUND 1)

# For `find_dependency` function.
include(CMakeFindDependencyMacro)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR})

# If PAPILO was built with Quadmath then we also need it.
set(PAPILO_HAVE_FLOAT128 1)
if(PAPILO_HAVE_FLOAT128)
   if(NOT Quadmath_FOUND)
      find_dependency(Quadmath)
   endif()
endif()

# If PAPILO was built with GMP then we also need it.
set(PAPILO_HAVE_GMP 0)
if(PAPILO_HAVE_GMP AND PAPILO_FOUND)
   if(NOT GMP_FOUND)
      if(NOT GMP_DIR)
         set(GMP_DIR )
      endif()
      find_dependency(GMP)
   endif()
endif()

# If PAPILO was built with TBB then we also need it.
set(PAPILO_TBB on)
if(PAPILO_TBB AND PAPILO_FOUND)
   if(NOT TBB_FOUND)
      if(NOT TBB_DIR)
         set(TBB_DIR /usr/lib/x86_64-linux-gnu/cmake/TBB)
      endif()
      find_dependency(TBB 2018 COMPONENTS tbb tbbmalloc HINTS ${CMAKE_CURRENT_LIST_DIR}/_deps/local/ ${CMAKE_CURRENT_LIST_DIR}/_deps/local/lib)
   endif()
endif()

# If PAPILO uses the standard hashmap then we also do.
set(PAPILO_USE_STANDARD_HASHMAP 1)

# If PAPILO was built with iostreams / program_options / serialization then we also need it.
set(PAPILO_HAVE_BOOST_IOSTREAMS 0)
set(PAPILO_USE_BOOST_IOSTREAMS_WITH_ZLIB )
set(PAPILO_USE_BOOST_IOSTREAMS_WITH_BZIP2 )
set(PAPILO_COMMAND_LINE_AVAILABLE 0)
set(PAPILO_SERIALIZATION_AVAILABLE )
set(BOOST_COMPONENTS)
if(PAPILO_HAVE_BOOST_IOSTREAMS)
   set(BOOST_COMPONENTS ${BOOST_COMPONENTS} iostreams)
endif()
if(PAPILO_COMMAND_LINE_AVAILABLE)
   set(BOOST_COMPONENTS ${BOOST_COMPONENTS} program_options)
endif()
if(PAPILO_SERIALIZATION_AVAILABLE)
   set(BOOST_COMPONENTS ${BOOST_COMPONENTS} serialization)
endif()
if(BOOST_COMPONENTS AND PAPILO_FOUND)
   if((NOT Boost_PROGRAM_OPTIONS_FOUND AND PAPILO_COMMAND_LINE_AVAILABLE) OR (NOT Boost_SERIALIZATION_FOUND AND PAPILO_SERIALIZATION_AVAILABLE) OR (NOT Boost_IOSTREAMS_FOUND AND PAPILO_HAVE_BOOST_IOSTREAMS))
      if(NOT BOOST_ROOT)
         set(BOOST_ROOT )
      endif()
      find_dependency(Boost 1.65 COMPONENTS ${BOOST_COMPONENTS})
   endif()
endif()

# We also need Threads.
if(PAPILO_FOUND)
   if(NOT Threads_FOUND)
      find_dependency(Threads)
   endif()
endif()

if(1 AND PAPILO_FOUND)
   enable_language(Fortran)
endif()

if(PAPILO_FOUND)
  find_package_message(PAPILO "Found PAPILO: ${CMAKE_CURRENT_LIST_FILE} (found suitable version \"2.4.1.0\")"
    "[${PAPILO_FOUND}][${TBB_FOUND}]")
endif()

