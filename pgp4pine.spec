Summary:	A wrapper for Pine and GnuPG/PGP2/PGP5/PGP6
Summary(es.UTF-8):	Un filtro para el Pine y GnuPG/PGP2/PGP5/PGP6
Summary(pl.UTF-8):	Nakładka na Pine i GnuPG/PGP2/PGP5/PGP6
Summary(pt_BR.UTF-8):	Um filtro para o Pine e GnuPG/PGP2/PGP5/PGP6
Name:		pgp4pine
Version:	1.76
Release:	3
License:	GPL
Vendor:		Holger Lamm <holger@flatline.de>
Group:		Applications/Text
Source0:	http://pgp4pine.flatline.de/%{name}-%{version}.tar.gz
# Source0-md5:	235c44e0ef18dc3d0c78b3038c2ac56a
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-overflow.patch
URL:		http://pgp4pine.flatline.de/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	gnupg
Requires:	pine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A filter for Pine to encrypt/sign your Mail with PGP or GPG.

%description -l es.UTF-8
Un filtro para el Pine encriptar/assinar su correo electronico con PGP
o GPG.

%description -l pl.UTF-8
Filtr dla Pine umożliwiający podpisywanie/szyfrowanie poczty przy
użyciu PGP lub GPG.

%description -l pt_BR.UTF-8
Um filtro para o Pine encriptar/assinar seu correio eletrônico com PGP
ou GPG.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "ATTENTION! Installation is not yet complete."
echo "You must configure Pine to use pgp4pine!"
echo "Read %{_docdir}/%{name}-%{version}/INSTALL.gz to know how."

%files
%defattr(644,root,root,755)
%doc INSTALL README pgp4pine/docs/en/{FAQ,PGP_MIME}
%doc pgp4pine/docs/en/pgp4pinerc.example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
