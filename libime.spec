Name:		libime
Version:	1.1.10
Release:	1
Source0:	https://github.com/fcitx/libime/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/kpu/kenlm/archive/bcd4af619a2fa45f5876d8855f7876cc09f663af.tar.gz
Summary:	Library to support generic input method implementation
URL:		https://github.com/fcitx/libime
License:	LGPL-2.1
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Fcitx5Utils)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libzstd)
BuildSystem:	cmake

%description
Library to support generic input method implementation

%package devel
Summary:	Development files for the libIME input method library
Group:		Development/Libraries
Requires:	%{name} = %{EVRD}

%description devel
Development files for the libIME input method library

%prep -a
cd src/libime/core
rm -rf kenlm
tar xf %{S:1}
mv kenlm-* kenlm

%build -p
export LD_LIBRARY_PATH=$(pwd)/_OMV_rpm_build/src/libime/core:$(pwd)/_OMV_rpm_build/src/libime/pinyin:$(pwd)/_OMV_rpm_build/src/libime/table

%install -p
export LD_LIBRARY_PATH=$(pwd)/_OMV_rpm_build/src/libime/core:$(pwd)/_OMV_rpm_build/src/libime/pinyin:$(pwd)/_OMV_rpm_build/src/libime/table

%files
%{_bindir}/libime_*
%{_libdir}/libIMECore.so.*
%{_libdir}/libIMEPinyin.so.*
%{_libdir}/libIMETable.so.*
%{_libdir}/libime
%{_datadir}/libime

%files devel
%{_includedir}/LibIME
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so
%{_libdir}/cmake/LibIMECore
%{_libdir}/cmake/LibIMEPinyin
%{_libdir}/cmake/LibIMETable
