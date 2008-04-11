# NOTE
# - here should be rc-scripts dependencies that you don't need inside vserver
#   (interact with kernel / networking), the rest of the packages can
#   workarounded in sane way (for example udev + udev-core)
Summary:	A package providing fake packages for VServer guest system
Summary(pl.UTF-8):	Pakiet udostępniający fałszywe pakiety dla systemu gościnnego VServera
Name:		vserver-packages
Version:	3.1
Release:	1
License:	GPL
Group:		Base
# Do not put Obsoletes for all of the packages -- allows installing of the real package
Provides:	dev = 2.9.0-19
Provides:	fsck = 1.40.4
Provides:	iproute2 = 2.6.23
# don't provide this one since syslog-ng would obsolete whole package
# Provides:	klogd
Provides:	blockdev = 2.12r
Provides:	login = 2.12r
Provides:	lvm2 = 2.01.15
Provides:	mingetty = 0.9.4
Provides:	module-init-tools = 3.0
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
