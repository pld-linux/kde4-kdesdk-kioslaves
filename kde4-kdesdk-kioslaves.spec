#
# TODO:
# - add man files
#
%define		orgname		kdesdk-kioslaves
%define		_state		stable
%define		qtver		4.8.1

Summary:	kde-kio-slave
Summary(pl.UTF-8):	kde-kio-slave
Group:		X11/Libraries
Summary:	KDESDK - kde-kio-slave
Summary(pl.UTF-8):	KDESDK - kde-kio-slave
Name:		kde4-kdesdk-kioslaves
Version:	4.13.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	279eb840bf56c5347042765befc22dcf
#Patch100: %{name}-branch.diff
##Patch0: %{name}-kiosvn.patch
##Patch1: %{name}-include.patch
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	subversion-devel
Requires:	kde4-kdelibs >= %{version}
Provides:	kde-kio-slave = %{version}
Provides:	kde-kio-svn = %{version}
Obsoletes:	kde-kio-slave < 4.12.0
Obsoletes:	kde-kio-svn < 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kde-kio-slave.

%description -l pl.UTF-8
kde-kio-slave.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*svn*
%attr(755,root,root) %{_libdir}/kde4/kded_ksvnd.so
%attr(755,root,root) %{_libdir}/kde4/kio_perldoc.so
%attr(755,root,root) %{_libdir}/kde4/kio_svn.so
%dir %{_datadir}/apps/kio_perldoc
%{_datadir}/apps/kio_perldoc/pod2html.pl
%{_datadir}/dbus-1/interfaces/org.kde.ksvnd.xml
%{_datadir}/kde4/services/ServiceMenus/subversion*.desktop
%{_datadir}/kde4/services/kded/*svn*.desktop
%{_datadir}/kde4/services/perldoc.protocol
%{_datadir}/kde4/services/svn*.protocol
%{_iconsdir}/*/*/*/*svn*.*
