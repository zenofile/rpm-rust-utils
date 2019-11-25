Name:           bat
Version:        0.12.1
Release:        3%{?dist}
Summary:        Cat(1) clone with wings

License:        MIT or ASL 2.0
URL:            https://github.com/sharkdp/bat
Source0:        https://github.com/sharkdp/bat/archive/v%{version}.tar.gz

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires:  llvm-devel
BuildRequires:  clang-devel

%global _description %{expand:
Cat(1) clone with wings.}

%description %{_description}

%prep
%autosetup -n bat-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/bat
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 doc/bat.1
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d assets/completions/bat.fish

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/bat
%{_mandir}/man1/bat.1*

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/bat.fish
	
%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-3
- Fix description
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-2
- Add manpage and shell completion
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-1
- Initial package build
