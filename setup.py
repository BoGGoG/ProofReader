from setuptools import setup, find_packages

setup(
    name="ProofReader",
    version="0.0.1",
    description="A proofreader of English texts",
    author="Marco Knipfer",
    author_email="marco.knipfer@me.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': ["proofread = proofreader.proofread:main"],
    },
)

