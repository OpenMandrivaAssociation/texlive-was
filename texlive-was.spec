%global tl_name was
%global tl_revision 64691

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of small packages by Walter Schmidt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/was
License:	collection
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/was.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/was.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/was.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A bundle of packages that arise in the author's area of interest:
compliance of maths typesetting with ISO standards; symbols that work in
both maths and text modes commas for both decimal separator and maths;
and upright Greek letters in maths.

