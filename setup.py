from setuptools import setup, find_packages

setup(
    name='niuhe',
    version='0.1',
    url='https://github.com/lennon-guan/niuhe',
    description='A simple webapi framework',
    author='guan ming',
    license='MIT',
    install_requires=['Flask>=0.10', 'SQLAlchemy>=0.8'],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
)
