Summary:	A wrapper for Pine and GnuPG/PGP2/PGP5/PGP6
Summary(es):	Un filtro para el Pine y GnuPG/PGP2/PGP5/PGP6
Summary(pt_BR):	Um filtro para o Pine e GnuPG/PGP2/PGP5/PGP6
Name:		pgp4pine
Version:	1.76
Release:	1
License:	GPL
Vendor:		Holger Lamm <holger@flatline.de>
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://pgp4pine.flatline.de/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://pgp4pine.flatline.de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A filter for Pine to encrypt/sign your Mail with PGP or GPG.

%description -l es
Un filtro para el Pine encriptar/assinar su correo electronico con PGP
o GPG.

%description -l pt_BR
Um filtro para o Pine encriptar/assinar seu correio eletr�nico com PGP
ou GPG.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--with-docdir=%{_datadir}/doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#cp $RPM_BUILD_ROOT%{_docdir}/pgp4pine/* .

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
