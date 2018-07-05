from util import *
schedule = deque([
  (5885, 1, 0),
  (8771, 4, 3),
  (12820, 7, 2),
  (20896, 3, 6),
  (23234, 3, 6),
  (26649, 7, 7),
  (44420, 1, 0),
  (59408, 1, 0),
  (69565, 5, 3),
  (74575, 3, 2),
  (78325, 1, 7),
  (92091, 3, 3),
  (103619, 3, 0),
  (104627, 6, 0),
  (118973, 7, 0),
  (150329, 2, 1),
  (151671, 5, 3),
  (153788, 1, 0),
  (169328, 4, 3),
  (177960, 0, 6),
  (178807, 3, 6),
  (179234, 4, 6),
  (184555, 6, 5),
  (211226, 0, 4),
  (214413, 2, 7),
  (216014, 2, 6),
  (219231, 3, 3),
  (229293, 0, 2),
  (231021, 7, 2),
  (232314, 6, 0),
  (243659, 0, 4),
  (244886, 0, 7),
  (245600, 6, 0),
  (247193, 7, 0),
  (253973, 7, 0),
  (257561, 3, 3),
  (260628, 4, 3),
  (264474, 7, 0),
  (269124, 2, 3),
  (273111, 0, 3),
  (277182, 2, 2),
  (278142, 1, 0),
  (286315, 0, 4),
  (291508, 2, 7),
  (293302, 2, 2),
  (298260, 4, 3),
  (308255, 7, 0),
  (311954, 3, 3),
  (313095, 4, 0),
  (313638, 3, 2),
  (318421, 1, 0),
  (326602, 0, 1),
  (327399, 0, 0),
  (329530, 2, 3),
  (332691, 4, 7),
  (334657, 5, 6),
  (342378, 7, 7),
  (347696, 5, 4),
  (348695, 7, 0),
  (361531, 0, 0),
  (363825, 5, 3),
  (368164, 5, 5),
  (373517, 3, 2),
  (376192, 1, 1),
  (379023, 1, 4),
  (380453, 6, 0),
  (390805, 7, 6),
  (391503, 5, 6),
  (392184, 3, 3),
  (393806, 3, 3),
  (397264, 1, 0),
  (398116, 0, 0),
  (400649, 3, 3),
  (419149, 7, 7),
  (420430, 0, 3),
  (425192, 2, 3),
  (425872, 5, 7),
  (426988, 5, 3),
  (429154, 3, 2),
  (438221, 4, 3),
  (450286, 4, 3),
  (461190, 3, 3),
  (480675, 0, 5),
  (485773, 7, 0),
  (488339, 4, 2),
  (490964, 1, 3),
  (495989, 3, 6),
  (507489, 6, 0),
  (530691, 5, 4),
  (532607, 0, 5),
  (535348, 1, 0),
  (537561, 7, 7),
  (547228, 7, 0),
  (551499, 3, 3),
  (554184, 4, 3),
  (561467, 4, 1),
  (567496, 4, 3),
  (569393, 3, 3),
  (571397, 6, 0),
  (577310, 7, 7),
  (579182, 1, 7),
  (588013, 6, 1),
  (593276, 3, 5),
  (598884, 7, 4),
  (609610, 0, 5),
  (611320, 3, 6),
  (616158, 4, 3),
  (622651, 6, 0),
  (623447, 0, 7),
  (626793, 7, 0),
  (632368, 4, 6),
  (636919, 7, 4),
  (640774, 4, 3),
  (643991, 0, 3),
  (646205, 0, 0),
  (667071, 3, 3),
  (670729, 7, 0),
  (683688, 0, 3),
  (688537, 1, 6),
  (690463, 7, 3),
  (692297, 0, 0),
  (692989, 5, 3),
  (694449, 5, 7),
  (694685, 5, 3),
  (697020, 0, 3),
  (697636, 1, 3),
  (701606, 4, 3),
  (705326, 2, 6),
  (711823, 5, 6),
  (717444, 3, 4),
  (720491, 1, 0),
  (724413, 4, 7),
  (725120, 2, 6),
  (731942, 7, 0),
  (733611, 6, 3),
  (738150, 3, 1),
  (739151, 2, 3),
  (741854, 3, 6),
  (744484, 0, 0),
  (744494, 4, 3),
  (769227, 5, 2),
  (781016, 2, 1),
  (792170, 0, 5),
  (795745, 0, 0),
  (805344, 1, 0),
  (805659, 1, 0),
  (809681, 5, 2),
  (815058, 7, 5),
  (822835, 6, 6),
  (824835, 0, 1),
  (830347, 5, 6),
  (833789, 0, 3),
  (844151, 0, 2),
  (846697, 6, 2),
  (849722, 0, 0),
  (854623, 2, 6),
  (861972, 2, 3),
  (866439, 4, 6),
  (876887, 6, 0),
  (882248, 5, 7),
  (888823, 0, 0),
  (891083, 7, 7),
  (897726, 0, 0),
  (898484, 5, 5),
  (905591, 5, 0),
  (905922, 5, 3),
  (924034, 0, 0),
  (933191, 7, 1),
  (935047, 0, 4),
  (937417, 5, 6),
  (938727, 5, 3),
  (939738, 6, 0),
  (945663, 4, 3),
  (946915, 4, 7),
  (952151, 2, 2),
  (956447, 2, 6),
  (964815, 3, 3),
  (972204, 5, 2),
  (972985, 2, 3),
  (989963, 2, 0),
  (990652, 4, 7),
  (990805, 3, 1),
  (996654, 2, 4),
  (999232, 2, 6),
  (1011954, 4, 0),
  (1013608, 2, 3),
  (1018438, 1, 4),
  (1020588, 1, 1),
  (1031450, 2, 3),
  (1043077, 2, 2),
  (1047709, 0, 4),
  (1067073, 6, 0),
  (1079632, 3, 3),
  (1087120, 0, 0),
  (1087461, 3, 6),
  (1091524, 3, 5),
  (1120930, 0, 0),
  (1122218, 7, 0),
  (1136136, 5, 7),
  (1139056, 7, 3),
  (1145993, 5, 7),
  (1149657, 2, 0),
  (1158531, 1, 5),
  (1172132, 7, 3),
  (1177963, 6, 2),
  (1184553, 5, 4),
  (1197184, 5, 3),
  (1200955, 0, 0),
  (1201903, 0, 0),
  (1212587, 3, 6),
  (1213341, 7, 0),
  (1214334, 6, 3),
  (1218465, 5, 1),
  (1223241, 1, 6),
  (1227646, 2, 3),
  (1229423, 7, 4),
  (1232920, 7, 7),
  (1237538, 4, 7),
  (1240951, 7, 3),
  (1255841, 5, 4),
  (1259569, 6, 4),
  (1261847, 1, 0),
  (1266164, 4, 3),
  (1271037, 2, 6),
  (1282729, 6, 3),
  (1284419, 1, 4),
  (1287186, 1, 1),
  (1287187, 0, 3),
  (1287677, 6, 0),
  (1288143, 3, 1),
  (1288892, 1, 4),
  (1293498, 6, 3),
  (1294604, 7, 0),
  (1301389, 4, 4),
  (1304709, 6, 7),
  (1337865, 6, 7),
  (1342323, 0, 3),
  (1348035, 0, 0),
  (1372008, 6, 4),
  (1388099, 4, 3),
  (1389588, 4, 7),
  (1398059, 3, 1),
  (1408175, 1, 7),
  (1410599, 3, 4),
  (1420266, 2, 3),
  (1421282, 4, 6),
  (1422587, 0, 0),
  (1426221, 6, 3),
  (1427762, 4, 7),
  (1428136, 1, 3),
  (1435610, 2, 0),
  (1448275, 4, 7),
  (1451323, 4, 3),
  (1451840, 6, 7),
  (1452273, 7, 1),
  (1460008, 0, 4),
  (1464929, 1, 4),
  (1468680, 3, 3),
  (1470552, 1, 4),
  (1476054, 0, 0),
  (1477016, 7, 6),
  (1481442, 2, 3),
  (1485729, 6, 0),
  (1492715, 5, 7),
  (1493501, 5, 3),
  (1494330, 4, 3),
  (1509207, 7, 0),
  (1517957, 2, 7),
  (1522670, 5, 3),
  (1525318, 4, 4),
  (1530845, 7, 4),
  (1534151, 7, 3),
  (1536781, 3, 6),
  (1538415, 1, 0),
  (1540017, 5, 3),
  (1543508, 2, 3),
  (1543892, 0, 0),
  (1550207, 5, 2),
  (1554332, 6, 3),
  (1560601, 3, 6),
  (1564122, 4, 3),
  (1572933, 1, 3),
  (1574880, 7, 0),
  (1580780, 1, 7),
  (1585459, 5, 6),
  (1609998, 0, 0),
  (1615566, 5, 2),
  (1628531, 6, 5),
  (1628648, 3, 3),
  (1641813, 2, 6),
  (1648186, 3, 3),
  (1649743, 5, 3),
  (1652509, 7, 5),
  (1670075, 7, 1),
  (1670137, 1, 0),
  (1678692, 1, 0),
  (1687214, 7, 4),
  (1689174, 6, 0),
  (1691391, 2, 1),
  (1691653, 5, 1),
  (1694068, 4, 5),
  (1694500, 5, 3),
  (1700870, 0, 3),
  (1704134, 3, 6),
  (1707555, 6, 0),
  (1707734, 2, 3),
  (1710179, 5, 6),
  (1711161, 0, 7),
  (1714695, 2, 3),
  (1723899, 3, 2),
  (1723947, 1, 0),
  (1725064, 5, 3),
  (1733013, 3, 6),
  (1733029, 7, 0),
  (1744238, 2, 6),
  (1746387, 6, 0),
  (1750383, 1, 7),
  (1762928, 1, 3),
  (1780093, 6, 4),
  (1781324, 0, 5),
  (1793703, 7, 7),
  (1795356, 5, 7),
  (1811700, 0, 4),
  (1817704, 0, 0),
  (1824818, 3, 2),
  (1825359, 3, 7),
  (1829795, 5, 1),
  (1832815, 2, 4),
  (1834595, 4, 5),
  (1837677, 1, 3),
  (1840829, 2, 2),
  (1844549, 3, 3),
  (1851539, 0, 1),
  (1854208, 3, 1),
  (1855922, 4, 0),
  (1858755, 1, 4),
  (1862934, 6, 3),
  (1864834, 2, 3),
  (1867243, 1, 3),
  (1869920, 7, 0),
  (1870316, 3, 5),
  (1874098, 3, 4),
  (1880434, 4, 3),
  (1896513, 7, 4),
  (1897639, 4, 5),
  (1906334, 0, 0),
  (1923630, 6, 3),
  (1925967, 6, 4),
  (1929237, 1, 6),
  (1929857, 3, 0),
  (1935223, 5, 3),
  (1953928, 3, 2),
  (1969777, 6, 0),
  (1973676, 1, 7),
  (1975483, 0, 0),
  (1979335, 2, 3),
  (1981464, 0, 0),
  (1982832, 0, 6),
  (1985170, 6, 0),
  (1986384, 1, 3),
  (1988190, 6, 4),
  (2007785, 4, 7),
  (2015598, 2, 0),
  (2022964, 1, 7),
  (2028965, 3, 2),
  (2030229, 5, 3),
  (2039570, 4, 3),
  (2052104, 7, 0),
  (2054075, 6, 7),
  (2055082, 2, 1),
  (2056818, 7, 0),
  (2065881, 1, 1),
  (2068229, 4, 3),
  (2078317, 4, 3),
  (2085936, 0, 4),
  (2094127, 2, 7),
  (2100764, 4, 6),
  (2109897, 6, 0),
  (2113431, 5, 6),
  (2113779, 5, 2),
  (2115622, 5, 6),
  (2121064, 1, 7),
  (2130016, 1, 0),
  (2137005, 6, 7),
  (2150423, 4, 0),
  (2152011, 2, 2),
  (2155599, 2, 7),
  (2160733, 3, 3),
  (2171405, 0, 5),
  (2191733, 5, 7),
  (2192219, 4, 3),
  (2195762, 4, 2),
  (2201878, 0, 3),
  (2206161, 3, 3),
  (2210461, 2, 2),
  (2220846, 5, 7),
  (2228878, 3, 2),
  (2229819, 0, 2),
  (2232551, 1, 1),
  (2239692, 2, 3),
  (2248242, 2, 7),
  (2258995, 0, 1),
  (2260064, 7, 3),
  (2272512, 7, 7),
  (2286189, 4, 3),
  (2294534, 5, 6),
  (2299789, 1, 0),
  (2312298, 0, 4),
  (2321995, 5, 3),
  (2323890, 1, 0),
  (2328938, 2, 5),
  (2336403, 2, 1),
  (2338289, 6, 0),
  (2349682, 5, 3),
  (2357638, 3, 7),
  (2364485, 6, 2),
  (2366398, 3, 2),
  (2372985, 6, 0),
  (2379628, 0, 0),
  (2381324, 1, 3),
  (2385084, 7, 0),
  (2387082, 6, 3),
  (2390210, 3, 2),
  (2401582, 3, 2),
  (2404481, 7, 0),
  (2407059, 3, 7),
  (2428851, 6, 0),
  (2429466, 2, 6),
  (2430359, 5, 3),
  (2438208, 4, 4),
  (2452134, 6, 6),
  (2459697, 6, 7),
  (2461266, 7, 0),
  (2465072, 4, 3),
  (2465721, 1, 0),
  (2473650, 3, 3),
  (2478360, 0, 4),
  (2482333, 7, 0),
  (2485817, 7, 4),
  (2487530, 7, 0),
  (2497182, 0, 0),
  (2498411, 6, 0),
  (2502551, 7, 1),
  (2507087, 2, 6),
  (2516712, 3, 3),
  (2525181, 2, 7),
  (2526277, 6, 0),
  (2529134, 3, 0),
  (2533248, 2, 1),
  (2533619, 4, 2),
  (2538143, 2, 3),
  (2539688, 6, 4),
  (2557963, 0, 4),
  (2562015, 4, 6),
  (2571955, 7, 1),
  (2575979, 3, 3),
  (2580954, 2, 3),
  (2581733, 5, 1),
  (2591923, 0, 0),
  (2596781, 5, 7),
  (2614342, 6, 1),
  (2616900, 7, 6),
  (2628659, 4, 1),
  (2633045, 0, 0),
  (2635406, 5, 3),
  (2646918, 5, 3),
  (2649305, 1, 1),
  (2653618, 2, 7),
  (2658494, 0, 4),
  (2664611, 7, 1),
  (2668441, 0, 7),
  (2669363, 1, 4),
  (2673747, 6, 0),
  (2690140, 5, 0),
  (2695435, 4, 2),
  (2707470, 2, 2),
  (2708024, 7, 5),
  (2721887, 3, 3),
  (2723228, 7, 4),
  (2724096, 3, 3),
  (2725632, 0, 7),
  (2734309, 6, 7),
  (2737298, 0, 4),
  (2739570, 0, 5),
  (2745780, 6, 6),
  (2755943, 4, 0),
  (2763165, 7, 0),
  (2777518, 4, 6),
  (2796294, 6, 0),
  (2796701, 7, 7),
  (2805342, 5, 3),
  (2810690, 2, 3),
  (2826203, 4, 6),
  (2840787, 1, 0),
  (2841775, 3, 3),
  (2845466, 5, 3),
  (2847858, 6, 4),
  (2848567, 3, 7),
  (2857406, 2, 3),
  (2857714, 5, 7),
  (2868976, 5, 2),
  (2884709, 0, 0),
  (2895505, 0, 0),
  (2896620, 4, 6),
  (2928618, 5, 7),
  (2933463, 4, 7),
  (2945779, 1, 0),
  (2965164, 2, 2),
  (2969916, 5, 2),
  (2975914, 6, 4),
  (2980859, 1, 7),
  (2991643, 1, 0),
  (2999303, 2, 0),
  (3004587, 6, 0),
  (3006872, 3, 6),
  (3008981, 5, 2),
  (3017637, 1, 0),
  (3021392, 0, 4),
  (3025832, 5, 6),
  (3031370, 0, 6),
  (3038154, 3, 7),
  (3038274, 5, 3),
  (3045953, 0, 2),
  (3058590, 3, 4),
  (3080818, 6, 0),
  (3084594, 0, 4),
  (3095525, 7, 4),
  (3104502, 0, 0),
  (3108536, 4, 3),
  (3109635, 7, 4),
  (3111543, 5, 6),
  (3114052, 4, 3),
  (3124913, 6, 0),
  (3132027, 4, 1),
  (3140759, 1, 4),
  (3151396, 4, 5),
  (3152504, 7, 0),
  (3158807, 1, 0),
  (3162047, 4, 3),
  (3164353, 1, 3),
  (3181839, 6, 3),
  (3197320, 6, 3),
  (3198860, 3, 6),
  (3221962, 4, 6),
  (3222991, 5, 7),
  (3226776, 5, 2),
  (3237623, 2, 3),
  (3256462, 2, 3),
  (3261655, 5, 3),
  (3276965, 5, 3),
  (3279386, 0, 0),
  (3281931, 0, 7),
  (3296184, 1, 4),
  (3308122, 4, 0),
  (3310063, 4, 6),
  (3310310, 5, 3),
  (3313584, 1, 0),
  (3322087, 2, 7),
  (3324905, 1, 0),
  (3332766, 0, 0),
  (3333435, 7, 1),
  (3333547, 5, 6),
  (3351028, 1, 0),
  (3354632, 3, 3),
  (3362616, 7, 7),
  (3363286, 1, 4),
  (3364549, 0, 1),
  (3385159, 6, 6),
  (3409834, 4, 2),
  (3421475, 1, 0),
  (3429283, 7, 7),
  (3432848, 1, 4),
  (3435804, 1, 0),
  (3440381, 7, 3),
  (3445907, 7, 0),
  (3446630, 2, 3),
  (3461601, 5, 6),
  (3466935, 7, 6),
  (3467816, 5, 3),
  (3474022, 2, 6),
  (3484654, 7, 3),
  (3491521, 0, 7),
  (3492536, 3, 6),
  (3500779, 3, 2),
  (3501281, 3, 3),
  (3509328, 6, 0),
  (3517499, 5, 0),
  (3519374, 3, 7),
  (3520547, 0, 7),
  (3520941, 5, 2),
  (3521723, 1, 7),
  (3551978, 4, 7),
  (3554017, 1, 1),
  (3555688, 7, 7),
  (3558469, 3, 3),
  (3563535, 1, 1),
  (3563860, 4, 7),
  (3570429, 3, 1),
  (3570668, 5, 3),
  (3579247, 3, 4),
])
