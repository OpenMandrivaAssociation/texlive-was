Name:		texlive-was
Version:	64691
Release:	2
Summary:	A collection of small packages by Walter Schmidt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/was
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/was.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/was.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/was.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A bundle of packages that arise in the author's area of
interest: - compliance of maths typesetting with ISO standards;
- symbols that work in both maths and text modes; - commas for
both decimal separator and maths; and - upright Greek letters
in maths.

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/was
%doc %{_texmfdistdir}/doc/latex/was
#- source
%doc %{_texmfdistdir}/source/latex/was

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
