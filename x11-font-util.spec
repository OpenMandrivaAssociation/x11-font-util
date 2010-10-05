Name:		x11-font-util
Version:	1.1.2
Release:	%mkrel 1
Summary:	Xorg X11 font utilities
Group:		Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2 
License:	BSD

%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

%if !%bootstrap
Requires:	bdftopcf
%endif
Requires:	mkfontdir
Requires:	mkfontscale
Requires:	fonttosfnt
Requires:	fslsfonts
Requires:	fstobdf
Requires:	showfont
Requires:	xlsfonts

BuildRequires:	x11-util-macros >= 1.1.5

%description
Xorg X11 font utilities

%prep
%setup -q -n font-util-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-mapdir=%_datadir/fonts/util

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %_datadir/fonts/util
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%_datadir/fonts/util/*
%{_libdir}/pkgconfig/fontutil.pc
%{_datadir}/aclocal/fontutil.m4
%{_mandir}/man1/bdftruncate.*
%{_mandir}/man1/ucs2any.*

