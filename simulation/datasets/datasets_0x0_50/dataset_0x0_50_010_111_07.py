from src.util import *
schedule = deque([
  (1595, 3, 2),
  (2561, 3, 0),
  (7227, 1, 1),
  (9617, 1, 0),
  (14909, 0, 2),
  (23850, 2, 1),
  (31409, 3, 2),
  (40383, 1, 1),
  (54738, 1, 0),
  (57760, 3, 2),
  (61845, 0, 2),
  (63133, 2, 2),
  (65774, 2, 0),
  (69643, 3, 0),
  (73538, 1, 2),
  (77549, 2, 0),
  (85724, 1, 2),
  (88928, 3, 2),
  (90491, 1, 1),
  (96729, 1, 0),
  (102270, 2, 0),
  (105438, 0, 1),
  (109286, 1, 2),
  (146749, 0, 1),
  (147264, 1, 0),
  (148623, 2, 0),
  (154944, 3, 0),
  (158312, 3, 0),
  (160206, 2, 0),
  (161964, 0, 2),
  (167162, 3, 0),
  (181100, 1, 1),
  (186264, 1, 0),
  (187394, 1, 1),
  (191962, 0, 1),
  (193583, 2, 1),
  (197387, 3, 1),
  (211223, 3, 2),
  (216701, 2, 2),
  (223006, 1, 2),
  (231066, 2, 0),
  (233933, 1, 1),
  (234002, 0, 0),
  (241770, 1, 1),
  (275916, 0, 2),
  (277150, 1, 0),
  (278009, 3, 2),
  (283663, 2, 0),
  (287214, 2, 1),
  (294617, 1, 2),
  (296899, 1, 1),
  (299178, 0, 1),
  (311958, 1, 1),
  (315277, 3, 0),
  (333905, 0, 0),
  (336181, 2, 2),
  (363704, 3, 1),
  (371191, 0, 0),
  (374496, 2, 2),
  (378476, 3, 2),
  (384155, 2, 0),
  (400467, 1, 1),
  (403520, 0, 1),
  (406783, 2, 0),
  (409706, 3, 2),
  (431055, 0, 2),
  (441259, 2, 1),
  (442538, 1, 2),
  (446396, 3, 2),
  (449773, 0, 0),
  (449931, 3, 1),
  (454624, 2, 1),
  (455675, 0, 2),
  (463481, 2, 0),
  (474951, 2, 0),
  (484416, 3, 2),
  (488452, 2, 2),
  (490333, 1, 0),
  (506894, 0, 1),
  (511551, 1, 2),
  (519854, 2, 0),
  (529979, 0, 1),
  (535120, 0, 2),
  (537490, 2, 2),
  (546410, 1, 0),
  (555211, 3, 2),
  (562124, 1, 1),
  (566602, 0, 2),
  (578580, 1, 0),
  (582223, 1, 0),
  (588978, 0, 1),
  (593938, 3, 1),
  (604793, 3, 2),
  (605252, 1, 2),
  (605312, 1, 0),
  (606226, 3, 1),
  (608401, 0, 2),
  (609213, 0, 0),
  (626668, 2, 2),
  (635342, 3, 2),
  (636900, 0, 0),
  (639139, 2, 1),
  (654211, 2, 0),
  (663852, 3, 0),
  (665666, 0, 0),
  (669529, 0, 0),
  (669810, 1, 0),
  (671199, 2, 0),
  (686301, 3, 0),
  (690336, 3, 1),
  (690851, 2, 2),
  (691764, 1, 0),
  (708027, 2, 2),
  (719150, 2, 2),
  (720337, 1, 1),
  (724529, 2, 0),
  (732240, 1, 1),
  (738241, 2, 1),
  (740953, 3, 2),
  (749217, 0, 0),
  (763311, 2, 0),
  (777009, 3, 0),
  (779638, 3, 2),
  (783497, 3, 1),
  (794456, 0, 1),
  (800702, 3, 1),
  (802823, 0, 1),
  (805434, 3, 0),
  (805792, 0, 0),
  (806777, 3, 2),
  (812756, 3, 0),
  (817737, 0, 2),
  (835648, 1, 1),
  (842948, 3, 1),
  (848517, 3, 0),
  (849161, 0, 2),
  (855262, 3, 0),
  (857012, 3, 2),
  (869264, 0, 2),
  (872316, 0, 2),
  (880183, 3, 1),
  (882516, 3, 1),
  (897788, 1, 0),
  (899231, 1, 0),
  (899939, 0, 1),
  (904103, 0, 2),
  (911710, 3, 2),
  (914577, 3, 1),
  (927277, 1, 2),
  (929537, 2, 1),
  (930530, 1, 0),
  (937375, 1, 0),
  (970786, 1, 0),
  (975088, 1, 0),
  (975864, 3, 2),
  (975958, 1, 0),
  (976073, 1, 1),
  (977651, 1, 0),
  (978251, 2, 2),
  (980615, 3, 0),
  (984344, 2, 2),
  (996105, 3, 1),
  (996268, 0, 2),
  (997496, 3, 2),
  (999190, 1, 2),
  (1000895, 2, 2),
  (1002677, 0, 1),
  (1008382, 2, 1),
  (1032984, 1, 2),
  (1035281, 2, 0),
  (1040750, 2, 2),
  (1044001, 0, 0),
  (1051574, 0, 0),
  (1051806, 1, 1),
  (1087122, 2, 2),
  (1091775, 1, 0),
  (1093568, 0, 1),
  (1123274, 0, 2),
  (1126167, 0, 2),
  (1126214, 0, 1),
  (1127757, 0, 0),
  (1128083, 1, 1),
  (1131340, 1, 0),
  (1132659, 2, 0),
  (1135407, 1, 0),
  (1142864, 1, 0),
  (1154716, 0, 0),
  (1168915, 3, 1),
  (1170875, 1, 0),
  (1173987, 0, 2),
  (1177415, 3, 2),
  (1190979, 0, 2),
  (1197419, 3, 0),
  (1200570, 1, 2),
  (1200763, 1, 2),
  (1201855, 1, 0),
  (1224828, 0, 1),
  (1246738, 1, 2),
  (1256753, 3, 2),
  (1266232, 1, 2),
  (1281068, 0, 0),
  (1285236, 3, 0),
  (1290093, 2, 2),
  (1299274, 1, 0),
  (1304900, 1, 2),
  (1323195, 3, 1),
  (1324302, 1, 1),
  (1328180, 2, 2),
  (1333244, 3, 0),
  (1335078, 3, 1),
  (1353816, 1, 2),
  (1359190, 0, 2),
  (1366457, 0, 0),
  (1379748, 3, 1),
  (1380925, 2, 0),
  (1382594, 0, 2),
  (1382788, 1, 1),
  (1392728, 3, 1),
  (1395310, 2, 1),
  (1398736, 1, 0),
  (1400696, 0, 2),
  (1402256, 2, 0),
  (1410595, 1, 0),
  (1417085, 2, 2),
  (1418937, 2, 0),
  (1419386, 3, 2),
  (1419900, 1, 0),
  (1421123, 0, 2),
  (1427605, 0, 2),
  (1427983, 1, 1),
  (1442592, 1, 0),
  (1443759, 1, 2),
  (1446214, 2, 1),
  (1449195, 1, 1),
  (1452324, 2, 2),
  (1458074, 0, 2),
  (1468265, 3, 2),
  (1468410, 3, 1),
  (1470056, 0, 1),
  (1472632, 1, 2),
  (1477900, 2, 1),
  (1478936, 2, 0),
  (1485581, 0, 2),
  (1488753, 0, 2),
  (1493503, 2, 1),
  (1498029, 3, 2),
  (1500290, 0, 2),
  (1501383, 0, 0),
  (1501570, 1, 1),
  (1504864, 0, 0),
  (1517936, 0, 1),
  (1519489, 0, 0),
  (1520673, 3, 1),
  (1524798, 3, 0),
  (1537499, 1, 1),
  (1541463, 0, 2),
  (1546741, 3, 2),
  (1549527, 3, 1),
  (1558680, 0, 2),
  (1559650, 3, 0),
  (1581644, 0, 1),
  (1589644, 3, 2),
  (1603204, 3, 2),
  (1603925, 1, 2),
  (1608212, 3, 0),
  (1620768, 1, 1),
  (1628627, 0, 0),
  (1631006, 1, 1),
  (1633487, 3, 0),
  (1643366, 2, 0),
  (1650850, 0, 1),
  (1651753, 0, 2),
  (1652666, 2, 2),
  (1666875, 2, 0),
  (1667886, 2, 2),
  (1667950, 3, 0),
  (1671804, 1, 0),
  (1675293, 1, 2),
  (1675293, 2, 2),
  (1686535, 3, 0),
  (1689368, 3, 1),
  (1703018, 0, 1),
  (1708628, 1, 0),
  (1732194, 0, 0),
  (1737059, 2, 1),
  (1738836, 0, 0),
  (1741839, 0, 0),
  (1746411, 0, 1),
  (1752912, 3, 1),
  (1756492, 2, 1),
  (1770132, 3, 1),
  (1773111, 0, 0),
  (1775646, 1, 0),
  (1783407, 0, 0),
  (1790989, 0, 2),
  (1803349, 0, 0),
  (1805140, 3, 2),
  (1815518, 0, 1),
  (1820508, 3, 2),
  (1826516, 1, 2),
  (1833288, 0, 0),
  (1835219, 1, 0),
  (1841572, 3, 1),
  (1842223, 3, 1),
  (1845042, 3, 1),
  (1845099, 3, 0),
  (1854643, 0, 0),
  (1855328, 0, 0),
  (1873221, 3, 0),
  (1886425, 1, 0),
  (1887772, 1, 0),
  (1905994, 2, 0),
  (1907496, 2, 1),
  (1912081, 0, 1),
  (1923384, 2, 2),
  (1934022, 3, 2),
  (1935066, 3, 0),
  (1935193, 0, 2),
  (1950934, 1, 2),
  (1954858, 2, 1),
  (1955818, 0, 0),
  (1959937, 2, 1),
  (1963523, 1, 1),
  (1976901, 2, 1),
  (1979993, 2, 1),
  (1993329, 1, 1),
  (2006739, 3, 1),
  (2009685, 3, 1),
  (2016782, 1, 2),
  (2019420, 1, 1),
  (2024230, 1, 1),
  (2038976, 0, 1),
  (2044565, 2, 1),
  (2044940, 0, 2),
  (2055205, 0, 1),
  (2066295, 3, 0),
  (2068846, 1, 1),
  (2072024, 0, 0),
  (2073564, 3, 2),
  (2074720, 1, 1),
  (2081895, 3, 0),
  (2085007, 0, 2),
  (2089734, 0, 1),
  (2095123, 2, 0),
  (2105301, 3, 2),
  (2105958, 3, 1),
  (2106800, 3, 0),
  (2112004, 3, 2),
  (2112238, 1, 2),
  (2112626, 2, 0),
  (2113471, 3, 0),
  (2115662, 3, 1),
  (2118027, 3, 0),
  (2118299, 3, 2),
  (2124786, 0, 0),
  (2129395, 0, 1),
  (2132413, 1, 2),
  (2132491, 1, 1),
  (2137788, 1, 1),
  (2140664, 3, 2),
  (2142496, 2, 1),
  (2150631, 2, 1),
  (2155351, 3, 1),
  (2163385, 3, 1),
  (2166330, 0, 2),
  (2166575, 2, 0),
  (2168499, 0, 0),
  (2170274, 0, 1),
  (2171517, 3, 1),
  (2180099, 2, 1),
  (2189477, 1, 0),
  (2192618, 1, 2),
  (2195409, 1, 0),
  (2197174, 2, 2),
  (2198688, 3, 2),
  (2212098, 3, 1),
  (2216044, 3, 2),
  (2216491, 2, 0),
  (2217934, 1, 2),
  (2220195, 3, 2),
  (2234816, 2, 0),
  (2236386, 2, 2),
  (2260059, 1, 0),
  (2271375, 0, 2),
  (2276242, 0, 0),
  (2284701, 0, 1),
  (2288510, 0, 0),
  (2294656, 3, 1),
  (2298395, 2, 2),
  (2300884, 3, 2),
  (2302718, 3, 2),
  (2316103, 3, 0),
  (2327728, 2, 2),
  (2336199, 1, 0),
  (2343864, 3, 1),
  (2348429, 2, 1),
  (2355216, 2, 0),
  (2361017, 2, 2),
  (2363554, 0, 1),
  (2367487, 3, 2),
  (2381528, 0, 2),
  (2382254, 0, 0),
  (2389867, 1, 2),
  (2392590, 2, 1),
  (2398856, 2, 2),
  (2415341, 0, 1),
  (2422713, 0, 0),
  (2423073, 3, 0),
  (2429260, 3, 0),
  (2432175, 0, 1),
  (2435238, 2, 2),
  (2445296, 3, 1),
  (2446853, 2, 1),
  (2454747, 3, 2),
  (2463280, 1, 0),
  (2473584, 2, 1),
  (2475112, 1, 2),
  (2478346, 1, 1),
  (2481709, 3, 1),
  (2489133, 2, 0),
  (2502448, 2, 0),
  (2503485, 1, 2),
  (2515983, 3, 2),
  (2522295, 3, 1),
  (2523848, 0, 0),
  (2531874, 1, 2),
  (2532806, 1, 0),
  (2537898, 3, 2),
  (2538881, 1, 2),
  (2549690, 1, 2),
  (2549822, 0, 0),
  (2554893, 0, 1),
  (2558995, 0, 0),
  (2566323, 3, 2),
  (2569234, 3, 2),
  (2569324, 1, 0),
  (2573626, 0, 2),
  (2575859, 2, 0),
  (2596901, 0, 2),
  (2607052, 3, 1),
  (2611076, 0, 1),
  (2622533, 0, 1),
  (2637664, 1, 0),
  (2643588, 1, 2),
  (2652853, 1, 1),
  (2655867, 3, 0),
  (2659107, 3, 2),
  (2661200, 1, 2),
  (2668847, 1, 0),
  (2670988, 0, 2),
  (2671731, 2, 2),
  (2675920, 1, 1),
  (2680459, 1, 2),
  (2691049, 3, 2),
  (2701458, 1, 1),
  (2702888, 1, 1),
  (2704910, 1, 1),
  (2716255, 2, 1),
  (2719228, 3, 0),
  (2721000, 3, 1),
  (2727125, 0, 0),
  (2734267, 2, 2),
  (2756643, 1, 2),
  (2774498, 2, 0),
  (2774581, 3, 2),
  (2775123, 1, 0),
  (2776122, 0, 0),
  (2776343, 2, 0),
  (2796018, 2, 0),
  (2798522, 0, 0),
  (2804017, 1, 1),
  (2804396, 0, 2),
  (2814187, 3, 0),
  (2818166, 1, 0),
  (2822774, 3, 1),
  (2827519, 0, 1),
  (2828525, 3, 0),
  (2829660, 3, 2),
  (2837352, 0, 1),
  (2858447, 3, 1),
  (2862317, 0, 1),
  (2864110, 0, 2),
  (2875170, 0, 1),
  (2882744, 1, 0),
  (2884083, 3, 2),
  (2884456, 1, 2),
  (2885144, 0, 2),
  (2899811, 0, 2),
  (2904061, 1, 2),
  (2914544, 3, 1),
  (2922957, 0, 1),
  (2925958, 3, 1),
  (2929983, 0, 1),
  (2941694, 1, 0),
  (2945192, 3, 1),
  (2960018, 1, 1),
  (2960377, 2, 0),
  (2970121, 1, 1),
  (2970234, 3, 0),
  (2975976, 0, 1),
  (2976030, 3, 2),
  (2986528, 1, 0),
  (3002349, 0, 1),
  (3007386, 2, 2),
  (3009616, 2, 0),
  (3012563, 3, 0),
  (3015307, 3, 0),
  (3015509, 0, 2),
  (3017400, 0, 2),
  (3025800, 1, 1),
  (3039883, 1, 1),
  (3046566, 3, 1),
  (3051769, 3, 1),
  (3053333, 3, 0),
  (3082412, 3, 1),
  (3083247, 2, 1),
  (3085711, 1, 1),
  (3086037, 0, 0),
  (3088418, 0, 0),
  (3092060, 3, 1),
  (3092716, 1, 0),
  (3094918, 1, 2),
  (3104932, 1, 2),
  (3115745, 0, 2),
  (3126725, 2, 0),
  (3132586, 3, 0),
  (3150709, 1, 1),
  (3156459, 0, 2),
  (3166174, 0, 1),
  (3181360, 1, 1),
  (3186042, 2, 1),
  (3191454, 3, 0),
  (3199233, 2, 1),
  (3201942, 0, 2),
  (3209364, 2, 2),
  (3212262, 2, 2),
  (3213173, 0, 1),
  (3214945, 3, 0),
  (3224366, 2, 0),
  (3236873, 1, 1),
  (3240538, 0, 2),
  (3244680, 1, 0),
  (3244994, 3, 2),
  (3245713, 1, 0),
  (3251738, 3, 1),
  (3252248, 0, 0),
  (3258452, 3, 2),
  (3260587, 2, 2),
  (3264841, 1, 2),
  (3264908, 1, 0),
  (3269171, 1, 0),
  (3275486, 3, 2),
  (3278043, 0, 0),
  (3286102, 3, 1),
  (3290190, 2, 2),
  (3309204, 0, 0),
  (3328283, 3, 0),
  (3333383, 1, 2),
  (3335023, 1, 2),
  (3337806, 3, 0),
  (3360352, 3, 2),
  (3372111, 0, 2),
  (3376076, 1, 1),
  (3377845, 1, 2),
  (3380987, 3, 1),
  (3382941, 0, 1),
  (3383800, 0, 0),
  (3387385, 3, 0),
  (3390994, 2, 2),
  (3395610, 0, 2),
  (3412394, 2, 0),
  (3412674, 2, 2),
  (3425426, 3, 2),
  (3438273, 2, 2),
  (3451160, 0, 0),
  (3455294, 0, 2),
  (3478820, 2, 0),
  (3491808, 3, 2),
  (3494671, 2, 1),
  (3506984, 1, 0),
  (3511901, 2, 2),
  (3514717, 3, 0),
  (3520348, 1, 2),
  (3526388, 1, 1),
  (3528488, 3, 1),
  (3529974, 0, 0),
  (3537482, 3, 2),
  (3538568, 1, 2),
  (3540260, 2, 2),
  (3552437, 3, 1),
  (3554861, 2, 0),
  (3556040, 1, 2),
  (3567109, 1, 2),
  (3568915, 3, 0),
  (3576306, 2, 0),
  (3576859, 3, 1),
  (3578244, 2, 2),
  (3580128, 2, 2),
  (3581863, 0, 0),
  (3595492, 1, 0),
])
