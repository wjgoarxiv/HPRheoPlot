from setuptools import setup

setup(
	  name='HPRheoPlot',
	  version='1.0.3',  
	  description='::A tool to automatically plot rheological data obtained from TA Instruments rheometers::',
	  long_description= '',
	  author='wjgoarxiv',
	  author_email='woo_go@yahoo.com',
	  url='https://pypi.org/project/hprheoplot/',
	  license='MIT',
	  py_modules=['HPRheoPlot'],
	  python_requires='>=3.6', #python version required
	  install_requires = [
    'pandas',
	  'matplotlib',
	  'numpy',
    'scipy', 
	  'scikit-learn',
	  'scipy',
	  'pandas',
	  'seaborn',
    'pyfiglet',
    'tabulate',
    'xlrd',
    'openpyxl',
	  ],
	  packages=['HPRheoPlot'],
		entry_points={
			'console_scripts': [
				'hprheoplot = HPRheoPlot.__main__:main'
			]
		}
	)