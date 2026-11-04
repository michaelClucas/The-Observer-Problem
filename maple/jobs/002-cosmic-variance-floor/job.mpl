# Job 002 - The cosmic-variance floor, as a triage instrument
#
# Run:  maple -q job.mpl > ../../results/002-cosmic-variance-floor/RESULT.txt
#
# See JOB.md. Blocks [1]-[4] are the pipeline check and are textbook: if
# FRAC_ERR_CL is not sqrt(2/((2*l+1)*fsky)) then the degrees-of-freedom
# convention is wrong and blocks [5]-[8] are meaningless.
#
# CONVENTION NOTE. fsky multiplies the MODE COUNT, not the power spectrum.
# Partial sky coverage removes independent modes; it does not change Cl.
# Getting this backwards is the single likeliest error here.

with(Statistics):

assume(l::nonnegint, nu > 0, Cl > 0, fsky > 0, fsky <= 1, n_sigma > 0, lmax::posint):

# ---------------------------------------------------------------- [1][2]
# The estimator of Cl from one sky is chi-squared distributed:
#   nu * Chat_l / Cl  ~  chi^2(nu),   nu = (2*l+1)*fsky
# so everything follows from the chi-squared moments. Derive them from the
# distribution rather than quoting them, so the derivation is the check.
X := RandomVariable(ChiSquare(nu)):
chi2_mean := simplify(Mean(X));
chi2_var  := simplify(Variance(X));
printf("[1] CHI2_MEAN:        %a      expected nu\n",   chi2_mean);
printf("[2] CHI2_VAR:         %a      expected 2*nu\n", chi2_var);

# ---------------------------------------------------------------- [3][4]
# Chat_l = (Cl/nu) * X, so Var(Chat_l) = (Cl/nu)^2 * 2*nu = 2*Cl^2/nu.
nu_l      := (2*l + 1)*fsky;
var_cl    := simplify( (Cl/nu_l)^2 * subs(nu = nu_l, chi2_var) );
frac_err  := simplify( sqrt(var_cl)/Cl );
printf("[3] VAR_CL:           %a\n", var_cl);
printf("[4] FRAC_ERR_CL:      %a      expected sqrt(2/((2*l+1)*fsky))\n", frac_err);

# ------------------------------------------------------------------- [5]
# A one-point statistic on the sky -- the amplitude of a sky-averaged
# signal -- draws on the monopole only: a single mode, times fsky.
# Written generally so the plan can substitute a window.
nmodes_1pt := simplify(fsky * 1);
printf("\n[5] NMODES_1PT:       %a   (monopole only; one mode per sky)\n", nmodes_1pt);

# The variance of a one-point amplitude estimated against a field whose
# fluctuations have spectrum Cl: the fluctuation power that leaks into the
# monopole measurement, summed over the modes the window admits.
#   Var(A_1pt) = C_0 / (4*Pi*fsky)   for a full-sky monopole of a field
# with monopole power C_0. Keep C_0 symbolic as Cl at l = 0.
var_1pt := Cl/(4*Pi*fsky);
printf("    VAR_1PT:          %a\n", var_1pt);

# ------------------------------------------------------------------- [6]
# Minimum detectable one-point amplitude at n_sigma significance.
min_detect_1pt := simplify(n_sigma * sqrt(var_1pt));
printf("[6] MIN_DETECT_1PT:   %a\n", min_detect_1pt);

# The floor proper: best case is full sky.
printf("    MIN_DETECT_1PT at fsky=1: %a\n",
       simplify(subs(fsky = 1, min_detect_1pt)));

# ------------------------------------------------------------------- [7]
# Three-point: count closed triangles (l1,l2,l3) with each l_i <= lmax,
# satisfying the triangle inequality and the parity condition that
# l1+l2+l3 be even for a parity-even bispectrum.
#
# Done as an explicit nested sum so Maple produces a closed form in lmax
# rather than a number. If it will not close, the fallback printed below
# is the leading scaling, which is what the plan needs.
ntri := add(add(add(
            piecewise( (l1 + l2 >= l3) and (l2 + l3 >= l1) and (l3 + l1 >= l2)
                        and (type(l1 + l2 + l3, even)), 1, 0),
            l3 = 0 .. lmax), l2 = 0 .. lmax), l1 = 0 .. lmax):
ntri_closed := simplify(ntri);
printf("\n[7] NTRIANGLES:       %a\n", ntri_closed);
printf("    leading scaling in lmax: %a\n",
       simplify(asympt(ntri_closed, lmax, 2))) assuming lmax > 0;

# ------------------------------------------------------------------- [8]
# Bispectrum amplitude floor. With N independent triangle configurations
# each contributing comparable signal-to-noise, the amplitude error scales
# as 1/sqrt(N * fsky).
min_detect_3pt := simplify(n_sigma / sqrt(ntri_closed * fsky));
printf("[8] MIN_DETECT_3PT:   %a\n", min_detect_3pt);

# ----------------------------------------------------------------- check
# Independent check on [7]: for lmax = 2 the closed, parity-even triangles
# can be enumerated by hand. Print the brute-force count at small lmax so
# the closed form can be compared against it.
printf("\n[CHECK] NTRIANGLES brute force at small lmax:\n");
for L from 0 to 6 do
  cnt := add(add(add(
            piecewise( (a + b >= c) and (b + c >= a) and (c + a >= b)
                        and (type(a + b + c, even)), 1, 0),
            c = 0 .. L), b = 0 .. L), a = 0 .. L);
  printf("        lmax=%d: %a    closed form: %a\n", L, cnt,
         simplify(subs(lmax = L, ntri_closed)));
od;

quit
