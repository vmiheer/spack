# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bear(CMakePackage):
    """Bear is a tool that generates a compilation database for clang tooling
    from non-cmake build systems."""
    
    maintainers = ['vmiheer']
    homepage = "https://github.com/rizsotto/Bear"
    url      = "https://github.com/rizsotto/Bear/archive/2.0.4.tar.gz"

    version('3.0.19', sha256='2fcfe2c6e029182cfc54ed26b3505c0ef12b0f43df03fb587f335afdc2ca9431')
    version('2.2.0', sha256='6bd61a6d64a24a61eab17e7f2950e688820c72635e1cf7ea8ea7bf9482f3b612')
    version('2.0.4', sha256='33ea117b09068aa2cd59c0f0f7535ad82c5ee473133779f1cc20f6f99793a63e')

    depends_on('python')
    depends_on('cmake@2.8:', type='build')
