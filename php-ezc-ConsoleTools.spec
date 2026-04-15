%define		pearname	ConsoleTools
%define		php_min_version 5.4.0
Summary:	ConsoleTools - A set of classes to do different actions with the console (also called shell)
Name:		php-ezc-ConsoleTools
Version:	1.7.5
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://github.com/zetacomponents/ConsoleTools/archive/%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	81a6c475a27262ada43aa8e1e29c533d
URL:		https://github.com/zetacomponents/ConsoleTools
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php(core) >= %{php_min_version}
Requires:	php(iconv)
Requires:	php(pcre)
Requires:	php-ezc-Base >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of classes to do different actions with the console (also called
shell). It can render a progress bar, tables and a status bar and
contains a class for parsing command line options.

%prep
%setup -q -n %{pearname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/ezc/autoload
install -d $RPM_BUILD_ROOT%{php_pear_dir}/ezc/ConsoleTools
cp -a src/* $RPM_BUILD_ROOT%{php_pear_dir}/ezc/ConsoleTools
mv $RPM_BUILD_ROOT%{php_pear_dir}/ezc/ConsoleTools/console_autoload.php \
	$RPM_BUILD_ROOT%{php_pear_dir}/ezc/autoload/console_autoload.php

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a docs/example* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog LICENSE.txt
%{php_pear_dir}/ezc/autoload/console_autoload.php
%{php_pear_dir}/ezc/ConsoleTools
%{_examplesdir}/%{name}-%{version}
