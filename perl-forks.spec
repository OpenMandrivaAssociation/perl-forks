%define module	forks
%define name	perl-%{module}
%define version	0.23
%define	release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Drop-in replacement for Perl threads using fork()
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel, perl-reaper
Provides:	perl(forks)

%description
The "forks" pragma allows a developer to use threads without having to have
a threaded perl, or to even run 5.8.0 or higher.

%prep
%setup -q -n %{module}-%{version}

%build
find -type f | xargs chmod 644
yes no | %{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG README TODO VERSION
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/auto/%{module}/*
%{perl_vendorarch}/%{module}/*
%{perl_vendorarch}/threads/shared/*
%{_mandir}/*/*

