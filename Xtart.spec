%define	name	Xtart
%define	version	1.0
%define release	22

Summary:	Use this to access any installed WM from a logged-in console
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-xvt.patch
# call startx instead of xinit, for ConsoleKit
Patch1:		%{name}-startx.patch
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
%patch0 -p0 -b .xvt
%patch1 -p0 -b .startx

%build

%install
%{__install} -m 0755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/Xtart


%changelog
* Wed Apr 20 2011 Antoine Ginies <aginies@mandriva.com> 1.0-16mdv2011.0
+ Revision: 656281
- bump release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-15mdv2010.1
+ Revision: 521931
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-14mdv2010.0
+ Revision: 413015
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-13mdv2008.1
+ Revision: 178761
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0-12mdv2008.0
+ Revision: 69328
- Update patch0 with correct path for xvt

* Wed Aug 22 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0-11mdv2008.0
+ Revision: 69151
- bunzip patch
- Patch1 (Charles A Edwards): call startx, for ConsoleKit support

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 1.0-10mdv2008.0
+ Revision: 30202
- use mkrel
- Import Xtart



* Fri Jun 06 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-9mdk
- remove redundant requires, common-licenses is required by the base system
- from andre <avblokland@gmx.net>:
	"Xtart assumes that xterm is installed on a Mandrake installation which doesn't 
	have to be true. But xvt is always installed (atleast if a term is installed)"
	- use xvt in stead of xterm

* Thu Jun 05 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-8mdk
- cleanup, fix so that we don't end up with unpackaged files
- macroize
- drop Source1, it's just a copy of the GPL-license, and it does'nt
  get packaged neither
- nicer formatting

* Mon Jul 22 2002 Jeff Garzik <jgarzik@mandrakesoft.com> 1.0-7mdk
- make this package 'noarch', its lone file is a Python script
- Requires: common-licenses

* Thu Oct 18 2001 dam's <damien@mandrakesoft.com> 1.0-6mdk
- removed useless documentation.

* Thu Oct 18 2001 Daouda LO <daouda@mandrakesoft.com> 1.0-5mdk
- rpmlint happier. Rank n°1.

* Thu Sep 5 2001 civileme <civileme@manddrakesoft.com> 1.0-4mdk
-Revised group and corrected versioning

* Thu Sep 5 2001 civileme <civileme@mandrakesoft.com> 1.0-3mdk
-Corrected dumb mistake about noarch Target

* Thu Sep 5 2001 civileme <civileme@mandrakesoft.com> 1.0-2mdk
-Revised group 

* Thu Aug 29 2001 civileme <tester@civileme.mandrakesoft.com> 1.0-1mdk
-Public Release of crashtesters package


# end of file
