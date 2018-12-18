from src.util import *
schedule = deque([
  (3220, 2, 1),
  (11519, 1, 2),
  (18478, 0, 1),
  (31473, 1, 0),
  (36980, 1, 0),
  (40527, 0, 2),
  (49994, 0, 1),
  (56953, 1, 2),
  (61423, 2, 2),
  (61942, 2, 2),
  (63439, 2, 2),
  (75810, 0, 0),
  (75897, 3, 2),
  (82418, 3, 1),
  (86368, 2, 2),
  (88673, 3, 1),
  (92204, 2, 2),
  (95145, 2, 2),
  (99961, 1, 0),
  (104231, 2, 1),
  (112109, 3, 0),
  (112397, 0, 1),
  (116403, 3, 1),
  (120451, 0, 0),
  (128594, 0, 2),
  (136766, 3, 2),
  (137211, 3, 1),
  (151389, 1, 0),
  (151694, 2, 0),
  (152389, 2, 2),
  (153781, 1, 0),
  (157672, 0, 2),
  (162033, 3, 2),
  (163740, 3, 1),
  (167378, 1, 2),
  (176352, 2, 0),
  (191903, 1, 2),
  (195715, 0, 1),
  (207878, 0, 0),
  (211635, 1, 1),
  (217199, 2, 0),
  (219407, 2, 2),
  (226110, 3, 2),
  (230898, 2, 2),
  (239859, 3, 1),
  (249802, 1, 0),
  (250577, 0, 2),
  (252355, 3, 1),
  (252591, 2, 0),
  (256086, 0, 2),
  (269377, 0, 2),
  (270594, 2, 2),
  (277366, 3, 0),
  (281186, 3, 0),
  (289885, 2, 1),
  (295822, 0, 2),
  (299522, 3, 1),
  (299855, 0, 0),
  (310131, 0, 1),
  (318808, 1, 0),
  (324932, 1, 1),
  (328347, 2, 1),
  (330389, 1, 0),
  (332734, 1, 0),
  (347672, 3, 1),
  (350161, 0, 1),
  (351440, 0, 2),
  (353094, 0, 0),
  (355710, 2, 0),
  (362385, 2, 2),
  (364141, 3, 2),
  (374457, 1, 1),
  (388686, 2, 0),
  (400416, 2, 0),
  (400658, 2, 0),
  (407077, 0, 1),
  (410717, 2, 2),
  (412885, 0, 2),
  (413968, 0, 1),
  (416975, 1, 1),
  (422548, 3, 1),
  (432900, 2, 1),
  (437733, 3, 1),
  (439978, 0, 2),
  (454193, 1, 2),
  (455784, 2, 0),
  (460931, 3, 2),
  (472660, 3, 2),
  (472699, 1, 0),
  (474945, 3, 1),
  (478226, 3, 1),
  (482203, 0, 0),
  (484855, 3, 2),
  (487190, 3, 0),
  (490214, 0, 2),
  (492804, 2, 1),
  (504190, 3, 2),
  (505793, 2, 1),
  (506096, 3, 2),
  (517410, 3, 0),
  (520232, 2, 0),
  (523411, 1, 2),
  (527869, 1, 0),
  (532159, 1, 1),
  (544381, 0, 2),
  (551790, 0, 1),
  (553462, 1, 1),
  (568743, 3, 1),
  (573375, 0, 2),
  (578199, 3, 2),
  (594687, 0, 2),
  (600553, 1, 2),
  (606592, 3, 1),
  (608367, 3, 0),
  (609421, 3, 0),
  (614503, 0, 0),
  (620209, 0, 0),
  (638032, 3, 2),
  (645771, 2, 2),
  (658591, 0, 1),
  (662199, 0, 0),
  (664017, 3, 1),
  (668899, 3, 0),
  (669613, 2, 0),
  (679560, 2, 0),
  (681079, 0, 1),
  (683283, 1, 1),
  (684080, 1, 2),
  (685991, 1, 2),
  (692252, 2, 1),
  (712866, 1, 0),
  (714283, 3, 1),
  (727563, 2, 2),
  (734248, 3, 2),
  (735906, 2, 0),
  (736099, 2, 0),
  (762698, 1, 2),
  (780107, 1, 2),
  (782333, 2, 0),
  (783647, 0, 0),
  (785279, 0, 2),
  (795375, 3, 2),
  (805831, 1, 1),
  (822447, 1, 1),
  (862479, 3, 2),
  (862673, 2, 1),
  (862697, 3, 0),
  (867416, 2, 2),
  (869580, 3, 0),
  (882824, 2, 2),
  (889515, 3, 1),
  (903834, 0, 2),
  (908315, 1, 0),
  (908673, 1, 0),
  (909229, 0, 2),
  (914551, 0, 2),
  (920560, 2, 2),
  (925702, 3, 2),
  (929796, 3, 0),
  (942920, 3, 1),
  (955745, 3, 1),
  (956523, 3, 2),
  (958891, 0, 0),
  (959460, 1, 2),
  (962226, 1, 2),
  (962670, 1, 2),
  (963065, 1, 1),
  (964994, 2, 1),
  (983479, 3, 2),
  (985562, 0, 2),
  (994808, 0, 2),
  (997170, 1, 1),
  (1000678, 3, 0),
  (1006437, 0, 2),
  (1014931, 2, 1),
  (1019467, 1, 2),
  (1026050, 0, 2),
  (1028253, 2, 2),
  (1036732, 3, 2),
  (1038971, 3, 0),
  (1044310, 1, 0),
  (1047134, 3, 1),
  (1048336, 2, 1),
  (1049916, 0, 2),
  (1053865, 3, 1),
  (1057744, 2, 1),
  (1057977, 0, 2),
  (1074546, 3, 2),
  (1075858, 3, 1),
  (1076209, 3, 1),
  (1088182, 1, 0),
  (1088587, 2, 1),
  (1103385, 0, 0),
  (1104051, 1, 2),
  (1110075, 1, 2),
  (1111902, 2, 2),
  (1116253, 3, 0),
  (1118571, 0, 0),
  (1124870, 0, 2),
  (1126261, 1, 2),
  (1134476, 0, 2),
  (1142246, 1, 1),
  (1151943, 1, 0),
  (1156086, 1, 1),
  (1158909, 0, 2),
  (1163895, 2, 1),
  (1164188, 3, 1),
  (1170424, 3, 1),
  (1190774, 2, 2),
  (1192140, 2, 0),
  (1205026, 3, 0),
  (1207050, 3, 2),
  (1212534, 2, 0),
  (1219885, 0, 2),
  (1223622, 3, 2),
  (1224534, 1, 2),
  (1232982, 2, 2),
  (1242329, 1, 1),
  (1248083, 3, 2),
  (1263288, 1, 2),
  (1271821, 2, 1),
  (1276778, 3, 2),
  (1278734, 3, 1),
  (1280316, 2, 0),
  (1298761, 3, 1),
  (1299364, 2, 1),
  (1311167, 0, 2),
  (1312998, 1, 1),
  (1347580, 3, 2),
  (1347631, 2, 1),
  (1373032, 3, 0),
  (1387645, 0, 2),
  (1391993, 1, 0),
  (1399799, 3, 0),
  (1412102, 0, 2),
  (1414565, 0, 2),
  (1432572, 2, 0),
  (1434492, 0, 0),
  (1442144, 0, 2),
  (1448615, 1, 0),
  (1464530, 0, 0),
  (1473414, 2, 0),
  (1493627, 2, 0),
  (1499894, 3, 0),
  (1513940, 0, 0),
  (1519816, 0, 0),
  (1530245, 3, 0),
  (1530652, 3, 1),
  (1537474, 2, 1),
  (1539906, 0, 1),
  (1554622, 2, 2),
  (1575645, 2, 1),
  (1588053, 2, 2),
  (1588843, 3, 1),
  (1591687, 3, 2),
  (1593999, 2, 0),
  (1595163, 1, 1),
  (1599725, 0, 2),
  (1601401, 1, 0),
  (1606038, 2, 2),
  (1606861, 1, 0),
  (1609226, 2, 2),
  (1619005, 0, 2),
  (1630125, 0, 1),
  (1638140, 2, 0),
  (1644299, 0, 1),
  (1645573, 3, 0),
  (1646092, 3, 1),
  (1648649, 0, 2),
  (1659027, 1, 0),
  (1659194, 3, 1),
  (1663219, 0, 1),
  (1670209, 3, 1),
  (1679172, 0, 2),
  (1681625, 0, 1),
  (1695723, 1, 1),
  (1698812, 0, 0),
  (1705810, 1, 1),
  (1715238, 1, 2),
  (1718235, 0, 2),
  (1724366, 3, 0),
  (1728900, 2, 2),
  (1728979, 2, 1),
  (1740370, 2, 1),
  (1740880, 3, 1),
  (1741950, 0, 2),
  (1743766, 3, 1),
  (1750695, 1, 2),
  (1754557, 3, 2),
  (1756188, 2, 0),
  (1758469, 3, 2),
  (1762190, 0, 0),
  (1763051, 0, 0),
  (1767908, 0, 0),
  (1770166, 1, 1),
  (1782473, 0, 0),
  (1784224, 3, 1),
  (1795459, 2, 1),
  (1804147, 0, 0),
  (1815578, 0, 0),
  (1815655, 2, 2),
  (1816377, 0, 0),
  (1822858, 2, 0),
  (1824757, 3, 2),
  (1825406, 3, 0),
  (1826826, 2, 0),
  (1830608, 3, 2),
  (1832105, 2, 2),
  (1835092, 3, 1),
  (1835982, 0, 0),
  (1847207, 1, 2),
  (1852240, 1, 1),
  (1854093, 1, 0),
  (1859017, 1, 0),
  (1867899, 1, 0),
  (1877304, 2, 2),
  (1879439, 0, 2),
  (1885837, 2, 0),
  (1887892, 2, 1),
  (1888268, 1, 1),
  (1899513, 2, 2),
  (1917082, 2, 2),
  (1918839, 0, 1),
  (1920687, 1, 1),
  (1920831, 0, 2),
  (1922003, 0, 1),
  (1929620, 3, 0),
  (1933358, 0, 1),
  (1941130, 2, 1),
  (1943620, 2, 2),
  (1950201, 1, 0),
  (1953057, 2, 1),
  (1967804, 2, 0),
  (1974180, 0, 0),
  (1976762, 3, 1),
  (1978517, 1, 1),
  (1984934, 2, 1),
  (1989408, 3, 1),
  (1990765, 3, 0),
  (2000330, 2, 0),
  (2004665, 1, 1),
  (2012992, 2, 0),
  (2023761, 3, 0),
  (2027024, 0, 0),
  (2038335, 2, 0),
  (2041995, 1, 0),
  (2042450, 3, 1),
  (2048764, 2, 2),
  (2059718, 2, 2),
  (2060622, 1, 0),
  (2062906, 1, 0),
  (2068682, 0, 1),
  (2084596, 3, 2),
  (2090088, 0, 2),
  (2105636, 0, 0),
  (2114965, 3, 2),
  (2120159, 2, 1),
  (2123777, 3, 2),
  (2135963, 1, 2),
  (2141542, 2, 0),
  (2143240, 0, 2),
  (2152584, 1, 2),
  (2156762, 3, 2),
  (2160158, 1, 2),
  (2166024, 2, 0),
  (2168365, 1, 0),
  (2182324, 2, 1),
  (2194747, 1, 0),
  (2213151, 2, 2),
  (2217642, 2, 1),
  (2218728, 3, 2),
  (2220798, 3, 1),
  (2226335, 2, 2),
  (2233372, 3, 1),
  (2239536, 3, 1),
  (2242933, 0, 2),
  (2249193, 1, 0),
  (2249505, 3, 2),
  (2257994, 3, 2),
  (2261560, 2, 1),
  (2261854, 2, 2),
  (2268620, 1, 0),
  (2269671, 0, 1),
  (2289826, 3, 2),
  (2291652, 2, 2),
  (2298014, 2, 1),
  (2300186, 2, 1),
  (2306639, 3, 1),
  (2311378, 2, 0),
  (2312251, 1, 1),
  (2322387, 2, 1),
  (2322887, 2, 1),
  (2324110, 2, 2),
  (2333809, 1, 0),
  (2334056, 0, 0),
  (2339020, 1, 2),
  (2347044, 2, 1),
  (2349859, 0, 0),
  (2350791, 2, 2),
  (2354186, 1, 2),
  (2365048, 3, 0),
  (2381766, 1, 0),
  (2386614, 0, 2),
  (2387096, 1, 2),
  (2390106, 1, 0),
  (2400139, 3, 1),
  (2400819, 0, 1),
  (2408185, 2, 1),
  (2411352, 2, 1),
  (2412007, 1, 2),
  (2414085, 0, 2),
  (2417574, 0, 0),
  (2432287, 2, 2),
  (2435104, 1, 1),
  (2443110, 0, 2),
  (2443186, 1, 0),
  (2450154, 2, 2),
  (2465689, 0, 2),
  (2470984, 2, 1),
  (2475643, 1, 0),
  (2476433, 0, 1),
  (2486902, 2, 2),
  (2493551, 2, 1),
  (2505232, 2, 2),
  (2512641, 2, 0),
  (2519471, 0, 0),
  (2521182, 0, 0),
  (2527452, 2, 1),
  (2538190, 0, 1),
  (2541703, 3, 2),
  (2545753, 3, 2),
  (2546437, 3, 1),
  (2562965, 1, 0),
  (2579083, 3, 2),
  (2602197, 2, 1),
  (2602450, 2, 1),
  (2605970, 1, 0),
  (2618358, 1, 1),
  (2623579, 3, 0),
  (2638878, 0, 1),
  (2652903, 3, 2),
  (2655917, 0, 1),
  (2665573, 0, 2),
  (2667011, 3, 0),
  (2673894, 3, 2),
  (2677771, 0, 1),
  (2679137, 1, 1),
  (2681232, 2, 1),
  (2687355, 3, 0),
  (2689478, 0, 0),
  (2702319, 2, 2),
  (2705725, 3, 1),
  (2709002, 3, 1),
  (2709875, 3, 0),
  (2720862, 0, 0),
  (2725946, 2, 2),
  (2736450, 2, 0),
  (2736860, 1, 1),
  (2752681, 0, 0),
  (2755551, 3, 1),
  (2756102, 3, 2),
  (2757316, 1, 1),
  (2761027, 2, 1),
  (2761262, 3, 1),
  (2768220, 2, 0),
  (2771978, 1, 0),
  (2775509, 2, 2),
  (2777076, 3, 1),
  (2796878, 3, 2),
  (2797501, 0, 1),
  (2800140, 2, 1),
  (2804252, 1, 2),
  (2806137, 0, 0),
  (2806443, 3, 0),
  (2820569, 2, 0),
  (2826755, 2, 1),
  (2844941, 0, 1),
  (2846706, 0, 0),
  (2852090, 0, 2),
  (2859411, 0, 2),
  (2862495, 2, 0),
  (2864503, 1, 2),
  (2878088, 1, 1),
  (2889388, 1, 1),
  (2901807, 3, 2),
  (2906008, 0, 0),
  (2910096, 2, 2),
  (2912879, 0, 2),
  (2913111, 0, 1),
  (2915314, 1, 0),
  (2927565, 2, 2),
  (2938842, 1, 2),
  (2946951, 1, 0),
  (2947046, 2, 0),
  (2951702, 1, 2),
  (2954788, 3, 2),
  (2955748, 0, 1),
  (2958931, 2, 2),
  (2960070, 1, 0),
  (2962596, 1, 1),
  (2964386, 3, 2),
  (2978730, 0, 2),
  (2979582, 3, 2),
  (2984050, 2, 0),
  (2988840, 3, 1),
  (2996045, 2, 0),
  (3004503, 1, 1),
  (3005218, 2, 1),
  (3005568, 0, 1),
  (3013064, 2, 2),
  (3013251, 0, 2),
  (3017242, 3, 1),
  (3030314, 3, 0),
  (3036455, 3, 2),
  (3043305, 0, 2),
  (3049231, 1, 2),
  (3060503, 3, 0),
  (3063775, 1, 0),
  (3073788, 2, 1),
  (3083147, 0, 1),
  (3093706, 2, 0),
  (3100869, 3, 2),
  (3101911, 1, 2),
  (3136452, 3, 2),
  (3141747, 2, 2),
  (3159362, 1, 0),
  (3161734, 0, 1),
  (3167355, 2, 2),
  (3170201, 1, 1),
  (3174512, 2, 2),
  (3176502, 3, 0),
  (3177864, 3, 2),
  (3185835, 2, 0),
  (3187582, 2, 2),
  (3189905, 0, 1),
  (3196449, 2, 2),
  (3211774, 3, 2),
  (3219645, 3, 2),
  (3225681, 3, 1),
  (3233037, 3, 2),
  (3234222, 1, 2),
  (3249649, 2, 1),
  (3252245, 0, 0),
  (3255853, 1, 2),
  (3270622, 1, 1),
  (3275059, 3, 1),
  (3285114, 3, 2),
  (3290642, 0, 2),
  (3291884, 2, 2),
  (3301066, 0, 0),
  (3311196, 1, 2),
  (3312410, 2, 0),
  (3315507, 1, 1),
  (3328972, 2, 2),
  (3338468, 0, 1),
  (3345970, 2, 1),
  (3347394, 1, 0),
  (3350086, 0, 2),
  (3355105, 1, 2),
  (3364233, 1, 0),
  (3371692, 1, 1),
  (3381073, 0, 2),
  (3387374, 0, 0),
  (3389091, 3, 0),
  (3392149, 2, 2),
  (3393808, 3, 0),
  (3400281, 0, 0),
  (3407249, 1, 1),
  (3407746, 0, 0),
  (3417128, 0, 1),
  (3424156, 1, 2),
  (3437528, 3, 1),
  (3439808, 1, 2),
  (3442301, 0, 2),
  (3444614, 3, 2),
  (3467683, 3, 0),
  (3469663, 0, 0),
  (3479274, 3, 0),
  (3479585, 1, 1),
  (3486720, 0, 2),
  (3494350, 0, 1),
  (3498601, 1, 0),
  (3499852, 3, 0),
  (3504959, 3, 0),
  (3505149, 0, 0),
  (3512454, 2, 2),
  (3515859, 0, 2),
  (3517401, 1, 2),
  (3531846, 2, 0),
  (3534774, 0, 2),
  (3536231, 1, 0),
  (3541264, 0, 2),
  (3548149, 2, 2),
  (3550658, 1, 1),
  (3563134, 3, 1),
  (3565749, 0, 2),
  (3577320, 1, 1),
  (3584074, 2, 1),
  (3590027, 0, 1),
  (3599623, 2, 2),
])
