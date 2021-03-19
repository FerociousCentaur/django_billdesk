import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Vivek Anand",
    author_email="vivek17212797@gmail.com",
    name='django_billdesk',
    license="MIT",
    description='A tool to integrate BillDesk in Django Site',
    version='v0.0.1',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/FerociousCentaur/py-billdesk',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[],
    keywords='billdesk python-billdesk py-billdesk django-billdesk',
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)