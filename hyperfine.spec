Name:           hyperfine
Version:        1.8.0
Release:        1%{?dist}
Summary:        A command-line benchmarking tool

License:        MIT or ASL 2.0
URL:            https://github.com/sharkdp/hyperfine
Source0:        https://github.com/sharkdp/hyperfine/archive/v%{version}.tar.gz

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires: /usr/bin/pathfix.py

%global _description %{expand:
A command-line benchmarking tool.}

%description %{_description}

%prep
%autosetup -n hyperfine-%{version} -p1
# Fix all Python shebangs recursively in .
# -p preserves timestamps
# -n prevents creating ~backup files
# -i specifies the interpreter for the shebang
# Need to list files that do not match ^[a-zA-Z0-9_]+\.py$ explicitly!
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/hyperfine
%{__install} -Dpm0755 -t %{buildroot}%{_datadir}/hyperfine/scripts scripts/*

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/hyperfine

%dir %{_datadir}/hyperfine
%dir %{_datadir}/hyperfine/scripts
%{_datadir}/hyperfine/scripts/*
	
%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 1.8.0-1
- Initial package build
