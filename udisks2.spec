#
# Conditional build:
%bcond_with	elogind		# elogind insead of systemd logind support
%bcond_without	iscsi		# iSCSI support
%bcond_without	libstoragemgmt	# libstoragemgmt support
%bcond_without	vdo		# VDO support (deprecated)
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries

Summary:	Disk Management Service
Summary(pl.UTF-8):	Usługa zarządzania dyskami
Name:		udisks2
Version:	2.9.4
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/storaged-project/udisks/releases
Source0:	https://github.com/storaged-project/udisks/releases/download/udisks-%{version}/udisks-%{version}.tar.bz2
# Source0-md5:	576e057d2654894fab58f0393d105b7b
Patch0:		automake-1.12.patch
Patch1:		%{name}-housekeeping_interval.patch
Patch2:		%{name}-iscsi.patch
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
BuildRequires:	libblockdev-devel >= 2.25
BuildRequires:	libblockdev-btrfs-devel >= 2.25
BuildRequires:	libblockdev-crypto-devel >= 2.25
BuildRequires:	libblockdev-fs-devel >= 2.25
BuildRequires:	libblockdev-kbd-devel >= 2.25
BuildRequires:	libblockdev-loop-devel >= 2.25
BuildRequires:	libblockdev-lvm-devel >= 2.25
BuildRequires:	libblockdev-mdraid-devel >= 2.25
BuildRequires:	libblockdev-part-devel >= 2.25
BuildRequires:	libblockdev-swap-devel >= 2.25
%{?with_vdo:BuildRequires:	libblockdev-vdo-devel >= 2.25}
%{?with_libstoragemgmt:BuildRequires:	libconfig-devel >= 1.3.2}
BuildRequires:	libmount-devel >= 2.30
%{?with_libstoragemgmt:BuildRequires:	libstoragemgmt-devel >= 1.3.0}
BuildRequires:	libtool
BuildRequires:	libuuid-devel >= 2.31
BuildRequires:	libxslt-progs
%{?with_iscsi:BuildRequires:	open-iscsi-devel >= 2.1.4-1}
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.102
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
%{!?with_elogind:BuildRequires:	systemd-devel >= 1:209}
BuildRequires:	udev-glib-devel >= 1:165
%{?with_elogind:BuildConflicts:	systemd-devel}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libatasmart >= 0.17
Requires:	libblockdev >= 2.25
Requires:	libblockdev-crypto >= 2.25
Requires:	libblockdev-fs >= 2.25
Requires:	libblockdev-loop >= 2.25
Requires:	libblockdev-mdraid >= 2.25
Requires:	libblockdev-part >= 2.25
Requires:	libblockdev-swap >= 2.25
Requires:	libmount >= 2.30
Requires:	polkit >= 0.102
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

%package module-bcache
Summary:	Bcache support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi Bcache dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblockdev-kbd >= 2.25

%description module-bcache
Bcache support module for udisks2.

%description module-bcache -l pl.UTF-8
Moduł obsługi Bcache dla udisks2.

%package module-btrfs
Summary:	BTRFS support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi BTRFS dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblockdev-btrfs >= 2.25

%description module-btrfs
BTRFS support module for udisks2.

%description module-btrfs -l pl.UTF-8
Moduł obsługi BTRFS dla udisks2.

%package module-iscsi
Summary:	iSCSI support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi iSCSI dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	open-iscsi >= 2.1.4

%description module-iscsi
iSCSI support module for udisks2.

%description module-iscsi -l pl.UTF-8
Moduł obsługi iSCSI dla udisks2.

%package module-lsm
Summary:	LibStorageMgmt support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi LibStorageMgmt dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libconfig >= 1.3.2
Requires:	libstoragemgmt-daemon >= 1.3.0

%description module-lsm
LibStorageMgmt support module for udisks2.

%description module-lsm -l pl.UTF-8
Moduł obsługi LibStorageMgmt dla udisks2.

%package module-lvm2
Summary:	LVM2 support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi LVM2 dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblockdev-lvm >= 2.25

%description module-lvm2
LVM2 support module for udisks2.

%description module-lvm2 -l pl.UTF-8
Moduł obsługi LVM2 dla udisks2.

%package module-vdo
Summary:	VDO support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi VDO dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblockdev-vdo >= 2.25

%description module-vdo
VDO support module for udisks2.

%description module-vdo -l pl.UTF-8
Moduł obsługi VDO dla udisks2.

%package module-zram
Summary:	ZRAM support module for udisks2
Summary(pl.UTF-8):	Moduł obsługi ZRAM dla udisks2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libblockdev-kbd >= 2.25
Requires:	libblockdev-swap >= 2.25

%description module-zram
ZRAM support module for udisks2.

%description module-zram -l pl.UTF-8
Moduł obsługi ZRAM dla udisks2.

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
BuildArch:	noarch

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
BuildArch:	noarch

%description -n bash-completion-udisks2
This package provides bash-completion for udisks2 (udisksctl command).

%description -n bash-completion-udisks2 -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie parametrów dla udisks2
(polecenia udisksctl).

%prep
%setup -q -n udisks-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
%dir %{_sysconfdir}/udisks2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/udisks2/udisks2.conf
%dir %{_sysconfdir}/udisks2/modules.conf.d
/lib/udev/rules.d/80-udisks2.rules
%{systemdunitdir}/udisks2.service
%{systemdtmpfilesdir}/udisks2.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.policy
%{_mandir}/man1/udisksctl.1*
%{_mandir}/man5/udisks2.conf.5*
%{_mandir}/man8/udisks.8*
%{_mandir}/man8/udisksd.8*
%{_mandir}/man8/umount.udisks2.8*
%attr(700,root,root) %dir /var/lib/udisks2

%if %{with vdo}
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_vdo.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.vdo.policy
%endif

%files module-bcache
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_bcache.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.bcache.policy

%files module-btrfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_btrfs.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy

%if %{with iscsi}
%files module-iscsi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_iscsi.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.iscsi.policy
%endif

%if %{with libstoragemgmt}
%files module-lsm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_lsm.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/udisks2/modules.conf.d/udisks2_lsm.conf
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lsm.policy
%{_mandir}/man5/udisks2_lsm.conf.5*
%endif

%files module-lvm2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_lvm2.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lvm2.policy

%files module-zram
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/udisks2/modules/libudisks2_zram.so
/lib/udev/rules.d/90-udisks2-zram.rules
%{systemdunitdir}/udisks2-zram-setup@.service
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.zram.policy

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
%if %{with iscsi}
%{_pkgconfigdir}/udisks2-iscsi.pc
%endif
%if %{with libstoragemgmt}
%{_pkgconfigdir}/udisks2-lsm.pc
%endif
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
