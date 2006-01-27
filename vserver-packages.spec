Summary:	A package providing fake packages for VServer guest system
Name:		vserver-packages
Version:	1
Release:	1.5
License:	GPL
Group:		Base
#Provides:	dev = 3.0.0
#Provides:	devfs
Provides:	kernel = 9.9
Provides:	kernel-smp = 9.9
Provides:	lvm
Provides:	lvm2
Provides:	mingetty
Provides:	module-init-tools
Provides:	udev
Provides:	login
Provides:	klogd
# Do not put Obsoletes for the following
# - allows installing of the real package
Provides:	fsck
Provides:	iproute2
Provides:	mount = 2.12
#Obsoletes:	devfs
Obsoletes:	kernel
Obsoletes:	klogd
Obsoletes:	kernel-smp
Obsoletes:	lvm
Obsoletes:	lvm2
Obsoletes:	mingetty
Obsoletes:	module-init-tools
Obsoletes:	udev
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package providing a fake packages to allow removal
of useless packages inside VPS.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
