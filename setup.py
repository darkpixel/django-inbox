from setuptools import find_packages, setup

from inbox import __version__ as version_string


gmail_oauth2_require = [
    'python-social-auth',
]

setup(
    name='django-mailbox-fork',
    version=version_string,
    url='http://github.com/darkpixel/django-inbox/',
    description='Import mail from POP3, IMAP, local mailboxes or directly into Django',
    long_description='Import mail from POP3, IMAP, local mailboxes or directly into Django',
    license='MIT',
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    extras_require={
        'gmail-oauth2': gmail_oauth2_require
    },
    python_requires=">=3",
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Post-Office',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',
        'Topic :: Communications :: Email :: Post-Office :: POP3',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six>=1.6.1'
    ]
)
