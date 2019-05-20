#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries

Summary:	Disk Management Service
Summary(pl.UTF-8):	Usługa zarządzania dyskami
Name:		udisks2
Version:	2.1.8
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://udisks.freedesktop.org/releases/udisks-%{version}.tar.bz2
# Source0-md5:	501d11c243bd8c6c00650474cd2afaab
Patch0:		automake-1.12.patch
URL:		https://www.freedesktop.org/wiki/Software/udisks
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 0.6.2
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool
BuildRequires:	libatasmart-devel >= 0.17
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.102
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	udev-glib-devel >= 1:165
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libatasmart >= 0.17
Requires:	systemd-units >= 44
Requires:	udev-core >= 1:147
Requires:	udev-glib >= 1:165
Suggests:	acl
Suggests:	cryptsetup-luks
Suggests:	dosfstools
Suggests:	e2fsprogs
Suggests:	gdisk
Suggests:	losetup
Suggests:	mount
Suggests:	nilfs-utils
Suggests:	ntfsprogs
Suggests:	parted
Suggests:	reiserfsprogs
Suggests:	util-linux
Suggests:	xfsprogs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
udisks provides a daemon, D-Bus API and command line tools for
managing disks and storage devices. This package is for the udisks 2.x
series.

%description -l pl.UTF-8
udisks dostarcza demona, API D-Bus oraz narzędzia linii poleceń do
zarządzania dyskami i innymi urządzeniami przechowującymi dane. Ten
pakiet jest przeznaczony dla udisks z serii 2.x.

%package libs
Summary:	udisks2 library
Summary(pl.UTF-8):	Biblioteka udisks2
License:	LGPL v2+
Group:		Libraries
Requires:	glib2 >= 1:2.36.0

%description libs
This package contains udisks2 library, which provides access to the
udisks daemon.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę udisks2, umożliwiającą dostęp do demona
udisks.

%package devel
Summary:	Header files for udisks2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki udisks2
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36.0

%description devel
Header files for udisks2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki udisks2.

%package static
Summary:	Static udisks2 library
Summary(pl.UTF-8):	Statyczna biblioteka udisks2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static udisks2 library.

%description static -l pl.UTF-8
Statyczna biblioteka udisks2.

%package apidocs
Summary:	udisks2 API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki udisks2
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for udisks2 library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki udisks2.

%package -n bash-completion-udisks2
Summary:	bash-completion for udisks2
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów dla udisks2
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-udisks2
This package provides bash-completion for udisks2 (udisksctl command).

%description -n bash-completion-udisks2 -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie parametrów dla udisks2
(polecenia udisksctl).

%prep
%setup -q -n udisks-%{version}
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
	%{__enable_disable static_libs static} \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--with-systemdsystemunitdir=%{systemdunitdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README
%attr(755,root,root) %{_bindir}/udisksctl
%dir %{_sysconfdir}/udisks2
%dir %{_libexecdir}/udisks2
%attr(755,root,root) %{_libexecdir}/udisks2/udisksd
%attr(755,root,root) %{_sbindir}/umount.udisks2
/etc/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{systemdunitdir}/udisks2.service
/lib/udev/rules.d/80-udisks2.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
%{_datadir}/polkit-1/actions/org.freedesktop.udisks2.policy
%{_mandir}/man1/udisksctl.1*
%{_mandir}/man8/udisks.8*
%{_mandir}/man8/udisksd.8*
%{_mandir}/man8/umount.udisks2.8*
%attr(700,root,root) %dir /var/lib/udisks2

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libudisks2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libudisks2.so.0
%{_libdir}/girepository-1.0/UDisks-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libudisks2.so
%{_datadir}/gir-1.0/UDisks-2.0.gir
%{_includedir}/udisks2
%{_pkgconfigdir}/udisks2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libudisks2.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/udisks2
%endif

%files -n bash-completion-udisks2
%defattr(644,root,root,755)
%{bash_compdir}/udisksctl
