from src.util import *
schedule = deque([
  (4959, 2, 7),
  (14362, 0, 6),
  (35906, 1, 0),
  (46637, 3, 3),
  (56606, 2, 3),
  (58460, 0, 0),
  (60432, 4, 3),
  (61568, 5, 3),
  (65852, 5, 3),
  (73173, 0, 0),
  (80821, 0, 6),
  (83181, 2, 3),
  (102312, 2, 7),
  (103662, 2, 3),
  (111028, 6, 4),
  (122090, 7, 0),
  (124380, 7, 5),
  (124604, 6, 0),
  (124821, 4, 7),
  (126892, 4, 3),
  (128268, 4, 7),
  (148892, 1, 0),
  (149436, 1, 6),
  (149818, 0, 0),
  (156503, 7, 4),
  (162779, 4, 2),
  (182483, 4, 3),
  (183927, 3, 3),
  (184749, 0, 0),
  (191390, 6, 4),
  (195652, 0, 6),
  (208091, 4, 3),
  (222519, 6, 0),
  (235121, 2, 3),
  (237919, 5, 0),
  (241444, 0, 0),
  (255668, 6, 4),
  (256674, 2, 7),
  (272839, 6, 4),
  (278997, 2, 3),
  (281234, 3, 7),
  (282762, 6, 3),
  (290942, 7, 0),
  (301076, 0, 6),
  (305784, 2, 3),
  (308659, 7, 0),
  (309991, 2, 7),
  (319496, 0, 3),
  (325317, 2, 3),
  (326467, 5, 6),
  (328773, 1, 5),
  (334295, 5, 3),
  (338046, 2, 7),
  (339245, 3, 1),
  (344443, 5, 3),
  (351081, 3, 6),
  (357783, 0, 7),
  (362541, 3, 2),
  (375086, 6, 0),
  (375636, 5, 2),
  (379295, 6, 0),
  (382454, 4, 0),
  (384584, 1, 6),
  (392043, 4, 3),
  (407676, 7, 3),
  (410528, 1, 0),
  (412663, 0, 6),
  (429077, 3, 3),
  (437543, 1, 7),
  (446856, 4, 6),
  (450427, 5, 3),
  (451624, 4, 6),
  (463709, 6, 0),
  (480446, 5, 2),
  (486279, 2, 5),
  (488816, 2, 3),
  (501803, 3, 1),
  (507249, 5, 6),
  (510070, 5, 7),
  (514809, 6, 2),
  (521646, 3, 3),
  (530322, 7, 7),
  (545584, 7, 0),
  (548013, 1, 0),
  (553500, 0, 4),
  (554288, 0, 3),
  (560311, 2, 3),
  (560981, 5, 3),
  (569221, 3, 6),
  (574872, 0, 2),
  (598943, 7, 1),
  (603624, 6, 3),
  (611688, 1, 7),
  (619118, 1, 2),
  (640428, 5, 3),
  (651236, 7, 0),
  (658718, 7, 3),
  (668820, 1, 4),
  (671388, 3, 3),
  (674848, 0, 0),
  (702578, 0, 0),
  (705878, 5, 7),
  (706615, 2, 7),
  (747979, 7, 0),
  (766167, 2, 3),
  (768250, 7, 0),
  (771343, 1, 0),
  (783925, 0, 0),
  (786386, 1, 7),
  (788519, 4, 0),
  (792640, 2, 3),
  (795661, 4, 3),
  (795780, 2, 7),
  (816208, 7, 0),
  (824497, 2, 3),
  (824758, 1, 0),
  (826277, 3, 7),
  (832845, 4, 3),
  (834203, 5, 2),
  (835416, 3, 7),
  (836653, 6, 0),
  (841473, 6, 4),
  (850915, 6, 4),
  (876926, 2, 3),
  (892486, 6, 0),
  (897524, 1, 0),
  (900081, 2, 5),
  (909704, 1, 0),
  (915730, 0, 0),
  (922618, 6, 3),
  (924865, 7, 4),
  (925763, 4, 2),
  (927585, 3, 6),
  (928630, 0, 3),
  (930131, 7, 0),
  (930759, 3, 2),
  (932129, 4, 3),
  (947688, 5, 2),
  (954899, 2, 3),
  (955815, 0, 0),
  (959467, 6, 4),
  (962302, 1, 0),
  (976336, 4, 3),
  (976738, 5, 5),
  (981358, 1, 0),
  (991954, 0, 1),
  (992164, 1, 0),
  (1001669, 6, 6),
  (1013515, 0, 3),
  (1015716, 7, 4),
  (1016417, 1, 0),
  (1040135, 6, 0),
  (1057378, 3, 3),
  (1059226, 3, 6),
  (1063273, 5, 0),
  (1068035, 6, 4),
  (1068614, 0, 7),
  (1074303, 0, 4),
  (1075533, 4, 3),
  (1078957, 3, 6),
  (1079866, 2, 3),
  (1083659, 0, 0),
  (1090825, 4, 3),
  (1098505, 7, 4),
  (1099470, 2, 2),
  (1109683, 5, 6),
  (1115002, 2, 3),
  (1115998, 5, 3),
  (1117000, 2, 2),
  (1117605, 0, 0),
  (1121412, 2, 3),
  (1121906, 6, 0),
  (1127619, 5, 3),
  (1130598, 5, 7),
  (1131361, 0, 3),
  (1147404, 0, 0),
  (1161752, 6, 4),
  (1162253, 3, 6),
  (1165614, 4, 3),
  (1167527, 2, 0),
  (1173109, 7, 5),
  (1174599, 7, 0),
  (1175631, 4, 7),
  (1195526, 0, 0),
  (1199119, 6, 0),
  (1201768, 5, 2),
  (1209597, 3, 2),
  (1220108, 7, 7),
  (1220962, 1, 0),
  (1221824, 3, 6),
  (1228763, 6, 3),
  (1248930, 6, 0),
  (1250398, 4, 2),
  (1252620, 6, 0),
  (1252992, 5, 4),
  (1254438, 0, 3),
  (1275559, 6, 0),
  (1276204, 2, 7),
  (1278427, 7, 0),
  (1278767, 2, 3),
  (1283483, 3, 0),
  (1284071, 6, 2),
  (1286038, 3, 7),
  (1293354, 1, 2),
  (1297056, 5, 6),
  (1305767, 3, 2),
  (1339242, 0, 4),
  (1344546, 5, 7),
  (1347485, 0, 0),
  (1350846, 2, 6),
  (1356704, 5, 4),
  (1363088, 3, 7),
  (1364439, 2, 6),
  (1366708, 1, 4),
  (1367557, 2, 0),
  (1371613, 5, 2),
  (1374225, 6, 0),
  (1375229, 3, 3),
  (1381466, 0, 2),
  (1389323, 7, 0),
  (1395508, 6, 7),
  (1396146, 4, 1),
  (1409143, 0, 0),
  (1409241, 7, 0),
  (1427820, 6, 7),
  (1431543, 5, 1),
  (1432520, 2, 3),
  (1434679, 0, 7),
  (1435451, 1, 0),
  (1442404, 5, 3),
  (1447516, 2, 2),
  (1457826, 0, 0),
  (1480181, 5, 2),
  (1486606, 6, 1),
  (1489436, 2, 2),
  (1499595, 1, 7),
  (1504521, 0, 4),
  (1518459, 0, 0),
  (1532247, 6, 0),
  (1536040, 6, 0),
  (1537859, 4, 3),
  (1539818, 2, 7),
  (1542648, 2, 7),
  (1550451, 7, 3),
  (1552829, 1, 3),
  (1567338, 0, 4),
  (1567541, 6, 4),
  (1568540, 4, 3),
  (1579356, 7, 0),
  (1584644, 5, 6),
  (1585755, 2, 3),
  (1587441, 3, 3),
  (1588222, 7, 0),
  (1595101, 3, 2),
  (1598169, 3, 4),
  (1603240, 3, 7),
  (1604601, 6, 0),
  (1608331, 3, 6),
  (1612981, 5, 2),
  (1614870, 6, 7),
  (1622332, 4, 3),
  (1628351, 7, 4),
  (1632077, 2, 5),
  (1632456, 4, 3),
  (1635057, 5, 3),
  (1648881, 3, 7),
  (1652766, 6, 0),
  (1653199, 6, 3),
  (1654110, 6, 2),
  (1655487, 0, 0),
  (1672978, 0, 0),
  (1673862, 6, 0),
  (1693594, 7, 0),
  (1694097, 2, 3),
  (1694402, 2, 6),
  (1699925, 1, 7),
  (1701153, 4, 6),
  (1704134, 7, 6),
  (1704682, 7, 0),
  (1708176, 4, 6),
  (1708537, 6, 3),
  (1710177, 2, 3),
  (1722235, 7, 0),
  (1728130, 3, 3),
  (1735469, 6, 2),
  (1736034, 3, 5),
  (1739880, 2, 3),
  (1746381, 4, 3),
  (1762124, 5, 6),
  (1762651, 6, 0),
  (1772879, 4, 3),
  (1777684, 1, 0),
  (1785383, 5, 6),
  (1789209, 3, 3),
  (1809424, 2, 2),
  (1815095, 7, 5),
  (1819100, 4, 3),
  (1828560, 2, 3),
  (1831195, 4, 6),
  (1840370, 6, 3),
  (1841577, 0, 0),
  (1842963, 6, 0),
  (1854562, 4, 3),
  (1854640, 4, 3),
  (1854811, 0, 0),
  (1865296, 7, 0),
  (1873574, 4, 2),
  (1881958, 2, 5),
  (1888825, 7, 0),
  (1925363, 1, 0),
  (1926243, 2, 3),
  (1927235, 4, 3),
  (1928545, 7, 3),
  (1934486, 4, 6),
  (1937012, 3, 2),
  (1939473, 1, 4),
  (1957712, 2, 0),
  (1962036, 3, 3),
  (1972070, 0, 2),
  (1972094, 2, 3),
  (1973969, 5, 3),
  (1974891, 5, 7),
  (1978313, 1, 6),
  (1990820, 2, 6),
  (1991775, 3, 3),
  (1996116, 2, 2),
  (2018127, 5, 3),
  (2023452, 5, 6),
  (2037765, 6, 7),
  (2037949, 7, 3),
  (2062921, 0, 0),
  (2076813, 4, 5),
  (2083023, 0, 7),
  (2104930, 3, 3),
  (2106932, 1, 4),
  (2113780, 2, 7),
  (2123141, 2, 7),
  (2126459, 2, 6),
  (2127955, 3, 3),
  (2129814, 7, 0),
  (2150263, 3, 3),
  (2150877, 4, 6),
  (2165273, 1, 3),
  (2180748, 6, 3),
  (2190067, 0, 3),
  (2196111, 6, 0),
  (2197693, 0, 0),
  (2215096, 0, 3),
  (2220193, 2, 6),
  (2225336, 7, 0),
  (2227635, 1, 0),
  (2228716, 4, 3),
  (2230376, 5, 3),
  (2233167, 1, 3),
  (2235809, 0, 3),
  (2238252, 0, 4),
  (2242995, 0, 4),
  (2244003, 0, 2),
  (2249162, 2, 3),
  (2255958, 6, 3),
  (2271682, 5, 3),
  (2273347, 4, 3),
  (2275483, 2, 3),
  (2279264, 0, 3),
  (2288944, 4, 0),
  (2291862, 0, 4),
  (2294092, 2, 4),
  (2295265, 3, 7),
  (2298258, 7, 0),
  (2303921, 0, 0),
  (2307007, 5, 3),
  (2308312, 0, 4),
  (2313509, 3, 6),
  (2314984, 1, 0),
  (2316210, 4, 3),
  (2319466, 5, 3),
  (2333560, 2, 7),
  (2340419, 1, 0),
  (2371736, 0, 2),
  (2376752, 3, 3),
  (2380069, 3, 3),
  (2386441, 7, 7),
  (2387102, 4, 6),
  (2387207, 5, 3),
  (2392314, 6, 2),
  (2394478, 5, 4),
  (2396132, 6, 5),
  (2398028, 7, 7),
  (2398865, 4, 7),
  (2401042, 7, 0),
  (2404108, 4, 1),
  (2404460, 2, 3),
  (2406220, 3, 2),
  (2407181, 7, 0),
  (2415775, 1, 0),
  (2417643, 7, 3),
  (2425590, 0, 7),
  (2431055, 3, 7),
  (2447506, 6, 7),
  (2451433, 1, 0),
  (2454094, 7, 0),
  (2455678, 3, 3),
  (2460872, 5, 7),
  (2473261, 7, 0),
  (2488076, 6, 7),
  (2492385, 1, 2),
  (2500981, 2, 7),
  (2541726, 4, 3),
  (2561187, 0, 4),
  (2562150, 2, 7),
  (2562634, 3, 5),
  (2563151, 2, 3),
  (2564896, 0, 0),
  (2593213, 5, 3),
  (2594466, 6, 0),
  (2594580, 2, 2),
  (2605389, 7, 6),
  (2612356, 7, 0),
  (2612573, 2, 2),
  (2619512, 3, 3),
  (2620894, 0, 5),
  (2625187, 5, 0),
  (2626994, 3, 7),
  (2628026, 5, 6),
  (2637764, 6, 7),
  (2639940, 1, 0),
  (2641488, 6, 4),
  (2657184, 2, 2),
  (2657294, 5, 2),
  (2659928, 0, 6),
  (2660962, 6, 5),
  (2668710, 7, 6),
  (2676930, 3, 3),
  (2680030, 7, 0),
  (2680881, 3, 1),
  (2683126, 1, 0),
  (2700704, 2, 3),
  (2710790, 1, 0),
  (2713299, 6, 7),
  (2718658, 7, 5),
  (2721951, 1, 0),
  (2723731, 7, 4),
  (2725979, 4, 3),
  (2734261, 6, 0),
  (2744291, 6, 3),
  (2745426, 6, 6),
  (2751370, 1, 7),
  (2752670, 7, 1),
  (2771372, 0, 4),
  (2783284, 2, 3),
  (2784943, 3, 6),
  (2787419, 7, 0),
  (2796309, 2, 2),
  (2796909, 7, 3),
  (2797883, 6, 6),
  (2814622, 7, 6),
  (2814841, 4, 6),
  (2816770, 3, 0),
  (2824851, 3, 1),
  (2831875, 1, 0),
  (2832374, 1, 1),
  (2833713, 2, 4),
  (2836620, 7, 4),
  (2837741, 7, 0),
  (2860209, 6, 0),
  (2869543, 6, 0),
  (2872487, 1, 0),
  (2874732, 3, 6),
  (2876089, 5, 1),
  (2879259, 7, 3),
  (2896246, 1, 0),
  (2898059, 4, 5),
  (2906577, 2, 6),
  (2906602, 3, 7),
  (2909590, 5, 3),
  (2912053, 3, 7),
  (2913861, 5, 2),
  (2925689, 5, 3),
  (2931173, 0, 0),
  (2933342, 5, 3),
  (2935907, 3, 4),
  (2937429, 3, 5),
  (2937449, 1, 0),
  (2940879, 6, 3),
  (2941446, 3, 6),
  (2941565, 3, 6),
  (2947047, 2, 7),
  (2950797, 6, 4),
  (2952306, 6, 3),
  (2961335, 3, 6),
  (2965787, 1, 0),
  (2976616, 2, 1),
  (2977467, 2, 3),
  (2979958, 4, 6),
  (2981326, 2, 2),
  (2991549, 1, 0),
  (3027781, 4, 3),
  (3028065, 7, 7),
  (3028867, 7, 0),
  (3030799, 4, 2),
  (3033921, 2, 7),
  (3040430, 3, 7),
  (3063021, 7, 0),
  (3078199, 6, 5),
  (3087673, 3, 3),
  (3088649, 5, 3),
  (3089383, 3, 6),
  (3092697, 6, 0),
  (3095550, 3, 3),
  (3099804, 5, 3),
  (3100645, 6, 7),
  (3102930, 2, 3),
  (3107475, 5, 7),
  (3109035, 1, 4),
  (3110399, 2, 2),
  (3112922, 0, 0),
  (3136333, 7, 0),
  (3136936, 7, 4),
  (3145671, 1, 4),
  (3157325, 7, 0),
  (3161979, 1, 4),
  (3167446, 4, 3),
  (3169089, 7, 0),
  (3183204, 4, 4),
  (3184386, 5, 6),
  (3207929, 0, 0),
  (3208320, 2, 2),
  (3208973, 3, 3),
  (3216828, 0, 0),
  (3218352, 2, 7),
  (3218726, 1, 7),
  (3230013, 2, 3),
  (3233499, 7, 0),
  (3234625, 5, 3),
  (3240061, 7, 0),
  (3255792, 3, 7),
  (3270636, 4, 6),
  (3272891, 2, 4),
  (3280738, 0, 0),
  (3287256, 7, 7),
  (3287396, 1, 7),
  (3290571, 0, 3),
  (3307906, 7, 0),
  (3310747, 1, 4),
  (3311392, 0, 6),
  (3324167, 0, 0),
  (3333483, 3, 5),
  (3336829, 0, 0),
  (3338107, 6, 0),
  (3354175, 7, 7),
  (3359268, 6, 3),
  (3362054, 7, 3),
  (3362865, 2, 1),
  (3379272, 4, 6),
  (3385811, 0, 5),
  (3389917, 4, 2),
  (3393268, 6, 4),
  (3396900, 6, 0),
  (3399770, 5, 4),
  (3403573, 5, 5),
  (3409509, 4, 3),
  (3420414, 0, 0),
  (3435170, 0, 0),
  (3443156, 3, 3),
  (3443744, 5, 2),
  (3445387, 2, 4),
  (3446530, 5, 3),
  (3446658, 7, 0),
  (3458921, 3, 3),
  (3464851, 4, 0),
  (3471495, 2, 3),
  (3472013, 3, 7),
  (3473110, 0, 7),
  (3481130, 0, 0),
  (3484455, 4, 7),
  (3488343, 3, 0),
  (3488606, 5, 6),
  (3488817, 7, 0),
  (3502780, 4, 3),
  (3504932, 7, 4),
  (3507764, 1, 0),
  (3512705, 5, 7),
  (3515661, 5, 7),
  (3518550, 1, 4),
  (3526350, 4, 3),
  (3527804, 4, 3),
  (3533355, 6, 4),
  (3537612, 2, 3),
  (3541320, 7, 3),
  (3550010, 1, 3),
  (3554323, 1, 7),
  (3555800, 2, 3),
  (3564433, 5, 3),
  (3565527, 6, 4),
  (3568331, 0, 0),
  (3568525, 2, 5),
  (3573322, 4, 3),
  (3573775, 5, 6),
  (3585836, 7, 0),
  (3590710, 3, 2),
])
