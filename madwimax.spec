Name: madwimax
Version: 0.1.1
Release: 2
Summary: madwimax userspace driver
License: GPLv2+
Group: Networking/Other
BuildRequires: pkgconfig(libusb-1.0) asciidoc docbook2x
Source0: %{name}-%{version}.tar.bz2

%description
MadWimax is a driver for the wimax device Samsung SWC U200.

%prep
%setup -q

%build
%configure --prefix=%{_prefix}
make

%install
%__install -dm 755 %{buildroot}/etc/udev/rules.d
%makeinstall_std

%files
%defattr(-, root, root, 0755)
%doc COPYING README
/etc/madwimax/*
/etc/udev/rules.d/*
#/usr/lib/debug/usr/sbin/*
/usr/sbin/*
/usr/share/man/man8/*
#/usr/src/debug/madwimax-0.1.1/src/*
