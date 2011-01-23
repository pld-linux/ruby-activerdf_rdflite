Summary:	ActiveRDF adaptor for RDFLite bindings
Name:		ruby-activerdf_rdflite
Version:	1.4.1
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/activerdf_rdflite-%{version}.gem
# Source0-md5:	3c5efda7f5de7c8e7e803e60cb3c1988
URL:		http://activerdf.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.4.1
Requires:	rdflite-bindings-ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ActiveRDF adaptor for RDFLite bindings.

%prep
%setup -q -c -n activerdf-%{version}
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm ri/created.rid
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/activerdf_rdflite*
%{ruby_ridir}/*
