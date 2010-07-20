%define upstream_name	 forks
%define upstream_version 0.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Drop-in replacement for Perl threads using fork()
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Reaper)

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Provides:	perl(forks)

%description
The "forks" pragma allows a developer to use threads without having to have
a threaded perl, or to even run 5.8.0 or higher.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
find -type f | xargs chmod 644
yes no | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

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
%{perl_vendorarch}/%{upstream_name}.pm
%{perl_vendorarch}/auto/%{upstream_name}/*
%{perl_vendorarch}/%{upstream_name}/*
%{perl_vendorarch}/threads/shared/*
%{_mandir}/*/*
