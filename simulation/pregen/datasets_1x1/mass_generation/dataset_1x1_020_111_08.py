from util import *
schedule = deque([
  (7240, 4, 3),
  (10398, 1, 4),
  (11898, 1, 0),
  (13533, 6, 2),
  (15474, 2, 3),
  (19681, 3, 2),
  (20089, 0, 7),
  (21289, 3, 2),
  (21766, 2, 2),
  (25257, 3, 7),
  (31992, 5, 7),
  (32499, 2, 3),
  (35539, 1, 7),
  (48159, 0, 3),
  (56409, 3, 6),
  (59757, 0, 0),
  (62589, 0, 0),
  (72172, 3, 7),
  (75748, 3, 4),
  (76315, 2, 7),
  (82967, 4, 3),
  (84942, 3, 3),
  (86812, 1, 4),
  (88230, 4, 3),
  (89561, 0, 2),
  (91061, 1, 0),
  (93452, 6, 7),
  (97896, 4, 2),
  (98372, 2, 7),
  (99529, 1, 7),
  (104175, 5, 3),
  (108840, 1, 0),
  (109520, 2, 3),
  (110469, 3, 3),
  (110638, 6, 3),
  (111285, 3, 2),
  (112922, 6, 0),
  (113245, 6, 0),
  (114181, 7, 3),
  (116148, 7, 0),
  (123508, 0, 0),
  (126798, 1, 0),
  (130679, 7, 0),
  (132922, 0, 3),
  (133302, 6, 0),
  (137990, 6, 0),
  (146674, 0, 5),
  (148162, 0, 7),
  (162041, 4, 3),
  (165441, 1, 4),
  (166490, 2, 5),
  (167704, 5, 6),
  (168005, 3, 3),
  (171823, 3, 7),
  (172205, 2, 6),
  (175619, 1, 0),
  (177465, 2, 3),
  (179752, 0, 3),
  (181243, 4, 0),
  (186802, 2, 7),
  (187153, 3, 3),
  (196175, 0, 1),
  (198064, 7, 2),
  (208015, 4, 7),
  (208513, 7, 0),
  (209123, 2, 3),
  (210794, 0, 0),
  (210901, 4, 5),
  (217511, 1, 0),
  (218765, 4, 3),
  (230474, 1, 2),
  (234224, 7, 4),
  (236323, 6, 3),
  (240623, 1, 1),
  (248015, 2, 3),
  (250021, 5, 7),
  (255222, 4, 6),
  (259387, 3, 3),
  (260521, 0, 7),
  (262934, 0, 1),
  (267813, 4, 3),
  (269047, 7, 0),
  (271433, 4, 1),
  (272763, 7, 7),
  (275205, 0, 0),
  (275696, 2, 7),
  (277420, 2, 3),
  (282054, 3, 3),
  (284235, 5, 2),
  (286278, 5, 6),
  (287724, 7, 0),
  (288625, 1, 4),
  (290350, 1, 7),
  (293962, 5, 6),
  (298707, 3, 6),
  (303492, 6, 0),
  (314610, 6, 7),
  (317366, 1, 4),
  (321637, 6, 0),
  (325499, 7, 4),
  (331620, 0, 0),
  (332888, 5, 3),
  (336488, 1, 1),
  (338519, 1, 0),
  (342346, 0, 0),
  (342643, 5, 3),
  (344866, 0, 3),
  (345134, 0, 2),
  (355101, 7, 0),
  (355481, 0, 0),
  (355680, 1, 4),
  (356876, 2, 3),
  (356981, 3, 2),
  (360486, 6, 3),
  (366521, 0, 3),
  (369165, 0, 0),
  (373634, 7, 0),
  (373759, 6, 5),
  (375274, 0, 0),
  (375682, 6, 3),
  (381787, 2, 3),
  (382928, 6, 3),
  (388881, 6, 5),
  (393573, 0, 3),
  (394993, 6, 7),
  (399575, 1, 0),
  (401601, 2, 3),
  (402736, 0, 7),
  (407309, 3, 5),
  (412809, 0, 4),
  (417171, 7, 0),
  (417212, 4, 3),
  (424180, 0, 7),
  (427472, 1, 5),
  (431539, 6, 5),
  (431694, 5, 1),
  (437058, 3, 3),
  (440575, 3, 3),
  (442134, 2, 3),
  (442432, 7, 0),
  (442566, 2, 3),
  (447345, 4, 3),
  (455315, 4, 5),
  (456192, 7, 0),
  (456297, 7, 1),
  (460859, 0, 7),
  (461412, 4, 4),
  (461698, 3, 0),
  (461893, 0, 2),
  (462266, 1, 3),
  (465976, 2, 3),
  (466873, 1, 0),
  (469482, 7, 3),
  (469718, 6, 0),
  (470857, 2, 6),
  (473031, 4, 3),
  (473709, 4, 3),
  (479775, 2, 3),
  (480455, 3, 6),
  (483645, 7, 0),
  (486957, 3, 3),
  (488812, 2, 7),
  (495489, 5, 6),
  (495994, 1, 0),
  (503106, 6, 0),
  (505121, 5, 6),
  (506627, 4, 3),
  (512724, 0, 4),
  (513653, 0, 0),
  (515364, 6, 0),
  (529799, 4, 2),
  (530327, 7, 0),
  (533109, 5, 2),
  (534801, 1, 6),
  (537110, 0, 3),
  (543757, 2, 3),
  (548054, 1, 0),
  (554245, 5, 0),
  (557735, 3, 5),
  (558358, 4, 3),
  (560262, 7, 6),
  (560461, 5, 5),
  (562020, 2, 3),
  (566661, 5, 3),
  (567772, 6, 0),
  (569648, 0, 7),
  (572162, 5, 3),
  (573147, 6, 4),
  (578938, 4, 3),
  (581658, 4, 0),
  (584399, 6, 4),
  (584548, 4, 6),
  (591608, 2, 3),
  (591650, 6, 0),
  (593008, 6, 7),
  (595376, 7, 3),
  (596610, 3, 5),
  (597343, 0, 2),
  (603158, 1, 2),
  (604462, 7, 0),
  (604972, 5, 7),
  (606664, 2, 3),
  (614465, 4, 3),
  (617219, 4, 2),
  (638187, 1, 0),
  (638242, 3, 1),
  (640208, 5, 6),
  (650378, 1, 0),
  (653359, 4, 3),
  (653729, 3, 3),
  (655914, 7, 0),
  (657732, 5, 3),
  (657937, 7, 4),
  (661953, 3, 0),
  (661986, 7, 3),
  (674472, 0, 1),
  (681843, 4, 3),
  (687755, 2, 7),
  (689609, 0, 0),
  (691966, 0, 1),
  (695454, 3, 6),
  (698013, 2, 3),
  (703299, 1, 0),
  (708099, 3, 2),
  (709157, 7, 4),
  (709496, 4, 2),
  (712831, 5, 1),
  (712954, 5, 2),
  (716912, 4, 7),
  (720549, 0, 0),
  (726566, 3, 3),
  (728269, 5, 3),
  (729844, 6, 4),
  (732393, 2, 3),
  (734022, 2, 3),
  (735644, 2, 7),
  (735949, 2, 6),
  (736342, 1, 0),
  (738427, 5, 3),
  (738593, 7, 0),
  (740626, 3, 3),
  (746140, 3, 1),
  (746318, 2, 6),
  (748982, 2, 3),
  (753268, 5, 7),
  (754696, 0, 4),
  (755223, 4, 1),
  (756097, 3, 3),
  (757546, 6, 0),
  (758398, 2, 6),
  (767950, 7, 3),
  (769271, 5, 4),
  (772019, 5, 7),
  (773766, 7, 0),
  (776464, 7, 3),
  (779157, 6, 5),
  (789948, 3, 2),
  (798218, 1, 1),
  (799509, 3, 3),
  (799913, 2, 7),
  (808212, 5, 2),
  (812427, 1, 7),
  (814426, 2, 0),
  (815711, 2, 3),
  (816467, 3, 7),
  (817648, 2, 6),
  (817772, 1, 4),
  (820347, 1, 4),
  (825339, 2, 3),
  (826793, 1, 0),
  (827899, 0, 0),
  (836346, 7, 2),
  (844834, 5, 3),
  (850839, 0, 1),
  (851112, 5, 6),
  (859284, 5, 4),
  (859567, 7, 0),
  (860415, 0, 4),
  (862668, 1, 0),
  (865772, 6, 0),
  (867334, 5, 4),
  (868837, 1, 0),
  (875296, 2, 3),
  (876119, 7, 0),
  (876159, 6, 3),
  (876574, 6, 4),
  (882437, 2, 3),
  (884176, 1, 7),
  (891882, 7, 4),
  (892606, 6, 5),
  (893533, 0, 6),
  (894433, 2, 0),
  (897291, 1, 3),
  (900111, 3, 2),
  (901145, 4, 3),
  (902393, 0, 0),
  (910138, 4, 3),
  (918945, 0, 3),
  (920170, 2, 3),
  (922987, 7, 5),
  (923675, 0, 3),
  (928044, 7, 0),
  (935033, 4, 3),
  (936612, 6, 3),
  (937620, 3, 6),
  (941848, 4, 2),
  (942478, 6, 0),
  (945297, 2, 6),
  (946980, 5, 3),
  (946999, 4, 0),
  (947529, 3, 7),
  (947777, 0, 7),
  (950435, 7, 1),
  (950476, 6, 0),
  (951585, 3, 2),
  (954784, 1, 6),
  (955665, 4, 6),
  (955969, 2, 7),
  (956951, 0, 0),
  (958323, 5, 6),
  (960434, 2, 3),
  (963771, 2, 3),
  (964407, 6, 7),
  (965332, 4, 7),
  (968420, 7, 4),
  (969981, 5, 3),
  (974718, 6, 0),
  (976935, 6, 0),
  (981460, 3, 2),
  (982253, 7, 5),
  (986663, 4, 3),
  (987912, 2, 3),
  (989019, 5, 3),
  (989221, 2, 5),
  (996468, 7, 0),
  (997108, 6, 0),
  (997764, 1, 1),
  (1000370, 7, 7),
  (1001045, 1, 5),
  (1004594, 3, 3),
  (1005025, 5, 6),
  (1005268, 3, 2),
  (1009229, 1, 3),
  (1011018, 3, 3),
  (1011106, 2, 3),
  (1018294, 2, 7),
  (1021730, 4, 5),
  (1022821, 2, 7),
  (1022902, 6, 0),
  (1023788, 2, 3),
  (1024816, 6, 6),
  (1029201, 4, 3),
  (1033420, 4, 6),
  (1034376, 5, 3),
  (1041715, 3, 3),
  (1046426, 3, 7),
  (1050655, 3, 3),
  (1055892, 3, 3),
  (1062286, 0, 3),
  (1062722, 5, 7),
  (1067721, 7, 7),
  (1087222, 0, 1),
  (1088278, 2, 6),
  (1088447, 0, 0),
  (1088667, 6, 0),
  (1090809, 5, 3),
  (1094124, 2, 3),
  (1095606, 0, 3),
  (1098646, 0, 3),
  (1098690, 3, 5),
  (1102303, 5, 2),
  (1105044, 0, 3),
  (1105183, 2, 2),
  (1105433, 4, 6),
  (1105561, 2, 3),
  (1116644, 7, 0),
  (1118799, 0, 7),
  (1120067, 5, 5),
  (1120237, 7, 7),
  (1126086, 5, 0),
  (1126236, 5, 0),
  (1129044, 6, 4),
  (1134439, 7, 0),
  (1138185, 1, 0),
  (1138786, 1, 4),
  (1143920, 5, 6),
  (1156120, 1, 0),
  (1160173, 5, 7),
  (1161785, 6, 0),
  (1168501, 0, 3),
  (1174850, 0, 0),
  (1175047, 7, 0),
  (1175953, 1, 2),
  (1177702, 6, 3),
  (1182456, 5, 1),
  (1186031, 7, 3),
  (1193606, 1, 3),
  (1197975, 5, 3),
  (1199626, 5, 7),
  (1202405, 7, 0),
  (1213191, 7, 5),
  (1217722, 5, 3),
  (1224185, 1, 3),
  (1236696, 4, 6),
  (1240991, 2, 6),
  (1242279, 5, 2),
  (1242441, 0, 5),
  (1243115, 0, 3),
  (1245913, 0, 0),
  (1249555, 5, 2),
  (1250014, 1, 7),
  (1251383, 7, 0),
  (1251668, 7, 0),
  (1252856, 3, 7),
  (1253303, 3, 7),
  (1253610, 6, 0),
  (1254599, 6, 7),
  (1257221, 0, 0),
  (1257823, 3, 3),
  (1258389, 2, 2),
  (1263348, 5, 2),
  (1274751, 3, 3),
  (1277374, 7, 3),
  (1279098, 1, 0),
  (1280567, 6, 0),
  (1285187, 2, 3),
  (1286181, 5, 1),
  (1288293, 1, 0),
  (1288884, 3, 1),
  (1294326, 4, 1),
  (1299891, 6, 7),
  (1306325, 6, 0),
  (1311621, 6, 0),
  (1312121, 0, 0),
  (1314109, 6, 7),
  (1331846, 5, 7),
  (1334815, 5, 4),
  (1337258, 3, 1),
  (1344676, 7, 4),
  (1352241, 3, 3),
  (1357636, 0, 7),
  (1363025, 4, 1),
  (1363995, 3, 6),
  (1364649, 2, 3),
  (1369891, 3, 2),
  (1381146, 4, 3),
  (1383612, 5, 3),
  (1385703, 1, 7),
  (1387970, 2, 3),
  (1396167, 0, 0),
  (1397949, 4, 3),
  (1401268, 5, 3),
  (1402392, 7, 4),
  (1403415, 6, 0),
  (1404589, 1, 0),
  (1406453, 7, 4),
  (1410101, 1, 5),
  (1410403, 5, 6),
  (1411193, 0, 5),
  (1419304, 1, 0),
  (1429856, 5, 3),
  (1431485, 4, 4),
  (1432123, 5, 6),
  (1432719, 2, 3),
  (1433894, 0, 3),
  (1434669, 7, 0),
  (1437735, 0, 7),
  (1438644, 1, 0),
  (1438884, 2, 3),
  (1442336, 6, 0),
  (1443345, 1, 4),
  (1447201, 3, 7),
  (1448697, 1, 4),
  (1450200, 1, 7),
  (1452515, 2, 7),
  (1467053, 0, 1),
  (1468843, 6, 0),
  (1469572, 1, 0),
  (1478068, 3, 1),
  (1483745, 6, 4),
  (1484258, 7, 0),
  (1486122, 0, 0),
  (1489665, 1, 7),
  (1491513, 7, 0),
  (1496423, 4, 7),
  (1503341, 6, 1),
  (1508490, 6, 7),
  (1512110, 1, 4),
  (1513555, 4, 0),
  (1514411, 0, 4),
  (1520783, 4, 5),
  (1523721, 5, 2),
  (1525323, 5, 2),
  (1526832, 1, 4),
  (1530462, 4, 0),
  (1534992, 1, 6),
  (1545337, 6, 7),
  (1546103, 0, 7),
  (1548781, 0, 0),
  (1556031, 7, 3),
  (1565403, 2, 3),
  (1569030, 1, 2),
  (1571690, 4, 5),
  (1575381, 1, 5),
  (1575416, 6, 3),
  (1576476, 0, 0),
  (1577122, 5, 2),
  (1582253, 1, 5),
  (1584423, 4, 3),
  (1584428, 0, 0),
  (1585092, 2, 3),
  (1585553, 3, 3),
  (1588109, 4, 5),
  (1591074, 5, 6),
  (1592256, 4, 3),
  (1594520, 0, 0),
  (1601380, 3, 0),
  (1602349, 7, 0),
  (1604369, 2, 3),
  (1604750, 6, 0),
  (1606731, 4, 0),
  (1608248, 5, 3),
  (1611709, 4, 3),
  (1613375, 6, 0),
  (1614045, 6, 4),
  (1614993, 6, 7),
  (1616108, 7, 0),
  (1620460, 3, 7),
  (1621396, 5, 3),
  (1627634, 2, 3),
  (1630127, 0, 4),
  (1631591, 6, 3),
  (1638575, 5, 3),
  (1638746, 4, 2),
  (1640524, 5, 7),
  (1646008, 3, 3),
  (1650174, 5, 6),
  (1650525, 3, 2),
  (1652030, 1, 7),
  (1658901, 2, 7),
  (1675949, 5, 6),
  (1678778, 1, 7),
  (1687097, 0, 0),
  (1690007, 1, 0),
  (1690227, 6, 7),
  (1690916, 6, 0),
  (1691508, 4, 0),
  (1697382, 4, 7),
  (1697710, 5, 7),
  (1700170, 7, 0),
  (1700240, 3, 6),
  (1701648, 5, 1),
  (1704506, 6, 0),
  (1708295, 4, 3),
  (1713709, 3, 6),
  (1718921, 7, 0),
  (1721378, 3, 1),
  (1725061, 4, 6),
  (1733417, 0, 3),
  (1735326, 3, 5),
  (1735721, 4, 3),
  (1739342, 0, 4),
  (1739883, 4, 3),
  (1741217, 0, 3),
  (1746940, 6, 5),
  (1755299, 6, 7),
  (1755826, 1, 4),
  (1757972, 5, 1),
  (1762801, 5, 3),
  (1763467, 6, 5),
  (1764374, 3, 3),
  (1764865, 6, 3),
  (1770672, 5, 3),
  (1773520, 6, 4),
  (1773724, 0, 4),
  (1774881, 6, 0),
  (1780162, 2, 3),
  (1785567, 2, 5),
  (1790260, 6, 7),
  (1792697, 0, 6),
  (1792997, 0, 3),
  (1793139, 5, 3),
  (1804659, 6, 0),
  (1805862, 1, 4),
  (1805910, 7, 0),
  (1807114, 2, 3),
  (1807532, 6, 0),
  (1821554, 3, 3),
  (1825774, 0, 2),
  (1826710, 2, 3),
  (1828685, 4, 3),
  (1833426, 7, 0),
  (1833499, 3, 3),
  (1838215, 2, 1),
  (1843199, 1, 3),
  (1844685, 0, 0),
  (1846924, 3, 3),
  (1849580, 7, 7),
  (1858937, 3, 3),
  (1860162, 4, 3),
  (1866313, 6, 0),
  (1869255, 3, 2),
  (1869478, 0, 0),
  (1876281, 0, 1),
  (1878616, 4, 3),
  (1880109, 2, 3),
  (1881476, 6, 4),
  (1888543, 7, 0),
  (1894501, 2, 7),
  (1895434, 2, 3),
  (1898683, 7, 0),
  (1901787, 1, 0),
  (1902199, 3, 6),
  (1902460, 4, 3),
  (1903764, 1, 0),
  (1905993, 3, 6),
  (1907668, 3, 6),
  (1909069, 2, 7),
  (1909449, 2, 6),
  (1912941, 1, 0),
  (1914427, 2, 3),
  (1914659, 7, 0),
  (1922858, 0, 2),
  (1928854, 6, 3),
  (1929629, 3, 3),
  (1929783, 1, 7),
  (1939850, 2, 3),
  (1942090, 4, 5),
  (1942809, 2, 1),
  (1946088, 6, 3),
  (1948073, 7, 0),
  (1949136, 3, 3),
  (1952511, 4, 3),
  (1956745, 5, 3),
  (1961549, 5, 0),
  (1965180, 7, 1),
  (1983466, 7, 0),
  (1983529, 0, 1),
  (1983577, 0, 0),
  (1983644, 1, 0),
  (1986455, 2, 3),
  (1988403, 6, 0),
  (1992234, 1, 4),
  (1994629, 0, 7),
  (1996101, 0, 5),
  (1996592, 0, 7),
  (2000064, 0, 0),
  (2000869, 1, 0),
  (2007317, 1, 1),
  (2009316, 7, 0),
  (2009781, 0, 7),
  (2011055, 2, 3),
  (2013138, 3, 5),
  (2015577, 4, 3),
  (2018925, 1, 7),
  (2022011, 7, 1),
  (2027488, 6, 1),
  (2035968, 4, 6),
  (2036132, 7, 4),
  (2038416, 7, 7),
  (2059454, 6, 0),
  (2063195, 7, 0),
  (2066713, 4, 7),
  (2072349, 2, 5),
  (2077493, 1, 4),
  (2077754, 3, 3),
  (2077836, 6, 4),
  (2079551, 1, 0),
  (2081379, 0, 0),
  (2083429, 4, 6),
  (2084709, 0, 0),
  (2084829, 2, 3),
  (2087264, 6, 5),
  (2087834, 7, 1),
  (2093327, 4, 0),
  (2097013, 0, 0),
  (2100889, 5, 3),
  (2101906, 3, 2),
  (2104610, 5, 3),
  (2105628, 2, 7),
  (2108326, 7, 4),
  (2109668, 0, 7),
  (2110513, 0, 0),
  (2118525, 3, 2),
  (2118851, 6, 7),
  (2120806, 2, 3),
  (2122418, 5, 3),
  (2123811, 5, 3),
  (2125533, 1, 4),
  (2128212, 6, 4),
  (2128978, 1, 3),
  (2129529, 0, 0),
  (2129731, 2, 5),
  (2134885, 6, 2),
  (2144310, 6, 7),
  (2147991, 7, 7),
  (2148706, 6, 4),
  (2149553, 2, 4),
  (2154275, 0, 7),
  (2159465, 6, 0),
  (2166381, 2, 2),
  (2169823, 6, 6),
  (2170150, 1, 0),
  (2174474, 2, 6),
  (2181541, 0, 7),
  (2182786, 5, 1),
  (2182982, 6, 0),
  (2183871, 6, 0),
  (2191188, 0, 0),
  (2200158, 0, 7),
  (2201697, 3, 6),
  (2203969, 1, 3),
  (2206147, 4, 7),
  (2206761, 5, 0),
  (2207029, 4, 7),
  (2209476, 4, 6),
  (2220653, 5, 5),
  (2225163, 2, 3),
  (2233588, 0, 7),
  (2235865, 5, 6),
  (2236089, 2, 3),
  (2237355, 6, 0),
  (2238881, 5, 3),
  (2243606, 4, 2),
  (2243920, 6, 7),
  (2250486, 3, 4),
  (2253698, 0, 2),
  (2254008, 2, 3),
  (2256691, 1, 1),
  (2266671, 6, 5),
  (2268702, 2, 3),
  (2270335, 6, 0),
  (2276119, 1, 7),
  (2280207, 2, 2),
  (2284054, 5, 2),
  (2284327, 5, 7),
  (2285195, 6, 3),
  (2288684, 5, 0),
  (2296043, 1, 0),
  (2301521, 2, 3),
  (2303469, 2, 1),
  (2306819, 2, 3),
  (2306909, 1, 7),
  (2307430, 0, 0),
  (2308615, 2, 3),
  (2310827, 6, 1),
  (2311819, 3, 2),
  (2313038, 6, 3),
  (2314406, 3, 7),
  (2315007, 1, 6),
  (2316296, 7, 7),
  (2318357, 3, 6),
  (2318495, 6, 2),
  (2318584, 4, 3),
  (2326551, 0, 3),
  (2330366, 4, 2),
  (2332200, 1, 3),
  (2332972, 2, 7),
  (2333457, 3, 6),
  (2333886, 7, 7),
  (2335133, 5, 5),
  (2336066, 5, 3),
  (2339431, 2, 1),
  (2340110, 5, 6),
  (2340755, 5, 5),
  (2340796, 5, 3),
  (2341164, 0, 6),
  (2345771, 7, 7),
  (2348031, 7, 7),
  (2353528, 3, 4),
  (2362163, 7, 7),
  (2365973, 2, 6),
  (2366752, 5, 7),
  (2368701, 6, 0),
  (2370083, 4, 2),
  (2370519, 4, 7),
  (2371693, 1, 0),
  (2374243, 5, 6),
  (2381563, 6, 0),
  (2386648, 2, 4),
  (2394401, 6, 3),
  (2396920, 3, 5),
  (2397165, 2, 3),
  (2403271, 0, 0),
  (2403651, 1, 0),
  (2406616, 0, 7),
  (2412600, 1, 0),
  (2417748, 3, 3),
  (2418439, 1, 0),
  (2424114, 0, 0),
  (2425061, 0, 1),
  (2425380, 2, 7),
  (2430583, 6, 0),
  (2432119, 4, 7),
  (2437250, 0, 2),
  (2444721, 1, 6),
  (2455252, 5, 4),
  (2460662, 6, 0),
  (2467228, 0, 0),
  (2467370, 2, 3),
  (2468072, 0, 0),
  (2475092, 6, 3),
  (2477812, 1, 0),
  (2478610, 6, 2),
  (2478923, 4, 7),
  (2479412, 7, 0),
  (2480766, 7, 7),
  (2481415, 6, 3),
  (2482145, 0, 7),
  (2485688, 5, 7),
  (2488593, 4, 2),
  (2492188, 0, 2),
  (2494854, 3, 5),
  (2496700, 1, 0),
  (2509282, 3, 6),
  (2510294, 4, 3),
  (2515223, 3, 7),
  (2515725, 1, 0),
  (2516599, 1, 0),
  (2518360, 1, 0),
  (2520622, 1, 7),
  (2524057, 4, 3),
  (2529805, 7, 3),
  (2538788, 5, 2),
  (2544587, 5, 3),
  (2551080, 4, 5),
  (2551152, 1, 0),
  (2553181, 2, 6),
  (2562114, 0, 0),
  (2564192, 2, 6),
  (2577425, 1, 1),
  (2583447, 2, 3),
  (2583466, 0, 3),
  (2585727, 7, 5),
  (2596662, 4, 2),
  (2599130, 4, 6),
  (2600474, 3, 2),
  (2601678, 1, 4),
  (2606786, 3, 4),
  (2613066, 0, 4),
  (2614771, 0, 7),
  (2614944, 7, 0),
  (2622775, 5, 2),
  (2624652, 6, 1),
  (2626159, 3, 3),
  (2631203, 0, 4),
  (2631480, 3, 3),
  (2632881, 6, 3),
  (2636094, 7, 4),
  (2637522, 4, 3),
  (2638490, 5, 3),
  (2648320, 1, 0),
  (2648715, 2, 2),
  (2649185, 7, 7),
  (2650792, 6, 4),
  (2652384, 3, 4),
  (2658909, 1, 7),
  (2660156, 1, 0),
  (2664008, 5, 3),
  (2666268, 2, 2),
  (2671081, 2, 3),
  (2671281, 5, 3),
  (2672645, 4, 3),
  (2674946, 7, 0),
  (2675212, 5, 3),
  (2680254, 5, 3),
  (2682022, 1, 0),
  (2682218, 5, 3),
  (2684241, 2, 2),
  (2688101, 6, 0),
  (2694241, 7, 4),
  (2700064, 6, 3),
  (2701480, 7, 3),
  (2704443, 7, 0),
  (2706830, 3, 3),
  (2709000, 7, 7),
  (2710827, 4, 3),
  (2713655, 4, 3),
  (2714512, 5, 3),
  (2715614, 1, 1),
  (2717944, 4, 2),
  (2719716, 3, 7),
  (2721247, 1, 3),
  (2722541, 1, 0),
  (2725165, 2, 4),
  (2725851, 1, 0),
  (2726364, 7, 3),
  (2728402, 1, 0),
  (2728958, 7, 4),
  (2729338, 3, 5),
  (2729622, 2, 6),
  (2729656, 2, 1),
  (2730616, 0, 0),
  (2731038, 5, 4),
  (2733068, 1, 0),
  (2737980, 5, 2),
  (2747885, 0, 4),
  (2751473, 4, 3),
  (2751955, 1, 5),
  (2753093, 0, 0),
  (2758198, 3, 4),
  (2759926, 1, 7),
  (2760435, 7, 6),
  (2760542, 2, 3),
  (2766065, 2, 6),
  (2771443, 3, 6),
  (2776373, 1, 0),
  (2780271, 5, 2),
  (2785517, 7, 4),
  (2794814, 2, 3),
  (2795951, 1, 4),
  (2801789, 6, 0),
  (2802453, 6, 4),
  (2805701, 1, 3),
  (2808570, 4, 5),
  (2816606, 6, 4),
  (2818352, 4, 3),
  (2823560, 4, 5),
  (2825286, 5, 3),
  (2825544, 4, 3),
  (2825700, 5, 6),
  (2828809, 5, 4),
  (2831855, 4, 6),
  (2835048, 3, 3),
  (2848053, 7, 3),
  (2854048, 2, 6),
  (2858432, 2, 3),
  (2858983, 4, 2),
  (2859438, 6, 0),
  (2860249, 2, 7),
  (2861073, 1, 0),
  (2869538, 3, 5),
  (2869804, 5, 7),
  (2872526, 0, 4),
  (2874017, 1, 4),
  (2876474, 2, 6),
  (2878252, 6, 0),
  (2881289, 6, 5),
  (2882496, 0, 7),
  (2884817, 1, 0),
  (2887860, 2, 3),
  (2888254, 0, 5),
  (2888707, 0, 3),
  (2891615, 7, 4),
  (2891688, 4, 6),
  (2893028, 1, 0),
  (2893292, 6, 0),
  (2900732, 3, 2),
  (2902655, 0, 0),
  (2903310, 2, 3),
  (2905350, 0, 5),
  (2905625, 6, 0),
  (2909946, 6, 1),
  (2911140, 5, 3),
  (2911623, 4, 0),
  (2912327, 1, 7),
  (2914461, 0, 0),
  (2915304, 3, 2),
  (2916639, 7, 4),
  (2926509, 1, 7),
  (2933284, 1, 7),
  (2940663, 1, 1),
  (2941945, 5, 6),
  (2941985, 6, 3),
  (2942674, 3, 3),
  (2943316, 0, 0),
  (2943501, 1, 7),
  (2943919, 7, 3),
  (2947055, 7, 0),
  (2947946, 4, 6),
  (2950372, 5, 6),
  (2960285, 7, 0),
  (2962099, 3, 7),
  (2962132, 1, 7),
  (2967449, 3, 6),
  (2970252, 6, 5),
  (2971618, 4, 7),
  (2972505, 6, 0),
  (2974208, 0, 0),
  (2974858, 3, 7),
  (2984143, 3, 3),
  (2985054, 4, 6),
  (2985438, 1, 0),
  (2988121, 1, 0),
  (2989776, 5, 6),
  (2990554, 5, 3),
  (2992080, 4, 3),
  (2994600, 7, 1),
  (3001371, 0, 0),
  (3001845, 3, 3),
  (3001955, 7, 0),
  (3002855, 5, 1),
  (3004119, 6, 5),
  (3011917, 2, 7),
  (3011941, 5, 3),
  (3018229, 4, 7),
  (3018942, 3, 5),
  (3028703, 5, 0),
  (3037116, 6, 0),
  (3042646, 1, 0),
  (3048544, 2, 2),
  (3048916, 7, 0),
  (3050233, 3, 2),
  (3054514, 5, 4),
  (3057767, 1, 5),
  (3060938, 0, 7),
  (3064224, 0, 4),
  (3066957, 5, 7),
  (3069889, 0, 6),
  (3070137, 4, 7),
  (3071602, 2, 7),
  (3075663, 1, 1),
  (3080076, 0, 5),
  (3084955, 7, 4),
  (3085663, 2, 6),
  (3087000, 5, 7),
  (3088902, 1, 7),
  (3091269, 6, 2),
  (3097644, 7, 2),
  (3100110, 0, 0),
  (3103920, 4, 7),
  (3105943, 1, 3),
  (3107317, 2, 0),
  (3114993, 1, 0),
  (3120076, 5, 3),
  (3126378, 4, 3),
  (3129114, 7, 7),
  (3132201, 7, 4),
  (3133780, 2, 3),
  (3134768, 4, 5),
  (3135354, 6, 0),
  (3138128, 3, 3),
  (3138458, 6, 6),
  (3142739, 4, 7),
  (3154606, 6, 0),
  (3154664, 3, 4),
  (3156485, 1, 0),
  (3159150, 6, 0),
  (3160006, 3, 3),
  (3167748, 5, 3),
  (3169901, 3, 7),
  (3170963, 5, 3),
  (3172902, 4, 5),
  (3176377, 3, 3),
  (3176823, 7, 0),
  (3180317, 4, 3),
  (3184880, 7, 1),
  (3185773, 2, 2),
  (3190228, 0, 3),
  (3191160, 6, 0),
  (3192518, 4, 7),
  (3196262, 7, 3),
  (3201119, 1, 4),
  (3206189, 2, 3),
  (3206869, 3, 3),
  (3208467, 1, 0),
  (3210972, 0, 0),
  (3212032, 0, 1),
  (3216101, 7, 5),
  (3216330, 4, 3),
  (3216654, 6, 4),
  (3217350, 0, 4),
  (3217722, 2, 7),
  (3220062, 0, 7),
  (3221317, 5, 3),
  (3223294, 4, 1),
  (3228218, 3, 6),
  (3232704, 3, 0),
  (3234915, 0, 4),
  (3236735, 1, 7),
  (3237846, 5, 3),
  (3245165, 0, 0),
  (3246996, 7, 0),
  (3250594, 5, 3),
  (3257356, 5, 6),
  (3261787, 5, 6),
  (3262484, 4, 3),
  (3267572, 1, 0),
  (3271946, 4, 7),
  (3273368, 2, 3),
  (3277248, 4, 5),
  (3277303, 5, 1),
  (3278186, 1, 0),
  (3280269, 6, 4),
  (3282866, 7, 7),
  (3285451, 4, 0),
  (3289001, 3, 3),
  (3299444, 7, 0),
  (3301344, 4, 2),
  (3303420, 2, 2),
  (3304708, 6, 0),
  (3304833, 5, 3),
  (3304908, 1, 0),
  (3307940, 5, 2),
  (3310304, 2, 7),
  (3312775, 7, 0),
  (3325038, 3, 3),
  (3325167, 3, 2),
  (3325174, 5, 0),
  (3329067, 2, 4),
  (3338808, 5, 3),
  (3339563, 6, 7),
  (3342524, 6, 0),
  (3343152, 2, 3),
  (3346720, 2, 1),
  (3347221, 1, 0),
  (3349427, 1, 7),
  (3351693, 5, 4),
  (3357345, 7, 3),
  (3358893, 7, 0),
  (3360795, 0, 0),
  (3364608, 5, 3),
  (3365638, 4, 3),
  (3369494, 3, 6),
  (3372016, 2, 7),
  (3372670, 6, 3),
  (3372693, 4, 0),
  (3379034, 0, 5),
  (3382010, 0, 0),
  (3383484, 3, 3),
  (3386618, 5, 4),
  (3397180, 5, 6),
  (3398236, 3, 7),
  (3401029, 7, 3),
  (3402236, 2, 7),
  (3403613, 3, 1),
  (3405436, 4, 0),
  (3408797, 2, 0),
  (3411087, 7, 7),
  (3418023, 3, 3),
  (3419455, 3, 1),
  (3428963, 1, 0),
  (3429358, 7, 4),
  (3430827, 3, 3),
  (3431286, 3, 3),
  (3432779, 2, 6),
  (3432975, 1, 7),
  (3438068, 5, 2),
  (3447842, 4, 3),
  (3448159, 2, 3),
  (3448471, 5, 6),
  (3449826, 7, 0),
  (3452327, 2, 6),
  (3461728, 0, 7),
  (3463235, 0, 6),
  (3465197, 5, 3),
  (3465989, 0, 3),
  (3466794, 5, 3),
  (3467134, 4, 7),
  (3468191, 0, 4),
  (3477101, 1, 7),
  (3480212, 7, 7),
  (3481603, 0, 0),
  (3487252, 3, 0),
  (3487341, 6, 4),
  (3488881, 2, 7),
  (3492478, 3, 3),
  (3498610, 0, 2),
  (3499783, 6, 4),
  (3501027, 3, 7),
  (3501569, 0, 7),
  (3502058, 5, 2),
  (3503212, 3, 5),
  (3503884, 6, 6),
  (3504127, 0, 3),
  (3505920, 2, 6),
  (3507352, 0, 0),
  (3508514, 0, 0),
  (3510731, 4, 3),
  (3513585, 2, 7),
  (3515533, 0, 0),
  (3518532, 2, 6),
  (3518840, 5, 7),
  (3519544, 1, 3),
  (3519832, 6, 3),
  (3525939, 0, 4),
  (3529161, 3, 3),
  (3533508, 1, 0),
  (3535262, 2, 3),
  (3536925, 4, 3),
  (3541944, 0, 0),
  (3543556, 0, 0),
  (3549724, 5, 3),
  (3553395, 0, 0),
  (3554090, 5, 3),
  (3564602, 2, 3),
  (3565281, 3, 3),
  (3568864, 5, 3),
  (3570241, 2, 7),
  (3573710, 7, 3),
  (3576431, 5, 3),
  (3576973, 6, 0),
  (3580944, 3, 3),
  (3582938, 7, 2),
  (3585718, 0, 0),
  (3585852, 7, 4),
  (3587062, 1, 3),
  (3587991, 7, 7),
  (3591934, 1, 3),
  (3598977, 1, 0),
])