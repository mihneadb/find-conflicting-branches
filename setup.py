from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.readlines()
reqs = [r.strip() for r in reqs if r.strip()]

setup(name='find-conflicting-branches',
      version='1.0.1',
      description="An easy way to find those annoying conflicting branches",
      url='https://github.com/mihneadb/find-conflicting-branches',
      author='Mihnea Dobrescu-Balaur',
      author_email='mihnea@linux.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=reqs,
      scripts=[
          'bin/find_conflicting_branches',
      ],
)
