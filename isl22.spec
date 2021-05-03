%define major	22
%define libname	%mklibname isl %{major}
%define devname	%mklibname %{name} -d
%define staticname %mklibname %{name} -s -d
%define debug_package %{nil}

Summary:	Old version of the Integer Set Library
Name:		isl22
Version:	0.22.1
Release:	3
License:	MIT
Group:		System/Libraries
Url:		git://repo.or.cz/isl.git
Source0:	http://isl.gforge.inria.fr/isl-%{version}.tar.xz
BuildRequires:	gmp-devel

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

This is an old version of isl, provided for compatibility with legacy
applications only.

%package -n	%{libname}
Summary:	Integer Set Library
Group:		System/Libraries

%description -n	%{libname}
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

This is an old version of isl, provided for compatibility with legacy
applications only.

%package -n	%{devname}
Summary:	Development files for the isl Integer Set Library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Header files for the isl Integer Set Library.

%package -n	%{staticname}
Summary:	Static library for the isl Integer Set Library
Group:		Development/C
Requires:	%{devname} = %{EVRD}

%description -n	%{staticname}
Static library for the isl Integer Set Library

%prep
%autosetup -p1 -n isl-%{version}
autoreconf -fi

%build
%configure --enable-static
%make

%check
# All tests must pass
make check

%install
%makeinstall_std

# No -devel for compat packages...
rm -rf	%{buildroot}%{_libdir}/libisl.so \
	%{buildroot}%{_libdir}/*.{a,py} \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_includedir}

%files -n %{libname}
%{_libdir}/libisl.so.%{major}
%{_libdir}/libisl.so.%{major}.[0-9].[0-9]

%if 0
%files -n %{devname}
%{_libdir}/libisl.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*isl*-gdb.py

%files -n %{staticname}
%{_libdir}/*.a
%endif
