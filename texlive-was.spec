# revision 21439
# category Package
# catalog-ctan /macros/latex/contrib/was
# catalog-date 2011-02-15 10:33:56 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-was
Version:	20110215
Release:	1
Summary:	A collection of small packages by Walter Schmidt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/was
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/was.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/was.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/was.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A bundle of packages that arise in the author's area of
interest: - compliance of maths typesetting with ISO standards;
- symbols that work in both maths and text modes; - commas for
both decimal separator and maths; and - upright Greek letters
in maths.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/was/fixmath.sty
%{_texmfdistdir}/tex/latex/was/gensymb.sty
%{_texmfdistdir}/tex/latex/was/icomma.sty
%{_texmfdistdir}/tex/latex/was/upgreek.sty
%doc %{_texmfdistdir}/doc/latex/was/fixmath.pdf
%doc %{_texmfdistdir}/doc/latex/was/gensymb.pdf
%doc %{_texmfdistdir}/doc/latex/was/icomma.pdf
%doc %{_texmfdistdir}/doc/latex/was/readme.1st
%doc %{_texmfdistdir}/doc/latex/was/upgreek.pdf
#- source
%doc %{_texmfdistdir}/source/latex/was/fixmath.dtx
%doc %{_texmfdistdir}/source/latex/was/fixmath.ins
%doc %{_texmfdistdir}/source/latex/was/gensymb.dtx
%doc %{_texmfdistdir}/source/latex/was/gensymb.ins
%doc %{_texmfdistdir}/source/latex/was/icomma.dtx
%doc %{_texmfdistdir}/source/latex/was/icomma.ins
%doc %{_texmfdistdir}/source/latex/was/upgreek.dtx
%doc %{_texmfdistdir}/source/latex/was/upgreek.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
