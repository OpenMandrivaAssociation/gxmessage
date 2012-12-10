%define name gxmessage
%define version 2.12.4
%define release %mkrel 2

Summary:	An xmessage substitute for gtk-2.0
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv3+
URL:		http://homepages.ihug.co.nz/~trmusson
Group:		Development/GNOME and GTK+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://homepages.ihug.co.nz/~trmusson/stuff/%name-%version.tar.gz
BuildRequires:	gtk+2-devel
BuildRequires:	intltool

%description
To quote from the xmessage manual page, xmessage is a program to
"display a message or query in a window." It returns an exit code based
on the user's response. gxmessage is a gtk-2.0 based clone of xmessage.


%prep
%setup -q


%build
%configure2_5x
%make

%install
%__rm -rf %buildroot
%makeinstall_std
%find_lang %name

%clean
%__rm -rf %buildroot

%files -f %name.lang
%defattr (0755,root,root,0755)
%_bindir/%name
%defattr (0644,root,root,0755)
%doc AUTHORS ChangeLog README
%_mandir/man1/%name.1*
%{_infodir}/gxmessage.info*
%{_iconsdir}/hicolor/*/apps/gxmessage.png


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.12.4-2mdv2011.0
+ Revision: 619322
- the mass rebuild of 2010.0 packages

* Wed Sep 30 2009 Frederik Himpe <fhimpe@mandriva.org> 2.12.4-1mdv2010.0
+ Revision: 451845
- Fix BuildRequires
- update to new version 2.12.4

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 2.12.3-1mdv2010.0
+ Revision: 447923
- update to new version 2.12.3

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 2.12.2-1mdv2010.0
+ Revision: 444863
- Update to new version 1.12.2
- License is now GPLv3+

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.6.2-4mdv2010.0
+ Revision: 429351
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.6.2-3mdv2009.0
+ Revision: 246776
- rebuild
- fix no-buildroot-tag
- fix spacing at top of description

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 2.6.2-1mdv2008.1
+ Revision: 161820
- New version 2.6.2

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 1mdv2008.1-current
+ Revision: 132983
- BR gtk+2-devel
- kill re-definition of %%buildroot on Pixel's request


* Thu Jan 26 2006 Lenny Cartier <lenny@mandriva.com> 2.6.0-1mdk
- 2.6.0

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.4.4-1mdk
- New release 2.4.4

* Mon Mar 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.4.3-1mdk
- 2.4.3

* Tue Feb 22 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.4.2-1mdk
- 2.4.2

* Mon Nov 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.11-1mdk
- 2.0.11

* Tue Oct 28 2003 Han Boetes <han@linux-mandrake.com> 2.0.5-1mdk
- Bump
- spec cleanup

