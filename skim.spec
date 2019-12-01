%define         pkgname         skim
%define         binary          sk
%global         forgeurl        https://github.com/lotabout/%{pkgname}
Version:        0.6.9

%forgemeta -i

Name:           %{pkgname}
Release:        5%{?dist}
Summary:        Fuzzy Finder in rust! 
License:        MIT

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39

%global _description %{expand:
Half of our life is spent on navigation: files, lines, commands…
You need skim! It is a general fuzzy finder that saves you time.
It is blazingly fast as it reads the data source asynchronously.}
	
%define         zsh_completion_path     %{_datadir}/zsh/site-functions
%define         bash_completion_path    %{_datadir}/bash-completion/completions
%define         vim_plugin_path         %{_datadir}/vim/vimfiles/plugin

%description %{_description}

%prep
%forgesetup

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/%{binary}
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} bin/%{binary}-tmux

%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/%{binary}.1
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/%{binary}-tmux.1

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgname} plugin/%{pkgname}.vim

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgname} shell/completion.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgname} shell/completion.zsh

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgname} shell/key-bindings.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgname} shell/key-bindings.zsh
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/%{pkgname} shell/key-bindings.fish

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{binary}
%{_bindir}/%{binary}-tmux
%{_mandir}/man1/%{binary}.1*
%{_mandir}/man1/%{binary}-tmux.1*
%{_datadir}/%{pkgname}

%triggerin -- vim-filesystem
ln -sf %{_datadir}/%{pkgname}/%{pkgname}.vim %{vim_plugin_path}/%{pkgname}.vim 

%triggerin -- bash-completion
ln -sf %{_datadir}/%{pkgname}m/completion.bash %{bash_completion_path}/%{binary}

%triggerin -- zsh
ln -sf %{_datadir}/%{pkgname}m/completion.zsh %{zsh_completion_path}/_%{binary}

%triggerun -- bash-completion
[ $2 -gt 0 ] && exit 0
rm -f %{bash_completion_path}/%{binary}

%triggerun -- zsh
[ $2 -gt 0 ] && exit 0
rm -f %{zsh_completion_path}/_%{binary}

%triggerun -- vim-filesystem
[ $2 -gt 0 ] && exit 0
rm -f %{vim_plugin_path}/%{pkgname}m.vim

%changelog
* Sun Dec 01 2019 zeno <zeno@bafh.org> 0.6.9-5
- Use forge macros
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-4
- minor fixes
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-3
- minor fixes
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-2
- use %trigger for linking files
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-1
- Initial package build
