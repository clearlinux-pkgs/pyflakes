#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0294A902A6830C07 (indigo@keybase.io)
#
Name     : pyflakes
Version  : 1.5.0
Release  : 30
URL      : http://pypi.debian.net/pyflakes/pyflakes-1.5.0.tar.gz
Source0  : http://pypi.debian.net/pyflakes/pyflakes-1.5.0.tar.gz
Source99 : http://pypi.debian.net/pyflakes/pyflakes-1.5.0.tar.gz.asc
Summary  : passive checker of Python programs
Group    : Development/Tools
License  : MIT
Requires: pyflakes-bin
Requires: pyflakes-legacypython
Requires: pyflakes-python3
Requires: pyflakes-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pyflakes
        ========
        
        A simple program which checks Python source files for errors.
        
        Pyflakes analyzes programs and detects various errors.  It works by
        parsing the source file, not importing it, so it is safe to use on
        modules with side effects.  It's also much faster.

%package bin
Summary: bin components for the pyflakes package.
Group: Binaries

%description bin
bin components for the pyflakes package.


%package legacypython
Summary: legacypython components for the pyflakes package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyflakes package.


%package python
Summary: python components for the pyflakes package.
Group: Default
Requires: pyflakes-legacypython
Requires: pyflakes-python3

%description python
python components for the pyflakes package.


%package python3
Summary: python3 components for the pyflakes package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyflakes package.


%prep
%setup -q -n pyflakes-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169167
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507169167
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyflakes

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
