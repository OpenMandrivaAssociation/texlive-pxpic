Name:		texlive-pxpic
Version:	61294
Release:	2
Summary:	Draw pixel pictures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pxpic
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpic.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpic.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With pxpic you draw pictures pixel by pixel. It was inspired by
a lovely post by Paulo Cereda, among other things (most notably
a beautiful duck) showcasing the use of characters from the
Mario video games by Nintendo in LaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pxpic
%{_texmfdistdir}/tex/latex/pxpic
%doc %{_texmfdistdir}/doc/latex/pxpic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
