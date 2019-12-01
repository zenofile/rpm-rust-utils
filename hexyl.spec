%define         pkgname         hexyl
%global         forgeurl        https://github.com/sharkdp/%{pkgname}
Version:        0.6.0

%forgemeta -i

Name:           %{pkgname}
Release:        2%{?dist}
Summary:        A command-line hex viewer
License:        MIT or ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

%global _description %{expand:
hexyl is a simple hex viewer for the terminal.
It uses a colored output to distinguish different categories of bytes
(NULL bytes, printable ASCII characters, ASCII whitespace characters,
other ASCII characters and non-ASCII)..}

%description %{_description}

%prep
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{pkgname}

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/%{pkgname}
	
%changelog
* Sun Dec 01 2019 zeno <zeno@bafh.org> 0.6.0-2
- Use forge macros
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.6.0-1
- Initial package build
