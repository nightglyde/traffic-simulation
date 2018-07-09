from util import *
schedule = deque([
  (706, 4, 7),
  (21357, 7, 3),
  (21603, 2, 2),
  (31142, 1, 4),
  (31650, 0, 6),
  (42960, 4, 6),
  (43369, 2, 3),
  (65921, 4, 6),
  (75114, 2, 2),
  (89386, 3, 3),
  (89913, 3, 3),
  (91228, 0, 0),
  (111107, 4, 7),
  (113118, 6, 0),
  (115295, 0, 5),
  (117745, 3, 3),
  (119718, 2, 4),
  (124278, 2, 3),
  (129567, 7, 0),
  (131287, 7, 0),
  (146161, 0, 0),
  (162998, 3, 3),
  (171862, 1, 0),
  (178034, 0, 3),
  (183375, 4, 2),
  (187969, 7, 1),
  (189401, 2, 3),
  (190881, 5, 3),
  (196526, 2, 7),
  (200529, 2, 0),
  (222708, 5, 0),
  (225790, 0, 0),
  (229429, 2, 3),
  (229450, 7, 0),
  (238199, 4, 1),
  (242952, 5, 6),
  (257703, 5, 3),
  (258982, 1, 5),
  (263362, 6, 0),
  (282144, 5, 7),
  (324455, 4, 2),
  (331289, 5, 3),
  (332512, 3, 6),
  (343358, 3, 5),
  (346515, 6, 1),
  (346778, 7, 3),
  (348474, 0, 0),
  (351396, 1, 3),
  (353225, 4, 6),
  (354274, 6, 0),
  (360474, 2, 0),
  (363516, 3, 6),
  (367765, 2, 4),
  (374313, 0, 5),
  (375262, 7, 4),
  (380565, 6, 0),
  (382002, 7, 6),
  (387261, 2, 3),
  (397053, 0, 1),
  (397781, 5, 7),
  (398612, 4, 3),
  (402043, 6, 0),
  (426544, 7, 1),
  (427506, 0, 3),
  (429468, 7, 4),
  (439231, 0, 1),
  (441491, 5, 7),
  (444658, 7, 5),
  (454379, 0, 0),
  (479058, 4, 3),
  (481878, 7, 1),
  (494971, 0, 0),
  (499656, 1, 7),
  (505017, 0, 0),
  (507024, 5, 3),
  (513940, 4, 7),
  (516989, 7, 4),
  (520435, 1, 6),
  (530176, 3, 3),
  (533982, 1, 4),
  (534562, 7, 3),
  (541889, 3, 3),
  (547402, 0, 0),
  (564919, 1, 7),
  (570720, 6, 0),
  (580410, 4, 3),
  (592250, 4, 6),
  (593030, 7, 3),
  (596040, 4, 3),
  (597331, 4, 2),
  (603293, 0, 0),
  (603446, 6, 6),
  (610790, 2, 0),
  (625686, 2, 3),
  (627574, 1, 0),
  (630605, 2, 3),
  (631863, 1, 0),
  (638633, 1, 0),
  (638994, 6, 7),
  (645001, 6, 0),
  (645120, 4, 3),
  (649610, 4, 3),
  (655237, 4, 3),
  (655396, 0, 0),
  (663541, 6, 0),
  (664666, 0, 2),
  (667659, 3, 3),
  (669360, 1, 0),
  (682834, 4, 0),
  (688352, 7, 4),
  (691805, 0, 0),
  (692701, 0, 0),
  (695004, 3, 4),
  (697509, 0, 0),
  (706099, 3, 4),
  (706476, 3, 3),
  (713873, 4, 3),
  (723280, 7, 7),
  (723988, 1, 7),
  (738339, 1, 4),
  (749753, 5, 0),
  (750537, 6, 7),
  (759356, 6, 0),
  (760564, 3, 3),
  (773879, 4, 7),
  (776796, 1, 2),
  (776947, 3, 3),
  (776990, 3, 3),
  (781624, 4, 6),
  (784477, 0, 0),
  (795064, 4, 7),
  (797329, 1, 0),
  (805998, 6, 7),
  (806163, 2, 7),
  (806207, 1, 0),
  (808650, 2, 3),
  (824902, 6, 0),
  (835831, 6, 3),
  (836863, 4, 7),
  (846024, 0, 0),
  (850313, 4, 2),
  (857455, 0, 6),
  (859600, 4, 2),
  (865468, 1, 3),
  (869986, 1, 0),
  (892509, 7, 7),
  (898768, 3, 4),
  (909964, 2, 5),
  (912721, 5, 6),
  (936057, 0, 5),
  (937801, 5, 7),
  (947815, 6, 0),
  (952365, 5, 2),
  (959982, 7, 0),
  (966147, 7, 0),
  (966256, 4, 3),
  (975553, 7, 0),
  (983421, 1, 0),
  (984344, 2, 6),
  (989828, 1, 6),
  (1003344, 6, 3),
  (1006225, 4, 2),
  (1007046, 7, 2),
  (1007225, 5, 7),
  (1011515, 2, 5),
  (1019705, 1, 7),
  (1022774, 3, 3),
  (1031294, 2, 3),
  (1035640, 2, 3),
  (1044591, 3, 3),
  (1046620, 4, 3),
  (1049054, 1, 0),
  (1054017, 3, 3),
  (1056073, 7, 4),
  (1070388, 4, 6),
  (1074012, 3, 7),
  (1076770, 2, 4),
  (1082622, 6, 7),
  (1085637, 0, 0),
  (1090283, 5, 2),
  (1091373, 1, 0),
  (1093323, 5, 3),
  (1102321, 4, 3),
  (1111122, 0, 0),
  (1114123, 4, 3),
  (1118307, 7, 7),
  (1124880, 6, 0),
  (1127222, 1, 5),
  (1128142, 1, 0),
  (1129645, 3, 3),
  (1130246, 7, 0),
  (1138680, 5, 7),
  (1142851, 7, 3),
  (1146126, 2, 7),
  (1148305, 2, 7),
  (1150911, 3, 5),
  (1155962, 4, 6),
  (1158667, 7, 0),
  (1182708, 6, 3),
  (1186662, 5, 3),
  (1197342, 0, 7),
  (1205656, 6, 0),
  (1209768, 3, 3),
  (1212138, 6, 0),
  (1230347, 0, 7),
  (1244329, 1, 0),
  (1247255, 6, 4),
  (1247679, 2, 1),
  (1250511, 1, 0),
  (1250860, 6, 0),
  (1254269, 4, 6),
  (1254436, 1, 0),
  (1261308, 7, 0),
  (1275052, 4, 7),
  (1277325, 7, 1),
  (1299105, 1, 0),
  (1304302, 1, 3),
  (1307089, 7, 3),
  (1321927, 2, 7),
  (1322398, 2, 2),
  (1324704, 1, 2),
  (1330261, 4, 3),
  (1339199, 3, 6),
  (1353284, 2, 2),
  (1357953, 0, 0),
  (1358391, 7, 0),
  (1362977, 5, 3),
  (1363032, 7, 0),
  (1366369, 1, 7),
  (1368581, 4, 3),
  (1373146, 1, 4),
  (1377028, 0, 5),
  (1384603, 0, 0),
  (1387866, 1, 0),
  (1432530, 5, 1),
  (1437217, 0, 4),
  (1450591, 4, 1),
  (1455407, 0, 6),
  (1456515, 4, 0),
  (1463130, 2, 3),
  (1467750, 0, 4),
  (1467819, 2, 6),
  (1469210, 5, 2),
  (1470293, 4, 3),
  (1477687, 4, 6),
  (1480976, 5, 7),
  (1482795, 0, 2),
  (1493746, 4, 7),
  (1499848, 7, 7),
  (1499963, 5, 3),
  (1509281, 2, 3),
  (1519221, 6, 7),
  (1524034, 4, 3),
  (1526964, 0, 0),
  (1532616, 7, 0),
  (1532632, 2, 6),
  (1538433, 0, 0),
  (1547099, 0, 7),
  (1547558, 1, 4),
  (1554986, 7, 4),
  (1562774, 4, 2),
  (1572680, 5, 3),
  (1582565, 2, 1),
  (1592792, 6, 3),
  (1604166, 5, 3),
  (1613736, 1, 6),
  (1621821, 5, 6),
  (1628859, 3, 3),
  (1641062, 4, 6),
  (1649985, 5, 5),
  (1656904, 3, 3),
  (1668182, 3, 6),
  (1673527, 5, 3),
  (1676231, 2, 3),
  (1676298, 2, 6),
  (1685462, 3, 4),
  (1688167, 3, 6),
  (1691802, 0, 1),
  (1724489, 1, 0),
  (1728721, 2, 0),
  (1734175, 0, 0),
  (1739972, 5, 6),
  (1743751, 1, 0),
  (1746136, 2, 6),
  (1746961, 7, 0),
  (1747486, 7, 0),
  (1754279, 0, 3),
  (1761693, 6, 0),
  (1766375, 5, 3),
  (1781023, 1, 0),
  (1781267, 0, 2),
  (1788189, 0, 4),
  (1795560, 4, 7),
  (1796673, 3, 6),
  (1798966, 3, 3),
  (1799026, 3, 2),
  (1799273, 3, 4),
  (1803920, 2, 2),
  (1807418, 3, 2),
  (1809246, 3, 6),
  (1812478, 7, 3),
  (1812617, 0, 7),
  (1814004, 5, 3),
  (1814620, 0, 4),
  (1835025, 0, 7),
  (1835260, 5, 7),
  (1854269, 2, 7),
  (1855330, 4, 0),
  (1858016, 0, 4),
  (1858633, 2, 6),
  (1858713, 4, 2),
  (1873686, 6, 7),
  (1878507, 3, 2),
  (1883582, 5, 7),
  (1884912, 0, 4),
  (1903656, 3, 3),
  (1906313, 3, 3),
  (1918990, 4, 3),
  (1924535, 2, 6),
  (1927747, 3, 3),
  (1933422, 2, 3),
  (1935172, 4, 7),
  (1942051, 0, 0),
  (1945311, 7, 3),
  (1946472, 4, 2),
  (1960258, 7, 0),
  (1961253, 7, 1),
  (1962192, 2, 6),
  (1964665, 7, 0),
  (1966714, 0, 7),
  (1970050, 0, 0),
  (1971544, 3, 3),
  (1977338, 3, 6),
  (1980780, 2, 3),
  (1989555, 6, 0),
  (1991582, 7, 3),
  (1997131, 6, 0),
  (1999893, 4, 6),
  (2011319, 4, 3),
  (2022705, 5, 3),
  (2024699, 7, 0),
  (2035254, 2, 3),
  (2037136, 3, 2),
  (2060950, 1, 4),
  (2064962, 1, 7),
  (2066321, 7, 4),
  (2067793, 6, 0),
  (2068462, 4, 2),
  (2079810, 5, 3),
  (2086335, 4, 2),
  (2095732, 3, 3),
  (2104437, 7, 3),
  (2121125, 0, 3),
  (2122735, 1, 5),
  (2125287, 4, 6),
  (2126375, 1, 3),
  (2129648, 2, 3),
  (2146012, 1, 7),
  (2150885, 5, 3),
  (2157985, 2, 3),
  (2167998, 1, 7),
  (2175901, 2, 4),
  (2177551, 1, 0),
  (2183356, 5, 3),
  (2185357, 7, 4),
  (2191489, 6, 1),
  (2192657, 4, 7),
  (2198460, 0, 0),
  (2204218, 2, 3),
  (2206116, 4, 3),
  (2216693, 5, 3),
  (2221958, 1, 0),
  (2225799, 2, 2),
  (2231947, 5, 1),
  (2234688, 0, 0),
  (2249335, 4, 3),
  (2257471, 7, 6),
  (2267427, 6, 5),
  (2277454, 4, 2),
  (2278185, 1, 5),
  (2281343, 5, 6),
  (2306346, 4, 2),
  (2307801, 2, 3),
  (2311853, 5, 3),
  (2320174, 3, 1),
  (2324666, 6, 3),
  (2326246, 0, 0),
  (2329505, 0, 0),
  (2330062, 6, 3),
  (2332103, 4, 3),
  (2339612, 7, 0),
  (2341084, 2, 3),
  (2352768, 1, 0),
  (2354471, 3, 3),
  (2373788, 4, 7),
  (2375403, 4, 6),
  (2391662, 3, 0),
  (2391949, 1, 1),
  (2402425, 0, 0),
  (2404268, 4, 3),
  (2419167, 3, 3),
  (2428314, 7, 4),
  (2445385, 1, 7),
  (2447150, 1, 0),
  (2455157, 0, 0),
  (2457384, 7, 0),
  (2459659, 7, 7),
  (2471128, 5, 2),
  (2474206, 5, 5),
  (2476862, 1, 4),
  (2479249, 6, 7),
  (2482208, 1, 0),
  (2490748, 4, 4),
  (2492218, 1, 3),
  (2502137, 2, 3),
  (2502848, 1, 7),
  (2509035, 7, 7),
  (2510108, 0, 5),
  (2521951, 0, 4),
  (2535702, 4, 3),
  (2537667, 7, 0),
  (2545730, 5, 4),
  (2551853, 5, 3),
  (2552532, 2, 6),
  (2553187, 6, 4),
  (2553583, 1, 6),
  (2558437, 1, 4),
  (2559290, 5, 2),
  (2576364, 0, 0),
  (2614702, 3, 2),
  (2615531, 7, 0),
  (2616895, 2, 3),
  (2624636, 4, 2),
  (2626869, 2, 3),
  (2629344, 2, 7),
  (2639456, 3, 1),
  (2643895, 7, 5),
  (2648025, 1, 1),
  (2649759, 5, 2),
  (2650727, 5, 2),
  (2660840, 4, 2),
  (2662754, 1, 7),
  (2663895, 4, 3),
  (2666075, 7, 0),
  (2672936, 3, 3),
  (2673452, 1, 7),
  (2683336, 0, 7),
  (2702021, 4, 3),
  (2708885, 7, 3),
  (2719201, 5, 5),
  (2724849, 4, 4),
  (2727068, 2, 6),
  (2743381, 4, 3),
  (2745961, 5, 7),
  (2749524, 7, 2),
  (2754412, 5, 3),
  (2760298, 4, 7),
  (2761791, 4, 7),
  (2765541, 0, 2),
  (2768559, 3, 7),
  (2777280, 2, 1),
  (2780794, 4, 1),
  (2791016, 7, 4),
  (2798504, 3, 2),
  (2800375, 7, 4),
  (2810062, 4, 5),
  (2821556, 6, 5),
  (2827973, 1, 0),
  (2832786, 4, 1),
  (2834612, 7, 5),
  (2839534, 1, 0),
  (2840835, 1, 7),
  (2850821, 0, 3),
  (2857739, 4, 6),
  (2870978, 6, 0),
  (2875633, 4, 2),
  (2876169, 6, 0),
  (2880324, 3, 1),
  (2889833, 2, 5),
  (2894694, 0, 0),
  (2903216, 3, 4),
  (2906860, 2, 3),
  (2915675, 3, 0),
  (2921423, 4, 3),
  (2933816, 2, 1),
  (2935726, 5, 6),
  (2937627, 2, 3),
  (2939042, 3, 3),
  (2944974, 6, 7),
  (2947018, 7, 7),
  (2960444, 5, 2),
  (2962673, 0, 2),
  (2969123, 5, 2),
  (2970861, 1, 0),
  (2973894, 2, 3),
  (2985161, 7, 0),
  (2989851, 7, 0),
  (2997826, 5, 3),
  (2998367, 1, 0),
  (3002267, 5, 3),
  (3007168, 1, 0),
  (3011610, 5, 6),
  (3011664, 0, 0),
  (3015086, 5, 7),
  (3016555, 2, 3),
  (3017186, 3, 3),
  (3017616, 2, 4),
  (3029936, 7, 0),
  (3041495, 7, 1),
  (3066785, 5, 3),
  (3070090, 5, 5),
  (3075125, 1, 0),
  (3077660, 2, 4),
  (3099421, 6, 0),
  (3100045, 7, 6),
  (3101059, 7, 0),
  (3102173, 3, 3),
  (3103641, 6, 0),
  (3105868, 2, 7),
  (3108344, 2, 3),
  (3110985, 1, 0),
  (3116589, 2, 0),
  (3117113, 7, 6),
  (3118670, 7, 6),
  (3121547, 2, 3),
  (3127422, 4, 2),
  (3138049, 0, 7),
  (3143418, 4, 3),
  (3144127, 6, 0),
  (3156262, 6, 4),
  (3157776, 7, 0),
  (3161782, 4, 2),
  (3161977, 0, 4),
  (3162869, 0, 5),
  (3168260, 3, 7),
  (3170956, 1, 3),
  (3174018, 3, 3),
  (3180626, 6, 0),
  (3182163, 4, 6),
  (3185724, 5, 7),
  (3200848, 4, 3),
  (3203203, 6, 0),
  (3204326, 7, 7),
  (3217099, 7, 3),
  (3223602, 3, 2),
  (3227554, 7, 7),
  (3231618, 7, 0),
  (3233240, 7, 0),
  (3240436, 2, 6),
  (3246603, 4, 3),
  (3253735, 7, 0),
  (3254529, 6, 0),
  (3260146, 2, 2),
  (3261892, 3, 4),
  (3262500, 3, 7),
  (3273225, 1, 3),
  (3287539, 1, 5),
  (3293391, 1, 7),
  (3301806, 4, 3),
  (3312801, 7, 0),
  (3336933, 3, 3),
  (3338878, 5, 7),
  (3339953, 0, 7),
  (3341000, 6, 7),
  (3350518, 2, 1),
  (3364338, 7, 0),
  (3377924, 1, 0),
  (3395474, 3, 3),
  (3395614, 5, 4),
  (3396285, 4, 4),
  (3405285, 4, 3),
  (3414903, 7, 0),
  (3418455, 0, 0),
  (3418685, 6, 6),
  (3423347, 5, 6),
  (3432863, 6, 2),
  (3434451, 6, 3),
  (3435557, 5, 3),
  (3440357, 7, 4),
  (3442954, 3, 3),
  (3452824, 2, 1),
  (3469085, 1, 0),
  (3471593, 6, 0),
  (3480213, 3, 2),
  (3480391, 2, 3),
  (3493480, 1, 5),
  (3507887, 5, 3),
  (3526005, 5, 2),
  (3538966, 1, 0),
  (3540563, 5, 0),
  (3541518, 0, 5),
  (3549908, 1, 3),
  (3550000, 4, 5),
  (3576073, 3, 7),
  (3580265, 5, 2),
  (3581815, 3, 6),
  (3588005, 3, 7),
  (3588705, 6, 3),
  (3591502, 3, 7),
  (3599769, 5, 6),
])