Name:           hexyl
Version:        0.6.0
Release:        1%{?dist}
Summary:        A command-line hex viewer

License:        MIT or ASL 2.0
URL:            https://github.com/sharkdp/hexyl
Source0:        https://github.com/sharkdp/hexyl/archive/v%{version}.tar.gz

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
%autosetup -n hexyl-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/hexyl

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/hexyl
	
%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.6.0-1
- Initial package build
