#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xdotool
Version  : 3.20160805.1
Release  : 4
URL      : https://github.com/jordansissel/xdotool/releases/download/v3.20160805.1/xdotool-3.20160805.1.tar.gz
Source0  : https://github.com/jordansissel/xdotool/releases/download/v3.20160805.1/xdotool-3.20160805.1.tar.gz
Summary  : Command-line X11 automation tool
Group    : Development/Tools
License  : BSD-3-Clause
Requires: xdotool-bin = %{version}-%{release}
Requires: xdotool-lib = %{version}-%{release}
Requires: xdotool-license = %{version}-%{release}
BuildRequires : libXinerama-dev
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xtst)

%description
xdotool: Fake input from the mouse and keyboard very easily.
Also supports window manager actions such as moving, activating, and other
actions on windows.
libxdo: C library for doing the same.

%package bin
Summary: bin components for the xdotool package.
Group: Binaries
Requires: xdotool-license = %{version}-%{release}

%description bin
bin components for the xdotool package.


%package dev
Summary: dev components for the xdotool package.
Group: Development
Requires: xdotool-lib = %{version}-%{release}
Requires: xdotool-bin = %{version}-%{release}
Provides: xdotool-devel = %{version}-%{release}
Requires: xdotool = %{version}-%{release}
Requires: xdotool = %{version}-%{release}

%description dev
dev components for the xdotool package.


%package lib
Summary: lib components for the xdotool package.
Group: Libraries
Requires: xdotool-license = %{version}-%{release}

%description lib
lib components for the xdotool package.


%package license
Summary: license components for the xdotool package.
Group: Default

%description license
license components for the xdotool package.


%prep
%setup -q -n xdotool-3.20160805.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561603737
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} WITHOUT_RPATH_FIX=1


%install
export SOURCE_DATE_EPOCH=1561603737
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdotool
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/xdotool/COPYRIGHT
%make_install PREFIX=/usr
## install_append content
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
## install_append end

%files
%defattr(-,root,root,-)
/usr/man/man1/xdotool.1

%files bin
%defattr(-,root,root,-)
/usr/bin/xdotool

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libxdo.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxdo.so.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdotool/COPYRIGHT
