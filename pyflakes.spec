#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyflakes
Version  : 2.4.0
Release  : 83
URL      : https://files.pythonhosted.org/packages/15/60/c577e54518086e98470e9088278247f4af1d39cb43bcbd731e2c307acd6a/pyflakes-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/60/c577e54518086e98470e9088278247f4af1d39cb43bcbd731e2c307acd6a/pyflakes-2.4.0.tar.gz
Summary  : passive checker of Python programs
Group    : Development/Tools
License  : MIT
Requires: pyflakes-bin = %{version}-%{release}
Requires: pyflakes-license = %{version}-%{release}
Requires: pyflakes-python = %{version}-%{release}
Requires: pyflakes-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
========
Pyflakes
========
A simple program which checks Python source files for errors.

%package bin
Summary: bin components for the pyflakes package.
Group: Binaries
Requires: pyflakes-license = %{version}-%{release}

%description bin
bin components for the pyflakes package.


%package license
Summary: license components for the pyflakes package.
Group: Default

%description license
license components for the pyflakes package.


%package python
Summary: python components for the pyflakes package.
Group: Default
Requires: pyflakes-python3 = %{version}-%{release}

%description python
python components for the pyflakes package.


%package python3
Summary: python3 components for the pyflakes package.
Group: Default
Requires: python3-core
Provides: pypi(pyflakes)

%description python3
python3 components for the pyflakes package.


%prep
%setup -q -n pyflakes-2.4.0
cd %{_builddir}/pyflakes-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633623078
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyflakes
cp %{_builddir}/pyflakes-2.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pyflakes/200da923b63ba8767fe085a65a35f9c01b5eb867
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyflakes

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyflakes/200da923b63ba8767fe085a65a35f9c01b5eb867

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
