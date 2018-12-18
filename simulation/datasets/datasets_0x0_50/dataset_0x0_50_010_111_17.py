from src.util import *
schedule = deque([
  (1628, 1, 2),
  (14744, 0, 2),
  (28769, 3, 1),
  (36065, 2, 0),
  (54431, 0, 1),
  (66684, 1, 1),
  (69051, 1, 0),
  (72630, 1, 2),
  (73355, 1, 1),
  (81841, 3, 2),
  (85937, 0, 1),
  (92171, 3, 2),
  (93384, 2, 1),
  (101699, 2, 1),
  (107910, 2, 0),
  (112237, 0, 1),
  (115096, 2, 1),
  (119676, 3, 0),
  (124560, 0, 1),
  (126199, 3, 0),
  (131621, 2, 1),
  (140160, 2, 0),
  (141641, 1, 1),
  (159333, 1, 0),
  (168013, 0, 0),
  (175603, 2, 2),
  (176457, 1, 2),
  (180746, 0, 2),
  (185499, 3, 2),
  (213546, 3, 1),
  (218610, 3, 2),
  (219568, 2, 1),
  (226337, 1, 2),
  (230857, 2, 2),
  (232432, 3, 1),
  (236968, 3, 1),
  (241704, 0, 0),
  (244926, 0, 1),
  (251519, 1, 2),
  (260518, 0, 2),
  (265247, 2, 2),
  (267347, 0, 2),
  (274758, 1, 2),
  (278585, 2, 1),
  (280234, 1, 0),
  (282968, 0, 0),
  (300456, 2, 1),
  (314474, 1, 1),
  (315503, 1, 0),
  (318725, 3, 2),
  (322690, 2, 0),
  (328805, 2, 1),
  (333680, 0, 1),
  (345361, 0, 2),
  (347862, 0, 0),
  (350330, 2, 1),
  (356733, 3, 1),
  (357649, 0, 0),
  (361679, 1, 1),
  (362034, 2, 2),
  (377887, 1, 2),
  (378290, 1, 0),
  (382895, 2, 1),
  (388705, 0, 2),
  (393561, 0, 0),
  (397057, 3, 2),
  (406795, 1, 1),
  (410961, 0, 1),
  (412651, 0, 2),
  (420312, 1, 0),
  (429610, 3, 2),
  (438282, 2, 0),
  (461203, 3, 0),
  (464530, 0, 0),
  (469526, 2, 0),
  (472062, 1, 2),
  (474513, 1, 2),
  (477316, 1, 2),
  (483943, 3, 2),
  (484995, 0, 2),
  (487044, 0, 1),
  (500397, 0, 1),
  (502398, 3, 0),
  (519961, 3, 2),
  (520861, 0, 1),
  (536435, 3, 2),
  (546306, 3, 2),
  (547681, 0, 0),
  (552867, 2, 2),
  (554586, 0, 0),
  (572398, 2, 0),
  (572885, 1, 1),
  (582776, 0, 1),
  (586581, 3, 0),
  (592055, 1, 0),
  (597675, 0, 1),
  (603280, 3, 2),
  (603744, 0, 0),
  (608468, 3, 1),
  (609776, 3, 2),
  (613171, 3, 0),
  (613307, 1, 0),
  (636847, 3, 1),
  (647268, 2, 0),
  (649088, 0, 0),
  (650441, 1, 1),
  (654653, 0, 1),
  (655585, 0, 2),
  (656013, 0, 2),
  (656713, 3, 0),
  (656817, 0, 0),
  (659923, 3, 2),
  (670434, 3, 2),
  (672057, 1, 2),
  (683813, 2, 1),
  (686033, 2, 2),
  (687238, 0, 1),
  (693033, 3, 0),
  (704692, 0, 2),
  (718740, 2, 0),
  (721899, 1, 2),
  (727295, 1, 1),
  (728040, 2, 2),
  (743022, 1, 2),
  (744375, 3, 2),
  (747454, 0, 2),
  (752416, 2, 0),
  (758646, 1, 0),
  (763279, 2, 0),
  (764691, 0, 2),
  (772410, 3, 0),
  (772622, 1, 2),
  (775518, 2, 0),
  (781510, 2, 2),
  (781649, 0, 1),
  (784703, 1, 0),
  (790181, 2, 1),
  (790272, 1, 1),
  (796019, 2, 1),
  (797344, 0, 0),
  (808498, 2, 1),
  (814424, 3, 2),
  (826260, 1, 0),
  (839408, 3, 0),
  (845519, 1, 0),
  (854929, 3, 1),
  (859169, 2, 0),
  (871759, 1, 1),
  (874653, 0, 2),
  (893907, 2, 0),
  (894500, 0, 1),
  (894740, 2, 1),
  (914675, 0, 1),
  (922173, 3, 0),
  (926530, 1, 2),
  (927340, 3, 2),
  (935540, 0, 0),
  (941732, 0, 1),
  (944169, 2, 2),
  (958013, 1, 0),
  (960898, 2, 2),
  (960942, 1, 0),
  (972324, 1, 2),
  (983923, 3, 0),
  (989063, 2, 2),
  (997713, 0, 2),
  (999624, 1, 1),
  (1006419, 3, 2),
  (1017722, 1, 1),
  (1020920, 0, 1),
  (1021837, 0, 1),
  (1025095, 0, 2),
  (1026846, 2, 2),
  (1036045, 3, 1),
  (1041362, 2, 1),
  (1066203, 2, 0),
  (1066263, 2, 2),
  (1069351, 3, 1),
  (1070856, 1, 1),
  (1088276, 0, 0),
  (1098617, 0, 0),
  (1098829, 1, 0),
  (1109699, 1, 1),
  (1128096, 0, 0),
  (1133562, 3, 0),
  (1137343, 3, 2),
  (1143840, 0, 0),
  (1144421, 1, 1),
  (1151646, 0, 2),
  (1155425, 2, 1),
  (1174859, 3, 1),
  (1195042, 1, 0),
  (1203536, 1, 2),
  (1204742, 2, 1),
  (1204891, 1, 2),
  (1210385, 0, 0),
  (1211305, 1, 1),
  (1236036, 0, 0),
  (1238077, 3, 1),
  (1243434, 1, 0),
  (1247019, 1, 2),
  (1253074, 3, 1),
  (1254417, 3, 0),
  (1256670, 2, 1),
  (1264190, 1, 0),
  (1265777, 1, 2),
  (1267037, 2, 0),
  (1267371, 0, 1),
  (1268110, 0, 0),
  (1276686, 3, 1),
  (1281323, 1, 2),
  (1282416, 2, 1),
  (1285489, 0, 1),
  (1293835, 0, 2),
  (1305375, 0, 2),
  (1306327, 2, 2),
  (1311113, 2, 1),
  (1313968, 1, 2),
  (1317943, 0, 2),
  (1319247, 1, 0),
  (1330899, 0, 0),
  (1331736, 1, 0),
  (1332134, 2, 0),
  (1332829, 1, 2),
  (1343012, 0, 0),
  (1349301, 2, 0),
  (1367781, 2, 0),
  (1367835, 1, 1),
  (1376861, 3, 1),
  (1378719, 3, 2),
  (1386032, 0, 0),
  (1397904, 0, 1),
  (1398688, 2, 0),
  (1409659, 2, 1),
  (1415870, 3, 2),
  (1418758, 3, 1),
  (1427046, 2, 0),
  (1433733, 2, 1),
  (1434560, 1, 0),
  (1436228, 2, 2),
  (1441370, 3, 2),
  (1444389, 1, 1),
  (1453473, 2, 1),
  (1455105, 0, 0),
  (1465973, 1, 0),
  (1468219, 1, 1),
  (1472629, 0, 2),
  (1472982, 1, 2),
  (1475428, 3, 2),
  (1475631, 1, 1),
  (1482171, 2, 2),
  (1485834, 0, 0),
  (1488762, 3, 1),
  (1489374, 3, 1),
  (1509912, 3, 2),
  (1510006, 2, 0),
  (1530235, 0, 2),
  (1530432, 2, 1),
  (1538230, 0, 2),
  (1548485, 3, 1),
  (1550311, 0, 1),
  (1558014, 1, 0),
  (1559904, 3, 2),
  (1563502, 2, 0),
  (1586408, 1, 0),
  (1586833, 2, 0),
  (1588466, 3, 2),
  (1619069, 0, 2),
  (1620295, 3, 1),
  (1622419, 0, 0),
  (1623721, 3, 1),
  (1634719, 0, 2),
  (1643736, 3, 1),
  (1648090, 0, 0),
  (1651861, 3, 2),
  (1659487, 2, 2),
  (1665568, 3, 0),
  (1675466, 1, 0),
  (1679099, 2, 0),
  (1682067, 1, 1),
  (1709009, 3, 2),
  (1710760, 0, 2),
  (1713550, 3, 0),
  (1721345, 1, 1),
  (1722382, 0, 1),
  (1723952, 1, 0),
  (1724343, 3, 1),
  (1726515, 3, 2),
  (1735540, 2, 2),
  (1737287, 2, 2),
  (1737992, 3, 1),
  (1743087, 3, 1),
  (1747829, 0, 2),
  (1748049, 1, 1),
  (1753622, 1, 2),
  (1757598, 3, 1),
  (1759859, 3, 1),
  (1760697, 1, 0),
  (1764687, 1, 2),
  (1779707, 0, 1),
  (1781192, 3, 1),
  (1783296, 2, 0),
  (1785050, 3, 0),
  (1787900, 3, 1),
  (1790220, 2, 1),
  (1791342, 0, 1),
  (1797410, 2, 1),
  (1810553, 2, 1),
  (1813318, 0, 0),
  (1817789, 2, 1),
  (1817997, 2, 1),
  (1834738, 3, 1),
  (1838886, 0, 1),
  (1857586, 2, 0),
  (1864620, 2, 1),
  (1883581, 2, 2),
  (1883946, 2, 1),
  (1888835, 1, 2),
  (1900926, 0, 0),
  (1901445, 1, 1),
  (1905522, 3, 1),
  (1914102, 3, 0),
  (1925901, 3, 0),
  (1928658, 0, 2),
  (1939969, 3, 2),
  (1941444, 2, 2),
  (1946210, 2, 0),
  (1963873, 2, 1),
  (1965783, 3, 2),
  (1971452, 1, 1),
  (1980686, 3, 0),
  (1983362, 1, 0),
  (1985575, 1, 1),
  (1988422, 3, 1),
  (1991140, 1, 1),
  (1995012, 3, 0),
  (2018022, 0, 0),
  (2021192, 2, 0),
  (2021753, 0, 2),
  (2023293, 1, 0),
  (2027086, 3, 2),
  (2030624, 2, 0),
  (2032714, 0, 0),
  (2037135, 3, 1),
  (2086603, 0, 2),
  (2087709, 0, 1),
  (2091923, 2, 1),
  (2100497, 3, 2),
  (2104068, 2, 2),
  (2111402, 0, 2),
  (2118965, 0, 1),
  (2123046, 1, 0),
  (2123915, 0, 1),
  (2133794, 1, 1),
  (2134170, 1, 2),
  (2137910, 3, 2),
  (2139900, 1, 0),
  (2145755, 0, 1),
  (2157832, 3, 0),
  (2157933, 1, 1),
  (2179519, 0, 1),
  (2190662, 1, 0),
  (2201290, 3, 2),
  (2201984, 2, 1),
  (2204479, 3, 0),
  (2209641, 3, 0),
  (2215244, 2, 2),
  (2216894, 2, 2),
  (2219190, 1, 2),
  (2246831, 1, 0),
  (2252400, 1, 1),
  (2257044, 2, 1),
  (2257613, 3, 1),
  (2283531, 2, 1),
  (2284412, 3, 2),
  (2287717, 1, 0),
  (2288441, 3, 1),
  (2289515, 0, 0),
  (2295286, 3, 2),
  (2295990, 0, 1),
  (2305346, 1, 0),
  (2312656, 0, 2),
  (2314175, 0, 0),
  (2318088, 2, 0),
  (2324223, 1, 0),
  (2328091, 2, 2),
  (2333171, 3, 1),
  (2338153, 0, 2),
  (2348038, 3, 2),
  (2359757, 3, 2),
  (2360707, 3, 2),
  (2364891, 2, 1),
  (2374181, 0, 0),
  (2382244, 3, 2),
  (2388474, 1, 1),
  (2393003, 1, 2),
  (2403306, 3, 1),
  (2413449, 2, 1),
  (2414280, 0, 1),
  (2425642, 0, 2),
  (2427088, 1, 0),
  (2455935, 0, 2),
  (2456936, 0, 1),
  (2461859, 0, 1),
  (2463944, 2, 2),
  (2471934, 1, 1),
  (2478325, 1, 0),
  (2479182, 3, 2),
  (2482650, 3, 2),
  (2483084, 2, 0),
  (2495794, 0, 2),
  (2500902, 2, 2),
  (2508094, 3, 0),
  (2512265, 3, 1),
  (2524929, 1, 0),
  (2527654, 1, 1),
  (2529839, 2, 0),
  (2539749, 2, 0),
  (2539952, 2, 0),
  (2541232, 0, 2),
  (2543517, 0, 0),
  (2545201, 2, 1),
  (2563378, 3, 2),
  (2579178, 2, 2),
  (2582645, 3, 1),
  (2584818, 3, 2),
  (2591948, 2, 1),
  (2595016, 1, 1),
  (2600813, 2, 2),
  (2614369, 1, 0),
  (2615418, 0, 1),
  (2628828, 3, 2),
  (2643379, 0, 1),
  (2645592, 1, 1),
  (2647047, 2, 2),
  (2655100, 0, 0),
  (2666173, 2, 0),
  (2680774, 2, 1),
  (2687770, 2, 1),
  (2695319, 0, 0),
  (2698748, 3, 0),
  (2700710, 0, 2),
  (2707580, 1, 2),
  (2710676, 1, 1),
  (2725482, 2, 2),
  (2728997, 0, 0),
  (2744892, 2, 1),
  (2747791, 0, 1),
  (2748046, 0, 2),
  (2751886, 2, 0),
  (2754126, 3, 2),
  (2757419, 1, 1),
  (2771947, 1, 2),
  (2773744, 0, 0),
  (2781607, 3, 2),
  (2787407, 3, 2),
  (2788012, 3, 0),
  (2793087, 3, 0),
  (2793862, 2, 1),
  (2798490, 3, 2),
  (2800013, 3, 2),
  (2823895, 2, 1),
  (2824968, 1, 2),
  (2825322, 2, 1),
  (2826796, 2, 2),
  (2834343, 2, 0),
  (2835646, 0, 0),
  (2837109, 1, 2),
  (2837490, 1, 2),
  (2840140, 1, 0),
  (2854182, 3, 1),
  (2855587, 2, 0),
  (2876064, 0, 0),
  (2876854, 1, 1),
  (2907371, 2, 1),
  (2907813, 2, 1),
  (2910876, 3, 2),
  (2917328, 0, 0),
  (2919677, 2, 2),
  (2920325, 0, 0),
  (2924180, 3, 0),
  (2928080, 3, 1),
  (2929648, 0, 0),
  (2944043, 0, 0),
  (2945292, 1, 2),
  (2948382, 1, 2),
  (2949895, 2, 0),
  (2951620, 2, 1),
  (2955704, 1, 2),
  (2961172, 2, 0),
  (2977759, 2, 1),
  (2978436, 3, 0),
  (2988357, 1, 2),
  (2988624, 0, 1),
  (2990697, 3, 0),
  (2991661, 1, 0),
  (3012647, 3, 2),
  (3018136, 2, 1),
  (3023619, 0, 0),
  (3029138, 0, 0),
  (3035069, 1, 2),
  (3036105, 1, 1),
  (3037309, 3, 1),
  (3044875, 1, 2),
  (3051537, 1, 2),
  (3053082, 1, 0),
  (3062874, 2, 1),
  (3064400, 3, 1),
  (3068715, 2, 1),
  (3080533, 1, 1),
  (3096942, 0, 0),
  (3099657, 1, 0),
  (3117312, 1, 0),
  (3117702, 3, 1),
  (3121368, 2, 1),
  (3122610, 3, 0),
  (3129788, 1, 0),
  (3134833, 1, 1),
  (3137410, 0, 1),
  (3137431, 0, 1),
  (3137664, 3, 1),
  (3144087, 1, 0),
  (3150202, 1, 1),
  (3154099, 3, 0),
  (3159940, 3, 0),
  (3169908, 1, 2),
  (3174790, 2, 2),
  (3186820, 2, 2),
  (3192237, 0, 0),
  (3198622, 3, 0),
  (3219769, 1, 2),
  (3224947, 2, 2),
  (3226166, 0, 2),
  (3255916, 2, 1),
  (3264209, 1, 1),
  (3265863, 1, 0),
  (3285556, 3, 1),
  (3286312, 1, 2),
  (3294372, 2, 1),
  (3297023, 2, 1),
  (3307362, 3, 1),
  (3311915, 1, 0),
  (3313916, 1, 0),
  (3333930, 3, 0),
  (3337666, 0, 1),
  (3341092, 0, 2),
  (3341720, 0, 0),
  (3350114, 2, 0),
  (3356503, 2, 0),
  (3356825, 3, 1),
  (3367374, 0, 1),
  (3369240, 3, 0),
  (3370857, 0, 0),
  (3374598, 3, 1),
  (3381208, 1, 0),
  (3385064, 2, 0),
  (3391418, 2, 0),
  (3394729, 3, 2),
  (3395814, 2, 2),
  (3401624, 1, 1),
  (3404524, 1, 2),
  (3404881, 1, 2),
  (3414785, 3, 1),
  (3418157, 2, 0),
  (3423981, 1, 1),
  (3429900, 0, 0),
  (3451084, 3, 0),
  (3453576, 2, 0),
  (3453719, 2, 1),
  (3461402, 1, 0),
  (3472547, 1, 0),
  (3472872, 0, 0),
  (3475080, 0, 2),
  (3482687, 0, 1),
  (3485988, 0, 0),
  (3492428, 3, 0),
  (3497797, 1, 1),
  (3505583, 0, 2),
  (3509567, 1, 1),
  (3511437, 2, 1),
  (3516680, 2, 1),
  (3519587, 1, 0),
  (3523829, 2, 1),
  (3526648, 3, 1),
  (3531059, 0, 0),
  (3532437, 3, 1),
  (3534073, 2, 0),
  (3537393, 0, 2),
  (3538595, 2, 0),
  (3554666, 0, 2),
  (3560611, 2, 1),
  (3565269, 3, 2),
  (3572268, 1, 2),
  (3575152, 1, 2),
  (3575183, 1, 0),
  (3578768, 3, 0),
  (3580727, 1, 1),
  (3589841, 2, 1),
  (3590466, 3, 1),
  (3599844, 0, 1),
])
