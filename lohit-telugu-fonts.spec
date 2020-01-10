%global fontname lohit-telugu
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.3
Release:        2%{?dist}
Summary:        Free Telugu font

Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Telugu truetype/opentype font.

%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-telugu.conf

%build
make %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README ChangeLog.old


%changelog
* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Resolved #950525

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Fri Nov 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-2
- Upstream release 2.5.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug 803563

* Wed Mar 28 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Wed Feb 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolved bug 640607

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Jul 27 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-14
- fixes bug 714557

* Fri Jul 15 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-13
- fixes bug 714560

* Fri Jul 15 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-12
- fixes bug 714563

* Thu Jun 30 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-11
- fixes bug 714561

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-10
- fixes bug 714562

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-9
- fixes bug 692368

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixes bug 673420

* Tue Aug 10 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- fixes bug 622682

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- fixes bug 578040

* Wed Dec 30 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixes bug 551317

* Mon Dec 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- corrected patch 

* Thu Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 548686, license field

* Wed Nov 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release
- bug fix 531201

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
