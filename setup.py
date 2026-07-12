import os
from subprocess import run
from subprocess import CalledProcessError

from setuptools import setup
from setuptools.command.build import build

import shutil


class MakeBuild(build):
    def finalize_options(self):
        super().finalize_options()
        # ensure attribute exists
        self.build_lib = getattr(self, "build_lib", os.path.abspath(os.path.join(self.build_base, "lib")))

    def run(self):
        try:
            result = run(["make", "all"], capture_output=True, text=True,check=True,)
        except CalledProcessError as call_error:
            print(call_error)
            print(call_error.stdout)
            print(call_error.stderr)

        print(result.stdout)
        print(result.stderr)
        # Copy compiled artifact into package
        shutil.copy(
            "build/yinit-bin",
            "yinit-bin",
        )

        #subprocess.check_call(["pwd"], cwd="..")
        super().run()
        #subprocess.check_call(["make"], #cwd=self.distribution.get_command_obj("build").build_base)


setup(
    cmdclass={
        "build": MakeBuild,
    },
)
