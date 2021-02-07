from distutils.core import setup

setup(
    name='os_image_handler',
    packages=['os_image_handler'],
    version='1.02',
    license='MIT',
    description='This script contains fundamental image manipulation actions.',
    author='Oz Shabat',
    author_email='admin@os-apps.com',
    url='https://github.com/osfunapps/os-image-handler-py',
    keywords=['python', 'osfunapps', 'osapps', 'image', 'image manipulation'],
    install_requires=['Pillow', 'os-tools'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
)
