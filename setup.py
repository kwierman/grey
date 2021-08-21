from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='grey',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Automically inserts docstrings in functions, classes and modules.",
    license="MIT",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/grey',
    packages=['grey'],
    entry_points={
        'console_scripts': [
            'grey=grey.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='grey',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
