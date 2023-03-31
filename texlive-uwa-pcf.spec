Name:		texlive-uwa-pcf
Version:	64491
Release:	2
Summary:	A Participant Consent Form (PCF) for a human research protocol at the University of Western Australia
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uwa-pcf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pcf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pcf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pcf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX class generates a Participant Consent Form (PCF) for
a human research protocol at the University of Western
Australia. It requires the UWA logo in PDF format, which is
available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Arial and UWA Slab fonts by
default. The class works with XeLaTeX and LuaLaTeX. It depends
on the uwa-letterhead package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uwa-pcf
%{_texmfdistdir}/tex/latex/uwa-pcf
%doc %{_texmfdistdir}/doc/latex/uwa-pcf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
