#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkdepim
Version  : 18.08.0
Release  : 2
URL      : https://download.kde.org/stable/applications/18.08.0/src/libkdepim-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/libkdepim-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/libkdepim-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libkdepim-lib
Requires: libkdepim-data
Requires: libkdepim-license
Requires: libkdepim-locales
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-search-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kldap-dev
BuildRequires : kmime-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
No detailed description available

%package data
Summary: data components for the libkdepim package.
Group: Data

%description data
data components for the libkdepim package.


%package dev
Summary: dev components for the libkdepim package.
Group: Development
Requires: libkdepim-lib
Requires: libkdepim-data
Provides: libkdepim-devel

%description dev
dev components for the libkdepim package.


%package lib
Summary: lib components for the libkdepim package.
Group: Libraries
Requires: libkdepim-data
Requires: libkdepim-license

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
%setup -q -n libkdepim-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535433949
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535433949
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libkdepim
cp COPYING %{buildroot}/usr/share/doc/libkdepim/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/libkdepim/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkdepim

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.addressbook.service.xml
/usr/share/dbus-1/interfaces/org.kde.mailtransport.service.xml
/usr/share/kdepimwidgets/pics/addresseelineedit.png
/usr/share/kdepimwidgets/pics/clicklineedit.png
/usr/share/kdepimwidgets/pics/kdateedit.png
/usr/share/kdepimwidgets/pics/ktimeedit.png
/usr/share/kservices5/kcmldap.desktop
/usr/share/xdg/libkdepim.categories
/usr/share/xdg/libkdepim.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Libkdepim/AddHostDialog
/usr/include/KF5/Libkdepim/AddresseeLineEditUtil
/usr/include/KF5/Libkdepim/BroadcastStatus
/usr/include/KF5/Libkdepim/CustomLogWidget
/usr/include/KF5/Libkdepim/EmailValidator
/usr/include/KF5/Libkdepim/KCheckComboBox
/usr/include/KF5/Libkdepim/KCursorSaver
/usr/include/KF5/Libkdepim/KDatePickerPopup
/usr/include/KF5/Libkdepim/KPrefsDialog
/usr/include/KF5/Libkdepim/KWeekdayCheckCombo
/usr/include/KF5/Libkdepim/KWidgetLister
/usr/include/KF5/Libkdepim/LdapClient
/usr/include/KF5/Libkdepim/LdapClientSearch
/usr/include/KF5/Libkdepim/LdapClientSearchConfig
/usr/include/KF5/Libkdepim/LdapSearchDialog
/usr/include/KF5/Libkdepim/MaillistDrag
/usr/include/KF5/Libkdepim/MultiplyingLine
/usr/include/KF5/Libkdepim/MultiplyingLineEditor
/usr/include/KF5/Libkdepim/OverlayWidget
/usr/include/KF5/Libkdepim/PIMMessageBox
/usr/include/KF5/Libkdepim/ProgressDialog
/usr/include/KF5/Libkdepim/ProgressIndicatorLabel
/usr/include/KF5/Libkdepim/ProgressIndicatorWidget
/usr/include/KF5/Libkdepim/ProgressManager
/usr/include/KF5/Libkdepim/ProgressStatusBarWidget
/usr/include/KF5/Libkdepim/RecentAddresses
/usr/include/KF5/Libkdepim/StatusbarProgressWidget
/usr/include/KF5/Libkdepim/UiStateSaver
/usr/include/KF5/LibkdepimAkonadi/AddContactJob
/usr/include/KF5/LibkdepimAkonadi/AddEmailAddressJob
/usr/include/KF5/LibkdepimAkonadi/AddEmailDisplayJob
/usr/include/KF5/LibkdepimAkonadi/AddresseeLineEdit
/usr/include/KF5/LibkdepimAkonadi/CollectionSearchJob
/usr/include/KF5/LibkdepimAkonadi/CompletionConfigureDialog
/usr/include/KF5/LibkdepimAkonadi/CompletionOrderEditor
/usr/include/KF5/LibkdepimAkonadi/OpenEmailAddressJob
/usr/include/KF5/LibkdepimAkonadi/Person
/usr/include/KF5/LibkdepimAkonadi/PersonSearchJob
/usr/include/KF5/LibkdepimAkonadi/ProgressManagerAkonadi
/usr/include/KF5/LibkdepimAkonadi/TagSelectionCombo
/usr/include/KF5/LibkdepimAkonadi/TagWidgets
/usr/include/KF5/libkdepim/addhostdialog.h
/usr/include/KF5/libkdepim/addresseelineeditutil.h
/usr/include/KF5/libkdepim/broadcaststatus.h
/usr/include/KF5/libkdepim/customlogwidget.h
/usr/include/KF5/libkdepim/emailvalidator.h
/usr/include/KF5/libkdepim/kcheckcombobox.h
/usr/include/KF5/libkdepim/kcursorsaver.h
/usr/include/KF5/libkdepim/kdatepickerpopup.h
/usr/include/KF5/libkdepim/kdepim_export.h
/usr/include/KF5/libkdepim/kprefsdialog.h
/usr/include/KF5/libkdepim/kweekdaycheckcombo.h
/usr/include/KF5/libkdepim/kwidgetlister.h
/usr/include/KF5/libkdepim/ldapclient.h
/usr/include/KF5/libkdepim/ldapclientsearch.h
/usr/include/KF5/libkdepim/ldapclientsearchconfig.h
/usr/include/KF5/libkdepim/ldapsearchdialog.h
/usr/include/KF5/libkdepim/maillistdrag.h
/usr/include/KF5/libkdepim/multiplyingline.h
/usr/include/KF5/libkdepim/multiplyinglineeditor.h
/usr/include/KF5/libkdepim/overlaywidget.h
/usr/include/KF5/libkdepim/pimmessagebox.h
/usr/include/KF5/libkdepim/progressdialog.h
/usr/include/KF5/libkdepim/progressindicatorlabel.h
/usr/include/KF5/libkdepim/progressindicatorwidget.h
/usr/include/KF5/libkdepim/progressmanager.h
/usr/include/KF5/libkdepim/progressstatusbarwidget.h
/usr/include/KF5/libkdepim/recentaddresses.h
/usr/include/KF5/libkdepim/statusbarprogresswidget.h
/usr/include/KF5/libkdepim/uistatesaver.h
/usr/include/KF5/libkdepim_version.h
/usr/include/KF5/libkdepimakonadi/addcontactjob.h
/usr/include/KF5/libkdepimakonadi/addemailaddressjob.h
/usr/include/KF5/libkdepimakonadi/addemaildisplayjob.h
/usr/include/KF5/libkdepimakonadi/addresseelineedit.h
/usr/include/KF5/libkdepimakonadi/collectionsearchjob.h
/usr/include/KF5/libkdepimakonadi/completionconfiguredialog.h
/usr/include/KF5/libkdepimakonadi/completionordereditor.h
/usr/include/KF5/libkdepimakonadi/kdepimakonadi_export.h
/usr/include/KF5/libkdepimakonadi/openemailaddressjob.h
/usr/include/KF5/libkdepimakonadi/person.h
/usr/include/KF5/libkdepimakonadi/personsearchjob.h
/usr/include/KF5/libkdepimakonadi/progressmanagerakonadi.h
/usr/include/KF5/libkdepimakonadi/tagselectioncombo.h
/usr/include/KF5/libkdepimakonadi/tagwidgets.h
/usr/include/KF5/libkdepimakonadi_version.h
/usr/lib64/cmake/KF5Libkdepim/KF5LibkdepimConfig.cmake
/usr/lib64/cmake/KF5Libkdepim/KF5LibkdepimConfigVersion.cmake
/usr/lib64/cmake/KF5Libkdepim/KF5LibkdepimTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Libkdepim/KF5LibkdepimTargets.cmake
/usr/lib64/cmake/KF5LibkdepimAkonadi/KF5LibkdepimAkonadiConfig.cmake
/usr/lib64/cmake/KF5LibkdepimAkonadi/KF5LibkdepimAkonadiConfigVersion.cmake
/usr/lib64/cmake/KF5LibkdepimAkonadi/KF5LibkdepimAkonadiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5LibkdepimAkonadi/KF5LibkdepimAkonadiTargets.cmake
/usr/lib64/cmake/MailTransportDBusService/MailTransportDBusServiceConfig.cmake
/usr/lib64/libKF5Libkdepim.so
/usr/lib64/libKF5LibkdepimAkonadi.so
/usr/lib64/qt5/mkspecs/modules/qt_Libkdepim.pri
/usr/lib64/qt5/mkspecs/modules/qt_LibkdepimAkonadi.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Libkdepim.so.5
/usr/lib64/libKF5Libkdepim.so.5.9.0
/usr/lib64/libKF5LibkdepimAkonadi.so.5
/usr/lib64/libKF5LibkdepimAkonadi.so.5.9.0
/usr/lib64/qt5/plugins/designer/kdepimakonadiwidgets.so
/usr/lib64/qt5/plugins/designer/kdepimwidgets.so
/usr/lib64/qt5/plugins/kcm_ldap.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/libkdepim/COPYING
/usr/share/doc/libkdepim/COPYING.LIB

%files locales -f libkdepim.lang
%defattr(-,root,root,-)

