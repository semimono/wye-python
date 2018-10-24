import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='wye_compile_python',
      version='0.0.1',
      description='A wye copmiler implemented in python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/semimono/wye-python',
      author='SemiMono',
      author_email='',
      license='MIT',
      packages=['wye_compile_python'],
      zip_safe=False)
