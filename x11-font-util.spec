%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

Name:		x11-font-util
Version:	1.3.0
Release:	5
Summary:	Xorg X11 font utilities
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
Source1:	x11-font-util.rpmlintrc
License:	BSD
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
Xorg X11 font utilities.

%prep
%setup -q -n font-util-%{version}
%apply_patches

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-mapdir=%{_datadir}/fonts/util

%make

%install
%makeinstall_std

%files
%dir %_datadir/fonts/util
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_datadir}/fonts/util/*
%{_libdir}/pkgconfig/fontutil.pc
%{_datadir}/aclocal/fontutil.m4
%{_mandir}/man1/bdftruncate.*
%{_mandir}/man1/ucs2any.*
