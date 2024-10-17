%define module   Test-Program
%define version    0.10
%define release    4

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Testing tools for Perl programs
Url:        https://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Exporter)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
You've written a command-line program, not just a module, and you want to make
sure that it compiles, runs and has valid POD embedded.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.10-2mdv2011.0
+ Revision: 658454
- rebuild for updates rpm-setup

* Sat May 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2010.0
+ Revision: 378932
- import perl-Test-Program


* Sat May 23 2009 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist

