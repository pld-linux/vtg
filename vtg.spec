Summary:	Vala tools for GEdit
Summary(pl.UTF-8):	Narzędzia Vala dla GEdita
Name:		vtg
Version:	0.10.0
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://vtg.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	18d55d3c560f8a684f7346dc448f389f
URL:		http://vtg.googlecode.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gedit2-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtksourcecompletion-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	vala >= 0.5.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for developing in Vala using GEdit.

%description -l pl.UTF-8
Narzędzia do programowania w języku Vala przy użyciu GEdita.

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libvtg.so
%attr(755,root,root) %{_libdir}/libafrodite.so.*.*.*
%{_libdir}/gedit-2/plugins/vtg.gedit-plugin
%{_datadir}/vtg
%{_mandir}/man1/vala-gen-project.1*
