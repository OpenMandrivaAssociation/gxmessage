%define name gxmessage
%define version 2.12.3
%define release %mkrel 1

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
