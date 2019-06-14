from src.util import *
schedule = deque([
  (1842, 2, 3),
  (12778, 0, 0),
  (13210, 4, 6),
  (22888, 1, 4),
  (32912, 4, 7),
  (33728, 3, 3),
  (35473, 5, 3),
  (35851, 7, 4),
  (41661, 0, 4),
  (44599, 3, 6),
  (59399, 7, 0),
  (70503, 6, 0),
  (70752, 1, 7),
  (76311, 7, 5),
  (81471, 7, 6),
  (108949, 1, 0),
  (109962, 0, 0),
  (113020, 6, 3),
  (113026, 7, 0),
  (125384, 3, 3),
  (131128, 2, 3),
  (133777, 2, 2),
  (144489, 0, 7),
  (154489, 6, 6),
  (164942, 6, 0),
  (170536, 5, 3),
  (174757, 3, 6),
  (175293, 5, 3),
  (179842, 7, 0),
  (194017, 6, 7),
  (205929, 5, 2),
  (210074, 5, 3),
  (213798, 1, 4),
  (220048, 4, 3),
  (236703, 7, 0),
  (248191, 3, 3),
  (248961, 0, 7),
  (250014, 3, 5),
  (251876, 7, 7),
  (252702, 4, 1),
  (252752, 6, 2),
  (258398, 6, 4),
  (273172, 5, 3),
  (282714, 7, 0),
  (287498, 3, 5),
  (288120, 2, 3),
  (294867, 3, 2),
  (296524, 3, 2),
  (298086, 2, 7),
  (302988, 6, 0),
  (313168, 2, 6),
  (322319, 6, 7),
  (329061, 1, 0),
  (332136, 7, 3),
  (347596, 1, 0),
  (349187, 3, 3),
  (350344, 3, 3),
  (358145, 0, 0),
  (359084, 0, 4),
  (359376, 5, 3),
  (363110, 0, 4),
  (365404, 1, 3),
  (379455, 6, 0),
  (389000, 0, 2),
  (391315, 7, 0),
  (405125, 3, 6),
  (408906, 0, 3),
  (416091, 6, 2),
  (416373, 1, 4),
  (420561, 7, 0),
  (422771, 0, 0),
  (432002, 6, 3),
  (436222, 6, 3),
  (436920, 2, 3),
  (441325, 5, 3),
  (453184, 4, 2),
  (453304, 4, 6),
  (455342, 6, 0),
  (467086, 6, 0),
  (467551, 3, 5),
  (469629, 2, 1),
  (489820, 7, 5),
  (503280, 6, 1),
  (527755, 4, 3),
  (528359, 0, 7),
  (531376, 2, 3),
  (535041, 7, 4),
  (538209, 7, 3),
  (553962, 2, 4),
  (558165, 6, 4),
  (561372, 6, 0),
  (564858, 5, 7),
  (568908, 5, 0),
  (578841, 3, 3),
  (579435, 1, 0),
  (582126, 3, 3),
  (594156, 3, 7),
  (594436, 6, 0),
  (595056, 6, 0),
  (597934, 5, 6),
  (602429, 2, 2),
  (610309, 1, 0),
  (633068, 5, 2),
  (635082, 3, 2),
  (636280, 1, 0),
  (638899, 0, 0),
  (661973, 7, 4),
  (668898, 2, 2),
  (696908, 2, 7),
  (698150, 2, 3),
  (720283, 2, 7),
  (721663, 5, 1),
  (723158, 3, 3),
  (733493, 0, 1),
  (734451, 0, 1),
  (740569, 5, 6),
  (758638, 3, 2),
  (762661, 3, 1),
  (766816, 2, 6),
  (769390, 4, 3),
  (770653, 5, 2),
  (771874, 4, 6),
  (771900, 3, 2),
  (773717, 0, 0),
  (774358, 6, 2),
  (776521, 1, 7),
  (787611, 5, 3),
  (791808, 2, 6),
  (819628, 1, 3),
  (822522, 5, 3),
  (827135, 7, 3),
  (828687, 0, 0),
  (829473, 6, 1),
  (830186, 6, 7),
  (837371, 3, 2),
  (840404, 1, 1),
  (843872, 1, 5),
  (847723, 6, 0),
  (852506, 4, 2),
  (856699, 7, 0),
  (870008, 0, 0),
  (873789, 7, 5),
  (875076, 3, 1),
  (882023, 0, 5),
  (888344, 7, 0),
  (894738, 0, 0),
  (900521, 1, 3),
  (901912, 1, 4),
  (906969, 5, 7),
  (913475, 0, 4),
  (926936, 7, 0),
  (933358, 7, 2),
  (937180, 6, 4),
  (946254, 2, 3),
  (947605, 4, 2),
  (947897, 4, 3),
  (961227, 0, 0),
  (968016, 4, 2),
  (969496, 5, 6),
  (972196, 1, 3),
  (973812, 2, 6),
  (976137, 7, 5),
  (988259, 0, 4),
  (990245, 3, 7),
  (993523, 1, 3),
  (994829, 3, 4),
  (1001284, 1, 0),
  (1003136, 5, 2),
  (1007445, 2, 4),
  (1008605, 4, 2),
  (1009879, 6, 7),
  (1010330, 6, 7),
  (1023522, 6, 7),
  (1024376, 7, 3),
  (1028617, 6, 3),
  (1029536, 4, 5),
  (1042279, 6, 4),
  (1045207, 7, 0),
  (1048950, 3, 7),
  (1050436, 1, 0),
  (1050982, 0, 3),
  (1051279, 5, 3),
  (1064474, 2, 3),
  (1068900, 1, 7),
  (1070619, 0, 7),
  (1071569, 5, 3),
  (1073417, 7, 1),
  (1074281, 1, 7),
  (1090692, 2, 6),
  (1093682, 3, 3),
  (1099212, 2, 6),
  (1099411, 4, 3),
  (1101085, 2, 3),
  (1115850, 3, 2),
  (1123323, 0, 3),
  (1128440, 4, 3),
  (1131099, 3, 7),
  (1133183, 5, 3),
  (1136006, 3, 3),
  (1136132, 1, 3),
  (1138485, 3, 3),
  (1139245, 6, 0),
  (1151913, 5, 1),
  (1157844, 3, 5),
  (1159802, 6, 7),
  (1161764, 3, 6),
  (1162942, 4, 6),
  (1171415, 7, 0),
  (1176696, 2, 1),
  (1192093, 6, 0),
  (1193873, 2, 7),
  (1200534, 5, 2),
  (1202371, 4, 3),
  (1203029, 7, 0),
  (1213666, 0, 3),
  (1214689, 3, 1),
  (1221451, 4, 5),
  (1232599, 4, 7),
  (1238353, 7, 3),
  (1239119, 3, 1),
  (1243447, 4, 3),
  (1246205, 2, 7),
  (1246520, 4, 3),
  (1260328, 0, 0),
  (1266475, 1, 0),
  (1272456, 5, 6),
  (1277045, 2, 3),
  (1281504, 5, 3),
  (1303570, 2, 7),
  (1305408, 0, 1),
  (1308900, 5, 2),
  (1313050, 6, 0),
  (1314240, 1, 0),
  (1318504, 0, 3),
  (1319023, 6, 0),
  (1325884, 1, 0),
  (1327345, 6, 0),
  (1338001, 1, 3),
  (1343091, 2, 6),
  (1347218, 6, 0),
  (1356054, 4, 3),
  (1356247, 5, 3),
  (1356562, 2, 3),
  (1357895, 0, 4),
  (1361253, 3, 3),
  (1361587, 3, 3),
  (1368619, 4, 3),
  (1378105, 5, 3),
  (1383915, 7, 0),
  (1386823, 0, 3),
  (1386924, 6, 0),
  (1389769, 4, 3),
  (1390246, 1, 6),
  (1393049, 7, 3),
  (1394793, 2, 7),
  (1405459, 5, 3),
  (1425416, 3, 2),
  (1445811, 7, 4),
  (1469941, 6, 4),
  (1470879, 2, 4),
  (1479995, 2, 2),
  (1482158, 6, 5),
  (1490948, 4, 1),
  (1497304, 4, 3),
  (1521935, 3, 0),
  (1531384, 4, 2),
  (1535874, 0, 3),
  (1541756, 6, 3),
  (1550251, 6, 1),
  (1559343, 4, 5),
  (1559925, 1, 4),
  (1562017, 4, 2),
  (1565830, 5, 5),
  (1566123, 4, 3),
  (1568527, 0, 7),
  (1568869, 7, 5),
  (1594584, 6, 0),
  (1619254, 4, 6),
  (1632067, 0, 3),
  (1637472, 5, 4),
  (1643792, 6, 0),
  (1646984, 7, 0),
  (1648923, 6, 3),
  (1651955, 5, 2),
  (1656952, 6, 0),
  (1680729, 1, 0),
  (1684282, 2, 6),
  (1693347, 7, 7),
  (1707639, 1, 3),
  (1709065, 0, 0),
  (1721944, 4, 4),
  (1730078, 7, 4),
  (1733067, 1, 3),
  (1744151, 0, 0),
  (1744593, 7, 3),
  (1751581, 6, 7),
  (1752106, 5, 3),
  (1754726, 3, 2),
  (1756096, 3, 3),
  (1759790, 6, 3),
  (1763132, 6, 7),
  (1769519, 2, 3),
  (1771799, 3, 6),
  (1777209, 5, 5),
  (1790175, 1, 0),
  (1791688, 1, 7),
  (1796113, 4, 6),
  (1796202, 2, 1),
  (1798423, 2, 6),
  (1802336, 5, 0),
  (1805195, 0, 0),
  (1823309, 6, 0),
  (1824483, 3, 6),
  (1824677, 6, 6),
  (1827695, 1, 5),
  (1834993, 1, 4),
  (1835707, 2, 2),
  (1848186, 0, 6),
  (1853602, 2, 3),
  (1856067, 3, 3),
  (1856365, 6, 0),
  (1860307, 7, 0),
  (1871528, 7, 0),
  (1874359, 6, 0),
  (1884021, 4, 2),
  (1892640, 3, 3),
  (1901718, 2, 6),
  (1905669, 5, 3),
  (1910028, 3, 2),
  (1912849, 1, 0),
  (1914268, 6, 0),
  (1922691, 2, 7),
  (1938667, 3, 3),
  (1947554, 2, 0),
  (1954558, 6, 4),
  (1961828, 3, 0),
  (1971343, 2, 6),
  (1982922, 6, 2),
  (2003237, 5, 4),
  (2003870, 3, 3),
  (2007525, 4, 3),
  (2010405, 5, 3),
  (2036194, 1, 7),
  (2055415, 5, 2),
  (2061843, 0, 3),
  (2063857, 0, 0),
  (2070997, 6, 5),
  (2075551, 7, 4),
  (2076957, 5, 3),
  (2078088, 7, 6),
  (2083251, 5, 2),
  (2086860, 6, 4),
  (2095096, 3, 4),
  (2105556, 4, 3),
  (2114458, 5, 2),
  (2115545, 3, 3),
  (2119757, 2, 2),
  (2120304, 0, 3),
  (2120958, 2, 3),
  (2127526, 5, 6),
  (2128371, 1, 0),
  (2134048, 3, 3),
  (2137003, 2, 3),
  (2148464, 4, 3),
  (2149131, 3, 0),
  (2151136, 5, 6),
  (2151375, 1, 1),
  (2161053, 4, 3),
  (2171362, 2, 6),
  (2172484, 4, 0),
  (2181042, 1, 7),
  (2186145, 5, 3),
  (2186809, 1, 0),
  (2188191, 0, 7),
  (2203099, 7, 0),
  (2205524, 7, 0),
  (2216635, 5, 5),
  (2222158, 0, 1),
  (2228681, 6, 4),
  (2230788, 7, 0),
  (2232231, 4, 3),
  (2234310, 6, 3),
  (2236067, 0, 0),
  (2240319, 2, 3),
  (2240607, 7, 3),
  (2244191, 6, 4),
  (2244925, 0, 7),
  (2254827, 5, 4),
  (2257436, 6, 3),
  (2262872, 4, 3),
  (2270919, 5, 2),
  (2274242, 1, 3),
  (2287547, 2, 6),
  (2298352, 5, 6),
  (2300243, 4, 3),
  (2303297, 5, 7),
  (2307077, 0, 7),
  (2309082, 7, 0),
  (2323450, 6, 1),
  (2324784, 7, 3),
  (2338557, 6, 0),
  (2345155, 1, 7),
  (2350506, 3, 2),
  (2354733, 7, 7),
  (2367273, 7, 3),
  (2382035, 1, 7),
  (2384240, 0, 0),
  (2388953, 1, 0),
  (2394647, 4, 5),
  (2397492, 7, 0),
  (2397986, 1, 0),
  (2406658, 3, 2),
  (2414344, 4, 7),
  (2416096, 2, 0),
  (2418798, 0, 0),
  (2420816, 1, 4),
  (2425043, 4, 7),
  (2437136, 4, 6),
  (2447254, 5, 4),
  (2447950, 2, 3),
  (2449044, 3, 6),
  (2473395, 4, 1),
  (2478479, 1, 4),
  (2485852, 4, 3),
  (2500675, 4, 3),
  (2509887, 3, 7),
  (2510027, 4, 7),
  (2533503, 0, 6),
  (2533623, 2, 3),
  (2534101, 0, 1),
  (2534575, 5, 3),
  (2534769, 1, 0),
  (2535923, 5, 2),
  (2543127, 0, 0),
  (2546054, 0, 0),
  (2562044, 7, 0),
  (2566496, 2, 2),
  (2574989, 3, 3),
  (2575291, 0, 6),
  (2582676, 6, 0),
  (2583389, 6, 4),
  (2588530, 7, 7),
  (2617095, 6, 3),
  (2623867, 4, 5),
  (2624367, 0, 0),
  (2626715, 1, 0),
  (2637522, 3, 4),
  (2637731, 5, 0),
  (2641066, 4, 5),
  (2657690, 2, 1),
  (2666071, 3, 2),
  (2666938, 5, 2),
  (2668425, 6, 0),
  (2682842, 6, 2),
  (2697051, 6, 0),
  (2702400, 1, 0),
  (2709267, 1, 0),
  (2729864, 2, 6),
  (2732555, 1, 7),
  (2733079, 2, 2),
  (2734968, 3, 7),
  (2743656, 2, 2),
  (2744713, 4, 6),
  (2746206, 1, 0),
  (2754170, 7, 0),
  (2754718, 7, 3),
  (2756828, 6, 5),
  (2758222, 1, 5),
  (2768729, 5, 6),
  (2768752, 5, 3),
  (2774854, 2, 7),
  (2797390, 2, 3),
  (2808856, 4, 2),
  (2812346, 1, 0),
  (2815992, 3, 7),
  (2816730, 5, 6),
  (2817623, 6, 0),
  (2818023, 6, 7),
  (2832702, 5, 3),
  (2833075, 3, 3),
  (2839863, 2, 3),
  (2855924, 4, 3),
  (2869037, 3, 0),
  (2876319, 0, 7),
  (2892102, 3, 5),
  (2895530, 0, 5),
  (2896155, 3, 3),
  (2900396, 6, 4),
  (2909703, 4, 2),
  (2910365, 6, 6),
  (2924470, 6, 3),
  (2934381, 2, 1),
  (2938131, 0, 7),
  (2943515, 7, 0),
  (2947026, 0, 0),
  (2976418, 0, 0),
  (2989794, 2, 4),
  (2989964, 2, 3),
  (3009237, 7, 0),
  (3012233, 5, 1),
  (3015030, 6, 0),
  (3020980, 4, 3),
  (3022978, 7, 6),
  (3030157, 5, 3),
  (3033532, 7, 0),
  (3036310, 3, 0),
  (3037967, 4, 3),
  (3044859, 5, 4),
  (3045029, 5, 1),
  (3047127, 4, 6),
  (3052095, 7, 2),
  (3070009, 0, 0),
  (3072674, 7, 3),
  (3074269, 5, 1),
  (3075109, 5, 6),
  (3080626, 3, 0),
  (3091224, 3, 6),
  (3103475, 6, 0),
  (3106887, 0, 3),
  (3110769, 3, 5),
  (3126965, 1, 4),
  (3133088, 2, 1),
  (3144387, 4, 3),
  (3154950, 3, 7),
  (3156496, 3, 6),
  (3167422, 5, 3),
  (3171160, 2, 3),
  (3171979, 3, 3),
  (3172872, 6, 7),
  (3176632, 5, 3),
  (3193133, 7, 0),
  (3194519, 7, 0),
  (3198558, 3, 3),
  (3203950, 2, 1),
  (3208008, 0, 1),
  (3224941, 0, 0),
  (3231412, 1, 3),
  (3232208, 1, 4),
  (3232615, 6, 2),
  (3239332, 6, 5),
  (3239481, 4, 0),
  (3245576, 7, 0),
  (3246183, 1, 0),
  (3250291, 0, 0),
  (3250612, 3, 3),
  (3252362, 1, 7),
  (3279977, 3, 3),
  (3281497, 0, 7),
  (3300244, 7, 0),
  (3301824, 5, 6),
  (3310876, 2, 4),
  (3311729, 4, 7),
  (3329420, 6, 3),
  (3341650, 7, 0),
  (3348321, 2, 3),
  (3353279, 0, 0),
  (3354233, 3, 3),
  (3368045, 1, 0),
  (3370358, 6, 4),
  (3378008, 6, 0),
  (3378190, 3, 2),
  (3380072, 2, 3),
  (3380718, 1, 0),
  (3387927, 2, 5),
  (3397537, 4, 6),
  (3397556, 0, 0),
  (3405491, 6, 0),
  (3408422, 1, 1),
  (3423925, 2, 7),
  (3449250, 1, 2),
  (3449464, 2, 3),
  (3451885, 7, 4),
  (3453902, 1, 6),
  (3455709, 7, 7),
  (3462376, 2, 6),
  (3464184, 5, 2),
  (3465709, 0, 7),
  (3466426, 4, 0),
  (3466912, 7, 3),
  (3470604, 1, 0),
  (3485187, 5, 3),
  (3485591, 5, 3),
  (3514559, 6, 0),
  (3515715, 5, 3),
  (3530387, 4, 3),
  (3533975, 7, 7),
  (3534620, 5, 6),
  (3543177, 6, 1),
  (3552326, 4, 3),
  (3567755, 0, 7),
  (3568660, 0, 3),
  (3569954, 7, 3),
  (3572450, 7, 3),
  (3575241, 6, 0),
  (3582475, 6, 6),
  (3583987, 3, 3),
  (3589779, 6, 0),
  (3591408, 4, 5),
  (3591775, 1, 5),
  (3598754, 4, 3),
])