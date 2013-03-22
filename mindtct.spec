Name: mindtct          
Version: 0.1       
Release:        1%{?dist}
Summary: C library and Java wrapper around mindtct minutiae extractor       

License: Booz Allen Hamilton       
Source0: %{name}-%{version}.tar.gz       

BuildRequires: cmake nbis 
Requires: java      

%description


%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT
make
javac *.java
jar cvf mindtct.jar *.class

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
* Fri Mar 22 2013 Aaron Donovan <amdonov@gmail.com> 0.1-1
- new package built with tito

