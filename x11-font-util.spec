%bcond_with bootstrap

Name:		x11-font-util
Version:	1.3.3
Release:	1
Summary:	Xorg X11 font utilities
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.xz
Source1:	x11-font-util.rpmlintrc
License:	BSD
%if !%{with bootstrap}
Requires:	bdftopcf
%endif
Requires:	mkfontdir
Requires:	mkfontscale
Requires:	fonttosfnt
Requires:	fslsfonts
Requires:	fstobdf
Requires:	showfont
Requires:	xlsfonts
BuildRequires:	pkgconfig(xorg-macros)

%description
Xorg X11 font utilities.

%prep
%autosetup -n font-util-%{version} -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-fontrootdir=%{_datadir}/fonts \
	--with-mapdir=%{_datadir}/fonts/util

%make_build

%install
%make_install

%files
%dir %{_datadir}/fonts/util
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_datadir}/fonts/util/*
%{_libdir}/pkgconfig/fontutil.pc
%{_datadir}/aclocal/fontutil.m4
%doc %{_mandir}/man1/bdftruncate.*
%doc %{_mandir}/man1/ucs2any.*
