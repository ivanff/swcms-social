import setuptools

from swcms_social import __author__, __version__, __license__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swcms-social",
    version=__version__,
    author=__author__,
    author_email="agestart@gmail.com",
    description="Collect of Django apps, shared part of likeis and posticas",
    license=__license__,
    long_description=long_description,
    url="https://github.com/ivanff/swcms-social",
    packages=setuptools.find_packages(),
    install_requires=(
            'django>=2.0',
            'django-ckeditor>=5.4.0',
            'djangorestframework>=3.7.7',
            'django-tz-detect',
            'django-ipware',
            'django-decorator-include',
            'pytz',
            'Babel',
    ),
    classifiers=(
        'Development Status :: 4 - Alpha',
        'Environment :: Web Environment',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 3.0',
    ),
    include_package_data = True,
)
