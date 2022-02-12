from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='indicparser',
  version='0.0.1',
  description='Grapheme Parser for indic language',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/mnansary/indicparser',  
  author='Bengali.ai',
  author_email='research.bengaliai@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['grapheme','indic languages'], 
  packages=find_packages(),
  install_requires=[''] 
)