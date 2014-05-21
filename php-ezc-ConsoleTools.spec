%define		status		stable
%define		pearname	ConsoleTools
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A set of classes to do different actions with the console (also called shell)
Name:		php-ezc-ConsoleTools
Version:	1.6.1
Release:	3
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://components.ez.no/get/%{pearname}-%{version}.tgz
# Source0-md5:	987783f590fc3a75fbf3c2e19818b2a4
URL:		http://components.ez.no/package/ConsoleTools/
BuildRequires:	php-channel(components.ez.no)
BuildRequires:	php-pear-PEAR >= 1:1.4.2
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php(core) >= %{php_min_version}
Requires:	php(iconv)
Requires:	php(pcre)
Requires:	php-channel(components.ez.no)
Requires:	php-ezc-Base >= 1.8
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of classes to do different actions with the console (also called
shell). It can render a progress bar, tables and a status bar and
contains a class for parsing command line options.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

install -d examples
mv docs/ConsoleTools/docs/img examples
mv docs/ConsoleTools/docs/example* examples
mv docs/ConsoleTools/docs/tutorial* examples
mv docs/ConsoleTools/docs/* .

# design docs
mv .%{php_pear_dir}/data/ConsoleTools/design .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE install.log design
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/ezc/autoload/console_autoload.php
%{php_pear_dir}/ezc/ConsoleTools
%{_examplesdir}/%{name}-%{version}
