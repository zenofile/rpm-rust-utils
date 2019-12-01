%define         pkgname         fd
%define         pkgfull         %{pkgname}-find
%global         forgeurl        https://github.com/sharkdp/%{pkgname}
Version:        7.4.0

%forgemeta -i

Name:           %{pkgname}-find
Release:        4%{?dist}
Summary:        A simple, fast and user-friendly alternative to find(1) 
License:        MIT or ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

BuildRequires:  llvm-devel
BuildRequires:  clang-devel

%define         fish_completion_path    %{_datadir}/fish/vendor_completions.d
%define         zsh_completion_path     %{_datadir}/zsh/site-functions
%define         bash_completion_path    %{_datadir}/bash-completion/completions

%global _description %{expand:
fd is a simple, fast and user-friendly alternative to find(1).
While it does not seek to mirror all of find's powerful functionality,
it provides sensible (opinionated) defaults for 80% of the use cases.}

%description %{_description}

%prep
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=. --color never

mv -vf target/release/build/%{pkgfull}-*/out/%{pkgname}.bash   %{_tmppath}/completion.bash
mv -vf target/release/build/%{pkgfull}-*/out/_%{pkgname}       %{_tmppath}/completion.zsh
mv -vf target/release/build/%{pkgfull}-*/out/%{pkgname}.fish   %{_tmppath}/completion.fish

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir}         target/release/%{pkgname}
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1    doc/%{pkgname}.1

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgfull} %{_tmppath}/completion.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgfull} %{_tmppath}/completion.zsh
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgfull} %{_tmppath}/completion.fish

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_datadir}/%{pkgfull}

%triggerin -- bash-completion
ln -sf %{_datadir}/%{pkgfull}/completion.bash %{bash_completion_path}/%{pkgname}

%triggerin -- zsh
ln -sf %{_datadir}/%{pkgfull}/completion.zsh %{zsh_completion_path}/_%{pkgname}

%triggerin -- fish
ln -sf %{_datadir}/%{pkgfull}/completion.fish %{fish_completion_path}/%{pkgname}.fish

%triggerun -- bash-completion
[ $2 -gt 0 ] && exit 0
rm -f %{bash_completion_path}/%{pkgname}

%triggerun -- zsh
[ $2 -gt 0 ] && exit 0
rm -f %{zsh_completion_path}/_%{pkgname}

%triggerun -- fish
[ $2 -gt 0 ] && exit 0
rm -f %{fish_completion_path}/%{pkgname}.fish
	
%changelog
* Sun Dec 01 2019 zeno <zeno@bafh.org> 7.4.0-4
- Use forge macros
* Mon Nov 25 2019 zeno <zeno@bafh.org> 7.4.0-3
- minor fixes
* Mon Nov 25 2019 zeno <zeno@bafh.org> 7.4.0-2
- use %trigger for linking files
* Mon Nov 25 2019 zeno <zeno@bafh.org> 7.4.0-1
- Initial package build
