%define upstream_name	 forks
%define upstream_version 0.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.340.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.340.0-2mdv2011.0
+ Revision: 555480
- rebuild

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 551213
- update to 0.34

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.1
+ Revision: 505335
- rebuild using %%perl_convert_version

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 0.33-1mdv2010.0
+ Revision: 372064
- New version 0.33

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.23-6mdv2009.0
+ Revision: 257062
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.23-4mdv2008.1
+ Revision: 152084
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-3mdv2008.1
+ Revision: 136994
- rebuild
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Erwan Velu <erwan@mandriva.org>
    - 0.23
      Adding "yes no |" to answer automatic questions


* Mon Jun 26 2006 Erwan Velu <erwan@seanodes.com> 0.19-1
- 0.19
- Remove patch0 merged upstream (thx erik)

* Mon Mar 06 2006 Erwan Velu <erwan@seanodes.com> 0.18-2mdk
- Applying Eric Rybskej Patch to solve SIGCHLD troubles

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- 0.18
- Add provides perl(forks)

* Sun Dec 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-1mdk
- 0.17
- Fix permissions

* Tue Jul 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- Initial Mandriva release

