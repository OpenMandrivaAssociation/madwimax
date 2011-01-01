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
BuildArch:	i586

%description
MadWimax is a driver for the wimax device Samsung SWC U200.

%prep
%setup -q

%build
%configure --prefix=/usr
make

%install
rm -rf %{buildroot}

%__install -dm 755 $RPM_BUILD_ROOT/etc/udev/rules.d
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
/etc/madwimax/*
/etc/udev/rules.d/*
#/usr/lib/debug/usr/sbin/*
/usr/sbin/*
/usr/share/man/man8/*
#/usr/src/debug/madwimax-0.1.1/src/*
