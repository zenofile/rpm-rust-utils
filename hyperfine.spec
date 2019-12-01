%define         pkgname         hyperfine
%global         forgeurl        https://github.com/sharkdp/%{pkgname}
Version:        1.9.0

%forgemeta -i

Name:           %{pkgname}
Release:        2%{?dist}
Summary:        A command-line benchmarking tool
License:        MIT or ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires: /usr/bin/pathfix.py

%global _description %{expand:
A command-line benchmarking tool.}

%description %{_description}

%prep
%forgesetup
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" scripts/

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{pkgname}
%{__install} -Dpm0755 -t %{buildroot}%{_datadir}/%{pkgname}/scripts scripts/*

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}/scripts/*
	
%changelog
* Sun Dec 01 2019 zeno <zeno@bafh.org> 1.9.0-2
- Use forge macros
* Tue Nov 26 2019 zeno <zeno@bafh.org> 1.9.0-1
- Bump version to 1.9.0
* Sun Nov 24 2019 zeno <zeno@bafh.org> 1.8.0-1
- Initial package build
