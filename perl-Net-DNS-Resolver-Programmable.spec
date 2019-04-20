#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-DNS-Resolver-Programmable
Version  : 0.009
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Net-DNS-Resolver-Programmable-0.009.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Net-DNS-Resolver-Programmable-0.009.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-dns-resolver-programmable-perl/libnet-dns-resolver-programmable-perl_0.009-1.debian.tar.xz
Summary  : 'programmable DNS resolver class for offline emulation of DNS'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Net-DNS-Resolver-Programmable-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Net::DNS)

%description
NAME
Net::DNS::Resolver::Programmable - programmable DNS resolver class for
offline emulation of DNS

%package dev
Summary: dev components for the perl-Net-DNS-Resolver-Programmable package.
Group: Development
Provides: perl-Net-DNS-Resolver-Programmable-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-DNS-Resolver-Programmable package.


%package license
Summary: license components for the perl-Net-DNS-Resolver-Programmable package.
Group: Default

%description license
license components for the perl-Net-DNS-Resolver-Programmable package.


%prep
%setup -q -n Net-DNS-Resolver-Programmable-0.009
cd ..
%setup -q -T -D -n Net-DNS-Resolver-Programmable-0.009 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-DNS-Resolver-Programmable-0.009/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-DNS-Resolver-Programmable
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-DNS-Resolver-Programmable/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Net/DNS/Resolver/Programmable.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::DNS::Resolver::Programmable.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-DNS-Resolver-Programmable/LICENSE
