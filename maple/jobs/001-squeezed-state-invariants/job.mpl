# Job 001 - Invariants of the squeezed inflationary state, exact and truncated
#
# Run:  maple -q job.mpl > ../../results/001-squeezed-state-invariants/RESULT.txt
#
# See JOB.md for what this computes and what a correct answer looks like.
# Blocks [1] and [2] are the pipeline check: if the Wronskian is not the
# constant I and DET_EXACT is not exactly 1/4, stop -- the job is wrong,
# not the papers.
#
# CONVENTION NOTE, the likeliest source of a wrong answer.
# We use the Mukhanov-Sasaki variable v with conformal time eta, and the
# canonical momentum p = dv/deta. On de Sitter with a = -1/(H*eta) the
# field redefinition has already absorbed the friction term, so p is the
# plain derivative and no (a'/a)*v subtraction appears. If the runner
# changes this, the Wronskian in block [1] will stop being constant and
# everything after it is meaningless.

with(LinearAlgebra):

# ---------------------------------------------------------------- setup
# Dimensionless time x = k*eta, with x < 0 during inflation and x -> 0-
# at late times (super-Hubble). Work in units hbar = 1 and scale out
# 1/sqrt(2k) so the Wronskian is clean.
#
# Exact de Sitter mode function, growing + decaying mode together:
v_exact  := (1 - I/x) * exp(-I*x);
# Momentum, p = dv/dx with the same scaling.
p_exact  := diff(v_exact, x);

# Vacuum normalisation is fixed by the Wronskian; N is the scaling we
# divide by so that W = I exactly.
Wsym := v -> simplify(expand(v * conjugate(diff(v,x)) - conjugate(v) * diff(v,x)));

# --------------------------------------------------------------- [1]
# Wronskian of the exact mode. For real x this must be a constant.
W_raw := simplify(evalc(Wsym(v_exact))) assuming x::real;
printf("[1] WRONSKIAN:        %a\n", W_raw);

# Normalisation constant that makes the Wronskian equal to I.
Nconst := simplify(sqrt(I/W_raw)) assuming x::real;
v0 := Nconst * v_exact;
p0 := diff(v0, x);

# ------------------------------------------------------- covariance
# Real symmetric covariance matrix of a Gaussian pure state built from a
# complex mode function: sigma = [[|v|^2, Re(v p*)],[Re(v p*), |p|^2]].
covmat := proc(vf, pf)
  local svv, spp, svp;
  svv := simplify(evalc(abs(vf)^2))                     assuming x::real;
  spp := simplify(evalc(abs(pf)^2))                     assuming x::real;
  svp := simplify(evalc(Re(vf * conjugate(pf))))        assuming x::real;
  return Matrix([[svv, svp],[svp, spp]]);
end proc:

sig_exact := covmat(v0, p0);

# --------------------------------------------------------------- [2]
# det(sigma) must be exactly 1/4, independent of x. This is the Wronskian
# identity restated, so it is forced, not discovered.
det_exact := simplify(Determinant(sig_exact)) assuming x::real;
printf("[2] DET_EXACT:        %a\n", det_exact);

# --------------------------------------------------------------- [3]
# Symplectic eigenvalues. For one mode these are both sqrt(det), so a pure
# state gives [1/2, 1/2].
sympeig := s -> simplify(sqrt(Determinant(s)));
printf("[3] SYMPEIG_EXACT:    %a\n", [sympeig(sig_exact), sympeig(sig_exact)]);

# ------------------------------------------------------ truncations
# The step the standard argument takes: keep the growing mode, drop the
# decaying one. Truncation order n keeps terms through x^(n-1) relative to
# the leading 1/x behaviour of v.
#
# n = 0 is the bare growing mode, which is what "set the decaying mode to
# zero" means literally.
# Built directly from the Laurent series of v0 about x = 0, keeping the
# leading term plus n corrections.
trunc_series := proc(n)
  local s, k, terms, lead;
  s := series(v0, x = 0, n + 3);
  lead := ldegree(convert(s, polynom), x);
  terms := add(coeff(convert(s, polynom), x, lead + k) * x^(lead + k), k = 0 .. n);
  return terms;
end proc:

printf("\n");
for n from 0 to 2 do
  vt := trunc_series(n);
  pt := diff(vt, x);
  st := covmat(vt, pt);
  dt := simplify(Determinant(st)) assuming x::real;
  printf("[4] DET_TRUNC(%d):     %a\n", n, dt);
  printf("[5] DELTA_RS(%d):      %a\n", n, simplify(dt - 1/4));
od;

# --------------------------------------------------------------- [6]
# Leading behaviour of the deficit at the order the literature uses.
# Reported as the first nonvanishing term in x and its sign.
printf("\n");
for n from 0 to 2 do
  vt := trunc_series(n);
  pt := diff(vt, x);
  st := covmat(vt, pt);
  d  := simplify(Determinant(st) - 1/4) assuming x::real;
  if simplify(d) = 0 then
    printf("[6] LEADING_ORDER(%d): exactly zero (purity restored)\n", n);
  else
    ser := series(d, x = 0, 4);
    printf("[6] LEADING_ORDER(%d): %a   (leading term of DELTA_RS)\n", n,
           convert(ser, polynom));
  fi;
od;

# ------------------------------------------------------------- check
# Independent check 2: the unsqueezed / vacuum limit. Taking |x| large
# sends the mode to the flat-space positive-frequency solution, whose
# covariance is the vacuum I/2 up to the rotation; det must still be 1/4.
printf("\n");
det_largex := simplify(limit(Determinant(sig_exact), x = -infinity)) assuming x::real;
printf("[CHECK] DET at large |x|: %a   expected 1/4\n", det_largex);

quit
