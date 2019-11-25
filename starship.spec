Name:           starship
Version:        0.26.4
Release:        3%{?dist}
Summary:        The cross-shell prompt for astronauts.

License:        ISC
URL:            https://github.com/starship/starship
Source0:        https://github.com/starship/starship/archive/v%{version}.tar.gz

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

%description
Starship is the minimal, blazing fast, and extremely customizable prompt for any shell!
The prompt shows information you need while you're working, while staying sleek and out of the way.

%prep
%autosetup -n starship-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/starship

%files
%{_bindir}/starship
%license LICENSE
%doc README.md docs/README.md

%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.26.4-3
- Initial package build
