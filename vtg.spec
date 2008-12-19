Summary:	Vala tools for GEdit
Name:		vtg
Version:	0.1.0
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://vtg.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ee5d3bb83b65b5f040f2350f647ea99a
URL:		http://www.paldo.org/vala/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gedit2-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-build-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtksourcecompletion-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for developing in Vala using GEdit.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gen-project
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/vtg/licenses
%{_libdir}/gedit-2/plugins/libvtg.so
%{_libdir}/gedit-2/plugins/vtg.gedit-plugin
%{_datadir}/vtg
