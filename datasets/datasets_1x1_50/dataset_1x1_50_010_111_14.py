from src.util import *
schedule = deque([
  (5106, 1, 2),
  (7638, 5, 2),
  (8095, 2, 2),
  (10355, 1, 7),
  (15497, 2, 3),
  (19184, 2, 3),
  (27261, 6, 4),
  (32957, 6, 0),
  (33224, 6, 4),
  (39987, 2, 4),
  (40418, 3, 4),
  (41969, 1, 0),
  (46538, 0, 0),
  (54821, 0, 4),
  (57766, 0, 0),
  (67909, 4, 3),
  (70446, 7, 7),
  (74808, 4, 6),
  (83384, 5, 3),
  (84634, 3, 7),
  (93142, 0, 5),
  (103268, 5, 2),
  (103431, 2, 4),
  (105684, 0, 4),
  (116719, 4, 3),
  (120595, 0, 4),
  (127062, 1, 7),
  (138961, 5, 7),
  (143152, 6, 1),
  (147754, 7, 0),
  (149471, 0, 3),
  (153101, 6, 3),
  (154562, 3, 2),
  (166997, 7, 0),
  (167687, 4, 3),
  (176554, 4, 2),
  (179867, 4, 2),
  (183977, 0, 0),
  (189403, 2, 4),
  (195704, 5, 6),
  (198958, 7, 2),
  (199565, 0, 4),
  (203609, 1, 0),
  (231380, 0, 0),
  (261708, 0, 3),
  (265068, 2, 3),
  (272578, 2, 3),
  (276364, 0, 0),
  (285861, 3, 3),
  (299419, 6, 0),
  (302120, 1, 7),
  (302302, 2, 7),
  (303218, 2, 3),
  (305587, 2, 6),
  (314850, 3, 3),
  (317267, 7, 1),
  (317889, 0, 4),
  (318952, 6, 0),
  (332662, 2, 3),
  (333560, 0, 0),
  (342429, 3, 3),
  (344025, 0, 4),
  (353155, 5, 3),
  (357427, 5, 7),
  (360823, 4, 1),
  (362509, 3, 6),
  (365014, 2, 2),
  (365588, 6, 0),
  (366469, 0, 0),
  (371000, 0, 3),
  (384775, 5, 5),
  (393555, 4, 7),
  (412758, 4, 3),
  (418226, 7, 4),
  (430109, 4, 5),
  (438984, 1, 0),
  (442626, 2, 0),
  (445264, 0, 0),
  (449812, 4, 3),
  (462469, 4, 7),
  (463369, 7, 3),
  (469626, 0, 4),
  (493496, 3, 3),
  (506182, 3, 6),
  (508349, 3, 2),
  (520831, 6, 3),
  (526020, 7, 3),
  (530805, 4, 5),
  (536064, 2, 2),
  (537767, 7, 0),
  (541242, 3, 3),
  (542521, 7, 3),
  (550972, 7, 7),
  (552280, 4, 7),
  (559546, 5, 6),
  (567333, 5, 7),
  (573444, 0, 7),
  (576216, 2, 0),
  (576340, 5, 0),
  (581478, 6, 0),
  (587695, 7, 3),
  (595238, 5, 5),
  (597541, 3, 2),
  (606511, 7, 0),
  (612835, 3, 3),
  (620997, 3, 3),
  (626100, 7, 3),
  (631883, 7, 6),
  (635817, 6, 0),
  (638140, 1, 5),
  (647949, 5, 6),
  (654369, 3, 5),
  (655492, 2, 3),
  (656925, 3, 6),
  (662820, 1, 7),
  (669875, 4, 7),
  (686824, 7, 7),
  (691355, 0, 7),
  (693677, 2, 3),
  (693773, 1, 0),
  (693811, 3, 2),
  (699239, 0, 0),
  (699595, 0, 0),
  (705672, 7, 0),
  (709335, 1, 3),
  (717338, 2, 3),
  (719460, 3, 7),
  (720333, 3, 2),
  (722777, 1, 0),
  (743953, 0, 3),
  (744563, 4, 3),
  (756158, 1, 1),
  (770876, 2, 6),
  (772739, 6, 0),
  (773176, 0, 0),
  (775657, 2, 7),
  (776838, 4, 7),
  (780918, 2, 6),
  (792135, 4, 4),
  (801984, 1, 7),
  (803510, 0, 3),
  (805197, 0, 0),
  (817059, 6, 2),
  (818924, 0, 0),
  (856096, 3, 3),
  (860361, 7, 7),
  (871572, 7, 3),
  (873117, 0, 0),
  (875924, 6, 6),
  (877834, 7, 0),
  (881843, 0, 0),
  (888716, 2, 7),
  (889028, 7, 0),
  (895238, 2, 3),
  (899039, 5, 2),
  (899126, 2, 3),
  (899889, 4, 3),
  (904343, 7, 2),
  (906585, 7, 0),
  (910404, 2, 2),
  (922340, 4, 3),
  (923452, 1, 0),
  (927687, 3, 3),
  (938921, 3, 3),
  (955924, 1, 0),
  (966215, 2, 6),
  (969838, 4, 3),
  (975180, 4, 3),
  (989914, 5, 4),
  (991623, 4, 3),
  (996732, 0, 2),
  (1010193, 5, 3),
  (1013630, 6, 0),
  (1015298, 1, 0),
  (1016094, 5, 4),
  (1016347, 7, 0),
  (1025870, 3, 5),
  (1026036, 1, 3),
  (1035573, 7, 4),
  (1037083, 2, 3),
  (1047354, 3, 3),
  (1048941, 0, 3),
  (1049528, 6, 2),
  (1053733, 5, 2),
  (1057657, 2, 7),
  (1077990, 0, 0),
  (1079171, 1, 0),
  (1084880, 1, 0),
  (1088516, 7, 0),
  (1088625, 1, 0),
  (1090973, 2, 2),
  (1105333, 1, 3),
  (1118207, 6, 5),
  (1120245, 3, 3),
  (1126688, 5, 6),
  (1130916, 3, 3),
  (1132372, 1, 0),
  (1134869, 4, 3),
  (1138990, 2, 3),
  (1139660, 7, 6),
  (1141091, 2, 5),
  (1145395, 3, 3),
  (1150181, 1, 7),
  (1153937, 0, 0),
  (1157784, 0, 5),
  (1163987, 4, 2),
  (1172159, 6, 7),
  (1186434, 2, 2),
  (1192865, 6, 7),
  (1193699, 7, 3),
  (1203184, 3, 3),
  (1207467, 5, 7),
  (1217665, 7, 4),
  (1224762, 6, 3),
  (1227089, 0, 0),
  (1227110, 2, 5),
  (1232482, 1, 0),
  (1234023, 2, 3),
  (1238897, 5, 7),
  (1244200, 1, 0),
  (1259456, 7, 2),
  (1265851, 5, 7),
  (1272064, 1, 0),
  (1274942, 2, 7),
  (1275499, 5, 2),
  (1277701, 7, 5),
  (1280562, 0, 2),
  (1280661, 5, 3),
  (1281911, 7, 7),
  (1282449, 3, 6),
  (1288450, 3, 2),
  (1291254, 1, 0),
  (1314608, 4, 6),
  (1316392, 3, 0),
  (1319039, 2, 2),
  (1324323, 5, 3),
  (1326881, 0, 4),
  (1336307, 1, 0),
  (1340796, 5, 5),
  (1356337, 5, 3),
  (1357569, 2, 3),
  (1362284, 0, 3),
  (1388743, 5, 3),
  (1390541, 7, 4),
  (1391911, 2, 2),
  (1403128, 2, 3),
  (1423172, 5, 7),
  (1427069, 4, 1),
  (1427970, 6, 0),
  (1432868, 6, 0),
  (1436454, 0, 3),
  (1440379, 4, 7),
  (1442080, 5, 6),
  (1442516, 2, 3),
  (1447003, 0, 0),
  (1448506, 7, 4),
  (1449221, 6, 1),
  (1450470, 3, 2),
  (1450843, 3, 3),
  (1460081, 6, 5),
  (1461466, 6, 0),
  (1461810, 4, 3),
  (1469220, 7, 7),
  (1474815, 2, 6),
  (1491693, 4, 6),
  (1492917, 2, 0),
  (1493202, 4, 2),
  (1498621, 5, 7),
  (1505830, 6, 2),
  (1508165, 0, 7),
  (1515162, 1, 4),
  (1516746, 3, 3),
  (1516920, 7, 6),
  (1530384, 1, 0),
  (1537664, 6, 0),
  (1540584, 2, 5),
  (1543127, 6, 0),
  (1543486, 1, 1),
  (1551695, 0, 0),
  (1560183, 6, 3),
  (1576928, 7, 0),
  (1582843, 6, 3),
  (1584155, 3, 3),
  (1586229, 0, 3),
  (1587394, 4, 2),
  (1588724, 0, 3),
  (1599419, 5, 3),
  (1600075, 7, 0),
  (1603392, 7, 0),
  (1604922, 0, 0),
  (1610235, 1, 0),
  (1627271, 0, 7),
  (1629894, 7, 7),
  (1632347, 7, 6),
  (1641528, 0, 0),
  (1645704, 4, 3),
  (1646848, 0, 3),
  (1665233, 2, 3),
  (1667302, 7, 0),
  (1669448, 0, 0),
  (1678945, 3, 3),
  (1679536, 4, 6),
  (1692424, 7, 0),
  (1692910, 7, 7),
  (1701126, 1, 4),
  (1708491, 3, 6),
  (1712813, 7, 3),
  (1714480, 2, 2),
  (1717568, 2, 3),
  (1726139, 5, 3),
  (1736061, 0, 1),
  (1736317, 0, 0),
  (1742330, 7, 0),
  (1775062, 1, 0),
  (1775214, 6, 0),
  (1778736, 3, 1),
  (1783753, 7, 0),
  (1791460, 7, 6),
  (1792295, 6, 1),
  (1800396, 0, 0),
  (1803816, 3, 3),
  (1805647, 5, 2),
  (1807272, 2, 1),
  (1810210, 7, 6),
  (1819614, 0, 4),
  (1820516, 1, 0),
  (1828588, 2, 3),
  (1830280, 6, 3),
  (1835960, 0, 0),
  (1848744, 3, 3),
  (1851906, 6, 4),
  (1857581, 5, 2),
  (1867095, 1, 6),
  (1868261, 6, 2),
  (1868593, 4, 7),
  (1878266, 0, 4),
  (1895497, 5, 6),
  (1898149, 0, 0),
  (1906673, 1, 0),
  (1907258, 6, 3),
  (1911724, 7, 0),
  (1926089, 2, 3),
  (1937500, 4, 3),
  (1945835, 2, 3),
  (1962325, 0, 0),
  (1963721, 6, 6),
  (1967763, 6, 0),
  (1967941, 7, 0),
  (1968907, 7, 3),
  (1969417, 2, 3),
  (1971611, 1, 2),
  (1982924, 4, 3),
  (1985076, 5, 0),
  (1992271, 5, 7),
  (1992373, 2, 3),
  (2004514, 5, 3),
  (2019326, 6, 2),
  (2024997, 3, 3),
  (2027774, 0, 0),
  (2031806, 2, 3),
  (2040516, 2, 3),
  (2043457, 4, 7),
  (2044837, 5, 5),
  (2047851, 4, 3),
  (2048196, 1, 3),
  (2052601, 0, 4),
  (2065447, 5, 3),
  (2069647, 0, 3),
  (2090252, 4, 3),
  (2094215, 4, 2),
  (2100099, 3, 3),
  (2105614, 7, 0),
  (2111321, 7, 7),
  (2111777, 6, 0),
  (2115439, 3, 6),
  (2125076, 6, 0),
  (2128330, 5, 7),
  (2135817, 4, 6),
  (2148447, 3, 2),
  (2149169, 1, 4),
  (2149427, 2, 7),
  (2152231, 2, 4),
  (2152408, 0, 0),
  (2164650, 5, 7),
  (2172985, 4, 1),
  (2175631, 3, 5),
  (2182540, 5, 3),
  (2191116, 6, 0),
  (2194618, 5, 3),
  (2203390, 0, 0),
  (2209788, 1, 3),
  (2217144, 5, 3),
  (2226978, 7, 4),
  (2234313, 5, 3),
  (2235914, 5, 6),
  (2268865, 1, 0),
  (2269310, 6, 0),
  (2269662, 5, 3),
  (2269686, 3, 2),
  (2281201, 3, 6),
  (2292705, 4, 6),
  (2292796, 3, 7),
  (2301481, 7, 7),
  (2306622, 6, 0),
  (2321593, 6, 0),
  (2328678, 1, 4),
  (2335833, 1, 3),
  (2336627, 5, 0),
  (2360594, 5, 6),
  (2370467, 7, 3),
  (2374281, 7, 0),
  (2374297, 6, 0),
  (2382285, 2, 3),
  (2395439, 0, 0),
  (2411112, 3, 6),
  (2430485, 3, 3),
  (2431578, 0, 7),
  (2435572, 3, 3),
  (2438123, 7, 4),
  (2444163, 2, 2),
  (2444913, 2, 3),
  (2452499, 2, 3),
  (2468630, 4, 6),
  (2472603, 2, 3),
  (2487820, 2, 3),
  (2502201, 4, 7),
  (2515323, 1, 0),
  (2521611, 2, 3),
  (2521636, 3, 7),
  (2524601, 2, 3),
  (2525598, 1, 3),
  (2530539, 6, 7),
  (2537429, 0, 0),
  (2537495, 7, 4),
  (2539241, 6, 3),
  (2550176, 3, 7),
  (2551934, 3, 4),
  (2557178, 5, 3),
  (2558008, 2, 3),
  (2564222, 5, 7),
  (2574512, 0, 1),
  (2577504, 0, 0),
  (2578243, 3, 2),
  (2578379, 6, 3),
  (2593847, 6, 6),
  (2602463, 5, 7),
  (2613949, 5, 6),
  (2615277, 5, 3),
  (2622361, 2, 6),
  (2628242, 7, 2),
  (2629541, 7, 0),
  (2630678, 6, 6),
  (2632396, 7, 4),
  (2650647, 7, 3),
  (2658896, 7, 0),
  (2664682, 6, 3),
  (2667544, 5, 3),
  (2675240, 3, 3),
  (2675695, 3, 3),
  (2677813, 7, 5),
  (2679802, 3, 2),
  (2689831, 3, 2),
  (2696320, 2, 3),
  (2703415, 1, 0),
  (2717877, 3, 3),
  (2718430, 4, 5),
  (2718734, 2, 2),
  (2721856, 7, 0),
  (2727858, 5, 7),
  (2733957, 4, 7),
  (2743503, 1, 4),
  (2751889, 3, 3),
  (2753119, 5, 0),
  (2771615, 5, 6),
  (2775878, 2, 2),
  (2779792, 7, 4),
  (2782354, 5, 0),
  (2792055, 7, 4),
  (2794363, 2, 6),
  (2795179, 4, 6),
  (2802071, 1, 0),
  (2815120, 4, 6),
  (2821624, 6, 3),
  (2858395, 0, 0),
  (2865735, 5, 0),
  (2886674, 4, 3),
  (2890844, 2, 3),
  (2893079, 7, 4),
  (2927621, 1, 7),
  (2935884, 4, 3),
  (2944271, 2, 3),
  (2947888, 5, 7),
  (2954195, 6, 4),
  (2956622, 3, 3),
  (2957885, 4, 1),
  (2958524, 6, 4),
  (2969948, 3, 3),
  (2974051, 0, 3),
  (2977360, 2, 2),
  (2980511, 6, 4),
  (2986444, 0, 3),
  (2991194, 2, 7),
  (3003742, 0, 6),
  (3008637, 4, 3),
  (3030994, 0, 5),
  (3032711, 2, 3),
  (3042839, 7, 0),
  (3043390, 1, 7),
  (3047638, 0, 0),
  (3053773, 5, 7),
  (3059347, 3, 7),
  (3068228, 0, 6),
  (3082203, 3, 6),
  (3085942, 1, 0),
  (3090788, 5, 3),
  (3104308, 5, 4),
  (3105043, 1, 0),
  (3107591, 2, 3),
  (3114517, 0, 4),
  (3128798, 6, 5),
  (3131003, 3, 6),
  (3132650, 3, 5),
  (3132950, 1, 2),
  (3142019, 0, 4),
  (3157577, 0, 0),
  (3161190, 2, 3),
  (3165894, 7, 0),
  (3166534, 2, 3),
  (3167123, 3, 7),
  (3172084, 5, 3),
  (3180834, 4, 3),
  (3185040, 2, 4),
  (3185127, 6, 0),
  (3199486, 6, 4),
  (3209144, 1, 2),
  (3209696, 0, 0),
  (3213703, 6, 0),
  (3213764, 6, 7),
  (3218778, 7, 0),
  (3226505, 0, 0),
  (3228646, 3, 3),
  (3233071, 1, 3),
  (3234814, 3, 7),
  (3239228, 5, 3),
  (3241792, 5, 3),
  (3245577, 5, 3),
  (3255964, 6, 2),
  (3258118, 5, 3),
  (3267142, 5, 0),
  (3268095, 5, 7),
  (3274815, 2, 3),
  (3276320, 3, 3),
  (3276904, 7, 3),
  (3277067, 7, 5),
  (3288425, 6, 0),
  (3300341, 4, 3),
  (3305845, 1, 0),
  (3306388, 0, 3),
  (3310864, 7, 6),
  (3312157, 4, 3),
  (3313010, 2, 7),
  (3317951, 7, 3),
  (3319243, 7, 0),
  (3337228, 4, 6),
  (3338945, 4, 2),
  (3343080, 5, 2),
  (3353960, 7, 5),
  (3365340, 3, 7),
  (3366251, 0, 1),
  (3368971, 1, 4),
  (3379172, 3, 3),
  (3388950, 2, 2),
  (3399771, 6, 4),
  (3422981, 5, 6),
  (3427302, 6, 1),
  (3444811, 5, 3),
  (3446663, 5, 3),
  (3457623, 4, 2),
  (3477855, 4, 2),
  (3483152, 1, 0),
  (3498353, 0, 3),
  (3502763, 3, 7),
  (3503634, 4, 3),
  (3511008, 0, 4),
  (3514611, 7, 7),
  (3515633, 3, 3),
  (3521596, 1, 7),
  (3524020, 0, 0),
  (3532746, 3, 3),
  (3538001, 1, 0),
  (3541488, 0, 0),
  (3543358, 4, 6),
  (3546367, 0, 3),
  (3552378, 4, 3),
  (3555729, 5, 2),
  (3563408, 7, 0),
  (3568450, 3, 5),
  (3569619, 2, 6),
  (3572569, 7, 4),
  (3598132, 2, 6),
])