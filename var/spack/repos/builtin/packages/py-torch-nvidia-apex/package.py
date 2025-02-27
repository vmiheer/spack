# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyTorchNvidiaApex(PythonPackage, CudaPackage):
    """A PyTorch Extension: Tools for easy mixed precision and
    distributed training in Pytorch"""

    homepage = "https://github.com/nvidia/apex/"
    git = "https://github.com/nvidia/apex/"

    license("BSD-3-Clause")

    version("master", branch="master")
    version("2020-10-19", commit="8a1ed9e8d35dfad26fb973996319965e4224dcdd")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-packaging", type="build")
    depends_on("py-torch@0.4:", type=("build", "run"))
    depends_on("cuda@9:", when="+cuda")
    depends_on("py-pybind11", type=("build", "link", "run"))

    variant("cuda", default=True, description="Build with CUDA")

    # https://github.com/NVIDIA/apex/issues/1498
    # https://github.com/NVIDIA/apex/pull/1499
    patch("1499.patch", when="@2020-10-19")

    def setup_build_environment(self, env):
        if "+cuda" in self.spec:
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
        else:
            env.unset("CUDA_HOME")

    @when("^python@:3.10")
    def global_options(self, spec, prefix):
        args = []
        if spec.satisfies("^py-torch@1.0:"):
            args.append("--cpp_ext")
            if "+cuda" in spec:
                args.append("--cuda_ext")
        return args

    @when("^python@3.11:")
    def config_settings(self, spec, prefix):
        return {
            "builddir": "build",
            "compile-args": f"-j{make_jobs}",
            "--global-option": "--cpp_ext --cuda_ext",
        }
