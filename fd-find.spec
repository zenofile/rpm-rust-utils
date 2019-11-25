Name:           fd-find
Version:        7.4.0
Release:        2%{?dist}
Summary:        A simple, fast and user-friendly alternative to find(1) 

License:        MIT or ASL 2.0
URL:            https://github.com/sharkdp/fd
Source0:        https://github.com/sharkdp/fd/archive/v%{version}.tar.gz

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
%autosetup -n fd-%{version} -p1

%build
cargo install --root=%{buildroot}%{_prefix} --path=.

mv -vf target/release/build/fd-find-*/out/fd.bash   %{_tmppath}/completion.bash
mv -vf target/release/build/fd-find-*/out/_fd       %{_tmppath}/completion.zsh
mv -vf target/release/build/fd-find-*/out/fd.fish   %{_tmppath}/completion.fish

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir}         target/release/fd
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1    doc/fd.1

%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/fd-find %{_tmppath}/completion.bash
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/fd-find %{_tmppath}/completion.zsh
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/fd-find %{_tmppath}/completion.fish

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md 

%{_bindir}/fd
%{_mandir}/man1/fd.1*
%{_datadir}/fd-find

%triggerin -- bash-completion
ln -sf %{_datadir}/fd-find/completion.bash %{bash_completion_path}/fd

%triggerin -- zsh
ln -sf %{_datadir}/fd-find/completion.zsh %{zsh_completion_path}/_fd

%triggerin -- fish
ln -sf %{_datadir}/fd-find/completion.fish %{fish_completion_path}/fd.fish

%triggerun -- bash-completion
[ $2 -gt 0 ] && exit 0
rm -f %{bash_completion_path}/fd

%triggerun -- zsh
[ $2 -gt 0 ] && exit 0
rm -f %{zsh_completion_path}/_fd

%triggerun -- fish
[ $2 -gt 0 ] && exit 0
rm -f %{fish_completion_path}/fd.fish
	
%changelog
* Mon Nov 25 2019 zeno <zeno@bafh.org> 7.4.0-2
- use %trigger for linking files
* Mon Nov 25 2019 zeno <zeno@bafh.org> 7.4.0-1
- Initial package build
