# NOTE
# - here should be rc-scripts dependencies that you don't need inside vserver
#   (interact with kernel / networking), the rest of the packages can
#   workarounded in sane way (for example udev + udev-core)
Summary:	A package providing fake packages for VServer guest system
Summary(pl.UTF-8):	Pakiet udostępniający fałszywe pakiety dla systemu gościnnego VServera
Name:		vserver-packages
Version:	3
Release:	1
License:	GPL
Group:		Base
# Do not put Obsoletes for all of the packages -- allows installing of the real package
Provides:	dev = 2.9.0-19
Provides:	fsck
Provides:	iproute2
# don't provide this one since syslog-ng would obsolete whole package
# Provides:	klogd
Provides:	blockdev
Provides:	login
Provides:	lvm2
Provides:	mingetty
Provides:	module-init-tools
Provides:	mount = 2.12
Obsoletes:	devfs
Obsoletes:	modutils
Obsoletes:	vserver-SysVinit
Obsoletes:	vserver-basesystem
Obsoletes:	vserver-dev
Obsoletes:	vserver-rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package providing a fake packages to allow removal of useless
packages inside VPS.

%description -l pl.UTF-8
Pakiet dostarczający fałszywe pakiety, aby umożliwić usunięcie
bezużytecznych pakietów z VPS-a.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
