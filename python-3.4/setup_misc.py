# used to build the tk interface and other extensions on 64-bit darwin
import sys
from distutils.core import setup, Extension


setup(
    ext_modules = [
        Extension(
            '_ssl', ['_ssl.c'],
            libraries = ['ssl', 'crypto'],
            depends = ['socketmodule.h'],
            include_dirs = [sys.prefix + '/include'],
            library_dirs = [sys.prefix + '/lib'],
        ),
        Extension(
            '_hashlib', ['_hashopenssl.c'],
            libraries = ['ssl', 'crypto'],
            include_dirs = [sys.prefix + '/include'],
            library_dirs = [sys.prefix + '/lib'],
        ),
    ],
)
