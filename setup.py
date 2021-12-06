from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    version='1.3.5',
    name='FuelSDKWrapper',
    description='Simplify and enhance the FuelSDK for Salesforce Marketing Cloud (ExactTarget)',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Seb Angel',
    author_email='seb.angel.force@gmail.com',
    py_modules=['FuelSDKWrapper'],
    packages=[],
    url='https://github.com/seb-angel/FuelSDK-Python-Wrapper',
    license='MIT',
    install_requires=[
        'Salesforce-FuelSDK>=1.3.1',
        'PyJWT>=0.1.9',
        'requests>=2.18.4',
        'suds-community>=0.7'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
