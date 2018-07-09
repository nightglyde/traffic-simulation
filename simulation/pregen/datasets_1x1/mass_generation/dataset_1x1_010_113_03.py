from util import *
schedule = deque([
  (601, 5, 3),
  (9302, 5, 3),
  (10999, 5, 7),
  (16562, 5, 7),
  (32702, 6, 7),
  (38241, 7, 3),
  (38575, 1, 0),
  (52893, 5, 3),
  (53272, 6, 4),
  (56784, 4, 7),
  (60620, 0, 4),
  (61780, 1, 4),
  (63230, 1, 6),
  (89834, 2, 7),
  (95048, 4, 2),
  (101972, 1, 3),
  (103990, 4, 3),
  (106366, 4, 2),
  (126373, 2, 7),
  (126715, 0, 0),
  (137131, 4, 6),
  (138774, 6, 6),
  (142261, 7, 7),
  (168159, 7, 3),
  (170814, 4, 3),
  (173512, 2, 7),
  (176181, 7, 3),
  (185244, 1, 7),
  (188184, 4, 3),
  (190202, 3, 3),
  (191049, 3, 1),
  (197350, 0, 4),
  (203167, 5, 5),
  (204830, 7, 6),
  (221558, 4, 7),
  (226205, 2, 7),
  (227993, 0, 5),
  (238697, 1, 6),
  (248483, 6, 7),
  (252199, 5, 7),
  (254233, 0, 3),
  (261462, 2, 7),
  (262496, 2, 7),
  (266288, 6, 7),
  (267822, 5, 3),
  (269738, 5, 7),
  (286184, 2, 5),
  (298061, 3, 2),
  (306552, 4, 0),
  (311942, 4, 7),
  (312987, 6, 0),
  (326133, 0, 7),
  (327383, 1, 3),
  (329277, 6, 7),
  (329521, 1, 5),
  (333206, 1, 0),
  (344615, 5, 3),
  (355470, 2, 3),
  (362221, 4, 7),
  (369382, 3, 2),
  (378742, 4, 7),
  (380401, 5, 7),
  (384518, 0, 7),
  (387516, 7, 7),
  (395553, 4, 5),
  (397888, 3, 3),
  (405016, 6, 6),
  (405515, 5, 3),
  (407340, 5, 1),
  (417002, 3, 7),
  (421988, 5, 7),
  (425814, 0, 4),
  (427601, 1, 3),
  (431995, 4, 7),
  (434199, 1, 3),
  (434655, 0, 0),
  (436510, 4, 6),
  (441361, 6, 4),
  (455831, 5, 3),
  (464295, 5, 3),
  (467307, 6, 4),
  (470671, 3, 5),
  (471278, 3, 3),
  (482383, 1, 7),
  (483528, 7, 7),
  (484427, 5, 2),
  (489169, 7, 3),
  (505973, 5, 7),
  (507744, 4, 7),
  (510900, 4, 6),
  (515497, 0, 7),
  (522257, 3, 6),
  (532172, 2, 2),
  (533094, 3, 2),
  (535309, 7, 7),
  (536840, 2, 3),
  (539226, 1, 7),
  (541488, 0, 7),
  (546364, 0, 0),
  (551237, 3, 2),
  (551861, 7, 7),
  (557417, 2, 2),
  (585124, 5, 3),
  (589377, 4, 6),
  (593134, 6, 0),
  (593147, 2, 7),
  (600482, 7, 7),
  (602658, 0, 7),
  (623032, 6, 7),
  (627819, 2, 3),
  (635069, 3, 7),
  (635703, 6, 7),
  (638494, 2, 7),
  (644939, 5, 3),
  (654380, 2, 7),
  (661397, 6, 6),
  (662974, 7, 7),
  (678852, 0, 7),
  (686413, 5, 7),
  (691873, 3, 3),
  (693413, 7, 0),
  (694844, 3, 7),
  (706136, 3, 6),
  (708660, 7, 7),
  (714829, 7, 7),
  (715211, 4, 5),
  (718287, 6, 7),
  (722170, 1, 0),
  (722475, 0, 6),
  (724015, 0, 7),
  (727979, 2, 7),
  (737122, 7, 0),
  (737261, 4, 3),
  (738906, 2, 2),
  (739295, 6, 7),
  (740453, 2, 7),
  (751947, 0, 7),
  (752072, 1, 0),
  (757345, 3, 3),
  (760188, 7, 0),
  (771443, 6, 7),
  (780572, 2, 7),
  (785712, 3, 7),
  (788631, 7, 0),
  (804157, 0, 0),
  (805242, 2, 7),
  (805673, 7, 0),
  (818341, 3, 2),
  (822411, 6, 0),
  (826952, 2, 7),
  (829647, 4, 3),
  (850659, 2, 7),
  (857478, 1, 6),
  (859441, 4, 7),
  (859845, 4, 2),
  (870404, 6, 4),
  (870606, 6, 7),
  (871452, 2, 6),
  (875219, 4, 6),
  (880803, 1, 7),
  (889588, 5, 7),
  (894085, 2, 2),
  (894390, 1, 7),
  (905771, 4, 7),
  (907843, 7, 0),
  (910956, 6, 7),
  (911111, 6, 6),
  (927132, 3, 7),
  (942121, 7, 7),
  (944002, 7, 3),
  (958251, 1, 7),
  (960669, 4, 1),
  (970220, 3, 3),
  (974475, 6, 0),
  (988930, 0, 5),
  (990884, 4, 4),
  (993343, 7, 7),
  (999273, 0, 7),
  (1002209, 5, 1),
  (1019688, 6, 7),
  (1032775, 3, 7),
  (1033839, 6, 0),
  (1042319, 2, 3),
  (1053407, 6, 0),
  (1054438, 2, 6),
  (1058066, 4, 3),
  (1059103, 4, 2),
  (1061476, 6, 3),
  (1075509, 2, 5),
  (1085460, 0, 7),
  (1096906, 0, 0),
  (1108670, 3, 2),
  (1115401, 4, 3),
  (1122057, 3, 3),
  (1122305, 3, 3),
  (1139143, 7, 7),
  (1145452, 4, 7),
  (1154016, 5, 5),
  (1157146, 0, 4),
  (1161631, 7, 0),
  (1163876, 6, 7),
  (1172503, 7, 3),
  (1172707, 3, 7),
  (1172748, 7, 7),
  (1176664, 5, 6),
  (1185950, 2, 7),
  (1187271, 0, 0),
  (1195231, 5, 7),
  (1220678, 2, 2),
  (1241533, 2, 7),
  (1241577, 6, 3),
  (1263539, 6, 7),
  (1293637, 3, 3),
  (1293744, 6, 7),
  (1296360, 3, 7),
  (1297204, 7, 0),
  (1298784, 2, 7),
  (1300488, 3, 4),
  (1305804, 4, 3),
  (1312539, 6, 7),
  (1315031, 7, 0),
  (1320321, 6, 3),
  (1322716, 2, 2),
  (1340713, 4, 6),
  (1341901, 7, 2),
  (1342795, 7, 7),
  (1361130, 3, 7),
  (1365898, 6, 0),
  (1377483, 4, 5),
  (1377982, 6, 0),
  (1380866, 4, 7),
  (1382610, 2, 3),
  (1400040, 1, 7),
  (1412420, 1, 7),
  (1413839, 0, 7),
  (1415705, 1, 7),
  (1424157, 0, 7),
  (1424502, 5, 5),
  (1424893, 0, 4),
  (1439702, 2, 7),
  (1448954, 0, 7),
  (1449243, 3, 7),
  (1456619, 7, 7),
  (1459373, 7, 0),
  (1474806, 6, 0),
  (1475894, 4, 7),
  (1479940, 3, 5),
  (1492507, 4, 7),
  (1496975, 5, 7),
  (1499469, 7, 7),
  (1504904, 2, 2),
  (1514161, 4, 5),
  (1521166, 3, 7),
  (1523772, 2, 5),
  (1524879, 6, 7),
  (1540369, 3, 7),
  (1547494, 7, 7),
  (1551977, 1, 0),
  (1552655, 7, 6),
  (1553016, 3, 6),
  (1559106, 7, 3),
  (1560994, 6, 0),
  (1568807, 6, 7),
  (1577179, 6, 0),
  (1581396, 0, 6),
  (1587041, 6, 0),
  (1602956, 4, 3),
  (1608272, 1, 3),
  (1612199, 0, 4),
  (1612514, 4, 6),
  (1615340, 7, 7),
  (1624395, 7, 1),
  (1636906, 5, 7),
  (1637383, 4, 7),
  (1638030, 2, 2),
  (1643713, 6, 4),
  (1643808, 5, 3),
  (1645344, 5, 7),
  (1647869, 1, 6),
  (1650992, 1, 7),
  (1653616, 2, 3),
  (1661406, 3, 3),
  (1667157, 3, 7),
  (1670461, 2, 6),
  (1670879, 7, 7),
  (1684171, 1, 6),
  (1692297, 6, 0),
  (1706612, 5, 2),
  (1706872, 2, 6),
  (1719928, 0, 7),
  (1724014, 2, 1),
  (1735708, 7, 4),
  (1741630, 2, 7),
  (1748644, 5, 7),
  (1753368, 1, 7),
  (1753811, 4, 7),
  (1756272, 1, 3),
  (1771316, 6, 7),
  (1789296, 3, 7),
  (1789423, 1, 4),
  (1791016, 7, 7),
  (1793566, 3, 7),
  (1795652, 7, 3),
  (1802479, 5, 6),
  (1803499, 1, 5),
  (1807024, 2, 1),
  (1809872, 3, 3),
  (1815960, 3, 7),
  (1817932, 5, 7),
  (1825370, 3, 3),
  (1830845, 6, 6),
  (1836751, 2, 7),
  (1837194, 1, 7),
  (1840642, 1, 7),
  (1842416, 5, 6),
  (1847039, 5, 3),
  (1853367, 0, 2),
  (1866238, 7, 0),
  (1867569, 2, 5),
  (1870838, 2, 3),
  (1878240, 3, 7),
  (1881537, 3, 6),
  (1882549, 5, 3),
  (1889372, 3, 6),
  (1889476, 1, 7),
  (1903888, 3, 7),
  (1928799, 6, 4),
  (1931109, 1, 7),
  (1935825, 1, 7),
  (1957199, 6, 0),
  (1962809, 3, 3),
  (1963679, 7, 7),
  (1964367, 3, 3),
  (1966215, 7, 0),
  (1966979, 5, 7),
  (1974984, 4, 6),
  (1975435, 3, 7),
  (1976505, 4, 3),
  (1980015, 4, 7),
  (1980181, 7, 0),
  (1983689, 0, 7),
  (1986806, 3, 7),
  (1992783, 3, 1),
  (1994649, 6, 0),
  (2001657, 3, 7),
  (2006104, 0, 7),
  (2009475, 4, 6),
  (2010462, 2, 6),
  (2027801, 2, 2),
  (2028690, 2, 7),
  (2029525, 6, 7),
  (2033725, 2, 2),
  (2035418, 4, 7),
  (2036295, 1, 7),
  (2037512, 2, 7),
  (2041938, 7, 7),
  (2050313, 7, 4),
  (2053955, 0, 4),
  (2063245, 7, 5),
  (2072172, 7, 0),
  (2074501, 1, 6),
  (2077271, 2, 7),
  (2086610, 7, 3),
  (2094540, 4, 7),
  (2096511, 4, 7),
  (2100989, 4, 4),
  (2107148, 0, 7),
  (2125024, 5, 7),
  (2144407, 0, 7),
  (2154794, 1, 7),
  (2158918, 2, 7),
  (2159554, 4, 7),
  (2159809, 2, 5),
  (2165159, 2, 5),
  (2170691, 5, 2),
  (2170963, 7, 7),
  (2177436, 4, 4),
  (2181996, 0, 7),
  (2193092, 7, 4),
  (2194907, 5, 7),
  (2195326, 5, 6),
  (2196513, 6, 3),
  (2198279, 7, 3),
  (2203117, 3, 5),
  (2204167, 3, 6),
  (2225590, 0, 7),
  (2238932, 5, 7),
  (2256439, 6, 0),
  (2257476, 3, 7),
  (2270481, 2, 7),
  (2276002, 4, 2),
  (2278686, 6, 4),
  (2282146, 5, 3),
  (2284803, 6, 7),
  (2308969, 0, 0),
  (2310268, 2, 7),
  (2316305, 5, 3),
  (2326052, 0, 0),
  (2327499, 0, 3),
  (2327786, 3, 7),
  (2330567, 0, 7),
  (2331012, 1, 4),
  (2334362, 0, 6),
  (2334934, 5, 2),
  (2338176, 4, 3),
  (2341468, 1, 0),
  (2342156, 3, 2),
  (2348824, 6, 7),
  (2374389, 2, 3),
  (2380630, 6, 7),
  (2385243, 0, 6),
  (2406266, 2, 2),
  (2407794, 5, 3),
  (2408032, 4, 3),
  (2410707, 0, 7),
  (2414541, 6, 6),
  (2432542, 1, 0),
  (2434941, 3, 7),
  (2439378, 6, 7),
  (2448835, 0, 6),
  (2453482, 5, 7),
  (2456983, 6, 7),
  (2457986, 6, 7),
  (2463918, 6, 4),
  (2464130, 6, 7),
  (2464308, 7, 7),
  (2467098, 6, 1),
  (2467813, 7, 7),
  (2468233, 7, 0),
  (2469209, 5, 7),
  (2475025, 5, 7),
  (2478520, 0, 6),
  (2478717, 0, 7),
  (2479499, 4, 3),
  (2487193, 5, 7),
  (2528378, 3, 6),
  (2532265, 7, 7),
  (2533894, 2, 2),
  (2533973, 3, 3),
  (2537563, 1, 7),
  (2538894, 4, 3),
  (2547751, 1, 6),
  (2550004, 7, 7),
  (2558894, 7, 4),
  (2567737, 3, 7),
  (2571410, 5, 6),
  (2582230, 2, 0),
  (2586951, 6, 0),
  (2593602, 4, 3),
  (2596710, 7, 3),
  (2598638, 5, 7),
  (2614373, 3, 2),
  (2623550, 3, 7),
  (2630337, 3, 7),
  (2640310, 0, 0),
  (2650123, 4, 7),
  (2677623, 6, 3),
  (2688369, 7, 0),
  (2689724, 4, 5),
  (2690019, 6, 3),
  (2694325, 4, 1),
  (2702317, 7, 6),
  (2718311, 3, 2),
  (2719275, 1, 4),
  (2733399, 2, 6),
  (2736224, 1, 3),
  (2747107, 5, 3),
  (2747195, 7, 0),
  (2776275, 2, 3),
  (2787341, 5, 3),
  (2799116, 0, 7),
  (2802556, 6, 0),
  (2808827, 4, 6),
  (2809383, 4, 0),
  (2811332, 3, 1),
  (2811729, 6, 7),
  (2816502, 4, 7),
  (2819929, 0, 7),
  (2835298, 0, 7),
  (2850015, 1, 7),
  (2859910, 4, 5),
  (2868965, 6, 7),
  (2874936, 6, 7),
  (2885606, 7, 0),
  (2894237, 7, 5),
  (2907649, 0, 4),
  (2913620, 4, 3),
  (2919044, 2, 7),
  (2928927, 5, 5),
  (2934347, 2, 7),
  (2942785, 4, 2),
  (2951664, 2, 6),
  (2955516, 4, 2),
  (2955996, 5, 7),
  (2956201, 2, 3),
  (2968322, 2, 7),
  (2971093, 5, 3),
  (2972061, 3, 7),
  (2990213, 2, 2),
  (2995663, 5, 3),
  (3000111, 0, 7),
  (3006220, 4, 3),
  (3020563, 3, 7),
  (3021663, 1, 7),
  (3025139, 4, 5),
  (3027810, 6, 7),
  (3034839, 5, 2),
  (3046261, 5, 6),
  (3048807, 6, 4),
  (3053853, 7, 3),
  (3063410, 2, 3),
  (3066429, 3, 3),
  (3075940, 5, 3),
  (3081062, 2, 6),
  (3084088, 5, 7),
  (3085709, 1, 7),
  (3085740, 3, 7),
  (3095100, 7, 0),
  (3097651, 6, 0),
  (3112223, 6, 7),
  (3122061, 2, 3),
  (3125218, 2, 2),
  (3129612, 7, 1),
  (3130588, 4, 4),
  (3138652, 5, 7),
  (3142455, 1, 0),
  (3152740, 4, 2),
  (3156183, 7, 0),
  (3179857, 2, 3),
  (3180350, 2, 7),
  (3193019, 0, 7),
  (3194209, 2, 6),
  (3196875, 5, 6),
  (3201699, 6, 3),
  (3209408, 2, 7),
  (3210271, 3, 3),
  (3219761, 0, 3),
  (3228951, 4, 5),
  (3236384, 2, 6),
  (3236798, 6, 7),
  (3237951, 7, 7),
  (3240377, 4, 7),
  (3242277, 0, 7),
  (3243078, 4, 3),
  (3249759, 2, 7),
  (3252074, 2, 7),
  (3261990, 6, 7),
  (3262508, 5, 3),
  (3275443, 1, 0),
  (3281133, 2, 7),
  (3284439, 5, 4),
  (3287848, 0, 7),
  (3288503, 4, 3),
  (3290709, 5, 7),
  (3294364, 3, 7),
  (3297204, 0, 7),
  (3302816, 7, 4),
  (3321128, 2, 7),
  (3321154, 1, 6),
  (3328761, 2, 2),
  (3332803, 4, 5),
  (3334235, 3, 6),
  (3338689, 3, 6),
  (3346109, 1, 6),
  (3361635, 6, 0),
  (3378479, 1, 3),
  (3388521, 2, 7),
  (3391972, 5, 6),
  (3395592, 6, 0),
  (3403559, 7, 6),
  (3416662, 2, 3),
  (3420479, 0, 7),
  (3421018, 2, 7),
  (3425113, 3, 3),
  (3426209, 5, 6),
  (3435764, 0, 7),
  (3462794, 6, 0),
  (3465025, 3, 1),
  (3470636, 4, 2),
  (3472915, 3, 2),
  (3473948, 5, 7),
  (3476962, 1, 5),
  (3481348, 7, 7),
  (3487569, 3, 2),
  (3503719, 1, 0),
  (3505883, 3, 7),
  (3533090, 0, 0),
  (3535297, 0, 3),
  (3544568, 1, 4),
  (3547308, 4, 1),
  (3554006, 1, 5),
  (3554818, 5, 7),
  (3559970, 6, 0),
  (3563117, 2, 7),
  (3564255, 3, 2),
  (3564299, 2, 2),
  (3566193, 3, 6),
  (3567852, 7, 4),
  (3588050, 0, 4),
  (3594570, 1, 0),
])