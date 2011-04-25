%define module   Test-Program
%define version    0.10
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Testing tools for Perl programs
Url:        http://search.cpan.org/dist/%{module}
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

