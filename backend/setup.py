from setuptools import setup, find_packages
import os

# Lê o README.md, LICENSE.md e requirements.txt corretamente
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, '../Readme.md'), encoding='utf-8') as f:
    readme = f.read()
with open(os.path.join(base_dir, '../LICENSE.md'), encoding='utf-8') as f:
    license = f.read()
with open(os.path.join(base_dir, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='synopz',
    version='0.1.0',
    description='Backend do Synopz: sumarização de vídeos com IA',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Gustavo MMH',
    author_email='seu-email@exemplo.com',
    url='https://github.com/gustavo-mmh/Synopz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.10',
    keywords='flask ia sumarização vídeo youtube gemini',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/gustavo-mmh/Synopz/issues',
        'Source': 'https://github.com/gustavo-mmh/Synopz',
    },
)
