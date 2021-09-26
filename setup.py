import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='notionsdk',
    version='0.0.1',
    author='Nilesh Pant',
    author_email='pant.nilesh1999@gmail.com',
    description='Python SDK for accessing Notion APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['fyle', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/fyle-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.25.0'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
