%global tl_name pxpic
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Draw pixel pictures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pxpic
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With pxpic you draw pictures pixel by pixel. It was inspired by a lovely
post by Paulo Cereda, among other things (most notably a beautiful duck)
showcasing the use of characters from the Mario video games by Nintendo
in LaTeX.

