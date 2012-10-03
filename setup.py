from setuptools import setup, find_packages

setup(
    name="bdpcrypt",
    version="0.1",
    packages=find_packages(),
    author="Jorge Niedbalski R.",
    author_email="jnr@pyrosome.org",
    description="Encrypt and decrypt Sony(TM) Blueray players images",
    keywords="bdpcrypt blueray sony decrypt encrypt encrypt bluray",
    include_package_data=False,
    license="BSD",
    classifiers=['Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Operating System :: Unix '],
    entry_points="""
    [console_scripts]
    bdpcrypt = bdpcrypt.cli:main
    """
)
