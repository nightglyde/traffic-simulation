from util import *
schedule = deque([
  (3460, 5, 5),
  (7542, 1, 0),
  (10270, 5, 7),
  (32665, 2, 6),
  (35519, 2, 7),
  (44334, 0, 7),
  (48616, 5, 2),
  (57315, 5, 7),
  (60847, 3, 7),
  (67962, 5, 3),
  (71289, 3, 7),
  (74436, 3, 7),
  (77309, 6, 4),
  (78374, 2, 7),
  (88032, 7, 7),
  (91309, 7, 7),
  (91627, 4, 3),
  (93569, 0, 0),
  (100868, 1, 7),
  (103366, 5, 7),
  (106410, 0, 0),
  (107087, 6, 0),
  (107221, 0, 7),
  (114218, 4, 3),
  (126100, 7, 7),
  (144180, 7, 7),
  (147532, 5, 2),
  (153156, 6, 7),
  (155536, 0, 6),
  (159513, 2, 3),
  (171956, 2, 3),
  (173345, 6, 4),
  (178957, 0, 7),
  (184594, 4, 7),
  (187224, 6, 4),
  (187885, 0, 0),
  (197125, 3, 6),
  (197303, 5, 7),
  (212977, 1, 0),
  (213522, 4, 3),
  (216645, 1, 4),
  (217003, 2, 3),
  (229194, 7, 7),
  (231264, 2, 6),
  (231938, 7, 7),
  (250921, 3, 3),
  (254216, 1, 6),
  (256958, 7, 7),
  (263122, 7, 0),
  (267110, 5, 4),
  (273721, 0, 4),
  (285316, 2, 7),
  (288160, 1, 3),
  (289408, 0, 4),
  (303027, 4, 6),
  (319239, 2, 5),
  (323851, 3, 3),
  (325550, 5, 7),
  (327111, 3, 2),
  (328983, 7, 3),
  (331818, 2, 1),
  (338456, 7, 3),
  (346781, 5, 7),
  (350562, 4, 7),
  (354614, 5, 3),
  (354856, 3, 3),
  (359412, 4, 5),
  (362880, 4, 6),
  (372142, 3, 7),
  (385838, 0, 4),
  (402916, 6, 7),
  (408737, 4, 7),
  (416434, 7, 6),
  (423713, 1, 7),
  (429508, 1, 0),
  (429523, 7, 3),
  (438100, 1, 7),
  (438225, 6, 7),
  (442090, 5, 2),
  (444655, 1, 0),
  (446929, 6, 1),
  (451427, 1, 7),
  (456135, 4, 3),
  (456953, 3, 3),
  (457852, 7, 2),
  (467319, 7, 4),
  (471694, 6, 3),
  (477247, 2, 2),
  (487741, 0, 7),
  (501853, 0, 0),
  (523972, 4, 5),
  (532232, 1, 6),
  (538705, 7, 7),
  (545064, 4, 3),
  (546909, 3, 7),
  (565000, 1, 0),
  (576771, 4, 7),
  (592311, 5, 1),
  (592874, 2, 3),
  (594438, 7, 0),
  (594828, 3, 6),
  (595896, 7, 7),
  (599238, 0, 0),
  (604124, 5, 3),
  (608885, 0, 7),
  (609474, 5, 4),
  (612430, 3, 7),
  (618336, 6, 3),
  (618549, 2, 7),
  (621217, 6, 7),
  (627260, 6, 7),
  (632445, 5, 6),
  (634774, 3, 7),
  (635289, 1, 0),
  (646819, 6, 7),
  (659026, 6, 4),
  (666700, 1, 7),
  (678747, 6, 0),
  (686932, 3, 3),
  (688727, 7, 7),
  (694263, 6, 3),
  (699816, 0, 7),
  (699849, 5, 6),
  (702909, 4, 7),
  (707271, 2, 5),
  (710215, 5, 7),
  (717261, 1, 7),
  (717387, 6, 3),
  (720073, 0, 7),
  (730094, 2, 7),
  (732602, 1, 7),
  (736573, 2, 3),
  (756006, 1, 7),
  (758380, 1, 2),
  (761750, 1, 3),
  (770985, 5, 7),
  (778719, 4, 7),
  (782448, 3, 7),
  (784497, 2, 3),
  (790988, 6, 1),
  (804765, 1, 4),
  (806310, 1, 0),
  (816577, 3, 7),
  (829007, 6, 7),
  (829153, 6, 3),
  (833818, 7, 7),
  (840915, 7, 3),
  (841254, 0, 7),
  (852343, 2, 7),
  (869740, 0, 7),
  (871307, 1, 0),
  (873067, 7, 7),
  (882294, 3, 3),
  (888589, 0, 5),
  (897784, 1, 0),
  (899583, 6, 7),
  (899779, 6, 7),
  (901351, 5, 3),
  (917270, 6, 0),
  (928809, 3, 7),
  (942462, 1, 7),
  (944226, 6, 7),
  (950920, 7, 4),
  (959557, 2, 7),
  (959625, 1, 4),
  (965110, 0, 3),
  (965876, 0, 0),
  (969698, 4, 3),
  (975654, 6, 4),
  (980587, 6, 6),
  (984806, 7, 7),
  (994209, 4, 3),
  (994511, 2, 3),
  (1002072, 1, 0),
  (1008697, 6, 7),
  (1019192, 7, 7),
  (1023461, 7, 0),
  (1027836, 7, 7),
  (1034884, 2, 5),
  (1044708, 6, 0),
  (1049554, 4, 3),
  (1053903, 7, 1),
  (1062753, 2, 3),
  (1073340, 6, 7),
  (1075475, 1, 7),
  (1078991, 3, 5),
  (1084882, 5, 1),
  (1087674, 7, 7),
  (1098175, 0, 7),
  (1105456, 1, 7),
  (1107769, 6, 3),
  (1119346, 0, 7),
  (1138922, 6, 3),
  (1145118, 2, 7),
  (1151837, 7, 0),
  (1167148, 7, 0),
  (1177639, 6, 4),
  (1177661, 5, 7),
  (1187078, 5, 7),
  (1189140, 5, 3),
  (1190812, 6, 3),
  (1200731, 0, 7),
  (1216789, 6, 7),
  (1219705, 6, 2),
  (1224698, 4, 7),
  (1227348, 5, 3),
  (1227611, 2, 2),
  (1228869, 4, 7),
  (1248451, 7, 4),
  (1248936, 0, 2),
  (1252287, 5, 3),
  (1260547, 6, 4),
  (1285276, 0, 7),
  (1292030, 5, 7),
  (1298415, 3, 2),
  (1300299, 1, 7),
  (1304110, 7, 5),
  (1308383, 1, 7),
  (1310273, 7, 7),
  (1325048, 6, 3),
  (1325527, 1, 7),
  (1334836, 1, 7),
  (1341968, 4, 7),
  (1344339, 4, 6),
  (1351648, 2, 7),
  (1366371, 3, 2),
  (1369200, 7, 3),
  (1376862, 3, 3),
  (1378939, 2, 7),
  (1395272, 6, 7),
  (1397676, 5, 6),
  (1406683, 6, 6),
  (1409405, 6, 0),
  (1413272, 2, 6),
  (1426047, 1, 4),
  (1435982, 3, 3),
  (1450837, 0, 7),
  (1464563, 1, 3),
  (1475603, 2, 6),
  (1486750, 3, 7),
  (1491703, 3, 7),
  (1492767, 2, 2),
  (1512564, 2, 3),
  (1515390, 5, 7),
  (1515807, 7, 7),
  (1519730, 1, 0),
  (1519917, 1, 7),
  (1522544, 7, 6),
  (1525097, 5, 7),
  (1525513, 5, 7),
  (1527099, 4, 7),
  (1532307, 0, 3),
  (1535614, 4, 6),
  (1536484, 5, 7),
  (1536875, 3, 6),
  (1549309, 1, 5),
  (1553700, 2, 7),
  (1555968, 6, 7),
  (1555984, 6, 4),
  (1562895, 0, 7),
  (1563542, 3, 3),
  (1576906, 3, 3),
  (1596179, 2, 7),
  (1607029, 1, 7),
  (1616060, 2, 5),
  (1616693, 7, 6),
  (1634074, 5, 3),
  (1637589, 0, 7),
  (1642060, 5, 6),
  (1643717, 6, 7),
  (1666102, 0, 7),
  (1669535, 2, 7),
  (1675736, 1, 7),
  (1675774, 3, 3),
  (1690928, 0, 7),
  (1693805, 2, 5),
  (1701304, 1, 6),
  (1702926, 0, 4),
  (1704306, 7, 7),
  (1708945, 6, 7),
  (1709501, 7, 7),
  (1713957, 1, 4),
  (1729491, 3, 7),
  (1733045, 3, 7),
  (1733876, 6, 4),
  (1736036, 6, 7),
  (1750744, 4, 4),
  (1754759, 6, 5),
  (1772982, 3, 1),
  (1773685, 7, 0),
  (1774978, 6, 7),
  (1780896, 6, 6),
  (1782176, 3, 2),
  (1787319, 3, 5),
  (1792761, 5, 2),
  (1795445, 1, 3),
  (1806644, 1, 7),
  (1814203, 1, 3),
  (1819881, 4, 3),
  (1825027, 6, 0),
  (1830678, 2, 7),
  (1831049, 7, 4),
  (1838200, 4, 7),
  (1851791, 0, 7),
  (1863834, 1, 0),
  (1871036, 4, 2),
  (1876702, 5, 7),
  (1885672, 3, 2),
  (1886367, 7, 4),
  (1888163, 2, 3),
  (1890310, 1, 7),
  (1899685, 5, 5),
  (1914118, 2, 7),
  (1921349, 6, 0),
  (1921950, 0, 7),
  (1923987, 2, 3),
  (1932903, 2, 1),
  (1933795, 5, 7),
  (1957930, 2, 7),
  (1966505, 2, 6),
  (1975513, 6, 3),
  (1976826, 7, 0),
  (1980499, 0, 2),
  (1980559, 5, 7),
  (1982936, 6, 0),
  (1987935, 3, 3),
  (1989726, 4, 5),
  (1990818, 4, 5),
  (2002309, 4, 2),
  (2003060, 4, 5),
  (2007858, 2, 7),
  (2024431, 3, 4),
  (2026902, 4, 6),
  (2027409, 5, 7),
  (2034559, 0, 3),
  (2036171, 7, 4),
  (2039917, 2, 4),
  (2046516, 3, 3),
  (2047071, 2, 7),
  (2047612, 5, 2),
  (2047667, 2, 3),
  (2057298, 3, 4),
  (2057532, 0, 7),
  (2064946, 6, 7),
  (2076634, 1, 7),
  (2078834, 1, 7),
  (2081011, 6, 7),
  (2090377, 6, 7),
  (2091672, 4, 7),
  (2093854, 5, 5),
  (2115880, 4, 3),
  (2119431, 7, 7),
  (2129307, 4, 5),
  (2136031, 3, 7),
  (2142511, 7, 7),
  (2146054, 0, 7),
  (2146720, 1, 7),
  (2147828, 1, 0),
  (2163291, 7, 7),
  (2164158, 2, 3),
  (2166255, 0, 3),
  (2167683, 2, 3),
  (2168785, 5, 3),
  (2195175, 3, 6),
  (2201465, 5, 5),
  (2201900, 6, 4),
  (2202035, 4, 7),
  (2206595, 5, 7),
  (2207145, 5, 5),
  (2207998, 4, 7),
  (2208061, 1, 4),
  (2211459, 2, 2),
  (2213309, 3, 3),
  (2223057, 6, 0),
  (2223351, 3, 2),
  (2223504, 2, 6),
  (2223967, 7, 0),
  (2226999, 5, 6),
  (2233346, 0, 6),
  (2255526, 5, 5),
  (2257485, 6, 7),
  (2262453, 7, 5),
  (2266811, 3, 5),
  (2274161, 0, 0),
  (2281303, 3, 7),
  (2283107, 4, 7),
  (2284744, 6, 0),
  (2294604, 5, 3),
  (2297406, 4, 7),
  (2308786, 7, 0),
  (2310345, 7, 3),
  (2312721, 7, 7),
  (2326428, 6, 7),
  (2327981, 3, 2),
  (2335861, 6, 0),
  (2336275, 5, 5),
  (2337225, 1, 6),
  (2345630, 3, 6),
  (2346187, 1, 0),
  (2350276, 3, 5),
  (2352099, 3, 3),
  (2357138, 5, 2),
  (2359652, 3, 3),
  (2371074, 3, 5),
  (2382880, 6, 7),
  (2391838, 5, 7),
  (2396527, 0, 7),
  (2405656, 0, 0),
  (2411345, 4, 3),
  (2413476, 4, 5),
  (2414987, 1, 7),
  (2417483, 0, 6),
  (2425953, 5, 7),
  (2429714, 4, 7),
  (2434800, 2, 4),
  (2446686, 7, 7),
  (2451468, 6, 4),
  (2471055, 2, 5),
  (2479082, 6, 0),
  (2486993, 2, 7),
  (2496124, 7, 7),
  (2500189, 6, 0),
  (2508792, 4, 7),
  (2513233, 3, 7),
  (2519430, 2, 7),
  (2533155, 7, 7),
  (2538010, 2, 7),
  (2541089, 5, 6),
  (2542574, 5, 7),
  (2549595, 2, 5),
  (2551642, 0, 0),
  (2551697, 2, 6),
  (2553980, 1, 0),
  (2559733, 5, 7),
  (2567452, 0, 0),
  (2568948, 2, 7),
  (2570423, 7, 5),
  (2580800, 3, 7),
  (2591460, 5, 3),
  (2598583, 4, 7),
  (2600505, 5, 3),
  (2602525, 6, 0),
  (2604462, 3, 2),
  (2604795, 2, 3),
  (2608187, 5, 3),
  (2624510, 4, 7),
  (2630356, 7, 7),
  (2630861, 4, 5),
  (2632015, 3, 4),
  (2635032, 2, 3),
  (2635282, 4, 2),
  (2636306, 7, 7),
  (2637445, 5, 2),
  (2664352, 7, 7),
  (2669202, 0, 0),
  (2677144, 7, 3),
  (2677512, 5, 7),
  (2680732, 5, 7),
  (2682324, 5, 3),
  (2689866, 6, 4),
  (2695370, 0, 7),
  (2709428, 6, 7),
  (2719600, 1, 7),
  (2719934, 7, 7),
  (2730551, 2, 7),
  (2731366, 3, 6),
  (2733923, 1, 0),
  (2734874, 2, 3),
  (2738745, 5, 3),
  (2745710, 7, 3),
  (2754534, 2, 6),
  (2758940, 7, 4),
  (2760219, 4, 6),
  (2767669, 7, 3),
  (2771643, 0, 4),
  (2775988, 1, 7),
  (2781621, 7, 7),
  (2785750, 2, 7),
  (2789425, 7, 7),
  (2790628, 4, 6),
  (2802244, 1, 5),
  (2802843, 3, 3),
  (2803676, 4, 5),
  (2806747, 1, 7),
  (2827074, 3, 5),
  (2828748, 5, 6),
  (2832119, 1, 7),
  (2845923, 6, 3),
  (2847927, 5, 4),
  (2848820, 4, 2),
  (2867397, 0, 7),
  (2882889, 1, 7),
  (2893219, 0, 7),
  (2903656, 5, 2),
  (2909050, 7, 4),
  (2911621, 7, 4),
  (2913125, 2, 6),
  (2924546, 3, 7),
  (2929862, 6, 4),
  (2945959, 6, 4),
  (2946910, 3, 5),
  (2949118, 4, 7),
  (2951826, 6, 4),
  (2956215, 2, 3),
  (2958782, 1, 7),
  (2962263, 7, 0),
  (2964405, 6, 7),
  (2965949, 6, 7),
  (2969944, 6, 0),
  (2979825, 5, 3),
  (2986272, 3, 7),
  (2991935, 2, 1),
  (2996646, 3, 5),
  (2997683, 2, 2),
  (2997752, 3, 2),
  (3005955, 6, 6),
  (3018508, 4, 3),
  (3026912, 2, 3),
  (3040964, 1, 7),
  (3053645, 5, 7),
  (3095010, 6, 6),
  (3105821, 5, 6),
  (3108152, 5, 7),
  (3115244, 3, 3),
  (3132781, 7, 4),
  (3136430, 6, 0),
  (3138504, 5, 7),
  (3147754, 7, 4),
  (3164405, 3, 7),
  (3179931, 2, 7),
  (3191360, 1, 7),
  (3191691, 7, 1),
  (3211066, 3, 1),
  (3213160, 5, 7),
  (3216938, 3, 7),
  (3220054, 5, 7),
  (3225850, 6, 7),
  (3228063, 7, 0),
  (3228875, 1, 3),
  (3235666, 0, 0),
  (3239042, 4, 5),
  (3241658, 4, 3),
  (3245491, 1, 3),
  (3257220, 7, 7),
  (3259027, 7, 0),
  (3264850, 0, 7),
  (3266961, 3, 7),
  (3268197, 1, 7),
  (3270717, 3, 7),
  (3274521, 0, 7),
  (3277852, 2, 3),
  (3291016, 5, 7),
  (3295801, 3, 6),
  (3305347, 4, 1),
  (3312887, 0, 4),
  (3341093, 4, 5),
  (3347408, 3, 3),
  (3353583, 7, 3),
  (3354842, 5, 7),
  (3354996, 3, 6),
  (3355324, 4, 3),
  (3358916, 5, 7),
  (3387225, 1, 7),
  (3391757, 3, 3),
  (3401402, 6, 6),
  (3403126, 2, 7),
  (3425574, 2, 3),
  (3428079, 3, 7),
  (3430698, 0, 7),
  (3432000, 1, 3),
  (3438714, 5, 6),
  (3445864, 3, 7),
  (3446243, 1, 4),
  (3452110, 5, 7),
  (3452815, 3, 3),
  (3455524, 5, 6),
  (3455711, 1, 4),
  (3473610, 2, 7),
  (3476094, 5, 2),
  (3478440, 2, 2),
  (3482012, 4, 7),
  (3490766, 1, 7),
  (3504623, 2, 7),
  (3511484, 1, 0),
  (3512355, 5, 2),
  (3513436, 7, 6),
  (3516505, 2, 6),
  (3518554, 3, 3),
  (3529613, 6, 7),
  (3531137, 2, 7),
  (3534717, 7, 3),
  (3538568, 5, 7),
  (3542472, 3, 6),
  (3548429, 5, 7),
  (3551752, 4, 2),
  (3567744, 0, 7),
  (3569127, 1, 0),
  (3569209, 6, 3),
  (3576123, 0, 0),
  (3579872, 2, 7),
])