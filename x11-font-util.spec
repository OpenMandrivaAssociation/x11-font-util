Name: x11-font-util
Version: 1.0.1
Release: %mkrel 3
Summary: Xorg X11 font utilities
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2 
License: CHECK
BuildRoot: %{_tmppath}/%{name}-root

Requires: bdftopcf
Requires: mkfontdir
Requires: mkfontscale
Requires: fonttosfnt
Requires: fslsfonts
Requires: fstobdf
Requires: mkcfm
Requires: showfont
Requires: xlsfonts


BuildRequires: x11-util-macros >= 1.0.1

%description
Xorg X11 font utilities

%prep
%setup -q -n font-util-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
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
%{_mandir}/man1/bdftruncate.1x.bz2
%{_mandir}/man1/ucs2any.1x.bz2




