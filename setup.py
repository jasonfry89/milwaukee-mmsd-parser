from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
	name="milwaukee-mmsd-parser",
	version="0.1.1",
	description="Milwaukee MMSD Parser",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jasonfry89/milwaukee-mmsd-parser",
	author="Jason Fry",
	py_modules=["milwaukee_mmsd_parser"],
	python_requires=">=3",
	setup_requires=[
		"wheel",
	],
	install_requires=[
		"beautifulsoup4>=4.6.1",
		"aiohttp>=3.6.0",
	],
)