#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018-2019 Mailgun Technologies Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

try:
    try:  # for pip >= 10
        from pip._internal.req import parse_requirements
    except ImportError:  # for pip <= 9.0.3
        from pip.req import parse_requirements
    support_pip_parse_requirements = True
except ModuleNotFoundError:
    support_pip_parse_requirements = False

from setuptools import setup, find_packages
import platform


def get_requirements():
    if platform.python_version_tuple()[0] == "2":
        requirements_txt = "requirements-py2.txt"
    else:
        requirements_txt = "requirements-py3.txt"

    if support_pip_parse_requirements:
        reqs = parse_requirements(requirements_txt, session="")

        # Generator must be converted to list, or we will only have one chance to read each element, meaning that the first requirement will be skipped.
        reqs = list(reqs)
        try:
            return [str(r.req) for r in reqs]
        except:
            return [str(r.requirement) for r in reqs]
    else:
        # python3 -m pip install --disable-pip-version-check --upgrade --no-deps . --use-pep517
        # https://stackoverflow.com/questions/49689880/proper-way-to-parse-requirements-file-after-pip-upgrade-to-pip-10-x-x
        import pkg_resources

        reqs = []
        with open(requirements_txt) as f:
            for req in pkg_resources.parse_requirements(f.read()):
                reqs.append(str(req))
        return reqs


setup(
    name="gubernator",
    version="v1.0.0-rc.8",
    description="Python client for gubernator",
    author="Derrick J. Wippler",
    author_email="thrawn01@gmail.com",
    url="https://github.com/mailgun/gubernator",
    package_dir={"": "."},
    packages=find_packages(".", exclude=["tests"]),
    install_requires=get_requirements(),
    license="Apache Software License 2.0",
    python_requires=">=2.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
