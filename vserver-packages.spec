# NOTE
# - here should be rc-scripts dependencies that you don't need inside vserver
#   (interact with kernel / networking), the rest of the packages can
#   workarounded in sane way (for example udev + udev-core)
%define		ul_ver	2.14.1
Summary:	A package providing fake packages for VServer guest system
Summary(pl.UTF-8):	Pakiet udostępniający fałszywe pakiety dla systemu gościnnego VServera
Name:		vserver-packages
Version:	3.3
Release:	5
License:	GPL
Group:		Base
# Do not put Obsoletes for all of the packages -- allows installing of the real package
# don't provide (klogd) this one since syslog-ng would obsolete whole package
Requires:	sed >= 4.0
Provides:	blockdev = %{ul_ver}
Provides:	dev = 3.4-4
Provides:	ethtool
Provides:	fsck = 1.40.10
Provides:	iproute2 = 2.6.23
Provides:	iputils-arping = 2:s20101006-2
Provides:	libcgroup
Provides:	login = %{ul_ver}
Provides:	lvm2 = 2.02.83
Provides:	mingetty = 0.9.4
Provides:	kmod = 4
Provides:	module-init-tools = 3.3
Provides:	mount = %{ul_ver}
Provides:	virtual(module-tools)
Obsoletes:	devfs
Obsoletes:	modutils
Obsoletes:	vserver-SysVinit
Obsoletes:	vserver-basesystem
Obsoletes:	vserver-dev
Obsoletes:	vserver-rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# find-debuginfo.sh can't live with missing $RPM_BUILD_ROOT and it's somewhy
# still called for noarch packages.
%define		_enable_debug_packages	0

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

%post
# remove "ignore = vserver-packages" from poldek config if this package is installed
if [ -f %{_sysconfdir}/%{name}/poldek.conf ]; then
	%{__sed} -i -e '/^ignore/s/vserver-packages//' %{_sysconfdir}/%{name}/poldek.conf
fi

%files
%defattr(644,root,root,755)
