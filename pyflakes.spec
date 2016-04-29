#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyflakes
Version  : 0.8.1
Release  : 12
URL      : https://pypi.python.org/packages/source/p/pyflakes/pyflakes-0.8.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyflakes/pyflakes-0.8.1.tar.gz
Summary  : passive checker of Python programs
Group    : Development/Tools
License  : MIT
Requires: pyflakes-bin
Requires: pyflakes-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========
Pyflakes
========
A simple program which checks Python source files for errors.

%package bin
Summary: bin components for the pyflakes package.
Group: Binaries

%description bin
bin components for the pyflakes package.


%package python
Summary: python components for the pyflakes package.
Group: Default

%description python
python components for the pyflakes package.


%prep
%setup -q -n pyflakes-0.8.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyflakes

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
