%define name 	tex2im
%define version 1.8
%define release 2

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
Requires: 	ImageMagick, tetex-latex, bash
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




