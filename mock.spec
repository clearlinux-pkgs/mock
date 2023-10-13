#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : mock
Version  : 4.0.1
Release  : 83
URL      : https://github.com/rpm-software-management/mock/releases/download/mock-4.0-1/mock-4.0.tar.gz
Source0  : https://github.com/rpm-software-management/mock/releases/download/mock-4.0-1/mock-4.0.tar.gz
Summary  : A simple chroot build environment manager for building RPMs
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ WTFPL
Requires: mock-bin = %{version}-%{release}
Requires: mock-data = %{version}-%{release}
Requires: mock-libexec = %{version}-%{release}
Requires: mock-license = %{version}-%{release}
Requires: mock-man = %{version}-%{release}
Requires: mock-python = %{version}-%{release}
Requires: mock-python3 = %{version}-%{release}
Requires: pypi(distro)
Requires: pypi(jinja2)
Requires: pypi(pyroute2)
Requires: pypi(templated_dictionary)
BuildRequires : pypi-mock
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-makefile-targets-for-Clear-Linux-OS.patch
Patch2: 0002-clearlinux-stateless-configuration.patch
Patch3: 0003-Do-not-reuse-mock-group.patch
Patch4: 0004-Add-entry-for-mock-in-sudoers.patch
Patch5: 0005-Allow-the-groupadd-g-command-to-fail.patch
Patch6: 0006-Set-chroot-group-to-mockbuild.patch
Patch7: 0007-Do-not-disable-unavailable-plugin.patch
Patch8: 0008-Fix-clear.cfg.patch
Patch9: 0009-Add-Clear-Linux-cert_path.patch
Patch10: 0010-Disable-bootstrap-by-default.patch
Patch11: 0011-Sort-the-installed_pkgs.log-file.patch
Patch12: 0012-Don-t-pass-cleanup-to-rpmbuild.patch

%description
Mock is used by the Fedora Build system to populate a chroot environment, which
is then used in building a source-RPM (SRPM). It can be used for long-term
management of a chroot environment, but generally a chroot is populated (using
DNF), an SRPM is built in the chroot to generate binary RPMs, and the chroot is
then discarded.

%package bin
Summary: bin components for the mock package.
Group: Binaries
Requires: mock-data = %{version}-%{release}
Requires: mock-libexec = %{version}-%{release}
Requires: mock-license = %{version}-%{release}

%description bin
bin components for the mock package.


%package data
Summary: data components for the mock package.
Group: Data

%description data
data components for the mock package.


%package libexec
Summary: libexec components for the mock package.
Group: Default
Requires: mock-license = %{version}-%{release}

%description libexec
libexec components for the mock package.


%package license
Summary: license components for the mock package.
Group: Default

%description license
license components for the mock package.


%package man
Summary: man components for the mock package.
Group: Default

%description man
man components for the mock package.


%package python
Summary: python components for the mock package.
Group: Default
Requires: mock-python3 = %{version}-%{release}

%description python
python components for the mock package.


%package python3
Summary: python3 components for the mock package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mock package.


%prep
%setup -q -n mock-4.0
cd %{_builddir}/mock-4.0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697217471
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697217471
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mock
cp %{_builddir}/mock-4.0/COPYING %{buildroot}/usr/share/package-licenses/mock/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
%make_install
## install_append content
install -d %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -m 440 mock.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/mock

ln -sf clear.cfg %{buildroot}/usr/share/defaults/mock/default.cfg
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mock
/usr/bin/mock-parse-buildlog
/usr/bin/mockchain

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mock
/usr/share/defaults/mock/clear.cfg
/usr/share/defaults/mock/default.cfg
/usr/share/defaults/mock/logging.ini
/usr/share/defaults/mock/site-defaults.cfg
/usr/share/defaults/sudo/sudoers.d/mock
/usr/share/pam.d/mock

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mock/create_default_route_in_container.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mock/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mock-parse-buildlog.1
/usr/share/man/man1/mock.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
