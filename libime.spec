Name:		libime
Version:	1.1.12
Release:	1
Source0:	https://github.com/fcitx/libime/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/kpu/kenlm/archive/bcd4af619a2fa45f5876d8855f7876cc09f663af.tar.gz
Source2:	https://download.fcitx-im.org/data/table-20240108.tar.zst
Source3:	https://download.fcitx-im.org/data/dict-20241001.tar.zst
Source4:	https://download.fcitx-im.org/data/lm_sc.arpa-20250113.tar.zst
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
cp %{S:2} %{S:3} %{S:4} data/
cd src/libime/core
rm -rf kenlm
tar xf %{S:1}
mv kenlm-* kenlm

%build -p
export LD_LIBRARY_PATH=$(pwd)/_OMV_rpm_build/bin:$(pwd)/_OMV_rpm_build/src/libime/core:$(pwd)/_OMV_rpm_build/src/libime/pinyin:$(pwd)/_OMV_rpm_build/src/libime/table

%install -p
export LD_LIBRARY_PATH=$(pwd)/_OMV_rpm_build/bin:$(pwd)/_OMV_rpm_build/src/libime/core:$(pwd)/_OMV_rpm_build/src/libime/pinyin:$(pwd)/_OMV_rpm_build/src/libime/table

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
