%define         pkgname         tokei
%global         forgeurl        https://github.com/XAMPPRocky/%{pkgname}
Version:        10.1.0

%forgemeta -i

Name:           %{pkgname}
Release:        2%{?dist}
Summary:        Count your code, quickly.
License:        MIT or ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

%global _description %{expand:
Tokei is a program that displays statistics about your code.
Tokei will show number of files, total lines within those files and code,
comments, and blanks grouped by language.}

%description %{_description}

%prep
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never --features all

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{pkgname}

%files
%license LICENCE-MIT LICENCE-APACHE
%doc README.md 

%{_bindir}/%{pkgname}
	
%changelog
* Sun Dec 01 2019 zeno <zeno@bafh.org> 10.1.0-2
- Use forge macros
* Sun Nov 26 2019 zeno <zeno@bafh.org> 10.1.0-1
- Initial package build
