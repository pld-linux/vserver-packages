Summary:	A package providing fake packages for VServer guest system
Summary(pl):	Pakiet udostêpniaj±cy fa³szywe pakiety dla systemu go¶cinnego VServera
Name:		vserver-packages
Version:	1
Release:	4
License:	GPL
Group:		Base
# Do not put Obsoletes for all of the packages -- allows installing of the real package
Provides:	SysVinit = 2.86-4
Provides:	dev = 2.9.0-19
Provides:	fsck
Provides:	iproute2
Provides:	klogd
Provides:	login
Provides:	lvm
Provides:	lvm2
Provides:	mingetty
Provides:	module-init-tools
Provides:	mount = 2.12
Provides:	udev
Obsoletes:	devfs
Obsoletes:	klogd
Obsoletes:	lvm
Obsoletes:	lvm2
Obsoletes:	mingetty
Obsoletes:	module-init-tools
Obsoletes:	modutils
Obsoletes:	udev
Obsoletes:	vserver-SysVinit
Obsoletes:	vserver-basesystem
Obsoletes:	vserver-dev
Obsoletes:	vserver-rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package providing a fake packages to allow removal of useless
packages inside VPS.

%description -l pl
Pakiet dostarczaj±cy fa³szywe pakiety, aby umo¿liwiæ usuniêcie
bezu¿ytecznych pakietów z VPS-a.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
