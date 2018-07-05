from util import *
schedule = deque([
  (4754, 5, 7),
  (7244, 7, 3),
  (9659, 3, 3),
  (21314, 5, 6),
  (25317, 4, 2),
  (51252, 2, 6),
  (51501, 5, 7),
  (56069, 3, 6),
  (56931, 1, 5),
  (60083, 3, 7),
  (61446, 4, 2),
  (72132, 2, 7),
  (72974, 0, 0),
  (83123, 5, 6),
  (85235, 4, 2),
  (85294, 6, 0),
  (86647, 4, 3),
  (103962, 2, 7),
  (106153, 1, 6),
  (121158, 6, 7),
  (133008, 6, 4),
  (136283, 0, 4),
  (137999, 4, 2),
  (139704, 3, 7),
  (153141, 4, 3),
  (155390, 0, 0),
  (157117, 7, 6),
  (172203, 3, 7),
  (172842, 3, 3),
  (187688, 1, 7),
  (188522, 0, 6),
  (194649, 1, 7),
  (194967, 2, 5),
  (196883, 2, 2),
  (197469, 4, 7),
  (198023, 6, 0),
  (202337, 7, 0),
  (211264, 0, 4),
  (217146, 1, 0),
  (220711, 2, 6),
  (221608, 2, 7),
  (228299, 5, 7),
  (229314, 5, 3),
  (237824, 1, 0),
  (241229, 1, 4),
  (249281, 7, 3),
  (252781, 1, 6),
  (256285, 4, 2),
  (259476, 4, 7),
  (260533, 7, 4),
  (262603, 2, 4),
  (264180, 3, 6),
  (266498, 0, 0),
  (266964, 2, 7),
  (267127, 7, 6),
  (271647, 2, 2),
  (284881, 0, 5),
  (307433, 0, 7),
  (319785, 6, 7),
  (325677, 4, 3),
  (327590, 1, 6),
  (328042, 5, 3),
  (331945, 2, 6),
  (335357, 1, 4),
  (339046, 1, 0),
  (340477, 7, 4),
  (342462, 1, 7),
  (363979, 0, 7),
  (369745, 5, 6),
  (370353, 1, 3),
  (371777, 3, 3),
  (374838, 4, 7),
  (376261, 2, 0),
  (377231, 3, 2),
  (379670, 7, 2),
  (381905, 5, 3),
  (382601, 7, 3),
  (384102, 1, 0),
  (385006, 4, 2),
  (391290, 4, 3),
  (396278, 6, 0),
  (397884, 5, 2),
  (405094, 3, 5),
  (408532, 3, 7),
  (409273, 5, 0),
  (417881, 4, 2),
  (422311, 2, 6),
  (422542, 1, 0),
  (429440, 2, 2),
  (433457, 4, 2),
  (436764, 0, 3),
  (439092, 6, 0),
  (443927, 5, 6),
  (446237, 0, 4),
  (454824, 5, 7),
  (459018, 0, 3),
  (462457, 6, 0),
  (466451, 0, 0),
  (467762, 2, 3),
  (475560, 6, 3),
  (480556, 6, 0),
  (481672, 3, 3),
  (497317, 2, 5),
  (502273, 2, 7),
  (507234, 5, 3),
  (517661, 4, 7),
  (523178, 5, 5),
  (528784, 7, 2),
  (532457, 2, 3),
  (539509, 2, 3),
  (542362, 5, 4),
  (547894, 7, 3),
  (563503, 2, 3),
  (565804, 7, 7),
  (599691, 3, 6),
  (600975, 0, 0),
  (608674, 6, 4),
  (612175, 3, 5),
  (616622, 5, 3),
  (630588, 6, 3),
  (631361, 0, 7),
  (632110, 5, 5),
  (632796, 3, 7),
  (633661, 6, 0),
  (634545, 2, 7),
  (643120, 3, 3),
  (656912, 2, 6),
  (661155, 4, 7),
  (672359, 5, 7),
  (673490, 2, 3),
  (679252, 1, 0),
  (686687, 5, 6),
  (690440, 2, 3),
  (699159, 5, 1),
  (702375, 3, 2),
  (707271, 0, 0),
  (709475, 3, 2),
  (722922, 2, 6),
  (728213, 0, 0),
  (728516, 2, 6),
  (730924, 6, 0),
  (739610, 3, 5),
  (752435, 0, 2),
  (756144, 2, 7),
  (771486, 0, 5),
  (772154, 6, 4),
  (773328, 0, 3),
  (779283, 2, 7),
  (780635, 1, 7),
  (782178, 6, 5),
  (782997, 7, 0),
  (784036, 3, 7),
  (784220, 4, 7),
  (789125, 7, 4),
  (795806, 6, 1),
  (796462, 1, 7),
  (799859, 2, 6),
  (801984, 1, 4),
  (804894, 1, 3),
  (805336, 4, 2),
  (809321, 0, 7),
  (823539, 2, 7),
  (825892, 0, 7),
  (829121, 4, 3),
  (834262, 5, 3),
  (839732, 1, 3),
  (845353, 6, 7),
  (847433, 7, 0),
  (852297, 7, 3),
  (853562, 0, 4),
  (861144, 1, 4),
  (866424, 7, 7),
  (868892, 1, 4),
  (889752, 2, 7),
  (898185, 6, 0),
  (908530, 2, 5),
  (912327, 1, 0),
  (919801, 6, 5),
  (921868, 3, 3),
  (941100, 3, 2),
  (949820, 3, 7),
  (950756, 3, 6),
  (950912, 1, 4),
  (953369, 3, 7),
  (955539, 3, 3),
  (955565, 1, 7),
  (955767, 6, 0),
  (970414, 1, 6),
  (971696, 7, 0),
  (991667, 0, 6),
  (997127, 1, 4),
  (1012725, 4, 5),
  (1021192, 4, 7),
  (1021793, 0, 7),
  (1025347, 4, 3),
  (1044419, 0, 7),
  (1045221, 1, 5),
  (1062647, 3, 2),
  (1065811, 6, 3),
  (1067654, 3, 2),
  (1093646, 2, 1),
  (1101968, 3, 6),
  (1105699, 4, 7),
  (1110237, 2, 3),
  (1111167, 2, 6),
  (1114253, 2, 7),
  (1116449, 7, 0),
  (1122237, 2, 7),
  (1125688, 5, 7),
  (1127189, 5, 7),
  (1128710, 5, 3),
  (1129323, 6, 4),
  (1145572, 0, 4),
  (1151248, 4, 3),
  (1156542, 4, 3),
  (1163637, 4, 7),
  (1175011, 7, 7),
  (1198490, 7, 3),
  (1212730, 5, 3),
  (1216540, 5, 2),
  (1217033, 1, 3),
  (1225735, 2, 7),
  (1230498, 1, 0),
  (1233585, 2, 6),
  (1240090, 5, 7),
  (1244378, 0, 4),
  (1254791, 3, 6),
  (1271872, 3, 1),
  (1272993, 7, 5),
  (1275481, 6, 5),
  (1285935, 7, 0),
  (1295200, 1, 6),
  (1295875, 3, 7),
  (1297503, 4, 3),
  (1302615, 2, 2),
  (1320814, 7, 5),
  (1344498, 0, 6),
  (1346000, 1, 0),
  (1354785, 2, 6),
  (1355265, 4, 4),
  (1361328, 1, 3),
  (1365534, 7, 6),
  (1367731, 1, 0),
  (1368949, 6, 6),
  (1372449, 2, 3),
  (1372594, 7, 3),
  (1375402, 0, 0),
  (1376695, 7, 0),
  (1380323, 6, 5),
  (1385802, 6, 4),
  (1389035, 2, 6),
  (1394708, 4, 2),
  (1398918, 6, 7),
  (1409310, 0, 0),
  (1417392, 7, 4),
  (1426190, 5, 7),
  (1435899, 4, 7),
  (1449998, 2, 2),
  (1460701, 1, 4),
  (1461951, 0, 7),
  (1470535, 0, 7),
  (1477093, 3, 4),
  (1484244, 3, 7),
  (1491823, 4, 7),
  (1499088, 3, 3),
  (1504718, 2, 2),
  (1514429, 3, 2),
  (1519217, 0, 7),
  (1521434, 1, 4),
  (1532868, 1, 7),
  (1551377, 0, 0),
  (1551595, 4, 2),
  (1555667, 2, 7),
  (1567564, 7, 0),
  (1568096, 5, 7),
  (1568813, 7, 7),
  (1570644, 4, 3),
  (1585696, 5, 2),
  (1596011, 7, 7),
  (1598633, 3, 3),
  (1619126, 4, 6),
  (1628800, 1, 4),
  (1629420, 6, 2),
  (1632919, 3, 3),
  (1635092, 6, 0),
  (1646943, 1, 2),
  (1653896, 5, 3),
  (1654173, 2, 3),
  (1667800, 3, 7),
  (1674113, 3, 7),
  (1674495, 1, 7),
  (1677013, 0, 4),
  (1680028, 4, 2),
  (1697392, 6, 2),
  (1701082, 5, 0),
  (1702242, 6, 7),
  (1715833, 5, 6),
  (1715980, 5, 7),
  (1719134, 3, 3),
  (1720819, 2, 6),
  (1724164, 3, 2),
  (1725330, 7, 0),
  (1739423, 6, 0),
  (1746923, 3, 2),
  (1747864, 1, 0),
  (1753392, 0, 4),
  (1754901, 1, 0),
  (1767996, 7, 6),
  (1780204, 7, 4),
  (1803072, 2, 3),
  (1805495, 7, 7),
  (1823254, 2, 7),
  (1830453, 6, 0),
  (1838373, 1, 7),
  (1840484, 6, 4),
  (1840753, 5, 7),
  (1856093, 2, 1),
  (1867532, 6, 7),
  (1884937, 5, 3),
  (1899182, 5, 7),
  (1907355, 0, 0),
  (1917413, 2, 3),
  (1931609, 6, 7),
  (1936456, 1, 0),
  (1938668, 7, 0),
  (1943731, 6, 0),
  (1945358, 7, 7),
  (1945837, 5, 6),
  (1946641, 2, 7),
  (1950717, 3, 7),
  (1953605, 5, 4),
  (1954656, 5, 4),
  (1960444, 7, 5),
  (1963382, 3, 3),
  (1972960, 2, 4),
  (1977116, 7, 1),
  (1978066, 6, 3),
  (1979413, 4, 2),
  (1981330, 3, 0),
  (1986498, 5, 3),
  (1987060, 2, 7),
  (1993051, 0, 0),
  (2016494, 1, 7),
  (2018505, 3, 0),
  (2019336, 1, 7),
  (2026421, 4, 3),
  (2031270, 7, 0),
  (2031602, 5, 7),
  (2037437, 4, 6),
  (2039188, 3, 7),
  (2040515, 6, 7),
  (2041063, 6, 4),
  (2041509, 7, 7),
  (2051618, 1, 3),
  (2060918, 4, 2),
  (2062009, 5, 7),
  (2062283, 1, 0),
  (2067727, 7, 0),
  (2071229, 6, 0),
  (2072451, 0, 2),
  (2076526, 6, 0),
  (2088978, 0, 7),
  (2089253, 4, 7),
  (2091858, 7, 3),
  (2100643, 2, 3),
  (2103173, 3, 7),
  (2126106, 3, 7),
  (2130391, 4, 5),
  (2132371, 4, 2),
  (2134614, 2, 6),
  (2141853, 6, 7),
  (2155041, 7, 5),
  (2156168, 1, 5),
  (2169461, 2, 2),
  (2174232, 2, 2),
  (2200081, 5, 0),
  (2203731, 6, 7),
  (2211417, 0, 7),
  (2225656, 4, 5),
  (2231122, 5, 1),
  (2235089, 2, 7),
  (2238082, 3, 3),
  (2241882, 0, 3),
  (2248149, 7, 7),
  (2249879, 4, 2),
  (2253704, 7, 0),
  (2254390, 5, 7),
  (2258140, 7, 7),
  (2270415, 2, 3),
  (2278553, 3, 3),
  (2287579, 1, 4),
  (2288143, 7, 7),
  (2290572, 1, 7),
  (2295155, 4, 2),
  (2319349, 0, 7),
  (2330096, 2, 5),
  (2344381, 1, 4),
  (2371623, 5, 6),
  (2377449, 2, 3),
  (2380051, 0, 0),
  (2380924, 3, 3),
  (2381029, 3, 2),
  (2395230, 3, 6),
  (2399850, 2, 5),
  (2403508, 1, 4),
  (2408718, 2, 2),
  (2408951, 7, 7),
  (2416948, 0, 6),
  (2446256, 2, 3),
  (2458615, 1, 4),
  (2466260, 1, 2),
  (2471862, 6, 4),
  (2482293, 0, 7),
  (2486997, 2, 6),
  (2489724, 5, 7),
  (2490919, 1, 2),
  (2491426, 4, 6),
  (2502544, 1, 6),
  (2506172, 5, 6),
  (2511806, 0, 7),
  (2515200, 2, 2),
  (2515506, 2, 6),
  (2528002, 4, 2),
  (2536924, 3, 7),
  (2549501, 6, 7),
  (2557160, 5, 6),
  (2560767, 6, 4),
  (2568651, 3, 3),
  (2569227, 0, 3),
  (2577703, 5, 2),
  (2581132, 5, 6),
  (2589821, 5, 3),
  (2598996, 1, 7),
  (2601784, 0, 4),
  (2607551, 6, 3),
  (2608521, 7, 7),
  (2615348, 5, 2),
  (2623903, 0, 7),
  (2626378, 6, 7),
  (2642773, 0, 0),
  (2654441, 0, 7),
  (2657159, 3, 4),
  (2657927, 3, 0),
  (2660697, 7, 0),
  (2660802, 5, 7),
  (2662629, 4, 3),
  (2666792, 6, 7),
  (2673144, 7, 3),
  (2676796, 6, 7),
  (2688605, 2, 6),
  (2694229, 7, 0),
  (2701689, 2, 4),
  (2702315, 2, 7),
  (2724509, 0, 7),
  (2724593, 4, 3),
  (2741879, 7, 2),
  (2742993, 6, 3),
  (2751685, 0, 6),
  (2752366, 5, 7),
  (2753013, 0, 7),
  (2757965, 5, 3),
  (2759489, 0, 0),
  (2761028, 1, 0),
  (2777429, 2, 3),
  (2787501, 4, 3),
  (2803680, 0, 7),
  (2812092, 0, 4),
  (2813002, 6, 7),
  (2821471, 6, 4),
  (2823822, 1, 4),
  (2830649, 7, 7),
  (2833958, 7, 3),
  (2850584, 4, 7),
  (2865007, 4, 2),
  (2866060, 4, 3),
  (2869592, 1, 7),
  (2875307, 2, 7),
  (2876236, 6, 0),
  (2886549, 6, 0),
  (2888404, 7, 7),
  (2895731, 5, 4),
  (2897919, 2, 7),
  (2902199, 7, 3),
  (2914796, 6, 7),
  (2914918, 2, 3),
  (2920259, 3, 6),
  (2921450, 6, 0),
  (2933687, 6, 0),
  (2940822, 0, 0),
  (2941844, 5, 7),
  (2953479, 6, 7),
  (2956957, 0, 3),
  (2970763, 4, 3),
  (2971680, 5, 6),
  (2978912, 5, 7),
  (2999368, 7, 5),
  (3003522, 3, 1),
  (3006013, 5, 7),
  (3008425, 0, 4),
  (3017692, 2, 7),
  (3021653, 3, 3),
  (3023974, 7, 3),
  (3026809, 3, 3),
  (3031588, 7, 4),
  (3036707, 2, 2),
  (3043452, 3, 2),
  (3048180, 5, 7),
  (3052345, 2, 2),
  (3052609, 2, 2),
  (3063240, 5, 3),
  (3064578, 2, 7),
  (3068759, 5, 0),
  (3073538, 0, 3),
  (3079435, 3, 3),
  (3090201, 2, 3),
  (3114751, 0, 3),
  (3127074, 4, 7),
  (3128049, 1, 0),
  (3142230, 3, 7),
  (3145240, 5, 5),
  (3159081, 3, 5),
  (3169263, 3, 2),
  (3187147, 2, 5),
  (3193255, 5, 3),
  (3196839, 7, 7),
  (3197910, 7, 7),
  (3216900, 4, 3),
  (3218912, 4, 7),
  (3222131, 7, 3),
  (3227485, 1, 7),
  (3229288, 7, 3),
  (3230808, 4, 2),
  (3237642, 4, 7),
  (3260643, 2, 7),
  (3263633, 0, 7),
  (3271251, 7, 0),
  (3277975, 3, 3),
  (3287147, 2, 6),
  (3289615, 7, 6),
  (3295739, 6, 7),
  (3300067, 3, 5),
  (3301037, 1, 4),
  (3305487, 2, 3),
  (3310001, 7, 4),
  (3311380, 7, 3),
  (3312356, 1, 7),
  (3316167, 1, 0),
  (3318328, 2, 3),
  (3324547, 2, 7),
  (3328756, 1, 3),
  (3331092, 2, 7),
  (3333626, 6, 3),
  (3336456, 6, 6),
  (3337791, 5, 7),
  (3346763, 4, 6),
  (3370199, 6, 7),
  (3376774, 4, 7),
  (3381978, 2, 3),
  (3386253, 6, 0),
  (3386276, 1, 7),
  (3386711, 0, 4),
  (3388441, 0, 4),
  (3390820, 6, 0),
  (3394568, 5, 3),
  (3396668, 2, 5),
  (3399644, 4, 6),
  (3405222, 5, 1),
  (3412030, 2, 3),
  (3416028, 2, 2),
  (3419232, 0, 7),
  (3420281, 5, 6),
  (3432055, 7, 5),
  (3441513, 1, 7),
  (3441860, 6, 0),
  (3448322, 1, 0),
  (3449105, 3, 6),
  (3472741, 0, 0),
  (3478007, 7, 0),
  (3483757, 2, 5),
  (3498179, 0, 7),
  (3502063, 6, 0),
  (3505672, 4, 7),
  (3509206, 0, 7),
  (3516981, 3, 2),
  (3526642, 7, 4),
  (3531372, 7, 7),
  (3546864, 1, 0),
  (3556757, 4, 3),
  (3557001, 1, 7),
  (3560173, 5, 0),
  (3569270, 4, 2),
  (3569509, 6, 6),
  (3573015, 2, 5),
  (3574006, 5, 3),
  (3586687, 4, 3),
  (3590050, 3, 7),
  (3590829, 4, 7),
  (3592755, 1, 6),
  (3593856, 3, 5),
  (3595390, 2, 7),
])
