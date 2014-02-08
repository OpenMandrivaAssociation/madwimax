Name: madwimax
Version: 0.1.1
Release: 3
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
%configure
make

%install
%__install -dm 755 $RPM_BUILD_ROOT/etc/udev/rules.d
%makeinstall_std

%files
%defattr(-, root, root, 0755)
%doc COPYING README
/etc/madwimax/*
/etc/udev/rules.d/*
/usr/sbin/*
/usr/share/man/man8/*


%changelog
* Sat Jan 01 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 627109
- initial release
- import madwimax


* Sun Apr 16 2010 Ángel Jiménez Álvaro <a.jimenez@upm.es>
- Packaged to Blogdrake Repository

