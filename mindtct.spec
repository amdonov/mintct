Name: mindtct          
Version: 0.1       
Release:        4%{?dist}
Summary: C library and Java wrapper around mindtct minutiae extractor       

License: Booz Allen Hamilton       
Source0: %{name}-%{version}.tar.gz       

BuildRequires: cmake, NBIS >= 4.1.0-6
Requires: java      

%description


%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT
make
javac -d . *.java
jar cvf mindtct.jar com

%install
rm -rf $RPM_BUILD_ROOT
make install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/*
%{_libdir}/*
%doc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%changelog
* Wed Mar 27 2013 Aaron Donovan <amdonov@gmail.com> 0.1-4
- Requiring version NBIS with threadsafe WSQ code (amdonov@gmail.com)

* Mon Mar 25 2013 Aaron Donovan <amdonov@gmail.com> 0.1-3
- Moving Java classes to com.bah.biometrics package (amdonov@gmail.com)
- Merge branch 'master' of github.com:amdonov/mintct (amdonov@gmail.com)
- Initial commit (amdonov@gmail.com)

* Fri Mar 22 2013 Aaron Donovan <amdonov@gmail.com> 0.1-2
- Corrected NBIS dependency (amdonov@gmail.com)

* Fri Mar 22 2013 Aaron Donovan <amdonov@gmail.com>
- Corrected NBIS dependency (amdonov@gmail.com)

* Fri Mar 22 2013 Aaron Donovan <amdonov@gmail.com> 0.1-1
- new package built with tito

