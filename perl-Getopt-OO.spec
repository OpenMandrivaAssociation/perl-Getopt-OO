%define upstream_name    Getopt-OO
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An object oriented command line parser.  It handles
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Getopt::OO is an object oriented tool for parsing command line arguments.
It expects a reference to the input arguments and uses a perl hash to
describe how the command line arguments should be parsed. Note that by
parsed, we mean what options expect values, etc. We check to make sure
values exist on the command line as necessary -- nothing else. The caller
is responsible for making sure that a value that he knows should be a file
exists, is writable, or whatever.

Command line arguments can be broken into two distinct types: options and
values that are associated with these options. In windows, options often
start with a '/' but sometimes with a '-', but in unix they almost
universally start with a '-'. For this module options start with a '-'. We
support two types of options: the short single dashed options and the long
double dashed options. The difference between these two is that with this
module the short options can be combined into a single option, but the long
options can not. For example, most of us will be familiar with the 'tar
-xvf file' command which can also be expressed as '-x -v -f file'. Long
options can not be combined this way, so '--help' for example must always
stand by itself.

The input template expects the option names as its keys. For instance if
you were expecting '-xv --hello' as possible command line options, the keys
for your template hash would be '-x', '-v', and '--hello'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 654196
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 401656
- rebuild using %%perl_convert_version
- fixed license field

* Fri Jan 30 2009 Olivier Thauvin <nanardon@mandriva.org> 0.07-1mdv2009.1
+ Revision: 335604
- import perl-Getopt-OO


* Fri Jan 30 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist

