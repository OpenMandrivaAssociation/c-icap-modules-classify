%define		git 4362fda
Name:           c-icap-modules-classify
Version:        20111022
Release:        %mkrel 1
Summary:        Classification module for c-icap

Group:          System/Servers
License:        LGPLv3+
URL:            https://c-icap.sourceforge.net/
Source0:        treveradams-C-ICAP-Classify-%{version}-0-g%{git}.tar.gz
BuildRequires:  c-icap-devel 
BuildRequires:	opencv-devel
BuildRequires:  tre-devel
Requires:	opencv
Requires:	tre
Requires:       c-icap-server

%description
This module can be setup to classify text & HTML pages as well as images. These
classifications are according to FastHyperSpace files or Intel OpenCV files
supplied by the user to recognize various image characteristics

%package -n	%{name}-training
Summary:	Programs to train FHS (Fast HyperSpace) or FNB (Fast Naive Bayes) files
Group:		System/Servers
Provides:       %{name}-training fhs_learn fhs_judge fhs_makepreload fnb_learn fnb_judge fnb_makepreload
Requires:	c_icap_classify

%description -n %{name}-training
Programs to train FHS (Fast HyperSpace) or FNB (Fast Naive Bayes) files for use by c_icap_classify

%prep
%setup -q -n treveradams-C-ICAP-Classify-%{git}
chmod 700 RECONF
./RECONF


%configure
%build
%make 


%install
rm -rf $RPM_BUILD_ROOT
# Make some directories
install -d %{buildroot}%{_sysconfdir}

# Now do install
make install DESTDIR=$RPM_BUILD_ROOT

# nuke unwanted devel files
rm -f %{buildroot}%{_libdir}/c_icap/srv_*.a
rm -f %{buildroot}%{_libdir}/c_icap/srv_*.la
rm -f %{buildroot}%{_libdir}/c_icap/sys_logger.la

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/c_icap/srv_classify.so


%files training
%{_bindir}/fhs_judge
%{_bindir}/fhs_learn
%{_bindir}/fhs_makepreload
%{_bindir}/fnb_judge
%{_bindir}/fnb_learn
%{_bindir}/fnb_makepreload




%changelog
* Tue Oct 25 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 20111022-1
+ Revision: 706506
- SPEC fixes
- import c-icap-modules-classify

