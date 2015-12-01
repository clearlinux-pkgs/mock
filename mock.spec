#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mock
Version  : 1.2.14
Release  : 9
URL      : https://git.fedorahosted.org/cgit/mock.git/snapshot/mock-1.2.14.tar.xz
Source0  : https://git.fedorahosted.org/cgit/mock.git/snapshot/mock-1.2.14.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mock-bin
Requires: mock-python
Requires: mock-data
Requires: mock-doc
BuildRequires : pkgconfig(bash-completion)

%description
These 3 src.rpms are setup to build on almost any rpm-based system.
They have a simple chain of buildrequires:

%package bin
Summary: bin components for the mock package.
Group: Binaries
Requires: mock-data

%description bin
bin components for the mock package.


%package data
Summary: data components for the mock package.
Group: Data

%description data
data components for the mock package.


%package doc
Summary: doc components for the mock package.
Group: Documentation

%description doc
doc components for the mock package.


%package python
Summary: python components for the mock package.
Group: Default

%description python
python components for the mock package.


%prep
%setup -q -n mock-1.2.14

%build
%autogen --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*