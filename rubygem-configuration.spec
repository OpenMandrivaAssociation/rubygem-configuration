%define oname configuration
%define geminstdir %{ruby_gemdir}/gems/%{oname}-%{version}

Summary:    Pure ruby scoped configuration files
Name:       rubygem-%{oname}
Version:    1.1.0
Release:    2
Group:      Development/Ruby
License:    Ruby License
URL:        http://github.com/ahoward/configuration/tree/master
Source0:    http://gems.rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Pure ruby scoped configuration files

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/config/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/samples/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/configuration.gemspec
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.erb
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Nov 03 2010 Rémy Clouard <shikamaru@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 592991
- import rubygem-configuration

