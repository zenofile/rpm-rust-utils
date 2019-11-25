Name:           skim
Version:        0.6.9
Release:        3%{?dist}
Summary:        Fuzzy Finder in rust! 

License:        MIT
URL:            https://github.com/lotabout/skim
Source0:        https://github.com/lotabout/skim/archive/v%{version}.tar.gz

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
%autosetup -n skim-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} target/release/sk
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} bin/sk-tmux

%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/sk.1
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/sk-tmux.1

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/skim plugin/skim.vim

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/skim shell/completion.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/skim shell/completion.zsh

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/skim shell/key-bindings.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/skim shell/key-bindings.zsh
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/skim shell/key-bindings.fish

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/sk
%{_bindir}/sk-tmux
%{_mandir}/man1/sk.1*
%{_mandir}/man1/sk-tmux.1*
%{_datadir}/skim

%triggerin -- vim-filesystem
ln -sf %{_datadir}/skim/skim.vim %{vim_plugin_path}/skim.vim 

%triggerin -- bash-completion
ln -sf %{_datadir}/skim/completion.bash %{bash_completion_path}/sk

%triggerin -- zsh
ln -sf %{_datadir}/skim/completion.zsh %{zsh_completion_path}/_sk

%triggerun -- bash-completion
[ $2 -gt 0 ] && exit 0
rm -f %{bash_completion_path}/sk

%triggerun -- zsh
[ $2 -gt 0 ] && exit 0
rm -f %{zsh_completion_path}/_sk

%triggerun -- vim-filesystem
[ $2 -gt 0 ] && exit 0
rm -f %{vim_plugin_path}/skim.vim

%changelog
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-3
- minor fixes
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-2
- use %trigger for linking files
* Mon Nov 25 2019 zeno <zeno@bafh.org> 0.6.9-1
- Initial package build
