# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install skel
#
# You can edit this file again by typing:
#
#     spack edit skel
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Skel(PythonPackage):
    """Skel provides a command line tool that supports instantiation of templates with models."""

    homepage = "https://github.com/isosc/skel-core"
    git      = "https://github.com/isosc/skel-core.git"

    # A list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['isosc']

    version('develop')

    # Dependencies
    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cheetah3',        type=('build', 'run'))

