from setuptools import setup

setup(
    name='ccd',
    version='0.1',
    py_modules=['ccd'],
    install_requires=[
        'Click',
        'blessed',
        'colorama',
        'cmd2',
    ],
    entry_points='''
        [console_scripts]
        ccd=ccd:hello
        ccdshell = ccd:shell
    ''',
)
