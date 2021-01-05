#!/usr/bin/env python

from setuptools import setup, find_packages
import sys
import os.path


PY36 = (sys.version_info[0] == 3 and (sys.version_info[1] >= 6))

# example taken from here: https://github.com/spyder-ide/spyder/blob/master/setup.py
v = sys.version_info
if v[:2] < (3,6):
    error = "ERROR: LabTests application requires Python version 3.6 or above."
    print(error, file=sys.stderr)
    sys.exit(1)
    
   
def get_data_files():
    """Return data_files in a platform dependent manner"""
    if sys.platform.startswith('linux'):
        if PY36:
            data_files = [('/usr/share/labtests/src/ui', ['src/ui/answer_ui.py']),
                  ('/usr/share/labtests/src/ui', ['src/ui/mainwindow_ui.py']),
                  ('/usr/share/labtests/src/ui', ['src/ui/mainwindow.ui']),
                  ('/usr/share/labtests/src/ui', ['src/ui/answer.ui']),
                  ('/usr/share/labtests/src', ['src/answer.py']),
                  ('/usr/share/labtests/src', ['src/MainWindow.py']),
                  ('/usr/share/labtests/src', ['src/Calculator.py']),
                  ('/usr/share/applications', ['LabTests.desktop']),
                  ('/usr/share/labtests', ['Copyright.txt']),
                  ('/usr/bin', ['labtests']),]
    else:
        data_files = []
    return data_files



if not os.path.exists("/usr/share/labtests/src/ui"):
    os.makedirs("/usr/share/labtests/src/ui")
    

setup(name='LabTests',
      version='1.0',
      description='Application for checking of laboratory results in daily speech',
      long_description=open('README.md').read(),
      author='Jagoda \"juliagoda\" Górska',
      author_email='juliagoda.pl@protonmail.com',
      maintainer='Jagoda \"juliagoda\" Górska',
      maintainer_email='juliagoda.pl@protonmail.com',
      url='https://github.com/juliagoda',
      packages=find_packages(exclude=['src', 'src/ui']),
      package_data={'': ['LabTests.desktop', 'Copyright.txt']},
      data_files=get_data_files(),
      install_requires=['setuptools', 'pyqt5'],
      keywords='blood liver labtest laboratory medical health pyqt5',
      project_urls={
          'Source': 'https://github.com/juliagoda/LabTests',
          'Tracker': 'https://github.com/juliagoda/LabTests/issues',
     },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: X11 Applications :: Qt',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Healthcare Industry',
          'Intended Audience :: Education',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering :: Medical Science Apps.',
          'Topic :: Education',
          ],
     ) 

