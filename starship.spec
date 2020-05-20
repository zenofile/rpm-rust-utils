%define         pkgname         starship
%global         forgeurl        https://github.com/%{pkgname}/%{pkgname}
Version:        0.42.0

%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        The cross-shell prompt for astronauts.
License:        ISC

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires:  pkgconfig(openssl)

%description
Starship is the minimal, blazing fast, and extremely customizable prompt for any shell!
The prompt shows information you need while you're working, while staying sleek and out of the way.

%prep
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{pkgname}

%files
%{_bindir}/%{pkgname}
%license LICENSE
%doc README.md docs/README.md

%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.26.4-3
- Initial package build
