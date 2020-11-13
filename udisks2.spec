# TODO:
# - iscsi: libiscsi.h, libiscsi_init in libiscsi
# - lsm: libstoragemgmt >= 1.3.0, libconfig >= 1.3.2
#
# Conditional build:
%bcond_with	elogind		# elogind insead of systemd logind support
%bcond_with	iscsi		# iSCSI support
%bcond_with	libstoragemgmt	# libstoragemgmt support
%bcond_without	vdo		# VDO support (deprecated)
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries

Summary:	Disk Management Service
Summary(pl.UTF-8):	Usługa zarządzania dyskami
Name:		udisks2
Version:	2.9.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/storaged-project/udisks/releases
Source0:	https://github.com/storaged-project/udisks/releases/download/udisks-%{version}/udisks-%{version}.tar.bz2
# Source0-md5:	aad9c50f4cafccee01a621a6a6665784
Patch0:		automake-1.12.patch
Patch1:		%{name}-housekeeping_interval.patch
URL:		https://www.freedesktop.org/wiki/Software/udisks
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
%{?with_elogind:BuildRequires:	elogind-devel >= 219}
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gobject-introspection-devel >= 0.6.2
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libatasmart-devel >= 0.17
# with btrfs,crypto,fs,kbd,loop,lvm2,mdraid,part,swap%{?with_vdo:,vdo} modules
BuildRequires:	libblockdev-devel >= 2.24
%{?with_libstoragemgmt:BuildRequires:	libconfig-devel >= 1.3.2}
BuildRequires:	libmount-devel >= 2.30
%{?with_libstoragemgmt:BuildRequires:	libstoragemgmt-devel >= 1.3.0}
BuildRequires:	libtool
BuildRequires:	libuuid-devel >= 2.31
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.102
%{!?with_elogind:BuildRequires:	systemd-devel >= 1:209}
BuildRequires:	udev-glib-devel >= 1:165
%{?with_elogind:BuildConflicts:	systemd-devel}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libatasmart >= 0.17
Requires:	libblockdev-crypto >= 2.24
Requires:	libblockdev-fs >= 2.24
Requires:	libblockdev-loop >= 2.24
Requires:	systemd-units >= 44
Requires:	udev-core >= 1:147
Requires:	udev-glib >= 1:165
Suggests:	acl
Suggests:	cryptsetup-luks
Suggests:	dosfstools
Suggests:	e2fsprogs
Suggests:	gdisk
Suggests:	libblockdev-plugins >= 2.24
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
Requires:	glib2 >= 1:2.50

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
Requires:	glib2-devel >= 1:2.50

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
%if "%{_rpmversion}" >= "4.6"
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
%if "%{_rpmversion}" >= "4.6"
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
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-available-modules \
	%{__enable_disable apidocs gtk-doc} \
	%{__enable_disable static_libs static} \
	--disable-silent-rules \
	%{?with_vdo:--enable-vdo} \
	--with-html-dir=%{_gtkdocdir} \
	--with-systemdsystemunitdir=%{systemdunitdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/udisks2/modules/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/udisks2/modules/*.a
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/udisksctl
%attr(755,root,root) %{_sbindir}/umount.udisks2
%dir %{_libexecdir}/udisks2
%attr(755,root,root) %{_libexecdir}/udisks2/udisksd
%if "%{_libdir}" != "%{_libexecdir}"
%dir %{_libdir}/udisks2
%endif
%dir %{_libdir}/udisks2/modules
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_bcache.so
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_btrfs.so
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_lvm2.so
%if %{with vdo}
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_vdo.so
%endif
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_zram.so
%dir %{_sysconfdir}/udisks2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/udisks2/udisks2.conf
/lib/udev/rules.d/80-udisks2.rules
/lib/udev/rules.d/90-udisks2-zram.rules
#%{systemdunitdir}/clean-mount-point@.service
%{systemdunitdir}/udisks2.service
%{systemdunitdir}/udisks2-zram-setup@.service
%{systemdtmpfilesdir}/udisks2.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.policy
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.bcache.policy
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lvm2.policy
%if %{with vdo}
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.vdo.policy
%endif
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.zram.policy
%{_mandir}/man1/udisksctl.1*
%{_mandir}/man5/udisks2.conf.5*
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
%{_pkgconfigdir}/udisks2-bcache.pc
%{_pkgconfigdir}/udisks2-btrfs.pc
%{_pkgconfigdir}/udisks2-lvm2.pc
%if %{with vdo}
%{_pkgconfigdir}/udisks2-vdo.pc
%endif
%{_pkgconfigdir}/udisks2-zram.pc

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
