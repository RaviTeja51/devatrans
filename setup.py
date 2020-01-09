""" Setup  for devatrans """

import setuptools

with open('README.md',"r") as f:
    README = f.read()

setuptools.setup(
    author="Ravi Teja",
    author_email="ravitejatasubilli@gmail.com",
    name='devatrans',
    license="Apache",
    description="""devatrans is an easy-to-use tool for transliteration,
                 back transliteration, inter transliteration of SANSKRIT.
                 """,
    version='v0.1',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/RaviTeja51/devatrans.git',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
