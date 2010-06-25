Summary:	A modern multi-purpose calculator library
Summary(pl.UTF-8):	Nowoczesna, wielozadaniowa biblioteka kalkulatora
Name:		libqalculate
Version:	0.9.7
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/project/qalculate/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a1507ab862f4ad9852788619aada35cd
URL:		http://qalculate.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cln-devel >= 1.3
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.0.0
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.3.8
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern multi-purpose calculator library.

%description -l pl.UTF-8
Nowoczesna, wielozadaniowa biblioteka kalkulatora.

%package devel
Summary:	Header files for qalculate library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qalculate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cln-devel >= 1.1
Requires:	glib2-devel >= 1:2.0.0
Requires:	libxml2-devel >= 1:2.3.8

%description devel
Header files for qalculate library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki qalculate.

%package static
Summary:	Static qalculate library
Summary(pl.UTF-8):	Statyczna biblioteka qalculate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static qalculate library.

%description static -l pl.UTF-8
Statyczna biblioteka qalculate.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/qalculate

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
