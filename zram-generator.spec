%define         pkgname         zram-generator
%global         forgeurl        https://github.com/systemd/%{pkgname}
Version:        0.2.0-rc.1

%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        swap-create@.service generator for zram devices
License:        MIT

URL:            %{forgeurl}
Source0:        %{forgesource}

%global         debug_package %{nil}

BuildRequires:  cargo >= 1.40
BuildRequires:  rust >= 1.40

BuildRequires:  llvm-devel
BuildRequires:  clang-devel

%global _description %{expand:
This generator provides a simple and fast mechanism to configure swap on /dev/zram* devices.}

%description %{_description}

%prep
%forgesetup

%build

%install
%make_install

%files
%license LICENSE
%doc README.md 

%{_systemdgeneratordir}/%{pkgname}
%{_unitdir}/swap-create@.service
%dir %{_datadir}/%{pkgname}/
%{_datadir}/%{pkgname}/zram-generator.conf.example

%{_mandir}/man5/%{pkgname}.conf.5*
%{_mandir}/man8/%{pkgname}.8*

%changelog
* Sun Jun 28 2020 zeno <zeno@bafh.org> 0.2.0-rc.1
- Initial package build
