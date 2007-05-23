%define	name	Xtart
%define	version	1.0
%define	release	9mdk

Summary:	Use this to access any installed WM from a logged-in console
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-xvt.patch.bz2
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	python
BuildArch:	noarch

%description
Xtart is a simple program that checks for properly installed window managers
and allows the user full menu access to them from a logged-in console.  The
special entry 00 in menu selectio will start X with an xterm to manually
start new installations of window managers or to do tests with X and no
window manager.  See /etc/X11/wmsession.d for proper WM integration.

%prep
%setup -q
%patch0 -p0 -b .peroyvind

%build

%install
%{__install} -m 0755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/Xtart
