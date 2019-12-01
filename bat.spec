%define         pkgname         bat
%global         forgeurl        https://github.com/sharkdp/%{pkgname}
Version:        0.12.1

%forgemeta -i

Name:           %{pkgname}
Release:        5%{?dist}
Summary:        Cat(1) clone with wings
License:        MIT or ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires:  llvm-devel
BuildRequires:  clang-devel

%define         fish_completion_path    %{_datadir}/fish/vendor_completions.d

%global _description %{expand:
Cat(1) clone with wings.}

%description %{_description}

%prep
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{pkgname}
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 doc/%{pkgname}.1
%{__install} -Dpm0644 assets/completions/%{pkgname}.fish %{buildroot}%{_datadir}/%{pkgname}/completion.fish

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_datadir}/%{pkgname}

%triggerin -- fish
ln -sf %{_datadir}/%{pkgname}/completion.fish %{fish_completion_path}/%{pkgname}.fish

%triggerun -- fish
[ $2 -gt 0 ] && exit 0
rm -f %{fish_completion_path}/%{pkgname}.fish

%changelog
* Sun Dec 01 2019 zeno <zeno@bafh.org> 0.12.1-5
- Use forge macros
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-4
- Use trigger scriptlets
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-3
- Fix description
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-2
- Add manpage and shell completion
* Sun Nov 24 2019 zeno <zeno@bafh.org> 0.12.1-1
- Initial package build
