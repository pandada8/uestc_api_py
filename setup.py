from setuptools import setup, find_packages

setup(
	name="uestc",
	version="0.0.1.dev1",
	url="https://github.com/pandada8/uestc_api_py",
	author="pandada8",
	author_email="pandada8@gmail.com",
	license="MIT",
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3'
	],
	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
	install_requires=['requests', 'pyquery']
)