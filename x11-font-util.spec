%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

Name:		x11-font-util
Version:	1.3.0
Release:	3
Summary:	Xorg X11 font utilities
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
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
Patch0:		aarch64.patch

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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2011.0
+ Revision: 671221
- mass rebuild

* Thu Oct 14 2010 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 585557
- new release

* Tue Oct 05 2010 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 583051
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.1-1mdv2010.1
+ Revision: 464647
- New version: 1.1.1

* Mon Sep 28 2009 Olivier Blin <oblin@mandriva.com> 1.0.2-2mdv2010.0
+ Revision: 450584
- add bootstrap flag for bdftopcf (from Arnaud Patard)

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 411532
- update to new version 1.0.2

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226006
- rebuild
- fix no-buildroot-tag

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 153831
- Update BuildRequires and resubmit package.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 75101
- rebuild for 2008
- drop dependency on mkcfm (it's deprecated)
- small spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:36:00 (50789)
- All fonts now moved to /usr/share/fonts. font-util need point to correct place

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

