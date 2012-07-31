%define		status		stable
%define		pearname	Horde_Oauth
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde OAuth client/server
Name:		php-horde-Horde_Oauth
Version:	1.0.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	067baa0bc72927dba722bd479439a552
URL:		http://pear.horde.org/package/Horde_Oauth/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-hash
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Http < 2.0.0
Requires:	php-openssl
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an OAuth consumer <http://oauth.net> and OAuth
infrastruture, and in the future will provide an OAuth server.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Horde_Oauth/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Oauth
