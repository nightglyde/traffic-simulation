from util import *
schedule = deque([
  (2804, 1, 3),
  (27043, 2, 7),
  (35227, 4, 6),
  (37061, 2, 3),
  (37079, 3, 3),
  (49675, 6, 6),
  (59019, 2, 3),
  (59976, 3, 3),
  (61775, 2, 0),
  (62697, 7, 7),
  (65615, 0, 2),
  (76911, 7, 0),
  (76972, 0, 4),
  (77966, 2, 5),
  (82969, 1, 7),
  (87125, 1, 0),
  (89086, 2, 7),
  (90109, 2, 3),
  (90511, 2, 0),
  (113798, 0, 7),
  (114059, 7, 0),
  (116221, 7, 0),
  (123162, 7, 0),
  (140477, 2, 3),
  (144671, 1, 7),
  (152740, 6, 7),
  (155420, 5, 7),
  (157709, 6, 7),
  (158064, 1, 4),
  (162739, 1, 7),
  (177298, 2, 7),
  (180135, 6, 6),
  (181200, 5, 6),
  (182628, 6, 7),
  (185293, 4, 5),
  (186184, 7, 4),
  (195269, 3, 6),
  (195636, 5, 2),
  (196598, 7, 7),
  (200707, 2, 3),
  (206920, 0, 7),
  (217304, 1, 7),
  (244262, 2, 5),
  (246943, 7, 7),
  (256408, 5, 7),
  (264471, 6, 0),
  (265790, 5, 6),
  (269227, 6, 0),
  (273762, 4, 7),
  (279497, 2, 3),
  (283758, 1, 5),
  (287525, 1, 0),
  (288453, 0, 0),
  (299028, 5, 6),
  (303016, 4, 3),
  (303710, 2, 4),
  (311465, 0, 2),
  (315553, 7, 0),
  (319927, 5, 3),
  (325135, 7, 7),
  (326757, 7, 4),
  (328007, 6, 0),
  (348887, 3, 6),
  (351120, 4, 3),
  (351349, 4, 3),
  (368733, 2, 2),
  (369635, 7, 7),
  (384567, 3, 5),
  (390194, 1, 0),
  (398133, 0, 0),
  (405721, 5, 2),
  (408395, 7, 0),
  (408680, 5, 7),
  (416791, 4, 7),
  (424552, 5, 3),
  (425273, 1, 7),
  (430995, 5, 3),
  (434194, 5, 7),
  (438467, 7, 7),
  (450687, 3, 2),
  (451135, 6, 3),
  (454689, 1, 3),
  (458333, 0, 4),
  (463647, 5, 6),
  (468325, 6, 3),
  (475323, 7, 0),
  (477420, 5, 7),
  (482990, 0, 4),
  (486924, 7, 4),
  (488562, 3, 3),
  (491697, 0, 0),
  (493672, 7, 4),
  (498698, 7, 4),
  (501854, 6, 0),
  (502070, 0, 4),
  (513867, 5, 6),
  (517979, 3, 4),
  (520083, 6, 6),
  (522821, 1, 0),
  (533945, 5, 2),
  (534610, 7, 0),
  (542710, 1, 7),
  (547022, 6, 2),
  (555090, 3, 7),
  (564110, 7, 4),
  (587321, 0, 5),
  (598760, 2, 7),
  (603934, 0, 6),
  (619374, 2, 6),
  (630685, 1, 3),
  (633118, 6, 7),
  (650906, 1, 0),
  (669293, 3, 2),
  (670733, 1, 7),
  (671733, 5, 3),
  (672027, 3, 7),
  (680741, 0, 6),
  (690270, 5, 7),
  (693067, 5, 3),
  (698005, 2, 6),
  (698122, 2, 3),
  (704194, 6, 4),
  (704419, 3, 2),
  (706454, 1, 7),
  (716894, 5, 5),
  (720436, 2, 7),
  (733686, 0, 7),
  (744025, 4, 3),
  (744680, 6, 7),
  (771804, 7, 0),
  (797246, 4, 5),
  (798512, 6, 7),
  (805293, 7, 1),
  (809072, 7, 7),
  (811926, 5, 4),
  (812770, 0, 6),
  (852420, 4, 5),
  (855039, 7, 0),
  (857244, 6, 0),
  (857472, 6, 0),
  (869433, 6, 7),
  (870965, 4, 2),
  (875720, 6, 3),
  (878219, 6, 7),
  (885753, 2, 7),
  (899650, 6, 3),
  (908927, 7, 0),
  (917931, 0, 4),
  (919960, 2, 3),
  (920435, 1, 2),
  (922217, 5, 7),
  (923025, 0, 5),
  (936704, 5, 7),
  (941097, 0, 0),
  (944735, 2, 7),
  (945134, 2, 3),
  (946100, 5, 2),
  (947266, 6, 3),
  (951757, 5, 2),
  (952730, 1, 5),
  (955031, 3, 2),
  (960988, 3, 6),
  (963562, 7, 7),
  (971324, 1, 5),
  (974663, 5, 2),
  (976218, 3, 1),
  (979010, 4, 3),
  (986699, 4, 6),
  (988732, 0, 7),
  (991537, 7, 4),
  (1000500, 4, 6),
  (1011311, 4, 7),
  (1018622, 7, 0),
  (1018623, 1, 7),
  (1031691, 0, 7),
  (1041713, 6, 7),
  (1042404, 1, 0),
  (1047037, 4, 1),
  (1051840, 0, 7),
  (1057323, 5, 7),
  (1057619, 5, 7),
  (1062313, 5, 7),
  (1062326, 3, 1),
  (1065058, 6, 7),
  (1067931, 3, 3),
  (1073157, 4, 3),
  (1075249, 1, 3),
  (1078268, 1, 3),
  (1087855, 0, 3),
  (1100222, 3, 3),
  (1108634, 3, 7),
  (1127719, 4, 6),
  (1131775, 5, 5),
  (1137665, 5, 6),
  (1137881, 4, 7),
  (1140130, 5, 2),
  (1140628, 3, 3),
  (1153060, 6, 7),
  (1153158, 3, 6),
  (1153604, 3, 3),
  (1177417, 5, 2),
  (1177813, 7, 0),
  (1186250, 4, 3),
  (1204608, 6, 7),
  (1213521, 5, 2),
  (1214236, 4, 7),
  (1220333, 4, 3),
  (1233767, 6, 7),
  (1238217, 4, 6),
  (1238286, 0, 7),
  (1238427, 0, 2),
  (1249627, 5, 3),
  (1253958, 5, 6),
  (1262856, 7, 3),
  (1266801, 6, 4),
  (1282816, 7, 0),
  (1286985, 5, 2),
  (1295631, 6, 3),
  (1297065, 3, 6),
  (1298886, 2, 6),
  (1306094, 7, 7),
  (1308305, 1, 0),
  (1309886, 1, 3),
  (1313069, 2, 3),
  (1313911, 7, 5),
  (1315375, 2, 2),
  (1315654, 3, 3),
  (1325005, 4, 2),
  (1331716, 1, 6),
  (1352885, 3, 3),
  (1358038, 3, 7),
  (1362447, 3, 6),
  (1372370, 4, 3),
  (1374278, 3, 3),
  (1380467, 0, 0),
  (1383341, 0, 4),
  (1388425, 1, 3),
  (1399647, 0, 6),
  (1412237, 1, 3),
  (1419703, 0, 0),
  (1428894, 0, 5),
  (1430289, 0, 0),
  (1433557, 6, 4),
  (1440564, 0, 4),
  (1457256, 5, 2),
  (1458176, 5, 7),
  (1465991, 6, 0),
  (1469883, 2, 2),
  (1473688, 7, 7),
  (1474363, 4, 7),
  (1474931, 0, 7),
  (1478853, 6, 0),
  (1479267, 7, 3),
  (1483090, 0, 3),
  (1493034, 6, 0),
  (1497574, 7, 4),
  (1500420, 0, 3),
  (1507487, 5, 3),
  (1519561, 5, 7),
  (1524175, 3, 7),
  (1536409, 0, 7),
  (1537853, 7, 4),
  (1553265, 1, 7),
  (1555340, 4, 3),
  (1564130, 7, 7),
  (1564571, 0, 7),
  (1573031, 5, 7),
  (1584893, 3, 3),
  (1600724, 3, 7),
  (1606896, 2, 7),
  (1610033, 1, 3),
  (1612630, 7, 0),
  (1619623, 3, 3),
  (1622951, 1, 6),
  (1631733, 7, 4),
  (1631866, 0, 4),
  (1654552, 3, 6),
  (1655485, 2, 3),
  (1658657, 1, 7),
  (1661989, 7, 6),
  (1662382, 3, 7),
  (1665924, 6, 0),
  (1709328, 2, 3),
  (1715110, 2, 3),
  (1717257, 1, 7),
  (1719671, 7, 5),
  (1723972, 5, 7),
  (1733587, 2, 7),
  (1733750, 6, 7),
  (1738488, 2, 6),
  (1740721, 2, 2),
  (1757659, 4, 5),
  (1765451, 4, 4),
  (1766899, 1, 6),
  (1770945, 2, 3),
  (1771369, 7, 0),
  (1775492, 3, 3),
  (1777386, 0, 6),
  (1777890, 0, 0),
  (1783385, 1, 7),
  (1785671, 1, 7),
  (1790088, 3, 3),
  (1793506, 2, 3),
  (1799409, 7, 7),
  (1800891, 6, 0),
  (1801073, 0, 7),
  (1826379, 6, 3),
  (1827578, 4, 7),
  (1831988, 3, 7),
  (1838614, 0, 3),
  (1846073, 4, 6),
  (1849779, 2, 5),
  (1859677, 6, 0),
  (1876785, 5, 3),
  (1885882, 6, 4),
  (1886018, 6, 4),
  (1896795, 7, 0),
  (1905980, 3, 6),
  (1919832, 3, 7),
  (1929983, 1, 6),
  (1934674, 0, 3),
  (1942128, 1, 6),
  (1948645, 7, 0),
  (1950232, 7, 7),
  (1951387, 0, 7),
  (1957347, 1, 4),
  (1972085, 7, 5),
  (1972157, 3, 3),
  (1975270, 4, 3),
  (1976213, 4, 3),
  (1989040, 6, 7),
  (1992769, 2, 3),
  (2003125, 7, 0),
  (2006752, 6, 3),
  (2011121, 2, 6),
  (2018359, 6, 7),
  (2028037, 0, 2),
  (2031668, 3, 5),
  (2046087, 6, 7),
  (2049218, 1, 3),
  (2057175, 7, 4),
  (2071134, 4, 2),
  (2072347, 6, 0),
  (2075411, 2, 4),
  (2082025, 7, 1),
  (2084155, 3, 3),
  (2100679, 7, 0),
  (2110689, 6, 0),
  (2118062, 4, 3),
  (2119496, 0, 7),
  (2131086, 3, 3),
  (2132878, 2, 1),
  (2143084, 5, 7),
  (2146150, 7, 5),
  (2165427, 5, 3),
  (2176328, 3, 3),
  (2183402, 2, 7),
  (2185212, 1, 3),
  (2189530, 4, 7),
  (2197500, 6, 3),
  (2200340, 1, 0),
  (2218878, 7, 0),
  (2224572, 2, 2),
  (2227516, 5, 3),
  (2228491, 7, 0),
  (2233682, 1, 4),
  (2240174, 7, 3),
  (2242710, 1, 5),
  (2245292, 0, 4),
  (2247654, 6, 7),
  (2250998, 7, 0),
  (2279627, 7, 3),
  (2282306, 1, 0),
  (2286677, 5, 3),
  (2303153, 7, 0),
  (2308729, 1, 0),
  (2314295, 5, 3),
  (2314947, 3, 7),
  (2328321, 4, 3),
  (2340302, 5, 6),
  (2340893, 1, 7),
  (2341431, 4, 7),
  (2342423, 1, 6),
  (2344786, 3, 3),
  (2347137, 6, 0),
  (2352859, 5, 0),
  (2369987, 4, 7),
  (2374897, 2, 3),
  (2387277, 6, 7),
  (2392945, 5, 3),
  (2393403, 6, 7),
  (2397479, 1, 0),
  (2406603, 4, 7),
  (2410021, 3, 7),
  (2410544, 3, 5),
  (2412433, 2, 7),
  (2413998, 1, 0),
  (2422527, 7, 7),
  (2424599, 7, 0),
  (2429200, 1, 7),
  (2429974, 2, 6),
  (2432975, 5, 6),
  (2437942, 1, 6),
  (2442198, 6, 4),
  (2458069, 0, 3),
  (2459124, 1, 3),
  (2460496, 0, 7),
  (2461124, 2, 6),
  (2463274, 6, 0),
  (2468149, 4, 7),
  (2470948, 5, 2),
  (2472548, 2, 1),
  (2486103, 7, 7),
  (2486928, 4, 7),
  (2505695, 0, 5),
  (2518876, 4, 6),
  (2521318, 1, 0),
  (2529512, 5, 6),
  (2546535, 2, 3),
  (2547702, 6, 3),
  (2548764, 4, 3),
  (2563436, 6, 3),
  (2565578, 5, 6),
  (2568795, 6, 0),
  (2575165, 1, 0),
  (2577473, 2, 6),
  (2579199, 6, 0),
  (2584434, 2, 3),
  (2584645, 6, 5),
  (2594365, 5, 5),
  (2596751, 7, 7),
  (2603211, 2, 3),
  (2607767, 7, 3),
  (2609717, 5, 3),
  (2610419, 1, 7),
  (2614136, 3, 6),
  (2617183, 2, 2),
  (2621222, 6, 7),
  (2624937, 3, 3),
  (2646955, 0, 3),
  (2658657, 3, 0),
  (2664845, 0, 3),
  (2670421, 5, 7),
  (2676035, 0, 3),
  (2679252, 4, 6),
  (2681518, 5, 2),
  (2690468, 5, 6),
  (2697584, 3, 2),
  (2698163, 0, 7),
  (2699317, 7, 7),
  (2702199, 5, 3),
  (2717649, 3, 6),
  (2725753, 3, 2),
  (2728269, 5, 7),
  (2730986, 6, 6),
  (2739710, 5, 3),
  (2750595, 1, 0),
  (2751894, 5, 3),
  (2752624, 6, 6),
  (2754793, 1, 2),
  (2765380, 6, 7),
  (2765869, 5, 6),
  (2773314, 7, 7),
  (2777865, 5, 7),
  (2783835, 3, 3),
  (2784887, 4, 7),
  (2786794, 5, 3),
  (2790891, 7, 7),
  (2796954, 3, 7),
  (2812936, 6, 7),
  (2822044, 6, 0),
  (2825469, 2, 7),
  (2827079, 1, 7),
  (2829342, 2, 4),
  (2832449, 5, 3),
  (2870411, 2, 2),
  (2876601, 6, 7),
  (2877765, 7, 0),
  (2877800, 2, 7),
  (2891140, 6, 6),
  (2902423, 7, 0),
  (2906684, 2, 5),
  (2917825, 5, 4),
  (2920677, 4, 7),
  (2927210, 7, 4),
  (2934535, 3, 7),
  (2935831, 3, 4),
  (2939339, 1, 4),
  (2941047, 0, 7),
  (2947629, 7, 7),
  (2955031, 1, 4),
  (2961762, 2, 3),
  (2963772, 4, 2),
  (2965073, 7, 7),
  (2973831, 7, 3),
  (2982432, 1, 0),
  (2992385, 0, 7),
  (2994031, 3, 2),
  (3000318, 2, 3),
  (3014633, 0, 6),
  (3025407, 1, 7),
  (3025788, 3, 6),
  (3031267, 2, 7),
  (3039066, 4, 3),
  (3047507, 1, 0),
  (3049676, 0, 6),
  (3080612, 5, 4),
  (3080811, 6, 7),
  (3107532, 1, 4),
  (3108063, 5, 7),
  (3115377, 6, 7),
  (3136546, 7, 4),
  (3148395, 7, 7),
  (3150327, 5, 7),
  (3151361, 6, 4),
  (3154400, 4, 6),
  (3154455, 0, 0),
  (3161849, 3, 3),
  (3162084, 5, 3),
  (3171310, 3, 3),
  (3174736, 6, 7),
  (3178277, 6, 3),
  (3179330, 0, 7),
  (3180474, 3, 2),
  (3193420, 5, 2),
  (3195265, 1, 0),
  (3197055, 2, 3),
  (3201919, 4, 5),
  (3210292, 7, 4),
  (3210719, 3, 5),
  (3213270, 4, 2),
  (3213809, 4, 3),
  (3215850, 7, 0),
  (3223697, 2, 3),
  (3223907, 1, 0),
  (3237022, 7, 3),
  (3242678, 2, 3),
  (3258454, 7, 7),
  (3262941, 6, 4),
  (3266261, 6, 0),
  (3267805, 0, 7),
  (3272091, 7, 4),
  (3272333, 0, 7),
  (3276840, 0, 4),
  (3277607, 4, 3),
  (3280193, 6, 3),
  (3290745, 2, 3),
  (3292442, 2, 3),
  (3301316, 5, 7),
  (3303080, 5, 3),
  (3304214, 0, 7),
  (3311453, 3, 4),
  (3330962, 6, 2),
  (3331925, 2, 3),
  (3337120, 0, 0),
  (3338370, 6, 0),
  (3351660, 0, 3),
  (3363058, 0, 4),
  (3369184, 7, 1),
  (3375427, 0, 7),
  (3378167, 4, 4),
  (3385154, 4, 6),
  (3385195, 6, 0),
  (3389521, 3, 2),
  (3389631, 4, 3),
  (3389881, 6, 3),
  (3391842, 3, 7),
  (3396765, 2, 2),
  (3396993, 0, 3),
  (3407609, 0, 3),
  (3411607, 7, 4),
  (3412438, 0, 7),
  (3419898, 2, 2),
  (3427371, 5, 7),
  (3429639, 4, 1),
  (3432174, 5, 3),
  (3435452, 1, 0),
  (3444655, 0, 5),
  (3453609, 7, 4),
  (3460022, 1, 0),
  (3475302, 2, 2),
  (3497099, 5, 3),
  (3499858, 3, 7),
  (3501290, 0, 0),
  (3505148, 5, 7),
  (3508677, 1, 0),
  (3509775, 4, 7),
  (3519690, 7, 7),
  (3532739, 7, 0),
  (3537144, 4, 3),
  (3547555, 2, 4),
  (3547659, 7, 6),
  (3553954, 4, 7),
  (3556150, 3, 7),
  (3557574, 0, 7),
  (3561188, 7, 4),
  (3567798, 7, 6),
  (3580701, 7, 0),
  (3595353, 1, 6),
  (3597918, 5, 5),
])