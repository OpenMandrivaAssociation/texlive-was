# revision 21439
# category Package
# catalog-ctan /macros/latex/contrib/was
# catalog-date 2011-02-15 10:33:56 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-was
Version:	20110215
Release:	8
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

%description
A bundle of packages that arise in the author's area of
interest: - compliance of maths typesetting with ISO standards;
- symbols that work in both maths and text modes; - commas for
both decimal separator and maths; and - upright Greek letters
in maths.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110215-2
+ Revision: 757499
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110215-1
+ Revision: 719903
- texlive-was
- texlive-was
- texlive-was

