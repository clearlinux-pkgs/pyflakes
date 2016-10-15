#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyflakes
Version  : 1.3.0
Release  : 16
URL      : http://pypi.debian.net/pyflakes/pyflakes-1.3.0.tar.gz
Source0  : http://pypi.debian.net/pyflakes/pyflakes-1.3.0.tar.gz
Summary  : passive checker of Python programs
Group    : Development/Tools
License  : MIT
Requires: pyflakes-bin
Requires: pyflakes-python
BuildRequires : pbr
BuildRequires : pip
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
%setup -q -n pyflakes-1.3.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyflakes

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
