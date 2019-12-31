%define         pkgname         mdcat
%global         forgeurl        https://github.com/lunaryorn/%{pkgname}
Version:        0.16.0
%global         tag             %{pkgname}-%{version}


%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Cat(1) for Markdown
License:        MIT or ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}

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
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{pkgname}

%files
%license LICENSE
%doc README.md 

%{_bindir}/%{pkgname}

%changelog
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.13.0-1
- Initial package build
