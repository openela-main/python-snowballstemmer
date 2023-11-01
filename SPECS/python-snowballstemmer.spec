%global pypi_name snowballstemmer

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        6%{?dist}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/20/6b/d2a7cb176d4d664d94a6debf52cd8dbae1f7203c8e42426daa077051d59c/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-devel
%endif # with python2
BuildRequires:  python3-devel

%description
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.


%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms
BuildArch:      noarch
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.
%endif # with python2


%package -n     python3-%{pypi_name}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.


%prep
%setup -qn %{pypi_name}-%{version}
# Remove upstream's egg-info
rm -rf %{pypi_name}.egg-info


%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build


%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install


%check
# No tests

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{pypi_name}/
%endif # with python2

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/


%changelog
* Thu Jun 14 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.2.1-6
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.2.1-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 1.2.1-1
- Update to 1.2.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.2.0-2
- Rebuilt for python 3.5

* Mon Aug 24 2015 Julien Enselme <jujens@jujens.eu> - 1.2.0-1
- Initial package
