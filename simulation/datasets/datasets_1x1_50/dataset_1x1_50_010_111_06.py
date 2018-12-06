from src.util import *
schedule = deque([
  (2421, 1, 5),
  (4261, 1, 0),
  (4903, 5, 6),
  (9183, 7, 7),
  (14351, 5, 3),
  (16330, 1, 2),
  (16390, 3, 7),
  (24346, 3, 3),
  (25360, 5, 3),
  (33322, 2, 6),
  (33468, 4, 2),
  (38340, 5, 5),
  (51062, 3, 3),
  (51896, 4, 6),
  (53799, 7, 0),
  (55236, 7, 4),
  (58626, 4, 3),
  (68949, 6, 1),
  (73190, 7, 5),
  (74535, 1, 4),
  (75827, 6, 0),
  (81412, 7, 2),
  (85016, 3, 4),
  (91578, 5, 3),
  (98822, 2, 3),
  (103846, 7, 4),
  (112168, 5, 6),
  (112974, 2, 1),
  (115892, 2, 7),
  (119987, 6, 0),
  (122635, 1, 4),
  (129128, 7, 5),
  (130348, 3, 3),
  (131350, 1, 3),
  (134697, 5, 3),
  (142120, 1, 4),
  (144117, 3, 2),
  (150969, 0, 4),
  (154601, 2, 6),
  (167474, 1, 4),
  (169875, 4, 5),
  (174724, 3, 3),
  (191962, 3, 7),
  (192214, 7, 0),
  (194837, 6, 0),
  (204316, 3, 3),
  (205482, 1, 7),
  (212741, 1, 6),
  (216820, 7, 7),
  (217744, 2, 1),
  (223954, 0, 0),
  (225937, 2, 7),
  (231320, 7, 4),
  (233322, 5, 3),
  (248697, 7, 3),
  (264570, 4, 7),
  (271713, 0, 4),
  (287700, 2, 3),
  (289642, 0, 7),
  (292424, 5, 6),
  (310896, 3, 0),
  (312607, 2, 5),
  (312897, 1, 0),
  (315315, 2, 6),
  (326178, 2, 3),
  (326288, 2, 1),
  (331283, 1, 4),
  (331892, 7, 2),
  (339631, 2, 2),
  (347362, 5, 0),
  (349063, 6, 4),
  (352230, 7, 0),
  (358162, 5, 3),
  (359590, 1, 0),
  (360590, 4, 7),
  (362964, 5, 3),
  (363190, 1, 5),
  (368301, 1, 0),
  (372594, 3, 3),
  (380105, 6, 1),
  (380254, 5, 7),
  (382907, 1, 1),
  (384661, 2, 3),
  (388282, 7, 3),
  (389857, 3, 5),
  (394903, 3, 3),
  (404461, 3, 3),
  (405581, 6, 6),
  (411551, 2, 6),
  (417116, 3, 6),
  (424790, 7, 6),
  (425550, 2, 3),
  (428974, 4, 2),
  (430789, 5, 6),
  (434293, 5, 3),
  (438702, 2, 7),
  (445689, 2, 0),
  (463773, 0, 0),
  (467783, 7, 0),
  (471117, 2, 3),
  (480194, 6, 0),
  (481056, 2, 7),
  (490801, 2, 3),
  (494762, 1, 7),
  (497573, 1, 0),
  (506937, 2, 7),
  (508852, 0, 0),
  (516561, 4, 3),
  (518985, 4, 4),
  (531478, 7, 4),
  (532378, 1, 4),
  (532916, 6, 3),
  (535053, 6, 3),
  (536938, 1, 0),
  (549262, 1, 3),
  (551860, 7, 2),
  (556061, 6, 2),
  (563497, 0, 0),
  (569300, 2, 5),
  (571648, 6, 4),
  (573911, 4, 3),
  (589306, 5, 3),
  (590589, 7, 6),
  (596695, 6, 3),
  (605407, 5, 6),
  (608108, 2, 5),
  (612086, 4, 7),
  (619274, 4, 0),
  (621907, 3, 3),
  (622304, 1, 4),
  (635482, 6, 3),
  (636574, 7, 0),
  (656327, 1, 0),
  (657708, 5, 3),
  (661081, 1, 0),
  (663816, 7, 0),
  (671646, 2, 2),
  (675778, 6, 0),
  (685509, 2, 3),
  (693525, 5, 3),
  (695007, 7, 3),
  (695814, 0, 0),
  (701297, 3, 3),
  (703669, 6, 0),
  (719387, 7, 4),
  (739060, 0, 6),
  (744181, 5, 3),
  (747115, 7, 0),
  (748482, 6, 3),
  (754578, 2, 2),
  (762680, 1, 3),
  (766529, 0, 4),
  (783081, 2, 3),
  (786764, 2, 6),
  (800342, 7, 5),
  (806203, 7, 3),
  (806994, 4, 2),
  (810504, 1, 6),
  (810534, 5, 4),
  (815040, 0, 2),
  (833851, 5, 3),
  (837196, 6, 3),
  (837604, 7, 4),
  (848526, 1, 0),
  (852864, 0, 0),
  (856827, 0, 0),
  (867618, 6, 6),
  (877262, 0, 7),
  (889921, 4, 1),
  (911457, 5, 1),
  (925853, 3, 3),
  (929290, 6, 1),
  (933833, 2, 2),
  (956068, 3, 7),
  (962494, 6, 4),
  (972379, 1, 0),
  (980857, 2, 3),
  (983151, 2, 4),
  (996720, 7, 6),
  (1001790, 1, 7),
  (1017678, 1, 4),
  (1022109, 6, 3),
  (1027025, 4, 7),
  (1032098, 1, 0),
  (1033328, 1, 7),
  (1054019, 3, 3),
  (1058506, 6, 0),
  (1078044, 1, 0),
  (1081349, 7, 4),
  (1085689, 0, 0),
  (1088426, 2, 7),
  (1108999, 1, 7),
  (1110694, 7, 7),
  (1115855, 1, 0),
  (1117622, 7, 6),
  (1120387, 5, 7),
  (1125905, 3, 0),
  (1132478, 7, 7),
  (1145294, 3, 4),
  (1148288, 6, 5),
  (1160384, 0, 7),
  (1162668, 5, 2),
  (1162711, 4, 2),
  (1164994, 3, 3),
  (1169299, 0, 0),
  (1170527, 5, 3),
  (1192074, 1, 0),
  (1199036, 5, 3),
  (1226109, 5, 3),
  (1227946, 7, 4),
  (1236217, 6, 0),
  (1237638, 6, 4),
  (1243651, 7, 7),
  (1246381, 6, 7),
  (1247119, 6, 3),
  (1264607, 6, 1),
  (1265634, 2, 3),
  (1273672, 2, 3),
  (1290402, 3, 1),
  (1291718, 5, 3),
  (1301574, 0, 6),
  (1310409, 6, 0),
  (1315936, 4, 2),
  (1320034, 4, 4),
  (1321381, 4, 3),
  (1343601, 6, 2),
  (1352922, 7, 0),
  (1354118, 5, 3),
  (1376582, 3, 3),
  (1376605, 7, 0),
  (1378036, 0, 3),
  (1387189, 6, 4),
  (1404839, 4, 3),
  (1405588, 3, 6),
  (1411065, 1, 0),
  (1419621, 0, 3),
  (1441309, 4, 7),
  (1453045, 7, 6),
  (1453909, 7, 0),
  (1455500, 0, 3),
  (1462674, 1, 0),
  (1467843, 3, 7),
  (1468063, 4, 7),
  (1490163, 6, 7),
  (1490943, 5, 2),
  (1499231, 0, 7),
  (1502804, 2, 4),
  (1523115, 3, 2),
  (1539325, 1, 5),
  (1551612, 3, 2),
  (1553222, 1, 7),
  (1554068, 1, 0),
  (1556827, 5, 2),
  (1559555, 2, 3),
  (1563545, 4, 2),
  (1569367, 4, 3),
  (1570153, 6, 5),
  (1570454, 1, 0),
  (1578775, 5, 3),
  (1579088, 3, 6),
  (1579296, 1, 4),
  (1579461, 7, 5),
  (1581074, 3, 2),
  (1581712, 5, 3),
  (1586999, 7, 0),
  (1589643, 3, 6),
  (1591029, 6, 0),
  (1596817, 2, 7),
  (1607168, 3, 2),
  (1608594, 3, 3),
  (1611539, 3, 3),
  (1613655, 6, 5),
  (1616335, 7, 3),
  (1616748, 0, 1),
  (1618408, 4, 3),
  (1626689, 4, 2),
  (1630622, 3, 6),
  (1630896, 4, 2),
  (1631553, 3, 3),
  (1632323, 5, 3),
  (1636796, 4, 3),
  (1638559, 4, 4),
  (1639587, 4, 7),
  (1654725, 7, 6),
  (1663623, 4, 1),
  (1670158, 4, 3),
  (1671341, 2, 6),
  (1672371, 5, 7),
  (1689764, 0, 4),
  (1696945, 1, 4),
  (1702836, 5, 7),
  (1710199, 0, 0),
  (1718585, 0, 0),
  (1719558, 5, 2),
  (1721513, 2, 3),
  (1727532, 7, 0),
  (1728808, 3, 3),
  (1741332, 6, 7),
  (1760995, 3, 3),
  (1762314, 7, 0),
  (1766314, 7, 6),
  (1780514, 5, 6),
  (1784966, 0, 3),
  (1790202, 1, 0),
  (1791631, 0, 0),
  (1794754, 3, 7),
  (1808689, 7, 0),
  (1812899, 0, 3),
  (1826882, 1, 5),
  (1829566, 1, 4),
  (1829800, 2, 5),
  (1837121, 6, 1),
  (1841259, 2, 6),
  (1842943, 4, 3),
  (1845945, 5, 3),
  (1851623, 3, 1),
  (1863949, 2, 3),
  (1866020, 3, 3),
  (1870846, 4, 3),
  (1871220, 6, 0),
  (1873070, 7, 4),
  (1873328, 5, 1),
  (1885374, 3, 7),
  (1886725, 3, 0),
  (1895211, 4, 7),
  (1896059, 0, 0),
  (1898729, 7, 0),
  (1904592, 3, 5),
  (1916836, 3, 7),
  (1928121, 5, 6),
  (1932669, 3, 7),
  (1936713, 1, 0),
  (1939761, 2, 3),
  (1952127, 2, 6),
  (1979087, 0, 0),
  (2008180, 4, 4),
  (2015742, 3, 1),
  (2017690, 7, 1),
  (2021281, 5, 4),
  (2026337, 3, 0),
  (2027440, 0, 6),
  (2043734, 6, 6),
  (2046573, 4, 2),
  (2047036, 2, 3),
  (2048240, 0, 0),
  (2059831, 6, 4),
  (2060079, 6, 0),
  (2067737, 6, 2),
  (2070337, 2, 6),
  (2070503, 0, 5),
  (2073394, 5, 3),
  (2075015, 6, 0),
  (2075222, 7, 0),
  (2092664, 4, 4),
  (2102651, 0, 5),
  (2104042, 2, 3),
  (2108260, 5, 2),
  (2109322, 3, 1),
  (2125698, 3, 3),
  (2134738, 7, 0),
  (2140187, 1, 0),
  (2145267, 4, 3),
  (2166736, 5, 3),
  (2175333, 5, 4),
  (2177372, 2, 2),
  (2179196, 1, 7),
  (2186081, 7, 5),
  (2192824, 2, 3),
  (2201469, 6, 1),
  (2219384, 4, 4),
  (2242201, 4, 6),
  (2242292, 5, 7),
  (2257512, 5, 5),
  (2267888, 7, 3),
  (2268255, 7, 5),
  (2286634, 6, 0),
  (2288227, 2, 3),
  (2290822, 4, 3),
  (2295586, 0, 0),
  (2299481, 6, 0),
  (2300545, 2, 2),
  (2305813, 4, 3),
  (2315329, 3, 3),
  (2319366, 5, 6),
  (2330250, 0, 5),
  (2333779, 4, 4),
  (2338559, 0, 0),
  (2342611, 0, 1),
  (2344714, 3, 3),
  (2346585, 1, 6),
  (2353615, 3, 2),
  (2353830, 6, 0),
  (2380203, 6, 6),
  (2383588, 6, 3),
  (2384420, 4, 3),
  (2384634, 3, 5),
  (2389083, 2, 7),
  (2404778, 7, 6),
  (2409253, 1, 0),
  (2411671, 3, 3),
  (2420154, 6, 4),
  (2432187, 2, 1),
  (2434985, 1, 7),
  (2455744, 1, 3),
  (2465181, 0, 6),
  (2469283, 5, 3),
  (2478916, 6, 4),
  (2479952, 1, 0),
  (2481906, 6, 5),
  (2484621, 5, 3),
  (2497293, 6, 0),
  (2497965, 6, 4),
  (2507092, 6, 2),
  (2516732, 4, 3),
  (2528951, 3, 1),
  (2529413, 7, 7),
  (2534626, 0, 0),
  (2538427, 6, 3),
  (2546638, 2, 3),
  (2549761, 3, 7),
  (2554117, 1, 3),
  (2555161, 6, 0),
  (2555447, 6, 0),
  (2562228, 4, 4),
  (2582189, 1, 3),
  (2582795, 4, 6),
  (2584843, 3, 2),
  (2587608, 5, 7),
  (2591078, 3, 1),
  (2592120, 3, 7),
  (2595069, 6, 0),
  (2596633, 3, 3),
  (2597987, 2, 3),
  (2602574, 7, 3),
  (2604796, 2, 3),
  (2605920, 3, 3),
  (2608919, 5, 7),
  (2614624, 3, 2),
  (2617148, 2, 3),
  (2630450, 5, 3),
  (2637828, 1, 0),
  (2639436, 4, 3),
  (2645477, 1, 1),
  (2645631, 7, 0),
  (2646746, 1, 0),
  (2647069, 1, 0),
  (2652994, 7, 7),
  (2659003, 2, 2),
  (2665932, 1, 0),
  (2668985, 3, 3),
  (2670226, 2, 6),
  (2677810, 3, 7),
  (2680455, 4, 1),
  (2702927, 7, 3),
  (2706127, 5, 2),
  (2715958, 7, 7),
  (2724296, 6, 2),
  (2724674, 5, 3),
  (2727924, 1, 0),
  (2728136, 7, 5),
  (2729916, 7, 7),
  (2734218, 2, 1),
  (2740605, 3, 2),
  (2747337, 2, 2),
  (2756675, 6, 3),
  (2758446, 0, 7),
  (2763711, 3, 3),
  (2765857, 1, 0),
  (2770515, 7, 7),
  (2779427, 0, 7),
  (2788100, 7, 4),
  (2800213, 6, 4),
  (2802810, 5, 7),
  (2805991, 7, 4),
  (2809840, 0, 3),
  (2815707, 1, 7),
  (2825968, 7, 3),
  (2829502, 4, 6),
  (2829742, 4, 7),
  (2830972, 6, 0),
  (2835977, 0, 0),
  (2842570, 3, 3),
  (2851399, 2, 2),
  (2852854, 2, 3),
  (2863909, 1, 0),
  (2875953, 4, 2),
  (2889309, 7, 0),
  (2896282, 5, 3),
  (2907611, 3, 3),
  (2912836, 6, 5),
  (2913046, 6, 0),
  (2921942, 5, 3),
  (2927529, 1, 0),
  (2928994, 6, 2),
  (2943673, 0, 0),
  (2943713, 1, 7),
  (2955568, 0, 0),
  (2961826, 0, 0),
  (2964024, 6, 7),
  (2967940, 7, 0),
  (2969320, 3, 2),
  (2975709, 5, 3),
  (2976481, 5, 3),
  (2988034, 4, 2),
  (2998486, 3, 6),
  (3004282, 0, 7),
  (3008759, 5, 2),
  (3010856, 0, 5),
  (3017690, 0, 0),
  (3030210, 5, 1),
  (3036413, 4, 7),
  (3036948, 6, 4),
  (3046944, 7, 7),
  (3047178, 2, 4),
  (3056301, 2, 3),
  (3058273, 7, 0),
  (3071195, 0, 2),
  (3074060, 7, 7),
  (3088764, 4, 7),
  (3106432, 5, 1),
  (3108777, 2, 7),
  (3113553, 1, 0),
  (3119553, 4, 3),
  (3122641, 6, 0),
  (3123509, 2, 3),
  (3141095, 6, 4),
  (3141160, 4, 0),
  (3142308, 0, 0),
  (3145316, 4, 7),
  (3165161, 5, 4),
  (3170013, 3, 7),
  (3179495, 2, 6),
  (3185588, 7, 7),
  (3193473, 3, 3),
  (3202790, 7, 7),
  (3219714, 0, 0),
  (3220932, 5, 6),
  (3223321, 2, 3),
  (3226598, 0, 0),
  (3228011, 0, 0),
  (3228263, 6, 1),
  (3228406, 3, 6),
  (3243740, 0, 0),
  (3247645, 1, 7),
  (3249960, 4, 3),
  (3252216, 6, 0),
  (3253083, 4, 3),
  (3259099, 2, 3),
  (3264087, 7, 0),
  (3275468, 1, 0),
  (3275961, 3, 5),
  (3286137, 6, 2),
  (3290144, 1, 4),
  (3294840, 3, 3),
  (3304245, 5, 3),
  (3306342, 0, 0),
  (3309020, 3, 2),
  (3317146, 6, 3),
  (3318403, 0, 3),
  (3331348, 2, 2),
  (3334201, 5, 6),
  (3335194, 0, 4),
  (3336024, 5, 6),
  (3338273, 1, 3),
  (3341825, 0, 3),
  (3352241, 1, 0),
  (3355099, 5, 3),
  (3364202, 5, 4),
  (3373207, 7, 7),
  (3376481, 5, 0),
  (3387845, 2, 6),
  (3392803, 3, 6),
  (3397121, 1, 4),
  (3411228, 0, 0),
  (3412493, 1, 0),
  (3412839, 7, 0),
  (3443010, 6, 6),
  (3444483, 5, 3),
  (3448331, 6, 0),
  (3448994, 6, 0),
  (3451397, 7, 7),
  (3452658, 2, 3),
  (3454340, 1, 3),
  (3465910, 6, 7),
  (3478673, 4, 0),
  (3504369, 5, 7),
  (3508773, 1, 0),
  (3509570, 2, 3),
  (3511173, 0, 2),
  (3511442, 7, 7),
  (3516498, 5, 3),
  (3552937, 5, 6),
  (3553827, 7, 5),
  (3560494, 2, 3),
  (3566010, 1, 3),
  (3579282, 4, 3),
  (3592920, 5, 1),
  (3595491, 0, 0),
  (3596226, 2, 3),
  (3597165, 6, 3),
])
