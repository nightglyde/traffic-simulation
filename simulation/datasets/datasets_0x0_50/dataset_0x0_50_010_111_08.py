from src.util import *
schedule = deque([
  (18006, 2, 2),
  (19000, 1, 2),
  (19140, 1, 1),
  (20796, 2, 0),
  (22926, 2, 2),
  (26019, 2, 1),
  (28959, 0, 2),
  (29214, 1, 1),
  (37940, 1, 0),
  (56271, 1, 0),
  (58810, 0, 2),
  (67477, 3, 0),
  (73099, 1, 2),
  (75055, 1, 2),
  (79138, 0, 2),
  (89455, 1, 1),
  (91003, 1, 2),
  (95396, 3, 2),
  (107522, 0, 1),
  (109071, 0, 1),
  (144447, 3, 2),
  (159986, 3, 1),
  (165755, 1, 1),
  (168245, 0, 1),
  (184277, 1, 1),
  (203924, 3, 2),
  (219129, 0, 0),
  (219170, 0, 1),
  (223220, 3, 1),
  (224376, 1, 2),
  (224826, 0, 2),
  (229173, 2, 2),
  (230240, 0, 1),
  (233301, 1, 0),
  (234137, 0, 1),
  (253934, 2, 0),
  (259985, 3, 0),
  (262795, 1, 1),
  (264456, 0, 2),
  (268645, 0, 0),
  (270585, 3, 0),
  (279925, 3, 0),
  (282730, 3, 2),
  (294860, 2, 1),
  (295412, 2, 0),
  (299855, 0, 1),
  (301017, 0, 2),
  (302797, 3, 2),
  (311763, 1, 0),
  (314658, 0, 0),
  (324664, 1, 1),
  (324790, 3, 2),
  (325487, 1, 2),
  (336389, 2, 1),
  (350512, 2, 2),
  (356844, 1, 1),
  (361181, 1, 0),
  (364702, 3, 0),
  (365572, 0, 2),
  (366295, 2, 2),
  (368566, 2, 0),
  (375551, 0, 0),
  (386309, 1, 2),
  (389302, 0, 1),
  (392447, 0, 2),
  (410914, 0, 1),
  (411208, 3, 0),
  (418936, 1, 0),
  (423164, 0, 0),
  (431625, 3, 1),
  (437181, 3, 2),
  (442192, 1, 1),
  (442970, 1, 2),
  (443213, 1, 0),
  (445447, 0, 0),
  (461651, 0, 1),
  (474261, 3, 2),
  (474627, 3, 2),
  (474844, 3, 2),
  (480341, 2, 1),
  (490076, 0, 0),
  (499021, 1, 2),
  (506009, 1, 1),
  (507067, 1, 1),
  (511595, 3, 2),
  (521570, 1, 0),
  (532084, 3, 2),
  (536364, 0, 2),
  (538627, 1, 1),
  (544870, 0, 0),
  (548354, 3, 2),
  (548397, 1, 0),
  (564269, 0, 2),
  (587931, 3, 0),
  (594534, 2, 1),
  (594873, 0, 2),
  (595158, 2, 2),
  (609908, 2, 2),
  (611016, 3, 0),
  (611770, 0, 1),
  (616302, 2, 0),
  (619153, 3, 1),
  (620671, 0, 2),
  (621484, 1, 2),
  (622416, 2, 1),
  (623207, 2, 2),
  (623679, 3, 0),
  (624430, 2, 2),
  (627352, 0, 0),
  (627896, 1, 0),
  (634538, 2, 1),
  (637588, 1, 0),
  (638892, 2, 0),
  (656666, 0, 1),
  (670795, 0, 1),
  (674740, 2, 1),
  (684937, 3, 2),
  (685246, 0, 1),
  (688044, 2, 1),
  (690750, 0, 2),
  (696118, 3, 2),
  (714924, 3, 0),
  (731643, 2, 2),
  (744662, 1, 2),
  (751561, 1, 0),
  (754357, 1, 2),
  (756805, 0, 2),
  (763103, 2, 2),
  (790116, 3, 2),
  (795041, 1, 2),
  (800239, 1, 0),
  (802908, 2, 0),
  (803464, 1, 0),
  (811750, 1, 0),
  (813586, 1, 1),
  (814674, 3, 0),
  (816583, 1, 1),
  (819915, 2, 2),
  (826203, 2, 2),
  (829349, 0, 1),
  (829994, 1, 1),
  (838857, 0, 0),
  (843580, 3, 0),
  (848401, 2, 1),
  (856691, 2, 2),
  (858138, 3, 2),
  (860249, 3, 2),
  (862944, 2, 2),
  (867297, 1, 0),
  (869574, 0, 0),
  (870042, 3, 2),
  (873711, 1, 2),
  (875695, 3, 0),
  (875845, 3, 0),
  (877605, 3, 2),
  (885619, 0, 2),
  (891909, 2, 1),
  (894412, 1, 2),
  (897265, 0, 2),
  (919061, 3, 2),
  (934552, 3, 1),
  (937945, 3, 1),
  (956532, 1, 0),
  (957870, 1, 0),
  (963039, 0, 0),
  (974698, 2, 1),
  (982310, 1, 1),
  (983132, 0, 0),
  (986307, 3, 0),
  (994326, 1, 0),
  (1001086, 2, 2),
  (1003131, 3, 2),
  (1009430, 2, 1),
  (1012719, 0, 0),
  (1020201, 0, 2),
  (1032404, 3, 1),
  (1048812, 3, 0),
  (1070997, 2, 0),
  (1080280, 3, 0),
  (1084541, 0, 1),
  (1097720, 0, 2),
  (1100938, 2, 2),
  (1102818, 2, 0),
  (1114280, 2, 1),
  (1126450, 0, 2),
  (1128401, 2, 1),
  (1133952, 2, 1),
  (1135780, 3, 0),
  (1154329, 3, 2),
  (1156383, 3, 0),
  (1167227, 2, 0),
  (1170738, 2, 1),
  (1171237, 0, 1),
  (1174461, 0, 1),
  (1177565, 0, 1),
  (1182887, 3, 1),
  (1192694, 0, 2),
  (1194353, 1, 0),
  (1194921, 2, 0),
  (1199064, 3, 1),
  (1201538, 3, 2),
  (1222277, 1, 0),
  (1231127, 1, 1),
  (1235987, 2, 1),
  (1240386, 1, 0),
  (1243619, 2, 1),
  (1257039, 3, 2),
  (1271391, 3, 1),
  (1271919, 3, 0),
  (1272901, 1, 1),
  (1274152, 2, 2),
  (1274310, 0, 1),
  (1279499, 0, 0),
  (1283661, 0, 2),
  (1284738, 3, 0),
  (1285911, 3, 1),
  (1287131, 0, 2),
  (1300251, 2, 1),
  (1302220, 2, 0),
  (1311190, 3, 0),
  (1311639, 2, 0),
  (1327064, 1, 0),
  (1336853, 0, 2),
  (1352886, 1, 2),
  (1353394, 3, 1),
  (1358054, 0, 0),
  (1367355, 1, 1),
  (1369359, 0, 2),
  (1399867, 3, 2),
  (1400564, 3, 1),
  (1401313, 0, 2),
  (1402397, 3, 1),
  (1417163, 1, 2),
  (1419899, 2, 0),
  (1434288, 3, 2),
  (1435781, 3, 1),
  (1437999, 1, 1),
  (1439518, 3, 1),
  (1450805, 3, 1),
  (1456809, 1, 1),
  (1457634, 1, 2),
  (1458420, 1, 0),
  (1459946, 3, 1),
  (1465193, 0, 2),
  (1466412, 0, 2),
  (1467387, 3, 0),
  (1474841, 2, 2),
  (1494864, 0, 2),
  (1498497, 3, 2),
  (1513404, 0, 2),
  (1515470, 1, 1),
  (1518422, 1, 0),
  (1519457, 1, 1),
  (1520039, 0, 1),
  (1522765, 0, 2),
  (1537174, 3, 0),
  (1538332, 2, 1),
  (1541597, 0, 1),
  (1556244, 1, 1),
  (1565621, 2, 0),
  (1566762, 2, 2),
  (1569413, 3, 2),
  (1611383, 2, 1),
  (1611732, 3, 0),
  (1627007, 1, 1),
  (1633466, 1, 2),
  (1635345, 2, 0),
  (1645674, 2, 2),
  (1679096, 0, 2),
  (1694619, 0, 2),
  (1695827, 0, 2),
  (1703210, 1, 1),
  (1707294, 0, 1),
  (1709513, 2, 2),
  (1713292, 1, 0),
  (1727401, 1, 1),
  (1728058, 3, 1),
  (1731078, 2, 1),
  (1733258, 2, 1),
  (1736521, 3, 1),
  (1741813, 2, 1),
  (1745048, 0, 1),
  (1748698, 3, 1),
  (1751608, 3, 1),
  (1769713, 1, 1),
  (1771093, 1, 2),
  (1782264, 3, 2),
  (1795990, 3, 0),
  (1805424, 2, 1),
  (1812929, 0, 1),
  (1818850, 2, 0),
  (1819960, 2, 2),
  (1822017, 3, 2),
  (1827468, 0, 1),
  (1829466, 3, 1),
  (1831881, 1, 0),
  (1832940, 1, 1),
  (1834974, 1, 0),
  (1850243, 0, 0),
  (1852518, 3, 0),
  (1855173, 2, 0),
  (1888212, 3, 2),
  (1889806, 2, 0),
  (1892872, 2, 2),
  (1897419, 1, 2),
  (1906271, 2, 2),
  (1908186, 3, 1),
  (1918468, 2, 2),
  (1921080, 2, 1),
  (1931293, 0, 2),
  (1934343, 0, 0),
  (1944137, 1, 0),
  (1949632, 1, 0),
  (1951434, 3, 2),
  (1953772, 0, 1),
  (1963541, 3, 0),
  (1967826, 1, 2),
  (1977703, 1, 2),
  (1989115, 3, 0),
  (1993075, 1, 2),
  (1994371, 0, 2),
  (1994660, 3, 2),
  (2002615, 0, 0),
  (2002692, 3, 1),
  (2008855, 0, 2),
  (2011406, 1, 1),
  (2014564, 2, 1),
  (2022567, 0, 0),
  (2026924, 0, 1),
  (2028001, 0, 0),
  (2029410, 3, 0),
  (2040516, 2, 0),
  (2053056, 2, 0),
  (2056902, 2, 0),
  (2065114, 3, 0),
  (2073621, 1, 1),
  (2074166, 0, 2),
  (2074171, 2, 0),
  (2079430, 2, 1),
  (2080731, 1, 0),
  (2092084, 0, 0),
  (2101336, 2, 0),
  (2104221, 1, 1),
  (2126141, 1, 2),
  (2127473, 2, 0),
  (2140340, 0, 2),
  (2144052, 0, 2),
  (2155745, 2, 1),
  (2171721, 2, 1),
  (2172030, 2, 1),
  (2174406, 3, 1),
  (2178785, 1, 1),
  (2179684, 2, 0),
  (2190927, 0, 2),
  (2192566, 0, 1),
  (2196362, 3, 1),
  (2197401, 3, 2),
  (2199297, 2, 0),
  (2200041, 2, 0),
  (2200979, 0, 2),
  (2201343, 0, 2),
  (2207726, 0, 0),
  (2209849, 3, 1),
  (2211922, 3, 2),
  (2222814, 1, 0),
  (2225075, 2, 2),
  (2235158, 2, 1),
  (2239261, 0, 1),
  (2244896, 1, 2),
  (2249395, 3, 2),
  (2250142, 0, 2),
  (2259866, 2, 2),
  (2260101, 2, 2),
  (2262634, 0, 0),
  (2275451, 2, 0),
  (2285445, 0, 1),
  (2285560, 1, 0),
  (2292643, 3, 2),
  (2308058, 1, 0),
  (2309137, 3, 0),
  (2319639, 1, 1),
  (2324259, 0, 2),
  (2332086, 0, 2),
  (2335831, 0, 1),
  (2337320, 2, 1),
  (2337347, 3, 2),
  (2355647, 3, 0),
  (2357829, 2, 2),
  (2368036, 3, 0),
  (2371643, 0, 0),
  (2382777, 0, 0),
  (2395932, 0, 1),
  (2397139, 0, 1),
  (2416886, 2, 2),
  (2427084, 2, 1),
  (2433281, 1, 2),
  (2434098, 2, 2),
  (2437269, 3, 0),
  (2442046, 1, 0),
  (2450774, 0, 1),
  (2451250, 1, 2),
  (2451655, 2, 1),
  (2453347, 2, 2),
  (2453698, 3, 0),
  (2469334, 0, 0),
  (2472044, 2, 1),
  (2474686, 3, 2),
  (2491780, 0, 0),
  (2506321, 1, 1),
  (2510816, 1, 2),
  (2511795, 1, 2),
  (2514154, 2, 0),
  (2516432, 1, 2),
  (2520444, 2, 0),
  (2525348, 2, 2),
  (2528539, 0, 2),
  (2537092, 2, 2),
  (2537461, 3, 1),
  (2538942, 2, 2),
  (2541897, 2, 2),
  (2542443, 1, 0),
  (2562553, 0, 1),
  (2563090, 3, 1),
  (2564881, 1, 0),
  (2574615, 1, 2),
  (2580327, 2, 1),
  (2585275, 2, 1),
  (2586834, 3, 1),
  (2588058, 1, 0),
  (2591364, 1, 2),
  (2594803, 0, 0),
  (2598883, 0, 2),
  (2605986, 0, 0),
  (2610155, 3, 0),
  (2612684, 2, 0),
  (2624169, 2, 0),
  (2626551, 2, 0),
  (2628021, 3, 1),
  (2629279, 2, 1),
  (2634421, 2, 2),
  (2634874, 1, 1),
  (2638281, 1, 0),
  (2663869, 2, 0),
  (2664970, 0, 0),
  (2671306, 2, 2),
  (2672888, 2, 1),
  (2676990, 1, 0),
  (2679025, 1, 0),
  (2691076, 1, 1),
  (2697050, 0, 0),
  (2697203, 2, 1),
  (2703951, 0, 2),
  (2720117, 1, 1),
  (2728417, 2, 2),
  (2731938, 3, 0),
  (2737681, 0, 2),
  (2743393, 1, 0),
  (2745659, 2, 0),
  (2750384, 0, 1),
  (2760263, 3, 1),
  (2764872, 2, 0),
  (2782950, 2, 0),
  (2785662, 0, 1),
  (2793392, 0, 1),
  (2795093, 2, 2),
  (2800801, 0, 2),
  (2803594, 1, 2),
  (2806394, 1, 1),
  (2813039, 2, 0),
  (2814970, 0, 2),
  (2817046, 3, 1),
  (2819326, 2, 2),
  (2819709, 1, 1),
  (2831737, 2, 0),
  (2832338, 0, 1),
  (2832674, 1, 1),
  (2836602, 1, 1),
  (2839677, 0, 2),
  (2851537, 2, 0),
  (2855831, 3, 1),
  (2857864, 1, 1),
  (2862648, 0, 2),
  (2868782, 3, 0),
  (2871707, 2, 1),
  (2882231, 1, 0),
  (2898621, 0, 1),
  (2902454, 2, 1),
  (2903229, 1, 2),
  (2904245, 3, 1),
  (2909969, 3, 1),
  (2911736, 1, 0),
  (2912012, 1, 0),
  (2913060, 3, 2),
  (2920443, 0, 1),
  (2921858, 2, 2),
  (2922654, 0, 2),
  (2928476, 2, 0),
  (2929446, 2, 1),
  (2935112, 2, 2),
  (2938608, 0, 1),
  (2955688, 3, 2),
  (2965195, 3, 0),
  (2986672, 1, 2),
  (3000415, 0, 0),
  (3004557, 0, 1),
  (3014213, 2, 2),
  (3020556, 0, 0),
  (3026704, 0, 1),
  (3026819, 2, 1),
  (3030358, 1, 2),
  (3056195, 3, 2),
  (3057306, 2, 1),
  (3060303, 2, 0),
  (3072962, 2, 1),
  (3077682, 3, 1),
  (3081731, 0, 2),
  (3084478, 2, 1),
  (3096820, 3, 1),
  (3103337, 2, 2),
  (3112149, 3, 2),
  (3112949, 3, 1),
  (3123327, 0, 2),
  (3124242, 0, 1),
  (3133131, 0, 1),
  (3145662, 2, 1),
  (3148976, 0, 1),
  (3149312, 0, 2),
  (3161434, 0, 0),
  (3162859, 2, 2),
  (3170877, 0, 2),
  (3179598, 3, 0),
  (3189533, 2, 1),
  (3193852, 3, 2),
  (3194471, 0, 0),
  (3194549, 3, 0),
  (3200495, 0, 0),
  (3202417, 3, 0),
  (3213631, 1, 2),
  (3217569, 2, 0),
  (3217727, 2, 2),
  (3223265, 0, 1),
  (3225907, 3, 2),
  (3227744, 0, 2),
  (3235616, 2, 1),
  (3240973, 0, 0),
  (3241536, 3, 1),
  (3253558, 2, 0),
  (3270549, 1, 2),
  (3285993, 1, 2),
  (3291853, 3, 2),
  (3292755, 0, 1),
  (3293016, 2, 1),
  (3294063, 2, 0),
  (3299929, 0, 0),
  (3316208, 2, 1),
  (3316975, 0, 2),
  (3328623, 2, 1),
  (3328923, 1, 2),
  (3339577, 0, 1),
  (3340008, 1, 0),
  (3340769, 2, 1),
  (3341056, 3, 2),
  (3341849, 0, 0),
  (3342884, 2, 2),
  (3363799, 3, 1),
  (3374791, 2, 1),
  (3388907, 0, 1),
  (3389128, 0, 0),
  (3405698, 2, 1),
  (3406465, 2, 2),
  (3409695, 0, 0),
  (3412374, 2, 0),
  (3413023, 3, 1),
  (3428902, 2, 1),
  (3432114, 0, 1),
  (3440866, 1, 2),
  (3451918, 3, 0),
  (3471838, 3, 0),
  (3475617, 2, 1),
  (3476888, 0, 0),
  (3477615, 1, 2),
  (3482676, 2, 0),
  (3486515, 3, 1),
  (3490333, 2, 2),
  (3496331, 2, 0),
  (3499697, 1, 2),
  (3501791, 3, 2),
  (3502087, 1, 2),
  (3516271, 2, 2),
  (3523843, 2, 1),
  (3530687, 3, 0),
  (3532071, 1, 2),
  (3533586, 0, 2),
  (3547022, 3, 2),
  (3558402, 1, 0),
  (3574933, 3, 0),
  (3581909, 1, 1),
  (3584750, 1, 2),
  (3593971, 0, 2),
  (3594097, 1, 2),
])
