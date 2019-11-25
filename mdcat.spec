Name:           mdcat
Version:        0.13.0
Release:        1%{?dist}
Summary:        Cat(1) for Markdown

License:        MIT or ASL 2.0
URL:            https://github.com/lunaryorn/mdcat
Source0:        https://github.com/lunaryorn/mdcat/archive/mdcat-%{version}.tar.gz

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires:  llvm-devel
BuildRequires:  clang-devel

BuildRequires:  pkgconfig(openssl)

%global _description %{expand:
Cat(1) for Markdown.}

%description %{_description}

%prep
%autosetup -n mdcat-mdcat-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/mdcat

%files
%license LICENSE
%doc README.md 

%{_bindir}/mdcat

%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.13.0-1
- Initial package build
