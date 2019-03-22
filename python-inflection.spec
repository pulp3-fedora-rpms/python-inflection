# Created by pyp2rpm-3.3.2
%global pypi_name inflection

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        A port of Ruby on Rails inflector to Python

License:        MIT
URL:            http://github.com/jpvanhal/inflection
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# Manually added dependencies so it builds successfully
BuildRequires:  python3dist(pytest)

%description
Inflection |build status|_.. |build statu .. _build status: is a string
transformation library. It singularizes and pluralizes English words, and
transforms strings from CamelCase to underscored string. Inflection is a port
of Ruby on Rails_' inflector_ to Python... _Ruby on Rails: .. _inflector: -
Documentation < - Issue Tracker <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Inflection |build status|_.. |build statu .. _build status: is a string
transformation library. It singularizes and pluralizes English words, and
transforms strings from CamelCase to underscored string. Inflection is a port
of Ruby on Rails_' inflector_ to Python... _Ruby on Rails: .. _inflector: -
Documentation < - Issue Tracker <


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.3.1-1
- Initial package.
