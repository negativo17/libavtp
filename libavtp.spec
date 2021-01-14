Name:           libavtp
Version:        0.1.0
Release:        1%{dist}
Summary:        Audio Video Transport Protocol (AVTP) Support Library
License:        BSD
URL:            https://github.com/AVnu/%{name}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/9482c1143d2bca1303c4c0eeff30674eb468d357.patch

BuildRequires:  gcc-c++ 
BuildRequires:  meson
BuildRequires:  pkgconfig(cmocka)

%description
Open source implementation of Audio Video Transport Protocol (AVTP) specified in
IEEE 1722-2016 spec.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed to
develop applications that require %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files 
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.%{version}

%ldconfig_scriptlets

%files devel
%doc README.md
%license LICENSE
%{_includedir}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/avtp.pc

%changelog
* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 0.1.0-1
- First build.
