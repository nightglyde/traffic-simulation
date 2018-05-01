from util import *
from road_network import Road, IntersectionRoad, Intersection

interroad_a = IntersectionRoad(Vector(101.6, 55.25), Vector(62.4, 55.25))
interroad_b = IntersectionRoad(Vector(62.4, 51.75), Vector(101.6, 51.75))
interroad_c = IntersectionRoad(Vector(101.6, 112.25), Vector(62.4, 112.25))
interroad_d = IntersectionRoad(Vector(62.4, 108.75), Vector(101.6, 108.75))
interroad_e = IntersectionRoad(Vector(51.75, 101.6), Vector(51.75, 62.4))
interroad_f = IntersectionRoad(Vector(55.25, 62.4), Vector(55.25, 101.6))
interroad_g = IntersectionRoad(Vector(108.75, 101.6), Vector(108.75, 62.4))
interroad_h = IntersectionRoad(Vector(112.25, 62.4), Vector(112.25, 101.6))
interroad_i = IntersectionRoad(Vector(5.4, 51.75), Vector(44.6, 51.75))
interroad_j = IntersectionRoad(Vector(158.6, 112.25), Vector(119.4, 112.25))
interroad_k = IntersectionRoad(Vector(5.4, 108.75), Vector(44.6, 108.75))
interroad_l = IntersectionRoad(Vector(158.6, 55.25), Vector(119.4, 55.25))
interroad_m = IntersectionRoad(Vector(55.25, 5.4), Vector(55.25, 44.6))
interroad_n = IntersectionRoad(Vector(108.75, 158.6), Vector(108.75, 119.4))
interroad_o = IntersectionRoad(Vector(112.25, 5.4), Vector(112.25, 44.6))
interroad_p = IntersectionRoad(Vector(51.75, 158.6), Vector(51.75, 119.4))
road_q = Road(Vector(44.6, 55.25), Vector(5.4, 55.25))
road_r = Road(Vector(119.4, 108.75), Vector(158.6, 108.75))
road_s = Road(Vector(44.6, 112.25), Vector(5.4, 112.25))
road_t = Road(Vector(119.4, 51.75), Vector(158.6, 51.75))
road_u = Road(Vector(51.75, 44.6), Vector(51.75, 5.4))
road_v = Road(Vector(112.25, 119.4), Vector(112.25, 158.6))
road_w = Road(Vector(108.75, 44.6), Vector(108.75, 5.4))
road_x = Road(Vector(55.25, 119.4), Vector(55.25, 158.6))
road_y = Road(Vector(62.4, 55.25), Vector(60.42597930092042, 55.527901173614765))
road_z = Road(Vector(60.42597930092042, 55.527901173614765), Vector(58.60540829946714, 56.34000215955095))
road_aa = Road(Vector(58.60540829946714, 56.34000215955095), Vector(57.07980834331931, 57.62317461736509))
road_ab = Road(Vector(57.07980834331931, 57.62317461736509), Vector(55.9677713257021, 59.27767165699379))
road_ac = Road(Vector(55.9677713257021, 59.27767165699379), Vector(55.25, 62.4))
road_ad = Road(Vector(51.75, 62.4), Vector(51.93724217621006, 60.41173474588463))
road_ae = Road(Vector(51.93724217621006, 60.41173474588463), Vector(52.492384736285906, 58.493382564645025))
road_af = Road(Vector(52.492384736285906, 58.493382564645025), Vector(53.39590728566313, 56.71239818626289))
road_ag = Road(Vector(53.39590728566313, 56.71239818626289), Vector(54.61603939647314, 55.13140609727426))
road_ah = Road(Vector(54.61603939647314, 55.13140609727426), Vector(56.1098777463325, 53.80599848534358))
road_ai = Road(Vector(56.1098777463325, 53.80599848534358), Vector(57.82489472143205, 52.782780459508075))
road_aj = Road(Vector(57.82489472143205, 52.782780459508075), Vector(59.70078543714179, 52.09773128171983))
road_ak = Road(Vector(59.70078543714179, 52.09773128171983), Vector(62.4, 51.75))
road_al = Road(Vector(62.4, 112.25), Vector(60.41173474588464, 112.06275782378994))
road_am = Road(Vector(60.41173474588464, 112.06275782378994), Vector(58.493382564645025, 111.5076152637141))
road_an = Road(Vector(58.493382564645025, 111.5076152637141), Vector(56.71239818626289, 110.60409271433687))
road_ao = Road(Vector(56.71239818626289, 110.60409271433687), Vector(55.13140609727426, 109.38396060352686))
road_ap = Road(Vector(55.13140609727426, 109.38396060352686), Vector(53.80599848534358, 107.8901222536675))
road_aq = Road(Vector(53.80599848534358, 107.8901222536675), Vector(52.782780459508075, 106.17510527856795))
road_ar = Road(Vector(52.782780459508075, 106.17510527856795), Vector(52.097731281719824, 104.29921456285823))
road_as = Road(Vector(52.097731281719824, 104.29921456285823), Vector(51.75, 101.6))
road_at = Road(Vector(55.25, 101.6), Vector(55.527901173614765, 103.57402069907957))
road_au = Road(Vector(55.527901173614765, 103.57402069907957), Vector(56.34000215955095, 105.39459170053284))
road_av = Road(Vector(56.34000215955095, 105.39459170053284), Vector(57.62317461736509, 106.92019165668069))
road_aw = Road(Vector(57.62317461736509, 106.92019165668069), Vector(59.27767165699379, 108.0322286742979))
road_ax = Road(Vector(59.27767165699379, 108.0322286742979), Vector(62.4, 108.75))
road_ay = Road(Vector(101.6, 51.75), Vector(103.58826525411536, 51.93724217621006))
road_az = Road(Vector(103.58826525411536, 51.93724217621006), Vector(105.50661743535497, 52.492384736285906))
road_ba = Road(Vector(105.50661743535497, 52.492384736285906), Vector(107.28760181373711, 53.39590728566313))
road_bb = Road(Vector(107.28760181373711, 53.39590728566313), Vector(108.86859390272573, 54.61603939647314))
road_bc = Road(Vector(108.86859390272573, 54.61603939647314), Vector(110.19400151465642, 56.1098777463325))
road_bd = Road(Vector(110.19400151465642, 56.1098777463325), Vector(111.21721954049193, 57.82489472143205))
road_be = Road(Vector(111.21721954049193, 57.82489472143205), Vector(111.90226871828017, 59.70078543714179))
road_bf = Road(Vector(111.90226871828017, 59.70078543714179), Vector(112.25, 62.4))
road_bg = Road(Vector(108.75, 62.4), Vector(108.47209882638523, 60.425979300920424))
road_bh = Road(Vector(108.47209882638523, 60.425979300920424), Vector(107.65999784044905, 58.60540829946715))
road_bi = Road(Vector(107.65999784044905, 58.60540829946715), Vector(106.37682538263492, 57.07980834331931))
road_bj = Road(Vector(106.37682538263492, 57.07980834331931), Vector(104.72232834300621, 55.9677713257021))
road_bk = Road(Vector(104.72232834300621, 55.9677713257021), Vector(101.6, 55.25))
road_bl = Road(Vector(101.6, 108.75), Vector(103.57402069907957, 108.47209882638523))
road_bm = Road(Vector(103.57402069907957, 108.47209882638523), Vector(105.39459170053284, 107.65999784044905))
road_bn = Road(Vector(105.39459170053284, 107.65999784044905), Vector(106.92019165668069, 106.3768253826349))
road_bo = Road(Vector(106.92019165668069, 106.3768253826349), Vector(108.0322286742979, 104.72232834300621))
road_bp = Road(Vector(108.0322286742979, 104.72232834300621), Vector(108.75, 101.6))
road_bq = Road(Vector(112.25, 101.6), Vector(112.06275782378994, 103.58826525411536))
road_br = Road(Vector(112.06275782378994, 103.58826525411536), Vector(111.5076152637141, 105.50661743535497))
road_bs = Road(Vector(111.5076152637141, 105.50661743535497), Vector(110.60409271433687, 107.28760181373711))
road_bt = Road(Vector(110.60409271433687, 107.28760181373711), Vector(109.38396060352686, 108.86859390272573))
road_bu = Road(Vector(109.38396060352686, 108.86859390272573), Vector(107.8901222536675, 110.19400151465642))
road_bv = Road(Vector(107.8901222536675, 110.19400151465642), Vector(106.17510527856795, 111.21721954049193))
road_bw = Road(Vector(106.17510527856795, 111.21721954049193), Vector(104.29921456285823, 111.90226871828017))
road_bx = Road(Vector(104.29921456285823, 111.90226871828017), Vector(101.6, 112.25))
road_by = Road(Vector(62.4, 55.25), Vector(44.6, 55.25))
road_bz = Road(Vector(51.75, 62.4), Vector(51.472098826385235, 60.42597930092042))
road_ca = Road(Vector(51.472098826385235, 60.42597930092042), Vector(50.65999784044905, 58.60540829946714))
road_cb = Road(Vector(50.65999784044905, 58.60540829946714), Vector(49.37682538263491, 57.07980834331931))
road_cc = Road(Vector(49.37682538263491, 57.07980834331931), Vector(47.72232834300621, 55.9677713257021))
road_cd = Road(Vector(47.72232834300621, 55.9677713257021), Vector(44.6, 55.25))
road_ce = Road(Vector(44.6, 51.75), Vector(62.4, 51.75))
road_cf = Road(Vector(44.6, 51.75), Vector(46.58826525411537, 51.93724217621006))
road_cg = Road(Vector(46.58826525411537, 51.93724217621006), Vector(48.506617435354975, 52.492384736285906))
road_ch = Road(Vector(48.506617435354975, 52.492384736285906), Vector(50.28760181373711, 53.39590728566313))
road_ci = Road(Vector(50.28760181373711, 53.39590728566313), Vector(51.86859390272574, 54.61603939647314))
road_cj = Road(Vector(51.86859390272574, 54.61603939647314), Vector(53.19400151465642, 56.1098777463325))
road_ck = Road(Vector(53.19400151465642, 56.1098777463325), Vector(54.217219540491925, 57.82489472143205))
road_cl = Road(Vector(54.217219540491925, 57.82489472143205), Vector(54.90226871828017, 59.70078543714179))
road_cm = Road(Vector(54.90226871828017, 59.70078543714179), Vector(55.25, 62.4))
road_cn = Road(Vector(101.6, 108.75), Vector(119.4, 108.75))
road_co = Road(Vector(112.25, 101.6), Vector(112.52790117361477, 103.57402069907957))
road_cp = Road(Vector(112.52790117361477, 103.57402069907957), Vector(113.34000215955095, 105.39459170053284))
road_cq = Road(Vector(113.34000215955095, 105.39459170053284), Vector(114.6231746173651, 106.92019165668069))
road_cr = Road(Vector(114.6231746173651, 106.92019165668069), Vector(116.27767165699379, 108.0322286742979))
road_cs = Road(Vector(116.27767165699379, 108.0322286742979), Vector(119.4, 108.75))
road_ct = Road(Vector(119.4, 112.25), Vector(101.6, 112.25))
road_cu = Road(Vector(119.4, 112.25), Vector(117.41173474588464, 112.06275782378994))
road_cv = Road(Vector(117.41173474588464, 112.06275782378994), Vector(115.49338256464503, 111.5076152637141))
road_cw = Road(Vector(115.49338256464503, 111.5076152637141), Vector(113.7123981862629, 110.60409271433687))
road_cx = Road(Vector(113.7123981862629, 110.60409271433687), Vector(112.13140609727427, 109.38396060352686))
road_cy = Road(Vector(112.13140609727427, 109.38396060352686), Vector(110.80599848534358, 107.8901222536675))
road_cz = Road(Vector(110.80599848534358, 107.8901222536675), Vector(109.78278045950807, 106.17510527856795))
road_da = Road(Vector(109.78278045950807, 106.17510527856795), Vector(109.09773128171983, 104.29921456285823))
road_db = Road(Vector(109.09773128171983, 104.29921456285823), Vector(108.75, 101.6))
road_dc = Road(Vector(62.4, 112.25), Vector(44.6, 112.25))
road_dd = Road(Vector(55.25, 101.6), Vector(55.06275782378994, 103.58826525411536))
road_de = Road(Vector(55.06275782378994, 103.58826525411536), Vector(54.507615263714094, 105.50661743535497))
road_df = Road(Vector(54.507615263714094, 105.50661743535497), Vector(53.60409271433687, 107.2876018137371))
road_dg = Road(Vector(53.60409271433687, 107.2876018137371), Vector(52.38396060352686, 108.86859390272573))
road_dh = Road(Vector(52.38396060352686, 108.86859390272573), Vector(50.8901222536675, 110.19400151465642))
road_di = Road(Vector(50.8901222536675, 110.19400151465642), Vector(49.17510527856795, 111.21721954049193))
road_dj = Road(Vector(49.17510527856795, 111.21721954049193), Vector(47.29921456285822, 111.90226871828017))
road_dk = Road(Vector(47.29921456285822, 111.90226871828017), Vector(44.6, 112.25))
road_dl = Road(Vector(44.6, 108.75), Vector(62.4, 108.75))
road_dm = Road(Vector(44.6, 108.75), Vector(46.57402069907958, 108.47209882638523))
road_dn = Road(Vector(46.57402069907958, 108.47209882638523), Vector(48.39459170053285, 107.65999784044905))
road_do = Road(Vector(48.39459170053285, 107.65999784044905), Vector(49.92019165668069, 106.3768253826349))
road_dp = Road(Vector(49.92019165668069, 106.3768253826349), Vector(51.0322286742979, 104.72232834300621))
road_dq = Road(Vector(51.0322286742979, 104.72232834300621), Vector(51.75, 101.6))
road_dr = Road(Vector(101.6, 51.75), Vector(119.4, 51.75))
road_ds = Road(Vector(108.75, 62.4), Vector(108.93724217621006, 60.41173474588463))
road_dt = Road(Vector(108.93724217621006, 60.41173474588463), Vector(109.4923847362859, 58.493382564645025))
road_du = Road(Vector(109.4923847362859, 58.493382564645025), Vector(110.39590728566313, 56.71239818626289))
road_dv = Road(Vector(110.39590728566313, 56.71239818626289), Vector(111.61603939647314, 55.13140609727426))
road_dw = Road(Vector(111.61603939647314, 55.13140609727426), Vector(113.1098777463325, 53.80599848534357))
road_dx = Road(Vector(113.1098777463325, 53.80599848534357), Vector(114.82489472143205, 52.782780459508075))
road_dy = Road(Vector(114.82489472143205, 52.782780459508075), Vector(116.70078543714179, 52.097731281719824))
road_dz = Road(Vector(116.70078543714179, 52.097731281719824), Vector(119.4, 51.75))
road_ea = Road(Vector(119.4, 55.25), Vector(101.6, 55.25))
road_eb = Road(Vector(119.4, 55.25), Vector(117.42597930092043, 55.527901173614765))
road_ec = Road(Vector(117.42597930092043, 55.527901173614765), Vector(115.60540829946716, 56.34000215955095))
road_ed = Road(Vector(115.60540829946716, 56.34000215955095), Vector(114.07980834331931, 57.62317461736509))
road_ee = Road(Vector(114.07980834331931, 57.62317461736509), Vector(112.96777132570212, 59.27767165699379))
road_ef = Road(Vector(112.96777132570212, 59.27767165699379), Vector(112.25, 62.4))
road_eg = Road(Vector(62.4, 55.25), Vector(60.41173474588463, 55.06275782378994))
road_eh = Road(Vector(60.41173474588463, 55.06275782378994), Vector(58.493382564645025, 54.507615263714094))
road_ei = Road(Vector(58.493382564645025, 54.507615263714094), Vector(56.71239818626289, 53.60409271433687))
road_ej = Road(Vector(56.71239818626289, 53.60409271433687), Vector(55.13140609727426, 52.38396060352686))
road_ek = Road(Vector(55.13140609727426, 52.38396060352686), Vector(53.80599848534358, 50.8901222536675))
road_el = Road(Vector(53.80599848534358, 50.8901222536675), Vector(52.782780459508075, 49.17510527856795))
road_em = Road(Vector(52.782780459508075, 49.17510527856795), Vector(52.09773128171983, 47.29921456285821))
road_en = Road(Vector(52.09773128171983, 47.29921456285821), Vector(51.75, 44.6))
road_eo = Road(Vector(51.75, 62.4), Vector(51.75, 44.6))
road_ep = Road(Vector(44.6, 51.75), Vector(46.57402069907958, 51.472098826385235))
road_eq = Road(Vector(46.57402069907958, 51.472098826385235), Vector(48.39459170053285, 50.65999784044905))
road_er = Road(Vector(48.39459170053285, 50.65999784044905), Vector(49.92019165668069, 49.37682538263491))
road_es = Road(Vector(49.92019165668069, 49.37682538263491), Vector(51.0322286742979, 47.72232834300621))
road_et = Road(Vector(51.0322286742979, 47.72232834300621), Vector(51.75, 44.6))
road_eu = Road(Vector(55.25, 44.6), Vector(55.527901173614765, 46.57402069907958))
road_ev = Road(Vector(55.527901173614765, 46.57402069907958), Vector(56.34000215955095, 48.39459170053285))
road_ew = Road(Vector(56.34000215955095, 48.39459170053285), Vector(57.62317461736509, 49.92019165668069))
road_ex = Road(Vector(57.62317461736509, 49.92019165668069), Vector(59.27767165699379, 51.0322286742979))
road_ey = Road(Vector(59.27767165699379, 51.0322286742979), Vector(62.4, 51.75))
road_ez = Road(Vector(55.25, 44.6), Vector(55.25, 62.4))
road_fa = Road(Vector(55.25, 44.6), Vector(55.06275782378994, 46.58826525411537))
road_fb = Road(Vector(55.06275782378994, 46.58826525411537), Vector(54.507615263714094, 48.506617435354975))
road_fc = Road(Vector(54.507615263714094, 48.506617435354975), Vector(53.60409271433687, 50.28760181373711))
road_fd = Road(Vector(53.60409271433687, 50.28760181373711), Vector(52.38396060352686, 51.86859390272574))
road_fe = Road(Vector(52.38396060352686, 51.86859390272574), Vector(50.8901222536675, 53.19400151465642))
road_ff = Road(Vector(50.8901222536675, 53.19400151465642), Vector(49.17510527856795, 54.217219540491925))
road_fg = Road(Vector(49.17510527856795, 54.217219540491925), Vector(47.29921456285822, 54.90226871828017))
road_fh = Road(Vector(47.29921456285822, 54.90226871828017), Vector(44.6, 55.25))
road_fi = Road(Vector(101.6, 108.75), Vector(103.58826525411536, 108.93724217621006))
road_fj = Road(Vector(103.58826525411536, 108.93724217621006), Vector(105.50661743535497, 109.4923847362859))
road_fk = Road(Vector(105.50661743535497, 109.4923847362859), Vector(107.2876018137371, 110.39590728566313))
road_fl = Road(Vector(107.2876018137371, 110.39590728566313), Vector(108.86859390272573, 111.61603939647314))
road_fm = Road(Vector(108.86859390272573, 111.61603939647314), Vector(110.19400151465642, 113.1098777463325))
road_fn = Road(Vector(110.19400151465642, 113.1098777463325), Vector(111.21721954049193, 114.82489472143205))
road_fo = Road(Vector(111.21721954049193, 114.82489472143205), Vector(111.90226871828017, 116.70078543714179))
road_fp = Road(Vector(111.90226871828017, 116.70078543714179), Vector(112.25, 119.4))
road_fq = Road(Vector(112.25, 101.6), Vector(112.25, 119.4))
road_fr = Road(Vector(119.4, 112.25), Vector(117.42597930092042, 112.52790117361477))
road_fs = Road(Vector(117.42597930092042, 112.52790117361477), Vector(115.60540829946716, 113.34000215955095))
road_ft = Road(Vector(115.60540829946716, 113.34000215955095), Vector(114.07980834331931, 114.62317461736508))
road_fu = Road(Vector(114.07980834331931, 114.62317461736508), Vector(112.9677713257021, 116.27767165699379))
road_fv = Road(Vector(112.9677713257021, 116.27767165699379), Vector(112.25, 119.4))
road_fw = Road(Vector(108.75, 119.4), Vector(108.47209882638523, 117.42597930092043))
road_fx = Road(Vector(108.47209882638523, 117.42597930092043), Vector(107.65999784044905, 115.60540829946716))
road_fy = Road(Vector(107.65999784044905, 115.60540829946716), Vector(106.37682538263492, 114.07980834331931))
road_fz = Road(Vector(106.37682538263492, 114.07980834331931), Vector(104.72232834300621, 112.9677713257021))
road_ga = Road(Vector(104.72232834300621, 112.9677713257021), Vector(101.6, 112.25))
road_gb = Road(Vector(108.75, 119.4), Vector(108.75, 101.6))
road_gc = Road(Vector(108.75, 119.4), Vector(108.93724217621006, 117.41173474588463))
road_gd = Road(Vector(108.93724217621006, 117.41173474588463), Vector(109.4923847362859, 115.49338256464503))
road_ge = Road(Vector(109.4923847362859, 115.49338256464503), Vector(110.39590728566313, 113.71239818626289))
road_gf = Road(Vector(110.39590728566313, 113.71239818626289), Vector(111.61603939647314, 112.13140609727427))
road_gg = Road(Vector(111.61603939647314, 112.13140609727427), Vector(113.1098777463325, 110.80599848534358))
road_gh = Road(Vector(113.1098777463325, 110.80599848534358), Vector(114.82489472143205, 109.78278045950807))
road_gi = Road(Vector(114.82489472143205, 109.78278045950807), Vector(116.70078543714179, 109.09773128171983))
road_gj = Road(Vector(116.70078543714179, 109.09773128171983), Vector(119.4, 108.75))
road_gk = Road(Vector(101.6, 51.75), Vector(103.57402069907957, 51.472098826385235))
road_gl = Road(Vector(103.57402069907957, 51.472098826385235), Vector(105.39459170053284, 50.65999784044905))
road_gm = Road(Vector(105.39459170053284, 50.65999784044905), Vector(106.92019165668069, 49.37682538263491))
road_gn = Road(Vector(106.92019165668069, 49.37682538263491), Vector(108.0322286742979, 47.72232834300621))
road_go = Road(Vector(108.0322286742979, 47.72232834300621), Vector(108.75, 44.6))
road_gp = Road(Vector(108.75, 62.4), Vector(108.75, 44.6))
road_gq = Road(Vector(119.4, 55.25), Vector(117.41173474588464, 55.06275782378994))
road_gr = Road(Vector(117.41173474588464, 55.06275782378994), Vector(115.49338256464503, 54.507615263714094))
road_gs = Road(Vector(115.49338256464503, 54.507615263714094), Vector(113.71239818626289, 53.60409271433687))
road_gt = Road(Vector(113.71239818626289, 53.60409271433687), Vector(112.13140609727427, 52.38396060352686))
road_gu = Road(Vector(112.13140609727427, 52.38396060352686), Vector(110.80599848534358, 50.8901222536675))
road_gv = Road(Vector(110.80599848534358, 50.8901222536675), Vector(109.78278045950807, 49.17510527856795))
road_gw = Road(Vector(109.78278045950807, 49.17510527856795), Vector(109.09773128171983, 47.29921456285821))
road_gx = Road(Vector(109.09773128171983, 47.29921456285821), Vector(108.75, 44.6))
road_gy = Road(Vector(112.25, 44.6), Vector(112.06275782378994, 46.58826525411537))
road_gz = Road(Vector(112.06275782378994, 46.58826525411537), Vector(111.5076152637141, 48.506617435354975))
road_ha = Road(Vector(111.5076152637141, 48.506617435354975), Vector(110.60409271433687, 50.28760181373711))
road_hb = Road(Vector(110.60409271433687, 50.28760181373711), Vector(109.38396060352686, 51.86859390272574))
road_hc = Road(Vector(109.38396060352686, 51.86859390272574), Vector(107.8901222536675, 53.19400151465642))
road_hd = Road(Vector(107.8901222536675, 53.19400151465642), Vector(106.17510527856795, 54.217219540491925))
road_he = Road(Vector(106.17510527856795, 54.217219540491925), Vector(104.29921456285823, 54.902268718280176))
road_hf = Road(Vector(104.29921456285823, 54.902268718280176), Vector(101.6, 55.25))
road_hg = Road(Vector(112.25, 44.6), Vector(112.25, 62.4))
road_hh = Road(Vector(112.25, 44.6), Vector(112.52790117361477, 46.57402069907958))
road_hi = Road(Vector(112.52790117361477, 46.57402069907958), Vector(113.34000215955095, 48.39459170053285))
road_hj = Road(Vector(113.34000215955095, 48.39459170053285), Vector(114.6231746173651, 49.92019165668069))
road_hk = Road(Vector(114.6231746173651, 49.92019165668069), Vector(116.27767165699379, 51.0322286742979))
road_hl = Road(Vector(116.27767165699379, 51.0322286742979), Vector(119.4, 51.75))
road_hm = Road(Vector(62.4, 112.25), Vector(60.42597930092042, 112.52790117361477))
road_hn = Road(Vector(60.42597930092042, 112.52790117361477), Vector(58.60540829946715, 113.34000215955095))
road_ho = Road(Vector(58.60540829946715, 113.34000215955095), Vector(57.07980834331931, 114.62317461736508))
road_hp = Road(Vector(57.07980834331931, 114.62317461736508), Vector(55.9677713257021, 116.27767165699379))
road_hq = Road(Vector(55.9677713257021, 116.27767165699379), Vector(55.25, 119.4))
road_hr = Road(Vector(55.25, 101.6), Vector(55.25, 119.4))
road_hs = Road(Vector(44.6, 108.75), Vector(46.58826525411537, 108.93724217621006))
road_ht = Road(Vector(46.58826525411537, 108.93724217621006), Vector(48.50661743535498, 109.4923847362859))
road_hu = Road(Vector(48.50661743535498, 109.4923847362859), Vector(50.28760181373711, 110.39590728566313))
road_hv = Road(Vector(50.28760181373711, 110.39590728566313), Vector(51.86859390272574, 111.61603939647314))
road_hw = Road(Vector(51.86859390272574, 111.61603939647314), Vector(53.19400151465642, 113.1098777463325))
road_hx = Road(Vector(53.19400151465642, 113.1098777463325), Vector(54.217219540491925, 114.82489472143205))
road_hy = Road(Vector(54.217219540491925, 114.82489472143205), Vector(54.902268718280176, 116.70078543714179))
road_hz = Road(Vector(54.902268718280176, 116.70078543714179), Vector(55.25, 119.4))
road_ia = Road(Vector(51.75, 119.4), Vector(51.93724217621006, 117.41173474588464))
road_ib = Road(Vector(51.93724217621006, 117.41173474588464), Vector(52.492384736285906, 115.49338256464503))
road_ic = Road(Vector(52.492384736285906, 115.49338256464503), Vector(53.39590728566313, 113.71239818626289))
road_id = Road(Vector(53.39590728566313, 113.71239818626289), Vector(54.61603939647314, 112.13140609727427))
road_ie = Road(Vector(54.61603939647314, 112.13140609727427), Vector(56.1098777463325, 110.80599848534358))
road_if = Road(Vector(56.1098777463325, 110.80599848534358), Vector(57.82489472143205, 109.78278045950807))
road_ig = Road(Vector(57.82489472143205, 109.78278045950807), Vector(59.70078543714179, 109.09773128171983))
road_ih = Road(Vector(59.70078543714179, 109.09773128171983), Vector(62.4, 108.75))
road_ii = Road(Vector(51.75, 119.4), Vector(51.75, 101.6))
road_ij = Road(Vector(51.75, 119.4), Vector(51.472098826385235, 117.42597930092043))
road_ik = Road(Vector(51.472098826385235, 117.42597930092043), Vector(50.65999784044905, 115.60540829946716))
road_il = Road(Vector(50.65999784044905, 115.60540829946716), Vector(49.37682538263491, 114.07980834331931))
road_im = Road(Vector(49.37682538263491, 114.07980834331931), Vector(47.72232834300621, 112.96777132570212))
road_in = Road(Vector(47.72232834300621, 112.96777132570212), Vector(44.6, 112.25))

intersection_0_0 = Intersection(0, 0, [interroad_a,interroad_e,interroad_i,interroad_m], [interroad_b,interroad_f,road_q,road_u])
interroad_a.setIntersection(intersection_0_0, 0)
intersection_0_0.addConnection(0, 1, [road_y,road_z,road_aa,road_ab,road_ac], LEFT)
intersection_0_0.addConnection(0, 2, [road_by], CENTRE)
intersection_0_0.addConnection(0, 3, [road_eg,road_eh,road_ei,road_ej,road_ek,road_el,road_em,road_en], RIGHT)
interroad_e.setIntersection(intersection_0_0, 1)
intersection_0_0.addConnection(1, 0, [road_ad,road_ae,road_af,road_ag,road_ah,road_ai,road_aj,road_ak], RIGHT)
intersection_0_0.addConnection(1, 2, [road_bz,road_ca,road_cb,road_cc,road_cd], LEFT)
intersection_0_0.addConnection(1, 3, [road_eo], CENTRE)
interroad_i.setIntersection(intersection_0_0, 2)
intersection_0_0.addConnection(2, 0, [road_ce], CENTRE)
intersection_0_0.addConnection(2, 1, [road_cf,road_cg,road_ch,road_ci,road_cj,road_ck,road_cl,road_cm], RIGHT)
intersection_0_0.addConnection(2, 3, [road_ep,road_eq,road_er,road_es,road_et], LEFT)
interroad_m.setIntersection(intersection_0_0, 3)
intersection_0_0.addConnection(3, 0, [road_eu,road_ev,road_ew,road_ex,road_ey], LEFT)
intersection_0_0.addConnection(3, 1, [road_ez], CENTRE)
intersection_0_0.addConnection(3, 2, [road_fa,road_fb,road_fc,road_fd,road_fe,road_ff,road_fg,road_fh], RIGHT)
intersection_0_1 = Intersection(0, 1, [interroad_c,interroad_f,interroad_k,interroad_p], [interroad_d,interroad_e,road_s,road_x])
interroad_c.setIntersection(intersection_0_1, 0)
intersection_0_1.addConnection(0, 1, [road_al,road_am,road_an,road_ao,road_ap,road_aq,road_ar,road_as], RIGHT)
intersection_0_1.addConnection(0, 2, [road_dc], CENTRE)
intersection_0_1.addConnection(0, 3, [road_hm,road_hn,road_ho,road_hp,road_hq], LEFT)
interroad_f.setIntersection(intersection_0_1, 1)
intersection_0_1.addConnection(1, 0, [road_at,road_au,road_av,road_aw,road_ax], LEFT)
intersection_0_1.addConnection(1, 2, [road_dd,road_de,road_df,road_dg,road_dh,road_di,road_dj,road_dk], RIGHT)
intersection_0_1.addConnection(1, 3, [road_hr], CENTRE)
interroad_k.setIntersection(intersection_0_1, 2)
intersection_0_1.addConnection(2, 0, [road_dl], CENTRE)
intersection_0_1.addConnection(2, 1, [road_dm,road_dn,road_do,road_dp,road_dq], LEFT)
intersection_0_1.addConnection(2, 3, [road_hs,road_ht,road_hu,road_hv,road_hw,road_hx,road_hy,road_hz], RIGHT)
interroad_p.setIntersection(intersection_0_1, 3)
intersection_0_1.addConnection(3, 0, [road_ia,road_ib,road_ic,road_id,road_ie,road_if,road_ig,road_ih], RIGHT)
intersection_0_1.addConnection(3, 1, [road_ii], CENTRE)
intersection_0_1.addConnection(3, 2, [road_ij,road_ik,road_il,road_im,road_in], LEFT)
intersection_1_0 = Intersection(1, 0, [interroad_b,interroad_g,interroad_l,interroad_o], [interroad_a,interroad_h,road_t,road_w])
interroad_b.setIntersection(intersection_1_0, 0)
intersection_1_0.addConnection(0, 1, [road_ay,road_az,road_ba,road_bb,road_bc,road_bd,road_be,road_bf], RIGHT)
intersection_1_0.addConnection(0, 2, [road_dr], CENTRE)
intersection_1_0.addConnection(0, 3, [road_gk,road_gl,road_gm,road_gn,road_go], LEFT)
interroad_g.setIntersection(intersection_1_0, 1)
intersection_1_0.addConnection(1, 0, [road_bg,road_bh,road_bi,road_bj,road_bk], LEFT)
intersection_1_0.addConnection(1, 2, [road_ds,road_dt,road_du,road_dv,road_dw,road_dx,road_dy,road_dz], RIGHT)
intersection_1_0.addConnection(1, 3, [road_gp], CENTRE)
interroad_l.setIntersection(intersection_1_0, 2)
intersection_1_0.addConnection(2, 0, [road_ea], CENTRE)
intersection_1_0.addConnection(2, 1, [road_eb,road_ec,road_ed,road_ee,road_ef], LEFT)
intersection_1_0.addConnection(2, 3, [road_gq,road_gr,road_gs,road_gt,road_gu,road_gv,road_gw,road_gx], RIGHT)
interroad_o.setIntersection(intersection_1_0, 3)
intersection_1_0.addConnection(3, 0, [road_gy,road_gz,road_ha,road_hb,road_hc,road_hd,road_he,road_hf], RIGHT)
intersection_1_0.addConnection(3, 1, [road_hg], CENTRE)
intersection_1_0.addConnection(3, 2, [road_hh,road_hi,road_hj,road_hk,road_hl], LEFT)
intersection_1_1 = Intersection(1, 1, [interroad_d,interroad_h,interroad_j,interroad_n], [interroad_c,interroad_g,road_r,road_v])
interroad_d.setIntersection(intersection_1_1, 0)
intersection_1_1.addConnection(0, 1, [road_bl,road_bm,road_bn,road_bo,road_bp], LEFT)
intersection_1_1.addConnection(0, 2, [road_cn], CENTRE)
intersection_1_1.addConnection(0, 3, [road_fi,road_fj,road_fk,road_fl,road_fm,road_fn,road_fo,road_fp], RIGHT)
interroad_h.setIntersection(intersection_1_1, 1)
intersection_1_1.addConnection(1, 0, [road_bq,road_br,road_bs,road_bt,road_bu,road_bv,road_bw,road_bx], RIGHT)
intersection_1_1.addConnection(1, 2, [road_co,road_cp,road_cq,road_cr,road_cs], LEFT)
intersection_1_1.addConnection(1, 3, [road_fq], CENTRE)
interroad_j.setIntersection(intersection_1_1, 2)
intersection_1_1.addConnection(2, 0, [road_ct], CENTRE)
intersection_1_1.addConnection(2, 1, [road_cu,road_cv,road_cw,road_cx,road_cy,road_cz,road_da,road_db], RIGHT)
intersection_1_1.addConnection(2, 3, [road_fr,road_fs,road_ft,road_fu,road_fv], LEFT)
interroad_n.setIntersection(intersection_1_1, 3)
intersection_1_1.addConnection(3, 0, [road_fw,road_fx,road_fy,road_fz,road_ga], LEFT)
intersection_1_1.addConnection(3, 1, [road_gb], CENTRE)
intersection_1_1.addConnection(3, 2, [road_gc,road_gd,road_ge,road_gf,road_gg,road_gh,road_gi,road_gj], RIGHT)

road_y.setNext(road_z)
road_z.setNext(road_aa)
road_aa.setNext(road_ab)
road_ab.setNext(road_ac)
road_ac.setNext(interroad_f)
road_ad.setNext(road_ae)
road_ae.setNext(road_af)
road_af.setNext(road_ag)
road_ag.setNext(road_ah)
road_ah.setNext(road_ai)
road_ai.setNext(road_aj)
road_aj.setNext(road_ak)
road_ak.setNext(interroad_b)
road_al.setNext(road_am)
road_am.setNext(road_an)
road_an.setNext(road_ao)
road_ao.setNext(road_ap)
road_ap.setNext(road_aq)
road_aq.setNext(road_ar)
road_ar.setNext(road_as)
road_as.setNext(interroad_e)
road_at.setNext(road_au)
road_au.setNext(road_av)
road_av.setNext(road_aw)
road_aw.setNext(road_ax)
road_ax.setNext(interroad_d)
road_ay.setNext(road_az)
road_az.setNext(road_ba)
road_ba.setNext(road_bb)
road_bb.setNext(road_bc)
road_bc.setNext(road_bd)
road_bd.setNext(road_be)
road_be.setNext(road_bf)
road_bf.setNext(interroad_h)
road_bg.setNext(road_bh)
road_bh.setNext(road_bi)
road_bi.setNext(road_bj)
road_bj.setNext(road_bk)
road_bk.setNext(interroad_a)
road_bl.setNext(road_bm)
road_bm.setNext(road_bn)
road_bn.setNext(road_bo)
road_bo.setNext(road_bp)
road_bp.setNext(interroad_g)
road_bq.setNext(road_br)
road_br.setNext(road_bs)
road_bs.setNext(road_bt)
road_bt.setNext(road_bu)
road_bu.setNext(road_bv)
road_bv.setNext(road_bw)
road_bw.setNext(road_bx)
road_bx.setNext(interroad_c)
road_by.setNext(road_q)
road_bz.setNext(road_ca)
road_ca.setNext(road_cb)
road_cb.setNext(road_cc)
road_cc.setNext(road_cd)
road_cd.setNext(road_q)
road_ce.setNext(interroad_b)
road_cf.setNext(road_cg)
road_cg.setNext(road_ch)
road_ch.setNext(road_ci)
road_ci.setNext(road_cj)
road_cj.setNext(road_ck)
road_ck.setNext(road_cl)
road_cl.setNext(road_cm)
road_cm.setNext(interroad_f)
road_cn.setNext(road_r)
road_co.setNext(road_cp)
road_cp.setNext(road_cq)
road_cq.setNext(road_cr)
road_cr.setNext(road_cs)
road_cs.setNext(road_r)
road_ct.setNext(interroad_c)
road_cu.setNext(road_cv)
road_cv.setNext(road_cw)
road_cw.setNext(road_cx)
road_cx.setNext(road_cy)
road_cy.setNext(road_cz)
road_cz.setNext(road_da)
road_da.setNext(road_db)
road_db.setNext(interroad_g)
road_dc.setNext(road_s)
road_dd.setNext(road_de)
road_de.setNext(road_df)
road_df.setNext(road_dg)
road_dg.setNext(road_dh)
road_dh.setNext(road_di)
road_di.setNext(road_dj)
road_dj.setNext(road_dk)
road_dk.setNext(road_s)
road_dl.setNext(interroad_d)
road_dm.setNext(road_dn)
road_dn.setNext(road_do)
road_do.setNext(road_dp)
road_dp.setNext(road_dq)
road_dq.setNext(interroad_e)
road_dr.setNext(road_t)
road_ds.setNext(road_dt)
road_dt.setNext(road_du)
road_du.setNext(road_dv)
road_dv.setNext(road_dw)
road_dw.setNext(road_dx)
road_dx.setNext(road_dy)
road_dy.setNext(road_dz)
road_dz.setNext(road_t)
road_ea.setNext(interroad_a)
road_eb.setNext(road_ec)
road_ec.setNext(road_ed)
road_ed.setNext(road_ee)
road_ee.setNext(road_ef)
road_ef.setNext(interroad_h)
road_eg.setNext(road_eh)
road_eh.setNext(road_ei)
road_ei.setNext(road_ej)
road_ej.setNext(road_ek)
road_ek.setNext(road_el)
road_el.setNext(road_em)
road_em.setNext(road_en)
road_en.setNext(road_u)
road_eo.setNext(road_u)
road_ep.setNext(road_eq)
road_eq.setNext(road_er)
road_er.setNext(road_es)
road_es.setNext(road_et)
road_et.setNext(road_u)
road_eu.setNext(road_ev)
road_ev.setNext(road_ew)
road_ew.setNext(road_ex)
road_ex.setNext(road_ey)
road_ey.setNext(interroad_b)
road_ez.setNext(interroad_f)
road_fa.setNext(road_fb)
road_fb.setNext(road_fc)
road_fc.setNext(road_fd)
road_fd.setNext(road_fe)
road_fe.setNext(road_ff)
road_ff.setNext(road_fg)
road_fg.setNext(road_fh)
road_fh.setNext(road_q)
road_fi.setNext(road_fj)
road_fj.setNext(road_fk)
road_fk.setNext(road_fl)
road_fl.setNext(road_fm)
road_fm.setNext(road_fn)
road_fn.setNext(road_fo)
road_fo.setNext(road_fp)
road_fp.setNext(road_v)
road_fq.setNext(road_v)
road_fr.setNext(road_fs)
road_fs.setNext(road_ft)
road_ft.setNext(road_fu)
road_fu.setNext(road_fv)
road_fv.setNext(road_v)
road_fw.setNext(road_fx)
road_fx.setNext(road_fy)
road_fy.setNext(road_fz)
road_fz.setNext(road_ga)
road_ga.setNext(interroad_c)
road_gb.setNext(interroad_g)
road_gc.setNext(road_gd)
road_gd.setNext(road_ge)
road_ge.setNext(road_gf)
road_gf.setNext(road_gg)
road_gg.setNext(road_gh)
road_gh.setNext(road_gi)
road_gi.setNext(road_gj)
road_gj.setNext(road_r)
road_gk.setNext(road_gl)
road_gl.setNext(road_gm)
road_gm.setNext(road_gn)
road_gn.setNext(road_go)
road_go.setNext(road_w)
road_gp.setNext(road_w)
road_gq.setNext(road_gr)
road_gr.setNext(road_gs)
road_gs.setNext(road_gt)
road_gt.setNext(road_gu)
road_gu.setNext(road_gv)
road_gv.setNext(road_gw)
road_gw.setNext(road_gx)
road_gx.setNext(road_w)
road_gy.setNext(road_gz)
road_gz.setNext(road_ha)
road_ha.setNext(road_hb)
road_hb.setNext(road_hc)
road_hc.setNext(road_hd)
road_hd.setNext(road_he)
road_he.setNext(road_hf)
road_hf.setNext(interroad_a)
road_hg.setNext(interroad_h)
road_hh.setNext(road_hi)
road_hi.setNext(road_hj)
road_hj.setNext(road_hk)
road_hk.setNext(road_hl)
road_hl.setNext(road_t)
road_hm.setNext(road_hn)
road_hn.setNext(road_ho)
road_ho.setNext(road_hp)
road_hp.setNext(road_hq)
road_hq.setNext(road_x)
road_hr.setNext(road_x)
road_hs.setNext(road_ht)
road_ht.setNext(road_hu)
road_hu.setNext(road_hv)
road_hv.setNext(road_hw)
road_hw.setNext(road_hx)
road_hx.setNext(road_hy)
road_hy.setNext(road_hz)
road_hz.setNext(road_x)
road_ia.setNext(road_ib)
road_ib.setNext(road_ic)
road_ic.setNext(road_id)
road_id.setNext(road_ie)
road_ie.setNext(road_if)
road_if.setNext(road_ig)
road_ig.setNext(road_ih)
road_ih.setNext(interroad_d)
road_ii.setNext(interroad_e)
road_ij.setNext(road_ik)
road_ik.setNext(road_il)
road_il.setNext(road_im)
road_im.setNext(road_in)
road_in.setNext(road_s)

roads = [interroad_a,interroad_b,interroad_c,interroad_d,interroad_e,interroad_f,road_y,road_z,road_aa,road_ab,road_ac,road_ad,road_ae,road_af,road_ag,road_ah,road_ai,road_aj,road_ak,road_al,road_am,road_an,road_ao,road_ap,road_aq,road_ar,road_as,road_at,road_au,road_av,road_aw,road_ax,interroad_g,interroad_h,road_ay,road_az,road_ba,road_bb,road_bc,road_bd,road_be,road_bf,road_bg,road_bh,road_bi,road_bj,road_bk,road_bl,road_bm,road_bn,road_bo,road_bp,road_bq,road_br,road_bs,road_bt,road_bu,road_bv,road_bw,road_bx,interroad_i,road_q,road_by,road_bz,road_ca,road_cb,road_cc,road_cd,road_ce,road_cf,road_cg,road_ch,road_ci,road_cj,road_ck,road_cl,road_cm,interroad_j,road_r,road_cn,road_co,road_cp,road_cq,road_cr,road_cs,road_ct,road_cu,road_cv,road_cw,road_cx,road_cy,road_cz,road_da,road_db,interroad_k,road_s,road_dc,road_dd,road_de,road_df,road_dg,road_dh,road_di,road_dj,road_dk,road_dl,road_dm,road_dn,road_do,road_dp,road_dq,interroad_l,road_t,road_dr,road_ds,road_dt,road_du,road_dv,road_dw,road_dx,road_dy,road_dz,road_ea,road_eb,road_ec,road_ed,road_ee,road_ef,interroad_m,road_u,road_eg,road_eh,road_ei,road_ej,road_ek,road_el,road_em,road_en,road_eo,road_ep,road_eq,road_er,road_es,road_et,road_eu,road_ev,road_ew,road_ex,road_ey,road_ez,road_fa,road_fb,road_fc,road_fd,road_fe,road_ff,road_fg,road_fh,interroad_n,road_v,road_fi,road_fj,road_fk,road_fl,road_fm,road_fn,road_fo,road_fp,road_fq,road_fr,road_fs,road_ft,road_fu,road_fv,road_fw,road_fx,road_fy,road_fz,road_ga,road_gb,road_gc,road_gd,road_ge,road_gf,road_gg,road_gh,road_gi,road_gj,interroad_o,road_w,road_gk,road_gl,road_gm,road_gn,road_go,road_gp,road_gq,road_gr,road_gs,road_gt,road_gu,road_gv,road_gw,road_gx,road_gy,road_gz,road_ha,road_hb,road_hc,road_hd,road_he,road_hf,road_hg,road_hh,road_hi,road_hj,road_hk,road_hl,interroad_p,road_x,road_hm,road_hn,road_ho,road_hp,road_hq,road_hr,road_hs,road_ht,road_hu,road_hv,road_hw,road_hx,road_hy,road_hz,road_ia,road_ib,road_ic,road_id,road_ie,road_if,road_ig,road_ih,road_ii,road_ij,road_ik,road_il,road_im,road_in]

entry_roads = [interroad_i,interroad_j,interroad_k,interroad_l,interroad_m,interroad_n,interroad_o,interroad_p]

intersections = [intersection_0_0,intersection_0_1,intersection_1_0,intersection_1_1]

grass = [
[Vector(5.4, 0.0), Vector(44.6, 0.0), Vector(50.0, 5.4), Vector(50.0, 44.6), Vector(44.6, 50.0), Vector(5.4, 50.0), Vector(0.0, 44.6), Vector(0.0, 5.4)],
[Vector(5.4, 57.0), Vector(44.6, 57.0), Vector(50.0, 62.4), Vector(50.0, 101.6), Vector(44.6, 107.0), Vector(5.4, 107.0), Vector(0.0, 101.6), Vector(0.0, 62.4)],
[Vector(5.4, 114.0), Vector(44.6, 114.0), Vector(50.0, 119.4), Vector(50.0, 158.6), Vector(44.6, 164.0), Vector(5.4, 164.0), Vector(0.0, 158.6), Vector(0.0, 119.4)],
[Vector(62.4, 0.0), Vector(101.6, 0.0), Vector(107.0, 5.4), Vector(107.0, 44.6), Vector(101.6, 50.0), Vector(62.4, 50.0), Vector(57.0, 44.6), Vector(57.0, 5.4)],
[Vector(62.4, 57.0), Vector(101.6, 57.0), Vector(107.0, 62.4), Vector(107.0, 101.6), Vector(101.6, 107.0), Vector(62.4, 107.0), Vector(57.0, 101.6), Vector(57.0, 62.4)],
[Vector(62.4, 114.0), Vector(101.6, 114.0), Vector(107.0, 119.4), Vector(107.0, 158.6), Vector(101.6, 164.0), Vector(62.4, 164.0), Vector(57.0, 158.6), Vector(57.0, 119.4)],
[Vector(119.4, 0.0), Vector(158.6, 0.0), Vector(164.0, 5.4), Vector(164.0, 44.6), Vector(158.6, 50.0), Vector(119.4, 50.0), Vector(114.0, 44.6), Vector(114.0, 5.4)],
[Vector(119.4, 57.0), Vector(158.6, 57.0), Vector(164.0, 62.4), Vector(164.0, 101.6), Vector(158.6, 107.0), Vector(119.4, 107.0), Vector(114.0, 101.6), Vector(114.0, 62.4)],
[Vector(119.4, 114.0), Vector(158.6, 114.0), Vector(164.0, 119.4), Vector(164.0, 158.6), Vector(158.6, 164.0), Vector(119.4, 164.0), Vector(114.0, 158.6), Vector(114.0, 119.4)],
]

world_width  = 164.0
world_height = 164.0

