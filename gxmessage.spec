%define name gxmessage
%define version 2.6.0
%define release %mkrel 1

Summary:	An xmessage substitute for gtk-2.0
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://homepages.ihug.co.nz/~trmusson
Group:		Development/GNOME and GTK+
Source:		%{URL}/stuff/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2.0

%description

To quote from the xmessage manual page, xmessage is a program to
"display a message or query in a window." It returns an exit code based
on the user's response. gxmessage is a gtk-2.0 based clone of xmessage.


%prep
%setup -q


%build
%configure --bindir=/usr/X11R6/bin
%make


%install
%__rm -rf %buildroot
%makeinstall bindir=%buildroot/usr/X11R6/bin

%find_lang %name

%clean
%__rm -rf %buildroot


%files -f %name.lang
%defattr (0755,root,root,0755)
/usr/X11R6/bin/%name
%defattr (0644,root,root,0755)
%doc AUTHORS ChangeLog README
%_mandir/man1/%name.1*
%_datadir/pixmaps/%name.png


