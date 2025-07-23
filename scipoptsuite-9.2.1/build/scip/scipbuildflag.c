/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                                           */
/*                  This file is part of the program and library             */
/*         SCIP --- Solving Constraint Integer Programs                      */
/*                                                                           */
/*  Copyright (c) 2002-2025 Zuse Institute Berlin (ZIB)                      */
/*                                                                           */
/*  Licensed under the Apache License, Version 2.0 (the "License");          */
/*  you may not use this file except in compliance with the License.         */
/*  You may obtain a copy of the License at                                  */
/*                                                                           */
/*      http://www.apache.org/licenses/LICENSE-2.0                           */
/*                                                                           */
/*  Unless required by applicable law or agreed to in writing, software      */
/*  distributed under the License is distributed on an "AS IS" BASIS,        */
/*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. */
/*  See the License for the specific language governing permissions and      */
/*  limitations under the License.                                           */
/*                                                                           */
/*  You should have received a copy of the Apache-2.0 license                */
/*  along with SCIP; see the file LICENSE. If not visit scipopt.org.         */
/*                                                                           */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

/**@file   scipbuildflags.c
 * @brief  build flags methods
 * @author Felipe Serrano
 */

/*---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8----+----9----+----0----+----1----+----2*/

#include "scip/scipbuildflags.h"

/** returns the flags that were used to build SCIP */
const char* SCIPgetBuildFlags(
   void
   )
{
   return " ARCH=x86_64\n\
 OSTYPE=Linux-5.15.0-134-generic\n\
 COMP=GNU 11.4.0\n\
 BUILD=Release\n\
 DEBUGSOL=OFF\n\
 EXPRINT=cppad\n\
 SYM=snauty\n\
 GMP=ON\n\
 IPOPT=ON\n\
 WORHP=OFF\n\
 LPS=spx\n\
 LPSCHECK=OFF\n\
 NOBLKBUFMEM=OFF\n\
 NOBLKMEM=OFF\n\
 NOBUFMEM=OFF\n\
 THREADSAFE=ON\n\
 READLINE=ON\n\
 SANITIZE_ADDRESS=OFF\n\
 SANITIZE_MEMORY=OFF\n\
 SANITIZE_UNDEFINED=ON\n\
 SANITIZE_THREAD=OFF\n\
 SHARED=ON\n\
 VERSION=9.2.1.0\n\
 API_VERSION=115\n\
 ZIMPL=OFF\n\
 ZLIB=ON";
}
