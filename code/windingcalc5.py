"""
Winding Calculator. Check README for instructions and unit definitions.

    python winding_calculator_gui.py

PyQt5 for GUI:
    pip install PyQt5
"""

import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, RadioButtons, TextBox

# Constants

SQRT3 = math.sqrt(3)
COPPER_RESISTIVITY_20C = 1.724e-8   # ohm*m
COPPER_TEMP_COEFF = 0.00393         # per C
K_T_CONSTANT = 8.27                 
GRADE_LIST = ["N35", "N38", "N40", "N42", "N45", "N48", "N50", "N52"]
GRADE_BR = {"N35": 1.195, "N38": 1.235, "N40": 1.265, "N42": 1.30, "N45": 1.35, "N48": 1.395, "N50": 1.425, "N52": 1.455, } # Flux remanence
RING_MU_R = {"metal": 2000.0, "plastic": 1.0} # Permeability of steel can vs. plastic/3D printed rotor can

# Theme
# =======================================

BG = "#1a1a1e"
PANEL = "#25252b"
SLIDER_TRACK = "#33333b"
ACCENT = "#4fd1c5"
TEXT = "#e8e8ec"
SUBTEXT = "#9a9aa5"
RED = "#ff6b6b"
BLUE = "#5b9bd5"

# Equations
# =======================================

def awg_bare_diameter_mm(awg):
    return 0.127 * 92 ** ((36 - awg) / 39)

def awg_area_mm2(awg):
    d = awg_bare_diameter_mm(awg)
    return math.pi / 4 * d ** 2

def area_to_equivalent_awg(area_mm2):
    d_equiv = 2 * math.sqrt(area_mm2 / math.pi)
    return 36 - 39 * math.log(d_equiv / 0.127, 92)

def kv_from_turns(turns, k_constant):
    return k_constant / turns

def turns_from_kv(target_kv, k_constant):
    return k_constant / target_kv

def kt_from_kv(kv, k_t_constant=K_T_CONSTANT):
    return k_t_constant / kv

def strands_for_current(current_A, awg, current_density):
    required_area = current_A / current_density
    single_area = awg_area_mm2(awg)
    strands = math.ceil(required_area / single_area)
    total_area = strands * single_area
    actual_density = current_A / total_area
    return strands, total_area, actual_density

def resistance_per_meter(awg, strands=1, temp_C=20.0):
    rho = COPPER_RESISTIVITY_20C * (1 + COPPER_TEMP_COEFF * (temp_C - 20))
    area_m2 = awg_area_mm2(awg) * 1e-6 * strands
    return rho / area_m2

def slot_area_mm2(w_slot_inner, w_slot_outer, r_depth):
    return 0.5 * (w_slot_inner + w_slot_outer) * r_depth

def mean_turn_length_mm(w_tooth, l_stack, buildup_correction_mm=0.0):
    return 2 * (w_tooth + l_stack) + buildup_correction_mm

def bg_from_magnet(Br, Lm, mu_r, g):
    """Simplified magnetic-circuit Bg: magnet as MMF source in series
    with airgap reluctance, ignoring iron reluctance/leakage/saturation."""
    return Br * Lm / (Lm + mu_r * g)

def translate_current(terminal_current_A, teeth_per_phase, coil_connection, phase_connection):
    phase_current_A = terminal_current_A if phase_connection == "star" else terminal_current_A / SQRT3
    if coil_connection == "series":
        coil_current_A = phase_current_A
    else:
        coil_current_A = phase_current_A / teeth_per_phase
    return phase_current_A, coil_current_A

# UI
# ==========================

# Window + panels
fig = plt.figure(figsize=(12, 10))
fig.patch.set_facecolor(BG)
fig.suptitle("Analytical 3-Phase BLDC Construction Calculator", fontsize=12, fontweight="bold", color=TEXT)

FS_LABEL = 7.5
FS_HEADER = 8.5
FS_RADIO = 7
FS_RADIO_TITLE = 7
FS_SUMMARY = 8

#Panel formatting
def panel(x, y, w, h, label):
    box = mpatches.FancyBboxPatch(
        (x, y), w, h, transform=fig.transFigure,
        boxstyle="round,pad=0.006,rounding_size=0.012",
        linewidth=1, edgecolor="#3a3a42", facecolor=PANEL, zorder=0)
    fig.add_artist(box)
    fig.text(x + 0.012, y + h - 0.020, label, fontsize=FS_HEADER, fontweight="bold",
              color=ACCENT, va="top")
    return box

# UI constants
h = 0.024
gap = 0.005
step = h + gap
SLIDER_W = 0.18
TOP = 0.94
TERMINAL_CURRENT_DEFAULT = 8.0  # I_term

# Radio box formatting
def style_radio(radio):
    for lbl in radio.labels:
        lbl.set_color(TEXT)
        lbl.set_fontsize(FS_RADIO)

# Slider construction function
def build_slider_group(specs, x, top_y, step, height, width=SLIDER_W):
    sliders = {}
    for i, (key, disp, lo, hi, default, sstep) in enumerate(specs):
        ax_s = fig.add_axes([x, top_y - i * step, width, height])
        ax_s.set_facecolor(SLIDER_TRACK)
        s = Slider(ax_s, disp, lo, hi, valinit=default, valstep=sstep, color=ACCENT)
        s.label.set_color(TEXT)
        s.label.set_fontsize(FS_LABEL)
        s.valtext.set_color(TEXT)
        s.valtext.set_fontsize(FS_LABEL)
        sliders[key] = s
    return sliders

# WINDING BOX
WINDING_SPECS = [
    ("awg", "AWG", 18, 32, 26, 0.5),
    ("turns", "Turns / tooth", 5, 15, 9, 1),
    ("strands", "Strands / bundle", 1, 40, 5, 1),
    ("buildup_mm", "Buildup (mm)", 0, 10, 8.0, 0.1),
    ("pitch_factor", "Kp", 0.5, 1.0, 1.0, 0.001),
    ("skew_factor", "Ksk", 0.5, 1.0, 1.0, 0.001),
    ("kw", "Kd", 0.5, 1.0, 0.933, 0.001),
]
WINDING_X = 0.42
WINDING_TOP_Y = 0.813
WINDING_STEP = 0.02
WINDING_H = 0.017
elec_sliders = build_slider_group(WINDING_SPECS, WINDING_X, WINDING_TOP_Y, WINDING_STEP, WINDING_H)

# Construction box
CONSTRUCTION_SPECS = [
    ("stator_dia", "Stator diameter", 20.0, 150.0, 81.0, 0.5),
    ("l_stack", "Stack length", 2, 30, 10.0, 0.5),
    ("w_tooth", "Tooth width", 1, 15, 2.0, 0.1),
    ("r_depth", "Tooth depth", 2, 30, 8.0, 0.1),
    ("w_slot_in", "Slot width (inner)", 1, 15, 3.5, 0.1),
    ("w_slot_out", "Slot width (out)", 1, 20, 5.0, 0.1),
    ("stator_gap", "Tooth gap (edge)", 0.5, 15.0, 3.5, 0.1),
]
CONSTRUCTION_X = 0.125
CONSTRUCTION_TOP_Y = 0.813
CONSTRUCTION_STEP = 0.02
CONSTRUCTION_H = 0.017
geo_sliders = build_slider_group(CONSTRUCTION_SPECS, CONSTRUCTION_X, CONSTRUCTION_TOP_Y, CONSTRUCTION_STEP, CONSTRUCTION_H)

# Slot/poles RADIO BOX
row2_label_y = TOP - 6 * step - 0.010
fig.text(0.05, row2_label_y + 0.12, "Slots", fontsize=FS_HEADER - 1, color=SUBTEXT)
fig.text(0.05, row2_label_y + 0.10, "Poles", fontsize=FS_HEADER - 1, color=SUBTEXT)

# Series/parallel and star/delta RADIO BOX
row2_y = row2_label_y - 0.028
ax_coil_conn = fig.add_axes([0.37, row2_y + 0.11, 0.10, 0.05])
ax_coil_conn.set_facecolor(SLIDER_TRACK)
ax_coil_conn.set_title("Coil Path", fontsize=FS_RADIO_TITLE, color=SUBTEXT)
coil_conn_radio = RadioButtons(ax_coil_conn, ("series", "parallel"), activecolor=ACCENT)
style_radio(coil_conn_radio)

ax_phase_conn = fig.add_axes([0.50, row2_y + 0.11, 0.10, 0.05])
ax_phase_conn.set_facecolor(SLIDER_TRACK)
ax_phase_conn.set_title("Phase", fontsize=FS_RADIO_TITLE, color=SUBTEXT)
phase_conn_radio = RadioButtons(ax_phase_conn, ("star", "delta"), activecolor=ACCENT)
style_radio(phase_conn_radio)

ax_nslots = fig.add_axes([0.08, row2_y + 0.145, 0.085, h])
ax_nslots.set_facecolor(SLIDER_TRACK)
nslots_box = TextBox(ax_nslots, "", initial="36", color=SLIDER_TRACK, hovercolor=SLIDER_TRACK)
nslots_box.text_disp.set_color(TEXT)
ax_npoles = fig.add_axes([0.08, row2_y + 0.115, 0.085, h])
ax_npoles.set_facecolor(SLIDER_TRACK)
npoles_box = TextBox(ax_npoles, "", initial="42", color=SLIDER_TRACK, hovercolor=SLIDER_TRACK)
npoles_box.text_disp.set_color(TEXT)

# ROTOR TYPE: Inrunner vs outrunner
row3_y = row2_y - 0.055 - 0.02 - 0.06
ax_rotor = fig.add_axes([0.18, row3_y + 0.25, 0.12, 0.065])
ax_rotor.set_facecolor(SLIDER_TRACK)
ax_rotor.set_title("ROTOR TYPE", fontsize=FS_RADIO_TITLE, color=SUBTEXT)
rotor_type_radio = RadioButtons(ax_rotor, ("outrunner", "inrunner"), activecolor=ACCENT)
style_radio(rotor_type_radio)

# K source
k_mode_y = row3_y - 0.01 - 0.075
ax_k_mode = fig.add_axes([0.54, 0.6, 0.08, 0.0455])
ax_k_mode.set_facecolor(SLIDER_TRACK)
ax_k_mode.set_title("K source", fontsize=FS_RADIO_TITLE, color=SUBTEXT)
k_mode_radio = RadioButtons(ax_k_mode, ("empirical", "analytical"), activecolor=ACCENT)
k_mode_radio.set_active(1)  # default: ANALYTICAL
style_radio(k_mode_radio)

panel(0.345, 0.69, 0.285, 0.26, "WINDING")
panel(0.042, 0.69, 0.285, 0.26, "STATOR CONSTRUCTION")

# ROTOR BOX (renamed to FLUX CONFIG)
ROTOR_PANEL_BOTTOM = 0.51
ROTOR_PANEL_HEIGHT = 0.16
ROTOR_PANEL_TOP = ROTOR_PANEL_BOTTOM + ROTOR_PANEL_HEIGHT

ROTOR_X = 0.093
ROTOR_STEP = 0.0181
ROTOR_H = 0.014
ROTOR_GRADE_Y = ROTOR_PANEL_TOP - 0.045    
ROTOR_TOP_Y = ROTOR_GRADE_Y - ROTOR_STEP  

ax_grade = fig.add_axes([ROTOR_X + 0.03, ROTOR_GRADE_Y-0.01, SLIDER_W, ROTOR_H])
ax_grade.set_facecolor(SLIDER_TRACK)
grade_slider = Slider(ax_grade, "NdFeB Grade", 0, len(GRADE_LIST) - 1, valinit=3, valstep=1, color=ACCENT)
grade_slider.label.set_color(TEXT)
grade_slider.label.set_fontsize(FS_LABEL)
grade_slider.valtext.set_color(TEXT)
grade_slider.valtext.set_fontsize(FS_LABEL)
grade_slider.valtext.set_text(GRADE_LIST[3])

ROTOR_SPECS = [
    ("Lm", "Magnet thickness", 1.0, 6.0, 2.5, 0.1),
    ("magnet_width", "Magnet width", 1.0, 10.0, 4.6, 0.1),
    ("mu_r", "Mag permeability", 0.9, 1.3, 1.05, 0.01),
    ("t_ring", "Ring thickness", 0.5, 10.0, 2.0, 0.1),
    ("g", "Airgap length", 0.1, 2.0, 0.65, 0.05),
]
print(ROTOR_TOP_Y)
magnet_sliders = build_slider_group(ROTOR_SPECS, ROTOR_X + 0.03, 0.595, ROTOR_STEP, ROTOR_H)

#print(ROTOR_X)
ax_ring_mat = fig.add_axes([0.45, 0.6, 0.08, 0.0455])
ax_ring_mat.set_facecolor(SLIDER_TRACK)
ax_ring_mat.set_title("Rotor Ring Material", fontsize=6, color=SUBTEXT)
ring_material_radio = RadioButtons(ax_ring_mat, ("metal", "plastic"), activecolor=ACCENT)
for lbl in ring_material_radio.labels:
    lbl.set_color(TEXT)
    lbl.set_fontsize(6)

panel(0.042, ROTOR_PANEL_BOTTOM, 0.285, ROTOR_PANEL_HEIGHT, "MAGNETIC FLUX")

# RESULTS BOX
row4_bottom = 0.267
results_top = row4_bottom - 0.01
results_bottom = 0.025
panel(0.042, 0.257, 0.588, 0.235, "RESULTS")
text_ax = fig.add_axes([0.13, 0.3, 0.545, results_top - results_bottom - 0.045])
text_ax.axis("off")
summary_text = text_ax.text(0, 1.0, "", family="monospace", fontsize=FS_SUMMARY, va="top", color=TEXT)

# Charts
panel(0.6475, 0.63, 0.34, 0.32, "")
panel(0.6475, 0.26, 0.34, 0.352, "")
ax1 = fig.add_axes([0.7175, 0.675, 0.2496, 0.20])
ax2 = fig.add_axes([0.7175, 0.35, 0.2496, 0.20])
CHART_BG = "#242430"
for ax in (ax1, ax2):
    ax.set_facecolor(CHART_BG)

fig.text(0.65, 0.925, "Target KV", fontsize=FS_LABEL, color=SUBTEXT)
ax_target_kv = fig.add_axes([0.65, 0.895, 0.10, h])
ax_target_kv.set_facecolor(SLIDER_TRACK)
target_kv_box = TextBox(ax_target_kv, "", initial="100", color=SLIDER_TRACK, hovercolor=SLIDER_TRACK)
target_kv_box.text_disp.set_color(TEXT)

fig.text(0.65, 0.60, "Target Density (A/mm\u00b2)", fontsize=FS_LABEL, color=SUBTEXT)
ax_density_tgt = fig.add_axes([0.65, 0.57, 0.10, h])
ax_density_tgt.set_facecolor(SLIDER_TRACK)
density_tgt_box = TextBox(ax_density_tgt, "", initial="6", color=SLIDER_TRACK, hovercolor=SLIDER_TRACK)
density_tgt_box.text_disp.set_color(TEXT)

fig.text(0.80, 0.60, "Terminal Current (A)", fontsize=FS_LABEL, color=SUBTEXT)
ax_iterm = fig.add_axes([0.80, 0.57, 0.09, h])
ax_iterm.set_facecolor(SLIDER_TRACK)
iterm_box = TextBox(ax_iterm, "", initial="8", color=SLIDER_TRACK, hovercolor=SLIDER_TRACK)
iterm_box.text_disp.set_color(TEXT)

# Correction Factors
CORRECTIONS_SPECS = [
    ("op_temp", "Op. temp. (C)", 20.0, 150.0, 75.0, 1.0),
    ("k_sigma", "k_sigma (leakage)", 0.70, 1.0, 0.90, 0.001),
    ("k_const", "K (empirical)", 500, 1500, 900, 10),
]
CORRECTIONS_X = 0.425
CORRECTIONS_TOP_Y = 0.57
CORRECTIONS_STEP = 0.025
CORRECTIONS_H = 0.017
correction_sliders = build_slider_group(CORRECTIONS_SPECS, CORRECTIONS_X, CORRECTIONS_TOP_Y, CORRECTIONS_STEP, CORRECTIONS_H)

panel(0.345, 0.51, 0.286, 0.16, "CORRECTIONS")


def redraw(_=None):
    turns = elec_sliders["turns"].val
    awg = elec_sliders["awg"].val
    try:
        terminal_A = float(iterm_box.text)
    except ValueError:
        terminal_A = TERMINAL_CURRENT_DEFAULT
    try:
        density_tgt = float(density_tgt_box.text)
    except ValueError:
        density_tgt = 6.0
    strands = int(elec_sliders["strands"].val)
    k_const = correction_sliders["k_const"].val
    try:
        n_slots = int(nslots_box.text)
    except ValueError:
        n_slots = 36
    try:
        n_poles = int(npoles_box.text)
    except ValueError:
        n_poles = 42
    n_slots = max(3, n_slots)
    n_poles = max(2, n_poles)
    teeth_per_phase = max(1, n_slots // 3)
    pole_pairs = max(1, n_poles // 2)
    cogging_lcm = math.lcm(n_slots, n_poles)

    w_slot_in = geo_sliders["w_slot_in"].val
    w_slot_out = geo_sliders["w_slot_out"].val
    r_depth = geo_sliders["r_depth"].val
    w_tooth = geo_sliders["w_tooth"].val
    l_stack = geo_sliders["l_stack"].val
    buildup_mm = elec_sliders["buildup_mm"].val

    coil_connection = coil_conn_radio.value_selected
    phase_connection = phase_conn_radio.value_selected
    k_mode = k_mode_radio.value_selected

    kd = elec_sliders["kw"].val

    grade_idx = int(round(grade_slider.val))
    grade_idx = max(0, min(len(GRADE_LIST) - 1, grade_idx))
    grade_name = GRADE_LIST[grade_idx]
    grade_slider.valtext.set_text(grade_name)
    Br = GRADE_BR[grade_name]
    Lm = magnet_sliders["Lm"].val
    g_mm = magnet_sliders["g"].val
    mu_r = magnet_sliders["mu_r"].val

    magnet_width = magnet_sliders["magnet_width"].val
    stator_dia = geo_sliders["stator_dia"].val
    stator_gap = geo_sliders["stator_gap"].val
    op_temp = correction_sliders["op_temp"].val
    rotor_type = rotor_type_radio.value_selected

    if rotor_type == "outrunner":
        r_gap_derived = stator_dia / 2 + g_mm / 2
        rotor_dia = stator_dia + 2 * g_mm
    else:
        r_gap_derived = stator_dia / 2 - g_mm / 2
        rotor_dia = stator_dia - 2 * g_mm
    r_gap_mm = r_gap_derived

    t_pole = math.pi * rotor_dia / n_poles
    w_gap_rotor = t_pole - magnet_width
    alpha_i = magnet_width / t_pole
    sigma_r = (w_gap_rotor / g_mm) / (5 + w_gap_rotor / g_mm)
    Kcr = t_pole / (t_pole - sigma_r * w_gap_rotor)

    t_stator = math.pi * stator_dia / n_slots
    sigma_s = (stator_gap / g_mm) / (5 + stator_gap / g_mm)
    Kcs = t_stator / (t_stator - sigma_s * stator_gap)

    t_ring = magnet_sliders["t_ring"].val
    mu_r_ring = RING_MU_R[ring_material_radio.value_selected]
    g_backiron = t_ring / mu_r_ring

    g_prime = g_mm * Kcs * Kcr + g_backiron
    Br_temp = Br * (1 + (-0.0012) * (op_temp - 20))
    k_sigma = correction_sliders["k_sigma"].val

    Bg_tesla = alpha_i * k_sigma * bg_from_magnet(Br_temp, Lm, mu_r, g_prime)

    kp = elec_sliders["pitch_factor"].val
    ksk = elec_sliders["skew_factor"].val
    kw = kd * kp * ksk

    pole_area_mm2 = (2 * math.pi * r_gap_mm / n_poles) * l_stack
    flux_pole_wb = Bg_tesla * pole_area_mm2 * 1e-6
    sqrt3_factor = SQRT3 if phase_connection == "star" else 1.0
    k_analytical = (60 / (2 * math.pi)) / (sqrt3_factor * teeth_per_phase * kw * pole_pairs * flux_pole_wb)

    active_k = k_const if k_mode == "empirical" else k_analytical

    kv = kv_from_turns(turns, active_k)
    kt = kt_from_kv(kv)
    kv_other = kv * SQRT3 if phase_connection == "star" else kv / SQRT3
    other_label = "delta" if phase_connection == "star" else "star"

    try:
        target_kv = float(target_kv_box.text)
    except ValueError:
        target_kv = kv
    required_turns = turns_from_kv(target_kv, active_k) if target_kv > 0 else float("nan")

    phase_A, coil_A = translate_current(terminal_A, teeth_per_phase, coil_connection, phase_connection)
    auto_strands, auto_area, auto_density = strands_for_current(coil_A, awg, density_tgt)

    # Peak torque: tau = Kt * I_phase 
    # for star, phase_A = terminal_A, for delta phase_A = terminal_A/sqrt3
    peak_torque_Nm = kt * phase_A

    single_area = awg_area_mm2(awg)
    bundle_area = strands * single_area
    bundle_density = coil_A / bundle_area if bundle_area > 0 else 0
    equiv_awg = area_to_equivalent_awg(bundle_area)

    slot_area = slot_area_mm2(w_slot_in, w_slot_out, r_depth)
    mtl = mean_turn_length_mm(w_tooth, l_stack, buildup_mm)

    # Estimated copper length per phase
    copper_length_per_phase_mm = teeth_per_phase * turns * strands * mtl
    copper_length_per_phase_m = copper_length_per_phase_mm / 1000

    # KV CHART VISUAL
    ax1.clear()
    ax1.set_facecolor(CHART_BG)
    turns_range = list(range(5, 16))
    ax1.plot(turns_range, [kv_from_turns(t, active_k) for t in turns_range], marker="o", color=BLUE)
    ax1.scatter([turns], [kv], color=RED, marker="D", zorder=6, s=50, label="selected")
    if 5 <= required_turns <= 15:
        ax1.scatter([required_turns], [target_kv], color="#f2c94c", marker="*", zorder=6, s=100, label=f"target {target_kv:g}KV")
        ax1.legend(fontsize=6.5, loc="upper right", facecolor=PANEL, edgecolor=SUBTEXT, labelcolor=TEXT)

    ax1.set_xlabel("Turns per tooth", color=TEXT)
    ax1.set_ylabel("KV (RPM/V)", color=TEXT)
    ax1.set_title(f"Turns vs KV  \u2014  {turns:.0f}T \u2192 {kv:.1f} KV", fontsize=9, color=TEXT)
    ax1.tick_params(colors=TEXT)
    for spine in ax1.spines.values():
        spine.set_color(SUBTEXT)
    ax1.grid(True, alpha=0.25, color=SUBTEXT)

    # CURRENT CHART VISUAL
    ax2.clear()
    ax2.set_facecolor(CHART_BG)
    density_range = [d / 2 for d in range(4, 29)]
    ax2.plot(density_range, [strands_for_current(coil_A, awg, d)[0] for d in density_range], marker="o", color=BLUE)
    ax2.scatter([bundle_density], [strands], color=RED, marker="D", zorder=6, s=50, label="selected")
    ax2.scatter([density_tgt], [auto_strands], color="#f2c94c", marker="*", zorder=6, s=100, label=f"target density")

    ax2.set_xlabel("Current density (A/mm\u00b2)", color=TEXT)
    ax2.set_ylabel(f"Strands of {awg:g}AWG per coil", color=TEXT)
    ax2.set_title("Current density vs strand count", fontsize=9, color=TEXT)
    ax2.tick_params(colors=TEXT)
    for spine in ax2.spines.values():
        spine.set_color(SUBTEXT)
    leg = ax2.legend(fontsize=6.5, loc="upper right", facecolor=PANEL, edgecolor=SUBTEXT)
    for text in leg.get_texts():
        text.set_color(TEXT)
    ax2.grid(True, alpha=0.25, color=SUBTEXT)

    # Results TEXT
    lines = [
        "Rendering as: OUTRUNNER" if rotor_type == "outrunner" else "Rendering as: INRUNNER",
        f"N_SLOTS={n_slots}  N_POLES={n_poles}  TEETH/PH={teeth_per_phase}  "
        f"POLE_PAIRS={pole_pairs}  LCM={cogging_lcm}",
        f"K: emp={k_const:.0f}  analyt={k_analytical:.0f}  (using {k_mode})",
        f"KV: {kv:.1f} ({phase_connection})   Kt: {kt:.4f} N\u00b7m/A   "
        f"\u2192 {other_label}: KV~{kv_other:.1f}",
        f"Peak Torque @ {terminal_A:.1f}A term ({phase_A:.2f}A phase): {peak_torque_Nm:.4f} N\u00b7m",
        f"Target {target_kv:g}KV \u2192 needs {required_turns:.1f} turns (using {k_mode} K)", "",
        f"Bg: {grade_name} Br={Br:.2f}T, L_M={Lm:.1f}mm, g={g_mm:.2f}mm \u2192 Bg={Bg_tesla:.3f}T",
        f"Kcs={Kcs:.3f} Kcr={Kcr:.3f} \u2192 g'={g_prime:.3f}mm  |  alpha_i={alpha_i:.3f}",
        f"k_sigma={k_sigma:.3f}  |  Br@{op_temp:g}C={Br_temp:.3f}T",
        f"r_gap (derived)={r_gap_derived:.1f}mm ({rotor_type})  |  "
        f"ring: {ring_material_radio.value_selected} t={t_ring:.1f}mm mu_r={mu_r_ring:.0f} \u2192 g_backiron={g_backiron:.4f}mm", "",

        f"Kw = kd\u00d7kp\u00d7ksk = {kd:.3f}\u00d7{kp:.3f}\u00d7{ksk:.3f} = {kw:.3f}",
        f"Slot area: {slot_area:.2f} mm\u00b2   MTL: {mtl:.2f} mm",
        f"I_term\u2192phase\u2192coil: {terminal_A:.1f}\u2192{phase_A:.2f}\u2192{coil_A:.3f} A "
        f"({coil_connection}, {teeth_per_phase} teeth/ph)",
        f"Bundle: {strands}\u00d7{awg:g}AWG = {bundle_area:.2f}mm\u00b2 "
        f"(\u2248{equiv_awg:.1f}AWG) @ {bundle_density:.2f} A/mm\u00b2",
        f"Est. copper length/phase (incl. buildup): {copper_length_per_phase_m:.1f} m",
    ]

    r_coil = resistance_per_meter(awg, strands) * (turns * mtl / 1000)
    r_phase = teeth_per_phase * r_coil if coil_connection == "series" else r_coil / teeth_per_phase
    p_phase = phase_A ** 2 * r_phase
    p_motor = 3 * p_phase
    lines.append(f"R_ph: {r_phase*1000:.2f}m\u03a9  P_ph: {p_phase:.2f}W  P_motor: {p_motor:.2f}W")

    total_copper_area = bundle_area * turns
    fill_factor = total_copper_area / slot_area if slot_area > 0 else 0
    status = "OK" if fill_factor <= 0.42 else "TOO FULL"
    lines.append(f"Slot fill: {fill_factor:.1%}  ({status})")

    summary_text.set_text("\n".join(lines))
    fig.canvas.draw_idle()

# Redraw inputs
for s in elec_sliders.values():
    s.on_changed(redraw)
for s in geo_sliders.values():
    s.on_changed(redraw)
for s in magnet_sliders.values():
    s.on_changed(redraw)
for s in correction_sliders.values():
    s.on_changed(redraw)
grade_slider.on_changed(redraw)
coil_conn_radio.on_clicked(redraw)
phase_conn_radio.on_clicked(redraw)
k_mode_radio.on_clicked(redraw)
rotor_type_radio.on_clicked(redraw)
ring_material_radio.on_clicked(redraw)
nslots_box.on_submit(redraw)
npoles_box.on_submit(redraw)
target_kv_box.on_submit(redraw)
density_tgt_box.on_submit(redraw)
iterm_box.on_submit(redraw)

redraw()
plt.show()
