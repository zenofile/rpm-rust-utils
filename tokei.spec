Name:           tokei
Version:        10.1.0
Release:        1%{?dist}
Summary:        Count your code, quickly.

License:        MIT or ASL 2.0
URL:            https://github.com/XAMPPRocky/tokei
Source0:        https://github.com/XAMPPRocky/tokei/archive/v%{version}.tar.gz

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

%global _description %{expand:
Tokei is a program that displays statistics about your code.
Tokei will show number of files, total lines within those files and code,
comments, and blanks grouped by language.}

%description %{_description}

%prep
%autosetup -n tokei-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --features all

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/tokei

%files
%license LICENCE-MIT LICENCE-APACHE
%doc README.md 

%{_bindir}/tokei
	
%changelog
* Sun Nov 26 2019 zeno <zeno@bafh.org> 10.1.0-1
- Initial package build
