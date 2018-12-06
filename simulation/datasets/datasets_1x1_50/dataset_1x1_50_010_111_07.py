from src.util import *
schedule = deque([
  (8945, 0, 0),
  (15987, 1, 1),
  (20841, 6, 7),
  (33597, 6, 4),
  (48819, 1, 2),
  (49587, 1, 3),
  (56107, 4, 3),
  (79902, 6, 0),
  (84092, 1, 0),
  (98108, 7, 0),
  (100123, 6, 1),
  (109245, 7, 0),
  (110882, 2, 3),
  (126779, 2, 7),
  (135973, 0, 0),
  (151309, 6, 3),
  (152810, 3, 6),
  (162699, 2, 7),
  (180194, 3, 3),
  (181595, 4, 3),
  (183960, 1, 4),
  (187492, 4, 3),
  (192546, 5, 3),
  (193817, 4, 3),
  (197000, 2, 3),
  (199476, 1, 4),
  (207651, 3, 3),
  (208000, 7, 4),
  (209214, 2, 5),
  (211974, 6, 3),
  (213367, 1, 0),
  (216255, 6, 0),
  (251007, 4, 3),
  (251388, 3, 2),
  (254556, 6, 0),
  (254851, 2, 7),
  (274618, 7, 3),
  (293505, 5, 2),
  (318720, 5, 3),
  (323547, 4, 3),
  (325833, 2, 7),
  (327313, 1, 4),
  (343833, 7, 0),
  (348447, 2, 2),
  (356009, 5, 1),
  (373841, 5, 4),
  (376820, 3, 6),
  (378894, 1, 0),
  (396489, 6, 7),
  (396788, 1, 0),
  (419490, 3, 7),
  (425878, 0, 6),
  (427576, 7, 0),
  (436533, 5, 0),
  (438257, 6, 3),
  (441557, 0, 3),
  (458724, 3, 7),
  (462881, 6, 0),
  (472795, 5, 3),
  (476274, 3, 7),
  (482841, 7, 3),
  (494931, 5, 6),
  (510910, 5, 5),
  (515433, 2, 6),
  (516279, 3, 0),
  (535830, 7, 0),
  (549904, 2, 2),
  (561535, 3, 3),
  (562802, 4, 7),
  (563025, 1, 3),
  (577597, 0, 4),
  (582853, 3, 3),
  (586035, 4, 2),
  (591269, 7, 4),
  (604130, 1, 1),
  (616100, 4, 2),
  (622085, 5, 7),
  (625013, 7, 7),
  (625433, 3, 4),
  (629464, 2, 3),
  (630491, 5, 6),
  (631262, 1, 7),
  (636556, 1, 0),
  (658140, 3, 3),
  (665372, 0, 0),
  (665563, 2, 7),
  (672068, 3, 6),
  (673256, 6, 0),
  (679580, 0, 0),
  (680002, 5, 3),
  (688466, 2, 5),
  (688602, 5, 3),
  (700406, 5, 6),
  (705987, 1, 4),
  (706923, 6, 0),
  (717219, 4, 3),
  (718778, 4, 3),
  (724256, 2, 4),
  (730749, 2, 3),
  (731081, 6, 0),
  (737800, 0, 0),
  (741775, 5, 3),
  (745863, 4, 7),
  (748939, 1, 5),
  (763962, 2, 6),
  (763998, 1, 0),
  (764381, 5, 3),
  (773731, 0, 4),
  (775123, 5, 7),
  (776280, 0, 7),
  (795266, 5, 3),
  (807952, 7, 4),
  (811882, 1, 6),
  (812203, 2, 4),
  (830949, 1, 6),
  (833839, 5, 6),
  (834580, 4, 2),
  (834715, 0, 0),
  (843162, 6, 3),
  (843354, 7, 4),
  (846506, 5, 3),
  (897893, 7, 7),
  (899689, 7, 2),
  (913751, 3, 1),
  (917486, 0, 0),
  (917885, 5, 3),
  (930303, 0, 0),
  (934470, 4, 4),
  (941992, 3, 3),
  (942647, 1, 0),
  (949439, 7, 0),
  (957830, 2, 7),
  (960517, 3, 5),
  (960895, 4, 7),
  (966894, 4, 6),
  (967757, 1, 4),
  (969944, 3, 4),
  (970784, 4, 3),
  (971770, 1, 6),
  (976771, 3, 5),
  (980548, 0, 0),
  (985080, 4, 2),
  (985142, 1, 3),
  (989985, 0, 4),
  (993821, 3, 3),
  (994975, 3, 2),
  (1000546, 2, 3),
  (1004648, 4, 3),
  (1023381, 6, 7),
  (1035626, 3, 3),
  (1035645, 5, 7),
  (1041011, 0, 0),
  (1042636, 3, 1),
  (1059110, 0, 3),
  (1067763, 4, 3),
  (1070360, 2, 3),
  (1074181, 2, 5),
  (1085138, 2, 3),
  (1095482, 3, 3),
  (1096695, 1, 0),
  (1099054, 3, 3),
  (1110725, 4, 3),
  (1115830, 5, 3),
  (1136734, 2, 1),
  (1144565, 2, 2),
  (1145366, 2, 3),
  (1149704, 4, 7),
  (1157067, 0, 7),
  (1160137, 3, 3),
  (1166184, 6, 0),
  (1168705, 2, 7),
  (1172695, 6, 4),
  (1174165, 5, 3),
  (1174847, 0, 6),
  (1177676, 1, 6),
  (1180554, 5, 3),
  (1197535, 0, 0),
  (1206825, 2, 5),
  (1219963, 4, 6),
  (1222340, 5, 3),
  (1224464, 2, 3),
  (1231127, 1, 1),
  (1231677, 6, 3),
  (1254739, 4, 3),
  (1272670, 3, 3),
  (1275825, 2, 3),
  (1280908, 6, 4),
  (1284531, 0, 5),
  (1288953, 7, 0),
  (1292191, 6, 0),
  (1312567, 7, 2),
  (1317256, 5, 7),
  (1317520, 3, 6),
  (1323990, 6, 5),
  (1360070, 3, 5),
  (1365616, 0, 3),
  (1366946, 5, 7),
  (1369126, 6, 3),
  (1370137, 2, 7),
  (1371324, 6, 7),
  (1371804, 1, 4),
  (1379973, 1, 2),
  (1380482, 6, 0),
  (1380757, 1, 3),
  (1384137, 7, 1),
  (1386575, 7, 7),
  (1393441, 4, 7),
  (1394434, 3, 3),
  (1397375, 2, 4),
  (1399344, 6, 4),
  (1408287, 2, 7),
  (1410492, 7, 7),
  (1415354, 7, 4),
  (1458892, 3, 3),
  (1469493, 1, 0),
  (1474863, 2, 3),
  (1478946, 0, 4),
  (1480571, 0, 7),
  (1487357, 6, 4),
  (1497306, 4, 6),
  (1512888, 6, 0),
  (1513769, 7, 3),
  (1515551, 7, 7),
  (1516511, 6, 0),
  (1523536, 4, 3),
  (1523632, 6, 7),
  (1526147, 1, 7),
  (1528322, 3, 2),
  (1535244, 7, 0),
  (1547738, 6, 2),
  (1550054, 2, 4),
  (1551772, 0, 4),
  (1557443, 2, 2),
  (1559963, 1, 7),
  (1560588, 3, 3),
  (1567685, 5, 3),
  (1568067, 0, 0),
  (1581102, 0, 7),
  (1587224, 3, 3),
  (1591181, 5, 3),
  (1593341, 7, 0),
  (1596703, 6, 4),
  (1603128, 3, 3),
  (1605164, 4, 3),
  (1607719, 6, 2),
  (1612970, 6, 7),
  (1614995, 1, 3),
  (1619960, 0, 4),
  (1621072, 3, 2),
  (1625241, 1, 3),
  (1630788, 4, 4),
  (1633446, 4, 7),
  (1635917, 6, 3),
  (1635922, 3, 3),
  (1637200, 6, 5),
  (1642468, 1, 0),
  (1647018, 3, 4),
  (1647084, 6, 0),
  (1657921, 4, 3),
  (1661634, 1, 7),
  (1679765, 3, 2),
  (1682756, 3, 3),
  (1691527, 3, 3),
  (1696729, 7, 6),
  (1699076, 0, 0),
  (1711922, 6, 5),
  (1712031, 3, 3),
  (1715058, 4, 2),
  (1721240, 1, 6),
  (1722832, 3, 3),
  (1723353, 6, 3),
  (1732681, 4, 2),
  (1735443, 5, 2),
  (1741985, 7, 0),
  (1751389, 6, 0),
  (1751550, 2, 1),
  (1767043, 5, 3),
  (1767394, 2, 5),
  (1784005, 7, 3),
  (1784120, 4, 1),
  (1791028, 4, 3),
  (1792920, 2, 3),
  (1797588, 6, 6),
  (1800256, 1, 0),
  (1800499, 2, 1),
  (1801379, 1, 0),
  (1813982, 3, 0),
  (1826289, 6, 0),
  (1845323, 6, 0),
  (1850950, 7, 0),
  (1853510, 2, 7),
  (1855328, 7, 0),
  (1856957, 3, 3),
  (1857839, 1, 0),
  (1864545, 1, 0),
  (1866082, 1, 6),
  (1875582, 2, 3),
  (1877077, 6, 3),
  (1880739, 0, 0),
  (1883682, 4, 3),
  (1888149, 1, 4),
  (1890552, 4, 2),
  (1894141, 2, 1),
  (1899629, 7, 0),
  (1903906, 1, 7),
  (1905375, 2, 3),
  (1906001, 7, 0),
  (1906045, 2, 3),
  (1907507, 0, 4),
  (1908173, 2, 5),
  (1909967, 7, 0),
  (1917342, 2, 3),
  (1917403, 6, 7),
  (1930709, 4, 6),
  (1933851, 3, 3),
  (1934550, 0, 0),
  (1941913, 6, 7),
  (1951717, 1, 7),
  (1957157, 4, 2),
  (1972432, 1, 2),
  (1981029, 4, 0),
  (1981285, 0, 0),
  (1984599, 1, 0),
  (1985281, 1, 7),
  (1992359, 3, 3),
  (1998489, 6, 2),
  (2007790, 2, 3),
  (2011854, 2, 3),
  (2013141, 4, 6),
  (2017549, 2, 7),
  (2019533, 1, 3),
  (2019758, 5, 1),
  (2021569, 6, 4),
  (2026938, 1, 0),
  (2028839, 3, 7),
  (2032867, 5, 5),
  (2035679, 1, 5),
  (2046478, 7, 0),
  (2056940, 6, 4),
  (2064562, 5, 3),
  (2069018, 6, 4),
  (2075388, 1, 6),
  (2080578, 3, 2),
  (2083022, 3, 6),
  (2086728, 1, 0),
  (2087054, 6, 7),
  (2092015, 5, 3),
  (2094146, 6, 0),
  (2099632, 4, 7),
  (2104345, 7, 6),
  (2105121, 4, 4),
  (2106267, 6, 7),
  (2113262, 1, 0),
  (2115997, 6, 0),
  (2117717, 6, 7),
  (2120156, 1, 7),
  (2121263, 0, 7),
  (2129872, 7, 4),
  (2141230, 2, 3),
  (2146960, 5, 7),
  (2152149, 7, 3),
  (2162698, 5, 3),
  (2162926, 3, 3),
  (2163837, 2, 0),
  (2167428, 0, 4),
  (2176059, 7, 0),
  (2178167, 0, 3),
  (2187777, 1, 1),
  (2188307, 7, 0),
  (2198498, 0, 6),
  (2201625, 7, 4),
  (2203324, 6, 5),
  (2203768, 5, 3),
  (2210548, 2, 5),
  (2215860, 4, 7),
  (2223996, 7, 3),
  (2229583, 1, 0),
  (2237638, 6, 4),
  (2262921, 7, 4),
  (2264225, 2, 6),
  (2267545, 4, 6),
  (2272792, 5, 0),
  (2282747, 3, 3),
  (2288655, 0, 0),
  (2288910, 7, 7),
  (2290249, 5, 3),
  (2291361, 0, 7),
  (2293932, 5, 0),
  (2297149, 7, 0),
  (2298595, 4, 2),
  (2299590, 6, 3),
  (2302217, 6, 0),
  (2305958, 3, 6),
  (2311452, 7, 0),
  (2315498, 4, 3),
  (2319078, 2, 3),
  (2319299, 2, 4),
  (2320092, 6, 0),
  (2329020, 1, 0),
  (2344104, 2, 0),
  (2346028, 3, 3),
  (2349304, 7, 5),
  (2350011, 1, 3),
  (2350173, 7, 0),
  (2356418, 0, 7),
  (2356486, 3, 6),
  (2370835, 6, 4),
  (2378368, 0, 3),
  (2379878, 4, 3),
  (2380835, 0, 2),
  (2384999, 1, 7),
  (2401066, 5, 7),
  (2410084, 6, 1),
  (2423986, 0, 2),
  (2426524, 1, 0),
  (2441703, 0, 3),
  (2442127, 1, 0),
  (2445622, 6, 4),
  (2453292, 4, 2),
  (2471638, 2, 3),
  (2471845, 3, 1),
  (2479393, 5, 3),
  (2482485, 5, 6),
  (2484582, 7, 4),
  (2485285, 5, 3),
  (2486571, 7, 5),
  (2492777, 3, 7),
  (2493257, 3, 2),
  (2496130, 7, 4),
  (2503601, 2, 7),
  (2504238, 6, 1),
  (2504272, 2, 4),
  (2507795, 5, 3),
  (2508362, 6, 0),
  (2521030, 7, 7),
  (2529462, 5, 2),
  (2530914, 4, 7),
  (2541263, 4, 7),
  (2543038, 0, 5),
  (2543826, 6, 0),
  (2546292, 5, 3),
  (2551249, 3, 5),
  (2551759, 2, 3),
  (2557457, 2, 0),
  (2558689, 5, 6),
  (2561975, 0, 0),
  (2567427, 7, 0),
  (2569835, 3, 3),
  (2575090, 0, 0),
  (2575899, 3, 6),
  (2585820, 0, 7),
  (2586724, 5, 3),
  (2593130, 6, 0),
  (2622441, 0, 1),
  (2622518, 5, 3),
  (2633311, 1, 6),
  (2657290, 3, 3),
  (2658289, 0, 0),
  (2668662, 4, 1),
  (2674509, 7, 7),
  (2680550, 4, 2),
  (2685890, 3, 6),
  (2697738, 5, 1),
  (2699473, 2, 3),
  (2715405, 5, 0),
  (2716274, 1, 0),
  (2717015, 3, 3),
  (2717218, 5, 3),
  (2733875, 6, 0),
  (2740457, 4, 3),
  (2744241, 1, 3),
  (2752333, 6, 4),
  (2762141, 4, 3),
  (2762912, 7, 0),
  (2770321, 0, 3),
  (2775627, 1, 0),
  (2777352, 1, 1),
  (2779133, 4, 3),
  (2784780, 6, 7),
  (2789063, 3, 1),
  (2801123, 3, 7),
  (2807315, 0, 0),
  (2809361, 7, 4),
  (2817577, 2, 3),
  (2821060, 5, 3),
  (2822086, 4, 7),
  (2827373, 1, 1),
  (2831163, 3, 5),
  (2845029, 3, 6),
  (2855848, 3, 7),
  (2865352, 0, 4),
  (2867122, 0, 7),
  (2873442, 2, 3),
  (2875043, 7, 1),
  (2876124, 3, 3),
  (2876844, 5, 2),
  (2877638, 4, 6),
  (2881377, 3, 0),
  (2882617, 1, 3),
  (2890257, 5, 5),
  (2893173, 4, 2),
  (2894071, 4, 3),
  (2894304, 4, 3),
  (2904486, 5, 7),
  (2915770, 1, 0),
  (2926038, 3, 4),
  (2929891, 2, 3),
  (2936049, 6, 0),
  (2936991, 1, 0),
  (2945506, 1, 0),
  (2963439, 0, 0),
  (2973931, 4, 3),
  (2974205, 4, 3),
  (2984890, 1, 0),
  (2988174, 4, 3),
  (2989515, 1, 3),
  (2995223, 0, 4),
  (3001724, 3, 3),
  (3005276, 3, 2),
  (3039187, 4, 3),
  (3042454, 1, 7),
  (3042717, 3, 6),
  (3046506, 6, 0),
  (3076901, 5, 3),
  (3083848, 4, 3),
  (3088638, 3, 7),
  (3088819, 0, 0),
  (3094065, 5, 3),
  (3097957, 1, 3),
  (3100597, 2, 3),
  (3102997, 4, 7),
  (3105649, 7, 1),
  (3122136, 7, 0),
  (3131282, 1, 4),
  (3136426, 4, 7),
  (3141698, 3, 6),
  (3153626, 6, 7),
  (3161232, 5, 7),
  (3162794, 2, 4),
  (3173266, 6, 2),
  (3175517, 1, 6),
  (3179188, 4, 6),
  (3188097, 5, 3),
  (3191658, 6, 0),
  (3206047, 4, 7),
  (3211152, 7, 6),
  (3227200, 6, 1),
  (3238071, 6, 0),
  (3238944, 0, 0),
  (3249360, 0, 0),
  (3283604, 1, 0),
  (3335486, 7, 4),
  (3336149, 3, 2),
  (3338096, 0, 0),
  (3341162, 5, 3),
  (3348580, 5, 3),
  (3363814, 6, 7),
  (3369980, 7, 4),
  (3382255, 5, 7),
  (3382402, 2, 3),
  (3392749, 7, 2),
  (3394826, 0, 5),
  (3400886, 3, 2),
  (3405672, 2, 1),
  (3406781, 4, 4),
  (3408845, 4, 5),
  (3409523, 1, 7),
  (3412085, 1, 3),
  (3424399, 3, 2),
  (3439338, 5, 4),
  (3444231, 1, 5),
  (3447979, 6, 3),
  (3448255, 4, 3),
  (3458890, 1, 7),
  (3460107, 6, 0),
  (3466813, 1, 3),
  (3475260, 6, 0),
  (3476728, 7, 3),
  (3477080, 4, 3),
  (3477134, 1, 7),
  (3479291, 7, 1),
  (3480210, 1, 5),
  (3486789, 4, 7),
  (3492854, 0, 0),
  (3496094, 3, 5),
  (3498646, 0, 4),
  (3503740, 4, 6),
  (3503902, 0, 0),
  (3515305, 0, 4),
  (3520152, 1, 3),
  (3522031, 3, 3),
  (3530791, 6, 6),
  (3532500, 2, 4),
  (3536997, 2, 5),
  (3558092, 6, 7),
  (3574821, 0, 7),
  (3581521, 7, 2),
  (3583204, 1, 0),
  (3595281, 4, 5),
  (3595675, 1, 2),
])
