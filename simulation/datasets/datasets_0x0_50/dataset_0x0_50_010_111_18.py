from src.util import *
schedule = deque([
  (762, 1, 1),
  (4981, 2, 2),
  (6101, 3, 1),
  (16375, 1, 0),
  (21150, 1, 1),
  (23968, 3, 2),
  (27201, 1, 1),
  (28719, 2, 2),
  (35933, 1, 2),
  (36488, 0, 0),
  (41205, 3, 0),
  (42815, 2, 1),
  (54950, 3, 0),
  (55666, 0, 2),
  (72506, 1, 2),
  (98784, 3, 0),
  (107663, 0, 1),
  (114227, 2, 0),
  (116812, 0, 0),
  (143075, 2, 0),
  (152537, 2, 1),
  (154673, 3, 0),
  (158942, 0, 1),
  (164405, 2, 1),
  (166305, 2, 0),
  (180649, 3, 2),
  (191834, 3, 0),
  (201776, 2, 2),
  (205544, 0, 0),
  (212758, 2, 0),
  (220848, 1, 2),
  (225761, 1, 0),
  (228078, 3, 0),
  (234965, 2, 1),
  (235121, 3, 0),
  (247378, 1, 1),
  (250934, 0, 2),
  (251997, 1, 1),
  (255561, 1, 2),
  (275302, 3, 1),
  (279829, 0, 0),
  (286821, 2, 1),
  (301385, 2, 0),
  (317384, 0, 0),
  (318603, 2, 2),
  (319307, 0, 1),
  (320581, 2, 1),
  (346251, 1, 1),
  (350598, 3, 1),
  (385727, 3, 0),
  (390997, 3, 0),
  (392886, 2, 1),
  (394594, 3, 2),
  (406567, 3, 0),
  (414946, 1, 0),
  (415916, 3, 0),
  (438268, 0, 2),
  (442988, 0, 2),
  (445032, 2, 0),
  (460134, 1, 0),
  (461130, 3, 2),
  (475207, 2, 1),
  (483763, 0, 2),
  (485066, 0, 1),
  (493274, 3, 1),
  (495754, 2, 2),
  (498238, 2, 1),
  (499118, 2, 1),
  (503995, 2, 1),
  (515668, 3, 2),
  (516652, 2, 1),
  (526892, 2, 0),
  (544115, 3, 1),
  (558150, 2, 0),
  (559627, 0, 2),
  (563015, 3, 2),
  (563755, 1, 1),
  (576230, 1, 0),
  (585953, 3, 0),
  (602088, 0, 2),
  (615537, 3, 0),
  (624636, 2, 1),
  (626456, 0, 2),
  (629556, 0, 1),
  (636968, 1, 2),
  (650232, 2, 0),
  (652362, 1, 2),
  (653305, 2, 0),
  (657308, 3, 2),
  (670268, 1, 0),
  (681363, 3, 0),
  (696996, 3, 2),
  (705021, 0, 1),
  (705545, 1, 0),
  (717087, 0, 0),
  (730151, 2, 2),
  (731658, 2, 0),
  (731695, 3, 2),
  (736889, 0, 1),
  (737380, 2, 1),
  (738994, 3, 2),
  (739944, 3, 1),
  (743158, 2, 0),
  (745900, 0, 0),
  (748837, 2, 1),
  (749313, 0, 2),
  (753455, 1, 2),
  (757858, 2, 0),
  (758462, 3, 1),
  (768394, 3, 0),
  (770798, 2, 0),
  (771594, 0, 1),
  (771762, 3, 2),
  (773524, 3, 0),
  (791661, 1, 0),
  (797332, 3, 0),
  (825245, 0, 0),
  (828720, 3, 0),
  (829280, 0, 2),
  (830464, 2, 0),
  (831174, 0, 0),
  (832750, 1, 1),
  (851932, 2, 2),
  (856484, 1, 2),
  (859013, 0, 0),
  (867239, 0, 2),
  (886974, 2, 0),
  (894844, 0, 2),
  (895631, 1, 1),
  (906717, 2, 0),
  (907224, 3, 0),
  (908451, 3, 2),
  (911021, 1, 2),
  (919153, 1, 2),
  (925189, 0, 2),
  (932555, 1, 0),
  (937752, 3, 2),
  (940356, 3, 2),
  (941279, 3, 0),
  (944255, 3, 0),
  (945457, 1, 0),
  (947369, 3, 2),
  (959019, 2, 0),
  (966798, 2, 2),
  (974439, 2, 0),
  (980674, 2, 0),
  (994038, 2, 2),
  (995845, 2, 1),
  (997484, 3, 2),
  (1016955, 1, 0),
  (1022305, 2, 0),
  (1039963, 0, 2),
  (1045712, 0, 0),
  (1056360, 3, 1),
  (1058004, 3, 2),
  (1058343, 3, 0),
  (1078206, 1, 2),
  (1078909, 2, 2),
  (1080546, 0, 1),
  (1082175, 0, 0),
  (1083771, 1, 0),
  (1087037, 1, 1),
  (1088251, 2, 1),
  (1091609, 1, 2),
  (1093647, 3, 2),
  (1103498, 1, 0),
  (1106313, 3, 2),
  (1114751, 0, 1),
  (1119645, 1, 1),
  (1129186, 1, 2),
  (1132155, 0, 1),
  (1134080, 1, 0),
  (1136309, 1, 0),
  (1136992, 3, 2),
  (1137291, 2, 2),
  (1145030, 1, 1),
  (1148478, 0, 2),
  (1158490, 2, 1),
  (1162034, 2, 0),
  (1186661, 3, 2),
  (1189404, 0, 2),
  (1196372, 1, 0),
  (1198589, 2, 0),
  (1205223, 3, 1),
  (1209526, 1, 2),
  (1214575, 2, 1),
  (1218286, 1, 0),
  (1223246, 2, 2),
  (1231849, 1, 2),
  (1233499, 2, 0),
  (1237490, 0, 2),
  (1249683, 0, 0),
  (1253055, 1, 2),
  (1258986, 3, 1),
  (1264360, 3, 1),
  (1286559, 0, 1),
  (1289364, 3, 0),
  (1289688, 2, 2),
  (1293252, 3, 0),
  (1293976, 2, 2),
  (1318984, 2, 2),
  (1335466, 2, 1),
  (1336424, 2, 1),
  (1341732, 0, 1),
  (1342353, 3, 0),
  (1353324, 3, 0),
  (1356121, 0, 1),
  (1360859, 3, 0),
  (1363643, 2, 1),
  (1376428, 2, 1),
  (1414440, 1, 0),
  (1427704, 3, 1),
  (1435401, 0, 0),
  (1443777, 1, 2),
  (1478172, 2, 2),
  (1478909, 3, 0),
  (1479499, 1, 1),
  (1480407, 0, 0),
  (1490493, 0, 0),
  (1497580, 0, 2),
  (1500144, 3, 1),
  (1500602, 3, 1),
  (1516225, 0, 1),
  (1517931, 0, 0),
  (1522540, 0, 0),
  (1526696, 1, 0),
  (1532706, 3, 2),
  (1552465, 2, 2),
  (1556219, 3, 2),
  (1556865, 3, 2),
  (1560255, 1, 0),
  (1560995, 3, 0),
  (1564107, 2, 1),
  (1565240, 0, 0),
  (1569791, 3, 2),
  (1570159, 0, 0),
  (1572503, 2, 1),
  (1578231, 1, 2),
  (1594853, 1, 2),
  (1611079, 2, 1),
  (1625470, 1, 2),
  (1625926, 0, 0),
  (1628617, 0, 2),
  (1631262, 2, 0),
  (1637974, 0, 0),
  (1639387, 2, 2),
  (1639560, 3, 1),
  (1640157, 1, 2),
  (1651961, 3, 0),
  (1658453, 3, 1),
  (1660162, 3, 1),
  (1674923, 1, 1),
  (1676551, 3, 0),
  (1681982, 1, 2),
  (1689270, 1, 2),
  (1693958, 3, 0),
  (1695627, 1, 0),
  (1697650, 3, 1),
  (1700287, 3, 2),
  (1709772, 2, 1),
  (1714496, 3, 2),
  (1719150, 3, 1),
  (1721785, 3, 1),
  (1722374, 1, 2),
  (1723132, 2, 0),
  (1726593, 2, 2),
  (1728865, 3, 0),
  (1730286, 1, 2),
  (1736932, 3, 1),
  (1740937, 0, 2),
  (1745321, 1, 1),
  (1746713, 0, 0),
  (1748985, 0, 0),
  (1751169, 2, 1),
  (1752463, 1, 1),
  (1758834, 2, 0),
  (1779850, 1, 1),
  (1780030, 1, 0),
  (1798723, 3, 1),
  (1827699, 2, 2),
  (1845229, 3, 2),
  (1850545, 3, 1),
  (1850795, 3, 1),
  (1851302, 2, 1),
  (1860740, 3, 2),
  (1861706, 1, 0),
  (1863192, 0, 0),
  (1864195, 2, 2),
  (1876283, 0, 0),
  (1881853, 3, 0),
  (1884182, 1, 0),
  (1886876, 1, 0),
  (1888551, 1, 0),
  (1891777, 2, 1),
  (1891950, 1, 2),
  (1892094, 3, 2),
  (1902973, 1, 2),
  (1905317, 2, 0),
  (1909466, 3, 2),
  (1918340, 0, 2),
  (1922707, 1, 0),
  (1929907, 0, 2),
  (1946102, 1, 2),
  (1960244, 1, 0),
  (1961479, 3, 1),
  (1961499, 1, 1),
  (1963313, 0, 0),
  (1971345, 0, 1),
  (1978513, 0, 1),
  (1986657, 0, 1),
  (1989680, 1, 2),
  (1995355, 1, 2),
  (1996960, 3, 0),
  (1999271, 0, 0),
  (2001920, 2, 0),
  (2002850, 2, 2),
  (2006101, 3, 2),
  (2011148, 0, 2),
  (2029788, 1, 0),
  (2038732, 0, 1),
  (2046270, 0, 2),
  (2049643, 0, 0),
  (2056144, 3, 2),
  (2059241, 2, 2),
  (2062245, 0, 2),
  (2067874, 2, 0),
  (2071094, 3, 1),
  (2085033, 2, 2),
  (2088659, 0, 0),
  (2097774, 0, 1),
  (2103510, 1, 0),
  (2107696, 2, 1),
  (2109321, 1, 2),
  (2113186, 0, 0),
  (2121558, 3, 2),
  (2123436, 1, 1),
  (2123847, 1, 1),
  (2141672, 2, 1),
  (2149233, 1, 2),
  (2154536, 0, 2),
  (2159891, 0, 0),
  (2166539, 2, 0),
  (2169906, 2, 1),
  (2171769, 3, 0),
  (2173501, 2, 0),
  (2185438, 1, 2),
  (2187166, 2, 1),
  (2187705, 1, 2),
  (2193258, 2, 2),
  (2194499, 3, 1),
  (2215597, 2, 1),
  (2223091, 2, 1),
  (2234241, 2, 1),
  (2235612, 2, 0),
  (2236964, 2, 1),
  (2239628, 2, 0),
  (2242787, 2, 2),
  (2252473, 1, 1),
  (2263921, 2, 2),
  (2268152, 0, 1),
  (2271805, 1, 1),
  (2282812, 3, 1),
  (2293865, 1, 1),
  (2305538, 3, 0),
  (2315328, 1, 0),
  (2324250, 2, 1),
  (2337110, 1, 1),
  (2345741, 1, 1),
  (2346090, 2, 2),
  (2349092, 3, 0),
  (2353585, 0, 0),
  (2357068, 2, 1),
  (2361742, 0, 0),
  (2366312, 0, 2),
  (2371524, 3, 0),
  (2373796, 3, 2),
  (2377430, 2, 0),
  (2381838, 3, 1),
  (2385166, 1, 1),
  (2387780, 1, 1),
  (2389872, 2, 2),
  (2392648, 1, 2),
  (2392737, 1, 0),
  (2403007, 0, 2),
  (2404091, 0, 2),
  (2408510, 3, 0),
  (2408859, 0, 1),
  (2415269, 2, 2),
  (2416617, 1, 2),
  (2424497, 2, 0),
  (2454666, 0, 1),
  (2458385, 1, 2),
  (2463947, 1, 0),
  (2465959, 0, 1),
  (2469986, 1, 2),
  (2470175, 0, 2),
  (2470307, 2, 1),
  (2473989, 1, 0),
  (2478625, 3, 1),
  (2484897, 3, 0),
  (2498045, 0, 0),
  (2499917, 0, 1),
  (2501443, 1, 0),
  (2501483, 2, 2),
  (2505913, 0, 1),
  (2511147, 2, 0),
  (2516519, 2, 0),
  (2521981, 1, 0),
  (2525892, 3, 2),
  (2531254, 3, 1),
  (2532735, 2, 2),
  (2542196, 3, 1),
  (2542533, 0, 0),
  (2543204, 2, 2),
  (2565607, 0, 2),
  (2566892, 0, 1),
  (2569422, 3, 2),
  (2575887, 3, 0),
  (2584978, 3, 1),
  (2588396, 3, 2),
  (2589668, 2, 1),
  (2590122, 3, 1),
  (2592038, 1, 2),
  (2593387, 2, 0),
  (2594386, 0, 2),
  (2597432, 0, 1),
  (2597841, 3, 2),
  (2608256, 1, 0),
  (2615774, 0, 0),
  (2621912, 0, 2),
  (2622836, 0, 2),
  (2623313, 1, 2),
  (2629538, 0, 2),
  (2633077, 2, 1),
  (2649169, 2, 0),
  (2649565, 3, 1),
  (2654698, 3, 2),
  (2657784, 0, 2),
  (2670011, 0, 2),
  (2693188, 2, 1),
  (2694462, 0, 0),
  (2698224, 1, 0),
  (2704545, 2, 1),
  (2706977, 2, 1),
  (2715154, 2, 0),
  (2717578, 3, 1),
  (2732272, 2, 1),
  (2736199, 3, 0),
  (2743635, 0, 0),
  (2750682, 3, 2),
  (2754848, 3, 1),
  (2761222, 0, 1),
  (2762859, 3, 0),
  (2763162, 3, 2),
  (2763479, 2, 2),
  (2769039, 0, 1),
  (2771016, 3, 0),
  (2772395, 3, 1),
  (2786433, 2, 0),
  (2788991, 2, 2),
  (2795465, 2, 1),
  (2796365, 3, 0),
  (2797580, 0, 0),
  (2798262, 0, 1),
  (2800614, 0, 0),
  (2810189, 2, 0),
  (2811839, 3, 0),
  (2816213, 0, 2),
  (2821339, 0, 0),
  (2826973, 3, 0),
  (2828652, 2, 2),
  (2838945, 0, 2),
  (2844782, 0, 2),
  (2850212, 0, 1),
  (2851487, 2, 0),
  (2852240, 1, 2),
  (2853832, 1, 0),
  (2854448, 1, 2),
  (2854723, 0, 0),
  (2866279, 0, 0),
  (2873802, 0, 0),
  (2874451, 3, 0),
  (2886709, 0, 1),
  (2893592, 2, 0),
  (2895263, 1, 1),
  (2898502, 2, 1),
  (2898784, 1, 2),
  (2915873, 0, 2),
  (2917944, 2, 2),
  (2922185, 3, 1),
  (2924546, 1, 2),
  (2927669, 3, 1),
  (2932054, 2, 0),
  (2935089, 3, 1),
  (2943109, 0, 2),
  (2943870, 3, 0),
  (2944841, 0, 1),
  (2952872, 3, 2),
  (2953876, 2, 0),
  (2967491, 2, 0),
  (2982207, 2, 1),
  (2983059, 2, 1),
  (2983445, 3, 0),
  (2992466, 3, 0),
  (2992484, 3, 1),
  (2995194, 0, 1),
  (3001038, 1, 1),
  (3002227, 0, 1),
  (3023576, 2, 2),
  (3023728, 3, 2),
  (3036511, 3, 1),
  (3046560, 2, 1),
  (3046684, 1, 1),
  (3047836, 0, 0),
  (3048325, 3, 2),
  (3049122, 2, 2),
  (3050736, 0, 0),
  (3055133, 0, 2),
  (3068112, 0, 0),
  (3077221, 0, 2),
  (3089333, 0, 2),
  (3099488, 3, 2),
  (3114777, 1, 1),
  (3119288, 0, 1),
  (3124595, 3, 0),
  (3127864, 1, 2),
  (3134774, 1, 1),
  (3140961, 0, 1),
  (3143796, 3, 0),
  (3144815, 3, 1),
  (3153526, 2, 1),
  (3153855, 3, 0),
  (3179394, 1, 0),
  (3187605, 3, 0),
  (3190715, 3, 2),
  (3190958, 3, 1),
  (3195143, 1, 2),
  (3195436, 1, 0),
  (3203129, 3, 0),
  (3210053, 1, 1),
  (3210478, 3, 2),
  (3232657, 3, 1),
  (3236147, 3, 2),
  (3241051, 1, 0),
  (3259750, 1, 0),
  (3265432, 0, 1),
  (3267639, 0, 2),
  (3268249, 1, 0),
  (3280237, 3, 0),
  (3281816, 1, 1),
  (3293168, 3, 0),
  (3301529, 2, 2),
  (3304679, 2, 2),
  (3317936, 0, 1),
  (3323951, 2, 0),
  (3341694, 1, 0),
  (3343221, 1, 0),
  (3346370, 2, 0),
  (3358033, 3, 2),
  (3373255, 3, 2),
  (3381642, 2, 2),
  (3391475, 2, 0),
  (3391884, 1, 2),
  (3408892, 0, 2),
  (3410248, 2, 1),
  (3416297, 2, 2),
  (3422392, 1, 1),
  (3424620, 0, 0),
  (3425635, 0, 0),
  (3434464, 1, 1),
  (3452534, 1, 0),
  (3463035, 0, 1),
  (3470140, 1, 1),
  (3473063, 3, 1),
  (3474244, 1, 1),
  (3479919, 0, 1),
  (3485247, 1, 2),
  (3492236, 1, 2),
  (3492266, 3, 2),
  (3494506, 1, 0),
  (3500970, 2, 0),
  (3501250, 0, 1),
  (3520845, 2, 1),
  (3522583, 0, 0),
  (3536063, 3, 1),
  (3536505, 3, 0),
  (3538441, 3, 1),
  (3539459, 1, 2),
  (3540174, 3, 2),
  (3567154, 0, 1),
  (3567521, 0, 1),
  (3569764, 1, 0),
  (3570081, 0, 1),
  (3580978, 3, 2),
  (3588714, 3, 0),
  (3589340, 1, 1),
  (3589404, 1, 0),
  (3593283, 3, 2),
  (3593679, 0, 2),
  (3596355, 0, 2),
])
