%define name 	tex2im
%define version 1.8
%define release 4

Summary: 	A simple tool for converting LaTeX formulas into pixmap graphics
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source0: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		Publishing
Url: 		http://www.nought.de/tex2im.php
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: 	imagemagick, tetex-latex, bash
Provides: 	tex2im = %{version}-%{release}

%description
Tex2im is a simple tool that converts LaTeX formulas into high resolution
pixmap graphics for inclusion in text processors or presentations. Many 
different graphics formats are supported.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 tex2im %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README LICENSE examples/
%{_bindir}/tex2im






%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8-3mdv2010.0
+ Revision: 434349
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.8-2mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Oct 24 2006 Lev Givon <lev@mandriva.org> 1.8-2mdv2007.0
+ Revision: 71706
- Clean up spec file.
- Remove changelog.
- import tex2im 1.8-1mdk

