# https://docs.python.org/3/distutils/setupscript.html#additional-meta-data

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

name = "pyvfx-boilerplate"
url = "https://github.com/fredrikaverpil/pyvfx-boilerplate"
description = "A boilerplate Qt Py* app that runs in dcc apps, py2, or py3."
package_dir = "src"
cli_modules = [
    "pyvfx-boilerplate=pyvfx_boilerplate.cli:main",
]

setuptools.setup(
    setup_requires=["setuptools_scm"],
    use_scm_version={"local_scheme": "node-and-timestamp"},
    name=name,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=setuptools.find_packages(package_dir),
    package_dir={"": package_dir},
    entry_points={"console_scripts": cli_modules},
    include_package_data=True,
    install_requires=["Qt.py"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
