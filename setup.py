from setuptools import setup, find_packages

setup(
	name='neomath',
	version='1.1.0',
	description='Librería personal para la materia de Métodos Numéricos',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='Neotingale',
	author_email='alu.23130570@correo.itlalaguna.edu.mx',
	url='https://github.com/Neotingale/neomath',
	packages=find_packages(),
	install_requires=[
		'prettytable>=3.14.0',
	],
	python_requires='>=3.8',
	license='CC BY 4.0',
	classifiers=[
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
	],
	include_package_data=True
)
