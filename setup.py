from setuptools import setup, find_packages

setup(
    name = 'print_h5',
    version = '1.0.0',
    url = 'https://github.com/tammojan/print_h5',
    author = 'Tammo Jan Dijkema',
    author_email = 'dijkema@astron.nl',
    description = 'Print contents of HDF5 file',
    packages = find_packages(),
    install_requires = ['numpy', 'h5py'],
)