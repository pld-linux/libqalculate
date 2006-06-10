Summary:	A modern multi-purpose calculator library
Summary(pl):	Nowoczesna, wielozadaniowa biblioteka kalkulatora
Name:		libqalculate
Version:	0.9.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/qalculate/%{name}-%{version}.tar.gz
# Source0-md5:	da762f9f072eb6ebaa8e3694521c0206
URL:		http://qalculate.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cln-devel >= 1.1
BuildRequires:	glib2-devel >= 1:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.3.8
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern multi-purpose calculator library.

%description -l pl
Nowoczesna, wielozadaniowa biblioteka kalkulatora.

%package devel
Summary:	Header files for qalculate library
Summary(pl):	Pliki nag³ówkowe biblioteki qalculate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cln-devel >= 1.1
Requires:	glib2-devel >= 1:2.0.0
Requires:	libxml2-devel >= 1:2.3.8

%description devel
Header files for qalculate library.

%description devel -l pl
Pliki nag³ówkowe biblioteki qalculate.

%package static
Summary:	Static qalculate library
Summary(pl):	Statyczna biblioteka qalculate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static qalculate library.

%description static -l pl
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/qalculate

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libqalculate
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
