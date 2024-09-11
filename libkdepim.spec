#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkdepim
Version  : 24.08.0
Release  : 79
URL      : https://download.kde.org/stable/release-service/24.08.0/src/libkdepim-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/libkdepim-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/libkdepim-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Libraries for KDE PIM applications
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: libkdepim-data = %{version}-%{release}
Requires: libkdepim-lib = %{version}-%{release}
Requires: libkdepim-license = %{version}-%{release}
Requires: libkdepim-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-search-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kldap-dev
BuildRequires : kmime-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

%package data
Summary: data components for the libkdepim package.
Group: Data

%description data
data components for the libkdepim package.


%package dev
Summary: dev components for the libkdepim package.
Group: Development
Requires: libkdepim-lib = %{version}-%{release}
Requires: libkdepim-data = %{version}-%{release}
Provides: libkdepim-devel = %{version}-%{release}
Requires: libkdepim = %{version}-%{release}

%description dev
dev components for the libkdepim package.


%package lib
Summary: lib components for the libkdepim package.
Group: Libraries
Requires: libkdepim-data = %{version}-%{release}
Requires: libkdepim-license = %{version}-%{release}

%description lib
lib components for the libkdepim package.


%package license
Summary: license components for the libkdepim package.
Group: Default

%description license
license components for the libkdepim package.


%package locales
Summary: locales components for the libkdepim package.
Group: Default

%description locales
locales components for the libkdepim package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkdepim-24.08.0
cd %{_builddir}/libkdepim-24.08.0
pushd ..
cp -a libkdepim-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724435166
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724435166
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdepim
cp %{_builddir}/libkdepim-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkdepim/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkdepim-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkdepim/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkdepim-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdepim/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/libkdepim-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdepim/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libkdepim-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libkdepim/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkdepim6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.addressbook.service.xml
/usr/share/dbus-1/interfaces/org.kde.mailtransport.service.xml
/usr/share/qlogging-categories6/libkdepim.categories
/usr/share/qlogging-categories6/libkdepim.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/Libkdepim/Libkdepim/KCheckComboBox
/usr/include/KPim6/Libkdepim/Libkdepim/KWidgetLister
/usr/include/KPim6/Libkdepim/Libkdepim/MultiplyingLine
/usr/include/KPim6/Libkdepim/Libkdepim/MultiplyingLineEditor
/usr/include/KPim6/Libkdepim/Libkdepim/ProgressDialog
/usr/include/KPim6/Libkdepim/Libkdepim/ProgressIndicatorLabel
/usr/include/KPim6/Libkdepim/Libkdepim/ProgressManager
/usr/include/KPim6/Libkdepim/Libkdepim/ProgressStatusBarWidget
/usr/include/KPim6/Libkdepim/Libkdepim/StatusbarProgressWidget
/usr/include/KPim6/Libkdepim/libkdepim/kcheckcombobox.h
/usr/include/KPim6/Libkdepim/libkdepim/kdepim_export.h
/usr/include/KPim6/Libkdepim/libkdepim/kwidgetlister.h
/usr/include/KPim6/Libkdepim/libkdepim/multiplyingline.h
/usr/include/KPim6/Libkdepim/libkdepim/multiplyinglineeditor.h
/usr/include/KPim6/Libkdepim/libkdepim/progressdialog.h
/usr/include/KPim6/Libkdepim/libkdepim/progressindicatorlabel.h
/usr/include/KPim6/Libkdepim/libkdepim/progressmanager.h
/usr/include/KPim6/Libkdepim/libkdepim/progressstatusbarwidget.h
/usr/include/KPim6/Libkdepim/libkdepim/statusbarprogresswidget.h
/usr/include/KPim6/Libkdepim/libkdepim_version.h
/usr/lib64/cmake/KPim6Libkdepim/KPim6LibkdepimConfig.cmake
/usr/lib64/cmake/KPim6Libkdepim/KPim6LibkdepimConfigVersion.cmake
/usr/lib64/cmake/KPim6Libkdepim/KPim6LibkdepimTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6Libkdepim/KPim6LibkdepimTargets.cmake
/usr/lib64/cmake/KPim6MailTransportDBusService/KPim6MailTransportDBusServiceConfig.cmake
/usr/lib64/libKPim6Libkdepim.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6Libkdepim.so.6.2.0
/V3/usr/lib64/qt6/plugins/designer/kdepim6widgets.so
/usr/lib64/libKPim6Libkdepim.so.6
/usr/lib64/libKPim6Libkdepim.so.6.2.0
/usr/lib64/qt6/plugins/designer/kdepim6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkdepim/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libkdepim/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libkdepim/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkdepim/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkdepim/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libkdepim6.lang
%defattr(-,root,root,-)

