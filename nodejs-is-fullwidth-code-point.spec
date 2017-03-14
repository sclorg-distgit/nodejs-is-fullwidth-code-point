%{?scl:%scl_package nodejs-is-fullwidth-code-point}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename is-fullwidth-code-point
%global enable_tests 0
# tests disabed until 'ava' is packaged for Fedora

Name:		%{?scl_prefix}nodejs-is-fullwidth-code-point
Version:	1.0.0
Release:	2%{?dist}
Summary:	Check if given Unicode code point is fullwidth

License:	MIT
URL:		https://github.com/sindresorhus/is-fullwidth-code-point
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/sindresorhus/is-fullwidth-code-point/v%{version}/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
BuildRequires:	%{?scl_prefix}npm(number-is-nan)
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(ava)
BuildRequires:	%{?scl_prefix}npm(code-point-at)
%endif

%description
Check if the character represented by a given Unicode code point is fullwidth

%prep
%setup -q -n package
# setup the tests
cp -r %{SOURCE1} .

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#%{__nodejs} test.js
#%else
#%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Built for RHSCL

* Tue Feb 23 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
