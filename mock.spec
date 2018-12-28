#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mock
Version  : 1.2.14
Release  : 39
URL      : https://github.com/rpm-software-management/mock/archive/mock-1.2.14.tar.gz
Source0  : https://github.com/rpm-software-management/mock/archive/mock-1.2.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mock-bin = %{version}-%{release}
Requires: mock-data = %{version}-%{release}
Requires: mock-license = %{version}-%{release}
Requires: mock-man = %{version}-%{release}
Requires: mock-python = %{version}-%{release}
Requires: mock-python3 = %{version}-%{release}
Requires: six
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : python3
Patch1: 0001-clearlinux-stateless-configuration.patch
Patch2: 0002-Do-not-reuse-mock-group-as-it-might-be-defined-in-th.patch
Patch3: 0003-Add-entry-for-mock-in-sudoers.patch
Patch4: 0004-ccache-use-different-bind-mount-directory.patch
Patch5: 0005-Allow-the-groupadd-g-command-to-fail.patch
Patch6: 0006-Disable-the-colourful-PROMPT_COMMAND-for-chroot.patch
Patch7: 0007-Fix-systemd-nspawn-use.patch

%description
These 3 src.rpms are setup to build on almost any rpm-based system.
They have a simple chain of buildrequires:

%package bin
Summary: bin components for the mock package.
Group: Binaries
Requires: mock-data = %{version}-%{release}
Requires: mock-license = %{version}-%{release}
Requires: mock-man = %{version}-%{release}

%description bin
bin components for the mock package.


%package data
Summary: data components for the mock package.
Group: Data

%description data
data components for the mock package.


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
%setup -q -n mock-mock-1.2.14
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538613511
%autogen --disable-static PYTHON=python3
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1538613511
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mock
cp COPYING %{buildroot}/usr/share/package-licenses/mock/COPYING
%make_install
## install_append content
install -d -m 755 %{buildroot}/usr/share/pam.d
install -d -m 755 %{buildroot}/usr/share/defaults/mock
install -p -D -m 440 mock.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/mock
install -p -D -m 644 etc/mock/logging.ini %{buildroot}/usr/share/defaults/mock/
install -p -D -m 644 etc/mock/clear.cfg %{buildroot}/usr/share/defaults/mock/
ln -sf clear.cfg %{buildroot}/usr/share/defaults/mock/default.cfg
install -p -D -m 644 etc/pam/mock %{buildroot}/usr/share/pam.d/
rm -rf %{buildroot}/etc
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mock
/usr/bin/mockchain

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mock
/usr/share/bash-completion/completions/mockchain
/usr/share/defaults/mock/clear.cfg
/usr/share/defaults/mock/default.cfg
/usr/share/defaults/mock/logging.ini
/usr/share/defaults/sudo/sudoers.d/mock
/usr/share/pam.d/mock

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/mock/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/mock.1
/usr/share/man/man1/mockchain.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
