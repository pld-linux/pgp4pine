Summary:	A wrapper for Pine and GnuPG/PGP2/PGP5/PGP6
Name:		pgp4pine
Version:	1.76
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://pgp4pine.flatline.de/%{name}-%{version}.tar.gz
URL:		http://pgp4pine.flatline.de
Vendor:		Holger Lamm <holger@flatline.de>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A filter for Pine to encrypt/sign your Mail with PGP or GPG
%prep
%setup -q

%build
./configure --with-docdir=%{_prefix}/doc
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} docdir=$RPM_BUILD_ROOT%{_docdir} install
cp $RPM_BUILD_ROOT%{_docdir}/pgp4pine/* .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README FAQ PGP_MIME pgp4pinerc.example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%post
echo "ATTENTION! Installation is not yet complete."
echo "You must configure Pine to use pgp4pine !"
echo "Read %{_docdir}/pgp4pine/INSTALL to know how !"
