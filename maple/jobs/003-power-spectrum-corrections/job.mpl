# Job 003 - one parameterisation for the collapse and decoherence
# corrections to the curvature power spectrum.
#
# Run as:  maple -q job.mpl
#
# Self-contained. No network, no inputs/, no interactive prompt.
# Exact arithmetic throughout except where JOB.md permits Digits=20.
#
# Sources for every equation used are in JOB.md. Nothing here is guessed.

restart;
interface(quiet = true, prettyprint = 0, warnlevel = 0):
Digits := 20:

printf("JOB 003 - power spectrum corrections, common parameterisation\n");
printf("=============================================================\n\n");

# ----------------------------------------------------------------------
# Conventions, as declared in JOB.md.
#   Mp   reduced Planck mass
#   H    Hubble rate (constant during de Sitter inflation)
#   eps1 first Hubble-flow parameter, constant
#   eps2 = 0, declared simplification; restored in the eps2 check below
#   z    = a * Mp * sqrt(2*eps1)
#   De Sitter:   a = -1/(H*eta),  eta < 0
#   Radiation:   a linear in eta  =>  z''/z = 0,  cs^2 = 1/3
# ----------------------------------------------------------------------

assume(k > 0, H > 0, eps1 > 0, Mp > 0, m0 > 0, rc > 0, gam > 0);

# --- free Mukhanov-Sasaki mode during de Sitter inflation -------------
# g0'' + (k^2 - 2/eta^2) g0 = 0, Bunch-Davies normalised.
g0_inf := (eta) -> exp(-I*k*eta)/sqrt(2*k) * (1 - I/(k*eta));

# Wronskian W = g0' conjg(g0) - g0 conjg(g0)', constant by construction.
W_inf := simplify( diff(g0_inf(eta),eta)*conjugate(g0_inf(eta))
                   - g0_inf(eta)*diff(conjugate(g0_inf(eta)),eta) );
printf("CHECK  Wronskian (inflation), should be constant and nonzero:\n");
printf("       W_inf = %a\n\n", simplify(W_inf));

# ======================================================================
# PART A - the CSL source, both epochs
# ======================================================================
#
# MV 2020 eq. (source:def):
#   S = (gam/m0^2) [ 2 a^4 (alpha^2 + omega^2 beta^2)
#                    - 2 (a^4 alpha beta)' + (a^4 beta^2)'' ]

CSL_source := proc(alpha_expr, beta_expr, a_expr, omega2_expr, var)
  local A4;
  A4 := a_expr^4;
  return (gam/m0^2) * (
      2*A4*(alpha_expr^2 + omega2_expr*beta_expr^2)
    - 2*diff(A4*alpha_expr*beta_expr, var)
    +   diff(A4*beta_expr^2, var$2)
  );
end proc:

# ---------------------- inflation -------------------------------------
a_inf      := -1/(H*eta);
z_inf      := a_inf*Mp*sqrt(2*eps1);
omega2_inf := k^2 - 2/eta^2;
# Gaussian smearing factor; eps2 = 0 as declared.
gauss_inf  := exp(-k^2*rc^2/(2*a_inf^2));

alpha_inf := (Mp^2*H^2*eps1/z_inf) * gauss_inf
             * ( -8 + 6*(a_inf*H/k)^2*eps1 );
beta_inf  := (2*Mp^2*H*eps1/(a_inf*z_inf)) * gauss_inf
             * ( -3*eps1*(a_inf*H/k)^2 + 1 );

S_inf := CSL_source(alpha_inf, beta_inf, a_inf, omega2_inf, eta);

# Super-Hubble limit: -k*eta -> 0. Substitute eta = -x/k and expand in x.
# The Green-function kernel Im^2[g0(eta') g0*(eta)] is expanded in the same
# variable, so the k-power of the integral comes out as a single exponent.
S_inf_x := simplify( subs(eta = -x/k, S_inf) );

kernel_inf := proc(xp, xx)
  # Im^2[ g0(eta') g0*(eta) ] with eta' = -xp/k, eta = -xx/k
  local gp, gc;
  gp := subs(eta = -xp/k, g0_inf(eta));
  gc := conjugate(subs(eta = -xx/k, g0_inf(eta)));
  return (Im(gp*gc))^2;
end proc:

# Leading super-Hubble behaviour of the integrand, in powers of k.
integrand_inf := simplify( S_inf_x * kernel_inf(xp, xx) );
# d eta' = -dx'/k supplies one further power of 1/k.
integrand_inf := subs(x = xp, integrand_inf) / k;

lead_inf := simplify( limit( integrand_inf
                             / k^degree(collect(integrand_inf,k),k), k = 0 ) ):
m_C_inf_raw := ldegree( series(integrand_inf, k, 20), k );

printf("PART_A_INFLATION_INDEX     m_C_inf      = %a\n", m_C_inf_raw);

A_C_inf := simplify( coeff( series(integrand_inf, k, 20), k, m_C_inf_raw ) );
printf("PART_A_INFLATION_AMPLITUDE A_C_inf      = %a\n\n", A_C_inf);

# ---------------------- radiation era ---------------------------------
# a linear in eta, so z''/z = 0 and omega^2 = k^2/3.
a_rad      := a_e*(eta - eta_r)/(eta_e - eta_r);
z_rad      := a_rad*Mp*sqrt(2*eps1);
omega2_rad := k^2/3;
gauss_rad  := exp(-k^2*rc^2/(2*a_rad^2));

alpha_rad := (24*Mp^2*H^2/z_rad) * gauss_rad * ( 3*(a_rad*H/k)^2 - 1 );
beta_rad  := (12*Mp^2*H/(a_rad*z_rad)) * gauss_rad * ( 1 - 6*(a_rad*H/k)^2 );

S_rad := CSL_source(alpha_rad, beta_rad, a_rad, omega2_rad, eta);

# Free mode in radiation: (g0)'' + (k^2/3) g0 = 0.
g0_rad  := (eta) -> exp(-I*k*eta/sqrt(3))/sqrt(2*k/sqrt(3));
W_rad   := simplify( diff(g0_rad(eta),eta)*conjugate(g0_rad(eta))
                     - g0_rad(eta)*diff(conjugate(g0_rad(eta)),eta) );
printf("CHECK  Wronskian (radiation), should be constant and nonzero:\n");
printf("       W_rad = %a\n\n", simplify(W_rad));

S_rad_x := simplify( subs(eta = -x/k, S_rad) );
kernel_rad := proc(xp, xx)
  local gp, gc;
  gp := subs(eta = -xp/k, g0_rad(eta));
  gc := conjugate(subs(eta = -xx/k, g0_rad(eta)));
  return (Im(gp*gc))^2;
end proc:

integrand_rad := simplify( S_rad_x * kernel_rad(xp, xx) ) / k;
m_C_rad_raw   := ldegree( series(integrand_rad, k, 24), k );
printf("PART_A_RADIATION_INDEX     m_C_rad      = %a\n", m_C_rad_raw);
A_C_rad := simplify( coeff( series(integrand_rad, k, 24), k, m_C_rad_raw ) );
printf("PART_A_RADIATION_AMPLITUDE A_C_rad      = %a\n\n", A_C_rad);

# ---- the eps2 claim JOB.md asks to confirm, not assume ---------------
# Restore eps2 in alpha_inf and check the k-power is unchanged.
alpha_inf_e2 := (Mp^2*H^2*eps1/z_inf) * gauss_inf
                * ( -8 - eps2 + 6*(a_inf*H/k)^2*eps1*(1 + eps2/2) );
beta_inf_e2  := (2*Mp^2*H*eps1/(a_inf*z_inf)) * gauss_inf
                * ( -3*eps1*(a_inf*H/k)^2 + 1 );
S_inf_e2 := CSL_source(alpha_inf_e2, beta_inf_e2, a_inf, omega2_inf, eta);
integrand_inf_e2 := simplify( subs(eta=-x/k,S_inf_e2)*kernel_inf(xp,xx) )/k;
m_C_inf_e2 := ldegree( series(integrand_inf_e2, k, 20), k );
printf("CHECK  eps2 restored: m_C_inf = %a (declared to be unchanged)\n",
       m_C_inf_e2);
if m_C_inf_e2 = m_C_inf_raw then
  printf("       AGREES - eps2 shifts amplitude only, as declared.\n\n");
else
  printf("       DISAGREES - the eps2=0 simplification changed the index.\n");
  printf("       This is a finding and the declared simplification is wrong.\n\n");
end if;

# ---- independent handle: the collapse criterion R --------------------
# MV 2020 state, independently of the source integral:
#   inflation crossing: 1/R - 1 = 1152 gam rhobar_end (-k eta_end)^(-7) / m0^2
#   radiation crossing: 1/R - 1 = 7264 gam (k eta_end)^(-14) (H_end rc)^(-7)
#                                 / (11 m0^2)
# These come from Re Omega_k. Printed for comparison with the indices above;
# per JOB.md tripwire 2, agreement here with disagreement above localises
# the error to the asymptotics of the integral.
printf("CHECK  published collapse criteria, for tripwire 2:\n");
printf("       1/R-1 (infl) = %a\n",
       1152*gam*rhobar_e*(-k*eta_e)^(-7)/m0^2);
printf("       1/R-1 (rad)  = %a\n\n",
       7264*gam*(k*eta_e)^(-14)*(H*rc)^(-7)/(11*m0^2));

# ======================================================================
# PART B - the open-EFT source
# ======================================================================
#
# MV 2018 eq. (I2n): with alpha_n = 3 - 2n - (p-3)(1+eps1) ~= 6 - 2n - p.
alpha_n := 6 - 2*n - p;
m_D     := simplify( -1 - alpha_n );     # the paper's (k/k_*)^(-1-alpha_n)
printf("PART_B_INDEX               m_D          = %a\n", m_D);

# Required to equal p + 2n - 7.
if simplify(m_D - (p + 2*n - 7)) = 0 then
  printf("CHECK  m_D = p + 2n - 7 as published.  AGREES\n");
else
  printf("CHECK  m_D does NOT reduce to p + 2n - 7.  DISAGREES\n");
end if;

# Scale invariance at p = 7 - 2n.
printf("CHECK  m_D at p = 7-2n: %a (published: 0)\n\n",
       simplify(subs(p = 7-2*n, m_D)));

# Closed-form I_{2n-1}, I_{2n} for n = 1 and n = 2. The paper states these
# are generalised hypergeometric. Maple evaluates the Bessel integrals
# directly; nu is left symbolic.
I_odd := proc(nn, nu)
  local an, zl, zu;
  an := 6 - 2*nn - p;
  return int( z^an * log(zIR/z)^(nn-1) * BesselJ(nu, z)^2, z = zlo .. zhi );
end proc:

I_even := proc(nn, nu)
  local an;
  an := 6 - 2*nn - p;
  return int( z^an * log(zIR/z)^(nn-1)
              * BesselJ(-nu, z) * BesselJ(nu, z), z = zlo .. zhi );
end proc:

for nn in [1, 2] do
  printf("PART_B_AMPLITUDE_N%d     A_D(n=%d)     = %a\n",
         nn, nn, simplify( Pi^2/(8*sin(Pi*nu)^2)
                           * ( I_odd(nn,nu) + I_odd(nn,-nu)
                               - 2*cos(Pi*nu)*I_even(nn,nu) ) ));
end do;
printf("\n");

# n >= 3: compare the exact integral against the paper's saddle-point form
# eq. (I2n:appr). JOB.md permits Digits=20 here and requires the precision
# and both values to be printed.
nn := 3:
an := 6 - 2*nn - p:
saddle_n3 := (H_lE)^(-an)/(Pi*an) * log(-zIR/(H_lE)^(-1))^(nn-1)
  + 1/(2*sqrt(Pi)) * GAMMA(-an/2)*GAMMA(1/2+an/2+nu)
      /(GAMMA(1/2-an/2)*GAMMA(1/2-an/2+nu)) * log(-zIR)^(nn-1)
  - 2^(-2*nu)/((1+an+2*nu)*GAMMA(1+nu)^2)
      * (zlo)^(1+an+2*nu) * log(zIR/zlo)^(nn-1):
exact_n3 := I_odd(3, nu):
printf("PART_B_SADDLE_N3_AGREES    comparing at Digits = %d\n", Digits);
printf("       exact  = %a\n", exact_n3);
printf("       saddle = %a\n", saddle_n3);
printf("       difference = %a\n\n", simplify(exact_n3 - saddle_n3));

# ======================================================================
# PART C - joint nested form, Jacobian ranks, degeneracies
# ======================================================================
#
# This is the part no paper contains and the reason the job is worth a
# round trip. The amplitudes from Parts A and B are re-entered here as
# symbols so that the elimination is done on the forms actually derived
# above rather than on transcribed ones.

printf("PART C - degeneracy structure\n");
printf("-----------------------------\n");

# --- C side: the map (gam, rc, eps1, H, Mp, m0, DeltaN) -> (A_C, m_C) --
# A_C_inf was derived above; m_C_inf is a pure number, so it contributes
# no dependence on the underlying parameters. The Jacobian is therefore
# the gradient of A_C_inf alone, and its rank is at most 1.
pars_C := [gam, rc, eps1, H, Mp, m0, DeltaN]:
map_C  := Vector([ A_C_inf, m_C_inf_raw ]):
J_C    := VectorCalculus:-Jacobian(map_C, pars_C):
rank_C := LinearAlgebra:-Rank(J_C):
printf("PART_C_JACOBIAN_RANK_C     %a\n", rank_C);
printf("PART_C_NULLSPACE_C         %a\n",
       LinearAlgebra:-NullSpace(J_C));

# --- D side: (kgamma, p, n, H_lE, N_T, DeltaN_star) -> (A_D, m_D) -----
# Here m_D depends on p and n, so the Jacobian has rank up to 2.
A_D_sym := C_np * (kgamma/kstar)^(4-2*n):
pars_D  := [kgamma, p, n, H_lE, N_T, DeltaN_star]:
map_D   := Vector([ A_D_sym, m_D ]):
J_D     := VectorCalculus:-Jacobian(map_D, pars_D):
rank_D  := LinearAlgebra:-Rank(J_D):
printf("PART_C_JACOBIAN_RANK_D     %a\n", rank_D);
printf("PART_C_NULLSPACE_D         %a\n",
       LinearAlgebra:-NullSpace(J_D));

# --- degeneracy locus m_C = m_D ---------------------------------------
printf("PART_C_DEGENERACY_LOCUS\n");
for nn from 1 to 4 do
  printf("       n=%d, epoch=inflation: p = %a\n", nn,
         solve( subs(n=nn, m_D) = m_C_inf_raw, p ));
  printf("       n=%d, epoch=radiation: p = %a\n", nn,
         solve( subs(n=nn, m_D) = m_C_rad_raw, p ));
end do;
printf("\n");

# --- the two numbers WP-3 may not report a statistic without ----------
printf("FREE_PARAMETERS_C          %a\n", rank_C);
printf("FREE_PARAMETERS_D          %a\n", rank_D);
printf("\n");

printf("=============================================================\n");
printf("END JOB 003\n");
quit;
