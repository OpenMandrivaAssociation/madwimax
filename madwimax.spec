%define distsuffix edm
Name: madwimax
Version: 0.1.1
Release: %mkrel 1
Summary: madwimax userspace driver
License: GPL
Group: Networking/Other
Requires: libusb1.0_0
BuildRequires: libusb1.0-devel asciidoc docbook2x
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
MadWimax is a driver for the wimax device Samsung SWC U200.

%prep
%setup -q

%build
%configure --prefix=/usr
make

%install
%__install -dm 755 $RPM_BUILD_ROOT/etc/udev/rules.d
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING README
/etc/madwimax/*
/etc/udev/rules.d/*
#/usr/lib/debug/usr/sbin/*
/usr/sbin/*
/usr/share/man/man8/*
#/usr/src/debug/madwimax-0.1.1/src/*

%clean
rm -rf $RPM_BUILD_ROOT

