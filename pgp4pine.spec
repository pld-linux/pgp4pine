Summary:	A wrapper for Pine and GnuPG/PGP2/PGP5/PGP6
Summary(es):	Un filtro para el Pine y GnuPG/PGP2/PGP5/PGP6
Summary(pl):	Nak³adka na Pine i GnuPG/PGP2/PGP5/PGP6
Summary(pt_BR):	Um filtro para o Pine e GnuPG/PGP2/PGP5/PGP6
Name:		pgp4pine
Version:	1.76
Release:	2
License:	GPL
Vendor:		Holger Lamm <holger@flatline.de>
Group:		Applications/Text
Source0:	http://pgp4pine.flatline.de/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://pgp4pine.flatline.de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	pine

%description
A filter for Pine to encrypt/sign your Mail with PGP or GPG.

%description -l es
Un filtro para el Pine encriptar/assinar su correo electronico con PGP
o GPG.

%description -l pl
Filtr dla Pine umo¿liwiaj±cy podpisywanie/szyfrowanie poczty przy
u¿yciu PGP lub GPG.

%description -l pt_BR
Um filtro para o Pine encriptar/assinar seu correio eletrônico com PGP
ou GPG.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-docdir=%{_datadir}/doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf INSTALL README pgp4pine/docs/en/{FAQ,PGP_MIME}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "ATTENTION! Installation is not yet complete."
echo "You must configure Pine to use pgp4pine!"
echo "Read %{_docdir}/%{name}-%{version}/INSTALL.gz to know how."

%files
%defattr(644,root,root,755)
%doc INSTALL.gz README.gz pgp4pine/docs/en/FAQ.gz pgp4pine/docs/en/PGP_MIME.gz
%doc pgp4pine/docs/en/pgp4pinerc.example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
