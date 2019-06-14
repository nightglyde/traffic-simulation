from src.util import *
from src.simulation.road_network import Road, IntersectionRoad, Intersection, FollowRoad, EnterIntersection

NUM_ROWS = 0
NUM_COLS = 0
world_width  = 107.0
world_height = 107.0

interroad_a = IntersectionRoad(Vector(5.4, 51.75), Vector(44.6, 51.75), False)
interroad_b = IntersectionRoad(Vector(101.6, 55.25), Vector(62.4, 55.25), False)
interroad_c = IntersectionRoad(Vector(55.25, 5.4), Vector(55.25, 44.6), False)
interroad_d = IntersectionRoad(Vector(51.75, 101.6), Vector(51.75, 62.4), False)
road_e = Road(Vector(44.6, 55.25), Vector(5.4, 55.25), False)
road_f = Road(Vector(62.4, 51.75), Vector(101.6, 51.75), False)
road_g = Road(Vector(51.75, 44.6), Vector(51.75, 5.4), False)
road_h = Road(Vector(55.25, 62.4), Vector(55.25, 101.6), False)
road_i = Road(Vector(44.6, 51.75), Vector(62.4, 51.75), True)
road_j = Road(Vector(62.4, 55.25), Vector(44.6, 55.25), True)
road_k = Road(Vector(44.6, 51.75), Vector(46.57402069907958, 51.472098826385235), True)
road_l = Road(Vector(46.57402069907958, 51.472098826385235), Vector(48.39459170053285, 50.65999784044905), True)
road_m = Road(Vector(48.39459170053285, 50.65999784044905), Vector(49.92019165668069, 49.37682538263491), True)
road_n = Road(Vector(49.92019165668069, 49.37682538263491), Vector(51.0322286742979, 47.72232834300621), True)
road_o = Road(Vector(51.0322286742979, 47.72232834300621), Vector(51.75, 44.6), True)
road_p = Road(Vector(62.4, 55.25), Vector(60.41173474588463, 55.06275782378994), True)
road_q = Road(Vector(60.41173474588463, 55.06275782378994), Vector(58.493382564645025, 54.507615263714094), True)
road_r = Road(Vector(58.493382564645025, 54.507615263714094), Vector(56.71239818626289, 53.60409271433687), True)
road_s = Road(Vector(56.71239818626289, 53.60409271433687), Vector(55.13140609727426, 52.38396060352686), True)
road_t = Road(Vector(55.13140609727426, 52.38396060352686), Vector(53.80599848534358, 50.8901222536675), True)
road_u = Road(Vector(53.80599848534358, 50.8901222536675), Vector(52.782780459508075, 49.17510527856795), True)
road_v = Road(Vector(52.782780459508075, 49.17510527856795), Vector(52.09773128171983, 47.29921456285821), True)
road_w = Road(Vector(52.09773128171983, 47.29921456285821), Vector(51.75, 44.6), True)
road_x = Road(Vector(55.25, 44.6), Vector(55.06275782378994, 46.58826525411537), True)
road_y = Road(Vector(55.06275782378994, 46.58826525411537), Vector(54.507615263714094, 48.506617435354975), True)
road_z = Road(Vector(54.507615263714094, 48.506617435354975), Vector(53.60409271433687, 50.28760181373711), True)
road_aa = Road(Vector(53.60409271433687, 50.28760181373711), Vector(52.38396060352686, 51.86859390272574), True)
road_ab = Road(Vector(52.38396060352686, 51.86859390272574), Vector(50.8901222536675, 53.19400151465642), True)
road_ac = Road(Vector(50.8901222536675, 53.19400151465642), Vector(49.17510527856795, 54.217219540491925), True)
road_ad = Road(Vector(49.17510527856795, 54.217219540491925), Vector(47.29921456285822, 54.90226871828017), True)
road_ae = Road(Vector(47.29921456285822, 54.90226871828017), Vector(44.6, 55.25), True)
road_af = Road(Vector(55.25, 44.6), Vector(55.527901173614765, 46.57402069907958), True)
road_ag = Road(Vector(55.527901173614765, 46.57402069907958), Vector(56.34000215955095, 48.39459170053285), True)
road_ah = Road(Vector(56.34000215955095, 48.39459170053285), Vector(57.62317461736509, 49.92019165668069), True)
road_ai = Road(Vector(57.62317461736509, 49.92019165668069), Vector(59.27767165699379, 51.0322286742979), True)
road_aj = Road(Vector(59.27767165699379, 51.0322286742979), Vector(62.4, 51.75), True)
road_ak = Road(Vector(44.6, 51.75), Vector(46.58826525411537, 51.93724217621006), True)
road_al = Road(Vector(46.58826525411537, 51.93724217621006), Vector(48.506617435354975, 52.492384736285906), True)
road_am = Road(Vector(48.506617435354975, 52.492384736285906), Vector(50.28760181373711, 53.39590728566313), True)
road_an = Road(Vector(50.28760181373711, 53.39590728566313), Vector(51.86859390272574, 54.61603939647314), True)
road_ao = Road(Vector(51.86859390272574, 54.61603939647314), Vector(53.19400151465642, 56.1098777463325), True)
road_ap = Road(Vector(53.19400151465642, 56.1098777463325), Vector(54.217219540491925, 57.82489472143205), True)
road_aq = Road(Vector(54.217219540491925, 57.82489472143205), Vector(54.90226871828017, 59.70078543714179), True)
road_ar = Road(Vector(54.90226871828017, 59.70078543714179), Vector(55.25, 62.4), True)
road_as = Road(Vector(62.4, 55.25), Vector(60.42597930092042, 55.527901173614765), True)
road_at = Road(Vector(60.42597930092042, 55.527901173614765), Vector(58.60540829946714, 56.34000215955095), True)
road_au = Road(Vector(58.60540829946714, 56.34000215955095), Vector(57.07980834331931, 57.62317461736509), True)
road_av = Road(Vector(57.07980834331931, 57.62317461736509), Vector(55.9677713257021, 59.27767165699379), True)
road_aw = Road(Vector(55.9677713257021, 59.27767165699379), Vector(55.25, 62.4), True)
road_ax = Road(Vector(55.25, 44.6), Vector(55.25, 62.4), True)
road_ay = Road(Vector(51.75, 62.4), Vector(51.472098826385235, 60.42597930092042), True)
road_az = Road(Vector(51.472098826385235, 60.42597930092042), Vector(50.65999784044905, 58.60540829946714), True)
road_ba = Road(Vector(50.65999784044905, 58.60540829946714), Vector(49.37682538263491, 57.07980834331931), True)
road_bb = Road(Vector(49.37682538263491, 57.07980834331931), Vector(47.72232834300621, 55.9677713257021), True)
road_bc = Road(Vector(47.72232834300621, 55.9677713257021), Vector(44.6, 55.25), True)
road_bd = Road(Vector(51.75, 62.4), Vector(51.93724217621006, 60.41173474588463), True)
road_be = Road(Vector(51.93724217621006, 60.41173474588463), Vector(52.492384736285906, 58.493382564645025), True)
road_bf = Road(Vector(52.492384736285906, 58.493382564645025), Vector(53.39590728566313, 56.71239818626289), True)
road_bg = Road(Vector(53.39590728566313, 56.71239818626289), Vector(54.61603939647314, 55.13140609727426), True)
road_bh = Road(Vector(54.61603939647314, 55.13140609727426), Vector(56.1098777463325, 53.80599848534358), True)
road_bi = Road(Vector(56.1098777463325, 53.80599848534358), Vector(57.82489472143205, 52.782780459508075), True)
road_bj = Road(Vector(57.82489472143205, 52.782780459508075), Vector(59.70078543714179, 52.09773128171983), True)
road_bk = Road(Vector(59.70078543714179, 52.09773128171983), Vector(62.4, 51.75), True)
road_bl = Road(Vector(51.75, 62.4), Vector(51.75, 44.6), True)

intersection_0_0 = Intersection(0, 0, [interroad_a,interroad_b,interroad_c,interroad_d], [road_e,road_f,road_g,road_h])
interroad_a.setIntersection(intersection_0_0, 0)
intersection_0_0.addConnection(0, 2, [road_i], CENTRE, 17.799999999999997)
intersection_0_0.addConnection(0, 1, [road_k,road_l,road_m,road_n,road_o], LEFT, -11.231193736583508)
intersection_0_0.addConnection(0, 3, [road_ak,road_al,road_am,road_an,road_ao,road_ap,road_aq,road_ar], RIGHT, 16.728980880365647)
interroad_b.setIntersection(intersection_0_0, 2)
intersection_0_0.addConnection(2, 0, [road_j], CENTRE, 17.799999999999997)
intersection_0_0.addConnection(2, 1, [road_p,road_q,road_r,road_s,road_t,road_u,road_v,road_w], RIGHT, 16.728980880365647)
intersection_0_0.addConnection(2, 3, [road_as,road_at,road_au,road_av,road_aw], LEFT, -11.231193736583508)
interroad_c.setIntersection(intersection_0_0, 1)
intersection_0_0.addConnection(1, 0, [road_x,road_y,road_z,road_aa,road_ab,road_ac,road_ad,road_ae], RIGHT, 16.728980880365647)
intersection_0_0.addConnection(1, 2, [road_af,road_ag,road_ah,road_ai,road_aj], LEFT, -11.231193736583508)
intersection_0_0.addConnection(1, 3, [road_ax], CENTRE, 17.799999999999997)
interroad_d.setIntersection(intersection_0_0, 3)
intersection_0_0.addConnection(3, 0, [road_ay,road_az,road_ba,road_bb,road_bc], LEFT, -11.231193736583508)
intersection_0_0.addConnection(3, 2, [road_bd,road_be,road_bf,road_bg,road_bh,road_bi,road_bj,road_bk], RIGHT, 16.728980880365647)
intersection_0_0.addConnection(3, 1, [road_bl], CENTRE, 17.799999999999997)

road_i.setNext(road_f)
road_j.setNext(road_e)
road_k.setNext(road_l)
road_l.setNext(road_m)
road_m.setNext(road_n)
road_n.setNext(road_o)
road_o.setNext(road_g)
road_p.setNext(road_q)
road_q.setNext(road_r)
road_r.setNext(road_s)
road_s.setNext(road_t)
road_t.setNext(road_u)
road_u.setNext(road_v)
road_v.setNext(road_w)
road_w.setNext(road_g)
road_x.setNext(road_y)
road_y.setNext(road_z)
road_z.setNext(road_aa)
road_aa.setNext(road_ab)
road_ab.setNext(road_ac)
road_ac.setNext(road_ad)
road_ad.setNext(road_ae)
road_ae.setNext(road_e)
road_af.setNext(road_ag)
road_ag.setNext(road_ah)
road_ah.setNext(road_ai)
road_ai.setNext(road_aj)
road_aj.setNext(road_f)
road_ak.setNext(road_al)
road_al.setNext(road_am)
road_am.setNext(road_an)
road_an.setNext(road_ao)
road_ao.setNext(road_ap)
road_ap.setNext(road_aq)
road_aq.setNext(road_ar)
road_ar.setNext(road_h)
road_as.setNext(road_at)
road_at.setNext(road_au)
road_au.setNext(road_av)
road_av.setNext(road_aw)
road_aw.setNext(road_h)
road_ax.setNext(road_h)
road_ay.setNext(road_az)
road_az.setNext(road_ba)
road_ba.setNext(road_bb)
road_bb.setNext(road_bc)
road_bc.setNext(road_e)
road_bd.setNext(road_be)
road_be.setNext(road_bf)
road_bf.setNext(road_bg)
road_bg.setNext(road_bh)
road_bh.setNext(road_bi)
road_bi.setNext(road_bj)
road_bj.setNext(road_bk)
road_bk.setNext(road_f)
road_bl.setNext(road_g)

roads = [interroad_a,road_e,interroad_b,road_f,road_i,road_j,interroad_c,road_g,road_k,road_l,road_m,road_n,road_o,road_p,road_q,road_r,road_s,road_t,road_u,road_v,road_w,road_x,road_y,road_z,road_aa,road_ab,road_ac,road_ad,road_ae,road_af,road_ag,road_ah,road_ai,road_aj,interroad_d,road_h,road_ak,road_al,road_am,road_an,road_ao,road_ap,road_aq,road_ar,road_as,road_at,road_au,road_av,road_aw,road_ax,road_ay,road_az,road_ba,road_bb,road_bc,road_bd,road_be,road_bf,road_bg,road_bh,road_bi,road_bj,road_bk,road_bl]

entry_roads = [interroad_a,interroad_b,interroad_c,interroad_d]

valid_routes = [
  [
    [EnterIntersection(interroad_a, LEFT), FollowRoad(road_k), FollowRoad(road_l), FollowRoad(road_m), FollowRoad(road_n), FollowRoad(road_o), FollowRoad(road_g)],
    [EnterIntersection(interroad_a, RIGHT), FollowRoad(road_ak), FollowRoad(road_al), FollowRoad(road_am), FollowRoad(road_an), FollowRoad(road_ao), FollowRoad(road_ap), FollowRoad(road_aq), FollowRoad(road_ar), FollowRoad(road_h)],
    [EnterIntersection(interroad_a, CENTRE), FollowRoad(road_i), FollowRoad(road_f)],
  ],
  [
    [EnterIntersection(interroad_b, LEFT), FollowRoad(road_as), FollowRoad(road_at), FollowRoad(road_au), FollowRoad(road_av), FollowRoad(road_aw), FollowRoad(road_h)],
    [EnterIntersection(interroad_b, RIGHT), FollowRoad(road_p), FollowRoad(road_q), FollowRoad(road_r), FollowRoad(road_s), FollowRoad(road_t), FollowRoad(road_u), FollowRoad(road_v), FollowRoad(road_w), FollowRoad(road_g)],
    [EnterIntersection(interroad_b, CENTRE), FollowRoad(road_j), FollowRoad(road_e)],
  ],
  [
    [EnterIntersection(interroad_c, LEFT), FollowRoad(road_af), FollowRoad(road_ag), FollowRoad(road_ah), FollowRoad(road_ai), FollowRoad(road_aj), FollowRoad(road_f)],
    [EnterIntersection(interroad_c, RIGHT), FollowRoad(road_x), FollowRoad(road_y), FollowRoad(road_z), FollowRoad(road_aa), FollowRoad(road_ab), FollowRoad(road_ac), FollowRoad(road_ad), FollowRoad(road_ae), FollowRoad(road_e)],
    [EnterIntersection(interroad_c, CENTRE), FollowRoad(road_ax), FollowRoad(road_h)],
  ],
  [
    [EnterIntersection(interroad_d, LEFT), FollowRoad(road_ay), FollowRoad(road_az), FollowRoad(road_ba), FollowRoad(road_bb), FollowRoad(road_bc), FollowRoad(road_e)],
    [EnterIntersection(interroad_d, RIGHT), FollowRoad(road_bd), FollowRoad(road_be), FollowRoad(road_bf), FollowRoad(road_bg), FollowRoad(road_bh), FollowRoad(road_bi), FollowRoad(road_bj), FollowRoad(road_bk), FollowRoad(road_f)],
    [EnterIntersection(interroad_d, CENTRE), FollowRoad(road_bl), FollowRoad(road_g)],
  ],
]

intersections = [intersection_0_0]

grass = [
[Vector(5.4, 0.0), Vector(44.6, 0.0), Vector(50.0, 5.4), Vector(50.0, 44.6), Vector(44.6, 50.0), Vector(5.4, 50.0), Vector(0.0, 44.6), Vector(0.0, 5.4)],
[Vector(5.4, 57.0), Vector(44.6, 57.0), Vector(50.0, 62.4), Vector(50.0, 101.6), Vector(44.6, 107.0), Vector(5.4, 107.0), Vector(0.0, 101.6), Vector(0.0, 62.4)],
[Vector(62.4, 0.0), Vector(101.6, 0.0), Vector(107.0, 5.4), Vector(107.0, 44.6), Vector(101.6, 50.0), Vector(62.4, 50.0), Vector(57.0, 44.6), Vector(57.0, 5.4)],
[Vector(62.4, 57.0), Vector(101.6, 57.0), Vector(107.0, 62.4), Vector(107.0, 101.6), Vector(101.6, 107.0), Vector(62.4, 107.0), Vector(57.0, 101.6), Vector(57.0, 62.4)],
]

