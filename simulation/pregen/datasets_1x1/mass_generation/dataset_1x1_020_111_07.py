from util import *
schedule = deque([
  (2024, 0, 0),
  (3698, 2, 3),
  (5705, 0, 0),
  (7213, 3, 3),
  (7414, 2, 6),
  (8354, 0, 0),
  (10924, 5, 2),
  (14673, 2, 2),
  (15836, 3, 6),
  (16631, 2, 3),
  (16695, 4, 7),
  (17398, 1, 5),
  (20285, 3, 7),
  (25557, 0, 0),
  (26393, 5, 0),
  (26718, 4, 2),
  (28533, 1, 1),
  (31592, 5, 2),
  (33196, 0, 0),
  (41956, 4, 0),
  (42569, 4, 3),
  (53055, 0, 5),
  (54308, 4, 3),
  (55496, 4, 1),
  (58191, 7, 4),
  (58468, 1, 1),
  (60231, 4, 0),
  (68799, 7, 7),
  (70892, 0, 0),
  (72927, 5, 2),
  (72988, 4, 3),
  (76138, 6, 0),
  (79089, 4, 0),
  (79422, 6, 0),
  (82887, 7, 4),
  (84816, 4, 3),
  (85622, 6, 0),
  (86087, 1, 3),
  (90308, 7, 4),
  (90786, 4, 2),
  (93623, 2, 7),
  (94503, 5, 2),
  (101084, 2, 3),
  (108003, 0, 3),
  (110932, 7, 0),
  (114738, 7, 7),
  (118474, 1, 1),
  (121728, 7, 0),
  (123956, 0, 0),
  (125734, 5, 2),
  (126115, 6, 4),
  (126605, 7, 4),
  (126625, 6, 4),
  (128302, 6, 0),
  (128900, 6, 0),
  (140178, 3, 3),
  (145385, 6, 0),
  (146840, 3, 3),
  (149882, 3, 3),
  (150324, 1, 0),
  (152490, 6, 1),
  (152719, 5, 2),
  (152752, 7, 4),
  (153122, 5, 6),
  (155489, 3, 3),
  (158764, 4, 6),
  (159621, 6, 0),
  (160373, 4, 2),
  (167602, 2, 3),
  (169520, 3, 7),
  (170799, 4, 3),
  (172202, 0, 4),
  (176896, 0, 2),
  (178398, 6, 0),
  (179715, 7, 0),
  (180249, 2, 3),
  (181632, 3, 3),
  (183833, 1, 3),
  (188005, 3, 3),
  (190010, 1, 0),
  (196749, 0, 7),
  (198355, 5, 0),
  (199524, 6, 3),
  (204466, 5, 7),
  (206787, 2, 3),
  (210311, 2, 3),
  (211329, 5, 4),
  (213419, 3, 5),
  (220042, 6, 3),
  (222908, 4, 3),
  (223029, 3, 3),
  (223438, 3, 3),
  (233454, 7, 3),
  (239001, 5, 7),
  (240811, 5, 7),
  (240886, 1, 0),
  (244757, 6, 0),
  (248375, 1, 0),
  (250318, 1, 0),
  (251306, 3, 2),
  (257980, 3, 3),
  (259868, 4, 3),
  (261886, 1, 4),
  (267313, 6, 3),
  (272427, 7, 0),
  (274212, 4, 3),
  (274326, 7, 4),
  (274931, 7, 0),
  (279790, 7, 0),
  (280232, 2, 3),
  (281194, 7, 4),
  (282577, 1, 3),
  (299874, 4, 6),
  (303024, 6, 0),
  (305042, 1, 5),
  (311472, 5, 3),
  (313698, 4, 3),
  (314789, 7, 3),
  (315057, 7, 7),
  (316169, 3, 1),
  (319948, 7, 3),
  (321741, 2, 3),
  (322157, 0, 2),
  (327332, 6, 4),
  (328091, 1, 7),
  (329260, 3, 5),
  (339716, 2, 6),
  (341184, 4, 2),
  (344410, 4, 3),
  (345395, 2, 3),
  (345405, 1, 3),
  (345838, 2, 7),
  (353905, 5, 6),
  (355594, 2, 2),
  (356560, 2, 3),
  (361808, 6, 2),
  (363216, 1, 3),
  (366803, 2, 2),
  (382076, 6, 0),
  (383460, 5, 3),
  (386021, 5, 3),
  (388906, 5, 3),
  (389252, 6, 5),
  (392422, 5, 4),
  (392455, 1, 3),
  (396047, 4, 7),
  (397560, 3, 6),
  (398274, 2, 3),
  (399601, 7, 0),
  (399937, 4, 3),
  (400468, 2, 3),
  (402161, 1, 4),
  (404251, 2, 2),
  (408178, 4, 3),
  (414358, 3, 1),
  (418497, 1, 0),
  (418649, 1, 7),
  (419516, 3, 6),
  (422629, 7, 0),
  (432071, 4, 3),
  (435315, 0, 3),
  (436347, 6, 0),
  (437883, 0, 0),
  (439657, 7, 0),
  (443946, 3, 5),
  (444573, 4, 4),
  (445162, 5, 2),
  (447725, 0, 0),
  (453558, 7, 7),
  (453794, 5, 3),
  (455764, 3, 6),
  (456090, 3, 3),
  (458791, 3, 6),
  (459676, 2, 3),
  (461162, 7, 6),
  (465872, 5, 5),
  (468478, 4, 3),
  (469691, 5, 7),
  (470132, 7, 4),
  (472193, 1, 0),
  (476522, 7, 0),
  (480598, 2, 3),
  (495112, 6, 4),
  (498664, 6, 2),
  (500243, 2, 7),
  (501553, 2, 7),
  (503504, 6, 0),
  (509018, 1, 0),
  (514264, 4, 2),
  (516401, 2, 6),
  (519035, 4, 3),
  (519425, 1, 7),
  (519843, 1, 7),
  (522170, 6, 0),
  (522682, 7, 1),
  (525337, 6, 0),
  (525411, 0, 2),
  (528172, 0, 3),
  (529981, 4, 6),
  (533066, 5, 1),
  (533295, 4, 3),
  (534484, 7, 4),
  (539491, 0, 0),
  (541440, 3, 4),
  (542708, 6, 3),
  (547556, 6, 4),
  (558792, 3, 3),
  (566547, 6, 0),
  (567247, 1, 7),
  (569333, 1, 5),
  (569339, 6, 5),
  (570733, 1, 0),
  (571119, 4, 5),
  (572250, 0, 0),
  (577701, 1, 7),
  (578183, 6, 5),
  (582031, 1, 3),
  (584988, 1, 7),
  (585777, 7, 7),
  (586905, 4, 3),
  (588043, 4, 3),
  (590422, 6, 3),
  (593085, 7, 4),
  (595803, 6, 3),
  (598039, 1, 5),
  (598588, 1, 3),
  (605197, 7, 0),
  (608460, 6, 4),
  (612743, 0, 7),
  (615543, 1, 3),
  (618883, 5, 2),
  (624217, 5, 3),
  (630222, 6, 6),
  (635424, 0, 4),
  (635916, 0, 5),
  (640563, 3, 3),
  (640565, 0, 3),
  (648085, 6, 4),
  (649331, 3, 3),
  (654436, 7, 0),
  (655366, 1, 4),
  (658539, 5, 3),
  (659598, 7, 0),
  (671358, 0, 3),
  (671764, 5, 3),
  (676570, 2, 3),
  (678973, 5, 5),
  (679647, 5, 3),
  (681049, 2, 3),
  (681754, 3, 5),
  (689398, 6, 3),
  (690988, 0, 7),
  (691234, 6, 2),
  (691597, 1, 0),
  (694394, 1, 0),
  (699243, 0, 0),
  (699782, 5, 3),
  (709223, 6, 0),
  (710638, 6, 7),
  (726177, 4, 3),
  (729625, 7, 7),
  (729954, 6, 0),
  (731025, 1, 4),
  (731408, 2, 3),
  (733499, 0, 4),
  (736361, 5, 2),
  (738029, 0, 4),
  (739035, 2, 2),
  (739899, 2, 1),
  (741581, 2, 7),
  (744364, 4, 5),
  (745477, 2, 2),
  (747436, 3, 7),
  (748355, 1, 7),
  (748455, 4, 3),
  (751117, 7, 2),
  (752129, 3, 3),
  (760343, 0, 0),
  (760700, 7, 0),
  (761575, 7, 5),
  (763106, 0, 0),
  (766301, 2, 6),
  (772763, 6, 0),
  (780164, 0, 4),
  (783749, 5, 3),
  (784521, 6, 0),
  (786514, 2, 1),
  (788699, 2, 6),
  (791778, 4, 7),
  (793391, 0, 0),
  (797604, 4, 1),
  (798541, 0, 5),
  (800836, 7, 0),
  (802279, 3, 3),
  (811610, 2, 2),
  (814317, 2, 2),
  (815096, 6, 1),
  (819104, 2, 3),
  (825264, 4, 7),
  (829108, 4, 6),
  (837243, 6, 3),
  (838378, 5, 2),
  (841769, 6, 3),
  (842020, 4, 3),
  (854599, 1, 0),
  (856453, 1, 4),
  (857128, 3, 6),
  (859287, 0, 0),
  (859348, 0, 0),
  (860872, 7, 3),
  (863909, 0, 0),
  (867787, 2, 0),
  (870177, 0, 3),
  (870819, 7, 2),
  (871393, 0, 4),
  (872470, 5, 3),
  (873975, 2, 2),
  (874236, 5, 6),
  (875696, 5, 1),
  (885887, 4, 3),
  (887993, 1, 3),
  (889065, 5, 7),
  (891978, 7, 3),
  (893555, 1, 0),
  (895756, 3, 7),
  (897521, 2, 3),
  (898337, 6, 3),
  (906413, 4, 3),
  (909661, 2, 4),
  (911326, 5, 7),
  (911925, 2, 3),
  (913404, 0, 3),
  (914761, 5, 3),
  (917474, 2, 0),
  (921255, 2, 7),
  (922117, 1, 3),
  (924957, 1, 5),
  (925805, 7, 0),
  (926710, 1, 0),
  (932502, 1, 4),
  (932884, 1, 2),
  (933501, 6, 4),
  (945392, 7, 4),
  (947934, 7, 0),
  (950005, 7, 0),
  (956750, 6, 0),
  (959338, 3, 3),
  (964218, 1, 5),
  (979009, 0, 4),
  (983590, 2, 6),
  (987065, 6, 3),
  (990660, 6, 0),
  (991678, 5, 3),
  (994188, 1, 0),
  (994293, 3, 2),
  (996326, 2, 1),
  (997254, 6, 7),
  (1001002, 1, 0),
  (1007730, 2, 3),
  (1010024, 0, 7),
  (1015249, 4, 5),
  (1023285, 2, 7),
  (1024363, 1, 0),
  (1025934, 5, 7),
  (1027850, 1, 5),
  (1034159, 3, 3),
  (1036054, 2, 2),
  (1038171, 3, 3),
  (1040046, 6, 0),
  (1043877, 6, 0),
  (1044380, 2, 2),
  (1062455, 1, 3),
  (1062650, 5, 6),
  (1064261, 5, 0),
  (1067706, 0, 0),
  (1069369, 7, 5),
  (1070421, 0, 2),
  (1074717, 1, 4),
  (1077185, 1, 7),
  (1078173, 3, 6),
  (1079303, 3, 2),
  (1082029, 5, 0),
  (1084287, 5, 7),
  (1084750, 3, 1),
  (1090062, 5, 4),
  (1091383, 4, 3),
  (1091616, 4, 6),
  (1093820, 6, 7),
  (1094341, 0, 3),
  (1095220, 4, 0),
  (1098244, 0, 0),
  (1098837, 1, 4),
  (1102521, 4, 3),
  (1109788, 6, 0),
  (1117767, 6, 2),
  (1118857, 3, 7),
  (1121278, 3, 7),
  (1128123, 1, 7),
  (1129672, 0, 3),
  (1130089, 0, 0),
  (1137325, 4, 3),
  (1137606, 2, 6),
  (1138439, 4, 2),
  (1151548, 1, 4),
  (1153538, 1, 3),
  (1154920, 2, 3),
  (1159579, 5, 6),
  (1161285, 6, 3),
  (1163977, 1, 1),
  (1170271, 2, 3),
  (1171181, 6, 6),
  (1177486, 4, 0),
  (1180926, 6, 5),
  (1184254, 0, 1),
  (1184599, 7, 3),
  (1184674, 5, 3),
  (1185919, 3, 3),
  (1187019, 2, 2),
  (1199049, 4, 3),
  (1206695, 6, 0),
  (1210778, 5, 3),
  (1212095, 6, 7),
  (1216218, 4, 1),
  (1226198, 2, 2),
  (1227503, 7, 3),
  (1227765, 7, 7),
  (1227996, 7, 1),
  (1228106, 5, 3),
  (1231179, 2, 2),
  (1232395, 5, 5),
  (1232865, 3, 3),
  (1237895, 0, 0),
  (1241528, 6, 3),
  (1242418, 7, 3),
  (1243471, 5, 3),
  (1244630, 4, 0),
  (1251466, 5, 1),
  (1258255, 1, 1),
  (1263226, 1, 0),
  (1265077, 5, 6),
  (1265636, 5, 1),
  (1276030, 4, 3),
  (1277121, 6, 4),
  (1277296, 1, 1),
  (1277522, 3, 2),
  (1278595, 4, 2),
  (1279301, 6, 0),
  (1279504, 2, 6),
  (1286271, 5, 3),
  (1287067, 0, 5),
  (1292400, 5, 3),
  (1298024, 6, 0),
  (1301062, 3, 4),
  (1301339, 1, 3),
  (1302749, 1, 0),
  (1307728, 4, 4),
  (1309038, 0, 7),
  (1314770, 1, 3),
  (1318808, 3, 3),
  (1320387, 6, 0),
  (1323514, 7, 0),
  (1326178, 3, 6),
  (1330323, 7, 0),
  (1332384, 2, 3),
  (1334172, 4, 3),
  (1334671, 6, 4),
  (1336357, 6, 0),
  (1337830, 0, 0),
  (1338143, 6, 6),
  (1340122, 7, 3),
  (1346265, 7, 3),
  (1347135, 5, 3),
  (1347873, 2, 3),
  (1349501, 6, 3),
  (1350843, 1, 0),
  (1352140, 2, 6),
  (1353528, 3, 3),
  (1358890, 6, 0),
  (1361246, 6, 7),
  (1363514, 5, 2),
  (1366154, 7, 0),
  (1370741, 5, 0),
  (1372665, 0, 0),
  (1373353, 3, 7),
  (1374264, 2, 3),
  (1374293, 6, 0),
  (1374618, 1, 0),
  (1383415, 1, 4),
  (1388364, 0, 5),
  (1390506, 1, 4),
  (1395443, 2, 6),
  (1397492, 5, 1),
  (1409806, 2, 3),
  (1411701, 1, 0),
  (1413903, 5, 4),
  (1418111, 0, 6),
  (1419605, 0, 3),
  (1426151, 3, 2),
  (1429466, 0, 7),
  (1431792, 7, 3),
  (1433484, 1, 3),
  (1433975, 1, 0),
  (1435361, 6, 1),
  (1435624, 6, 3),
  (1436801, 3, 3),
  (1441808, 4, 3),
  (1445735, 5, 3),
  (1446333, 6, 0),
  (1447869, 4, 3),
  (1450200, 7, 7),
  (1452191, 4, 4),
  (1461603, 4, 5),
  (1465433, 6, 4),
  (1466048, 5, 2),
  (1474015, 4, 2),
  (1474806, 3, 7),
  (1483046, 2, 4),
  (1488837, 2, 6),
  (1488893, 3, 2),
  (1490816, 1, 2),
  (1502325, 7, 7),
  (1505975, 2, 6),
  (1508055, 6, 4),
  (1510280, 6, 0),
  (1511988, 6, 0),
  (1513988, 0, 3),
  (1518146, 4, 3),
  (1519019, 7, 4),
  (1527504, 3, 3),
  (1536997, 4, 6),
  (1538195, 5, 2),
  (1540255, 2, 3),
  (1541064, 4, 0),
  (1542156, 5, 3),
  (1543997, 6, 0),
  (1546526, 4, 7),
  (1548462, 3, 7),
  (1548999, 1, 0),
  (1551337, 7, 0),
  (1556154, 7, 0),
  (1556168, 0, 0),
  (1556833, 7, 7),
  (1559216, 1, 7),
  (1560679, 6, 0),
  (1566894, 4, 3),
  (1567868, 4, 3),
  (1568633, 7, 4),
  (1574618, 4, 2),
  (1581374, 2, 2),
  (1582598, 4, 2),
  (1583489, 7, 4),
  (1586158, 4, 7),
  (1586473, 2, 7),
  (1594697, 3, 3),
  (1597551, 0, 0),
  (1601311, 1, 0),
  (1604578, 3, 4),
  (1605926, 6, 7),
  (1606125, 4, 6),
  (1608460, 7, 3),
  (1616818, 4, 2),
  (1619530, 5, 3),
  (1624074, 3, 7),
  (1629999, 5, 6),
  (1637329, 6, 0),
  (1643331, 4, 6),
  (1650068, 3, 3),
  (1652916, 1, 0),
  (1660303, 3, 5),
  (1667908, 4, 2),
  (1674979, 2, 4),
  (1681898, 2, 3),
  (1683957, 0, 1),
  (1689328, 4, 3),
  (1701069, 7, 0),
  (1703295, 0, 0),
  (1703546, 5, 7),
  (1707518, 6, 0),
  (1709338, 6, 0),
  (1709847, 5, 6),
  (1721827, 1, 0),
  (1727245, 1, 3),
  (1729155, 5, 6),
  (1735113, 2, 7),
  (1739312, 0, 0),
  (1741957, 3, 7),
  (1743858, 7, 3),
  (1743928, 4, 5),
  (1745167, 4, 6),
  (1745934, 1, 6),
  (1748928, 0, 0),
  (1760139, 4, 4),
  (1760741, 4, 2),
  (1762949, 1, 3),
  (1765223, 4, 3),
  (1774961, 6, 3),
  (1783660, 6, 0),
  (1785858, 7, 3),
  (1792699, 6, 4),
  (1796624, 3, 3),
  (1797744, 3, 2),
  (1802620, 3, 7),
  (1803210, 2, 3),
  (1807764, 1, 0),
  (1817727, 1, 0),
  (1818633, 5, 3),
  (1818742, 2, 3),
  (1821977, 4, 3),
  (1822210, 3, 7),
  (1828564, 2, 3),
  (1829579, 0, 0),
  (1831144, 0, 5),
  (1832356, 0, 0),
  (1839176, 6, 6),
  (1841419, 3, 7),
  (1847076, 3, 6),
  (1847099, 4, 1),
  (1851999, 4, 4),
  (1852219, 0, 0),
  (1861132, 5, 3),
  (1861422, 0, 4),
  (1865686, 2, 6),
  (1866391, 2, 2),
  (1867514, 7, 7),
  (1868209, 3, 7),
  (1870173, 1, 7),
  (1871340, 6, 3),
  (1873669, 5, 3),
  (1874940, 3, 2),
  (1876287, 3, 2),
  (1884848, 4, 4),
  (1884903, 1, 0),
  (1885991, 5, 7),
  (1893067, 3, 2),
  (1893106, 0, 2),
  (1893656, 3, 3),
  (1896550, 2, 2),
  (1896570, 5, 3),
  (1897852, 4, 1),
  (1901695, 0, 0),
  (1902285, 6, 0),
  (1903911, 6, 0),
  (1913117, 7, 6),
  (1914816, 2, 7),
  (1915286, 3, 3),
  (1917700, 5, 6),
  (1918628, 2, 4),
  (1919636, 1, 3),
  (1931896, 5, 7),
  (1935454, 5, 7),
  (1940718, 3, 7),
  (1944724, 0, 4),
  (1947919, 7, 3),
  (1956573, 5, 3),
  (1957611, 7, 0),
  (1960165, 0, 1),
  (1962107, 2, 3),
  (1966183, 2, 6),
  (1967112, 2, 3),
  (1972236, 4, 1),
  (1979254, 4, 3),
  (1979385, 3, 3),
  (1982910, 2, 2),
  (1983966, 5, 7),
  (1989005, 7, 4),
  (1990300, 4, 3),
  (1993356, 5, 0),
  (1995198, 6, 6),
  (2001939, 2, 3),
  (2009056, 7, 2),
  (2011592, 0, 4),
  (2012084, 7, 0),
  (2014994, 2, 7),
  (2018818, 3, 3),
  (2019584, 6, 0),
  (2022930, 3, 7),
  (2025853, 6, 0),
  (2029895, 6, 1),
  (2031475, 1, 0),
  (2032240, 4, 3),
  (2032334, 7, 4),
  (2038325, 4, 3),
  (2041457, 4, 7),
  (2046324, 1, 1),
  (2048828, 0, 4),
  (2051696, 5, 3),
  (2056800, 6, 0),
  (2058461, 2, 3),
  (2060112, 7, 0),
  (2062412, 0, 3),
  (2065269, 5, 7),
  (2065633, 7, 0),
  (2066494, 1, 2),
  (2066879, 3, 1),
  (2069111, 2, 3),
  (2071069, 0, 3),
  (2072817, 2, 6),
  (2080481, 6, 7),
  (2082497, 6, 3),
  (2083727, 0, 3),
  (2085718, 4, 1),
  (2086879, 1, 6),
  (2095156, 2, 6),
  (2098527, 2, 3),
  (2100245, 7, 2),
  (2100601, 0, 3),
  (2100616, 0, 0),
  (2100720, 1, 7),
  (2101406, 6, 0),
  (2104171, 3, 0),
  (2110652, 0, 0),
  (2117260, 1, 1),
  (2119262, 5, 1),
  (2122568, 4, 3),
  (2122686, 1, 7),
  (2123355, 0, 0),
  (2125775, 5, 3),
  (2127905, 2, 3),
  (2131743, 5, 3),
  (2136672, 3, 2),
  (2139375, 0, 0),
  (2141042, 3, 2),
  (2150244, 3, 3),
  (2152769, 3, 3),
  (2153342, 1, 4),
  (2153893, 1, 4),
  (2160139, 0, 0),
  (2161672, 2, 3),
  (2161769, 5, 2),
  (2169113, 3, 2),
  (2173252, 2, 3),
  (2189180, 2, 6),
  (2192372, 7, 7),
  (2200130, 1, 7),
  (2200513, 4, 3),
  (2204270, 3, 7),
  (2204752, 0, 0),
  (2205508, 0, 4),
  (2206972, 7, 0),
  (2208900, 1, 7),
  (2209661, 7, 0),
  (2210110, 4, 3),
  (2211279, 2, 2),
  (2217443, 7, 4),
  (2219749, 2, 3),
  (2220614, 2, 3),
  (2222824, 2, 6),
  (2226422, 4, 2),
  (2234382, 4, 6),
  (2235958, 7, 3),
  (2249049, 3, 5),
  (2254678, 5, 7),
  (2255432, 3, 3),
  (2262949, 5, 3),
  (2269048, 0, 0),
  (2271099, 1, 0),
  (2272819, 5, 6),
  (2276340, 1, 0),
  (2280200, 0, 4),
  (2280247, 6, 2),
  (2280934, 2, 3),
  (2281571, 1, 7),
  (2283839, 7, 7),
  (2284986, 7, 0),
  (2287832, 2, 7),
  (2295405, 3, 2),
  (2295518, 5, 5),
  (2295565, 0, 2),
  (2296276, 4, 6),
  (2298492, 5, 3),
  (2298642, 5, 2),
  (2300442, 6, 0),
  (2306825, 0, 4),
  (2317056, 4, 6),
  (2321188, 5, 7),
  (2321974, 2, 6),
  (2327577, 2, 2),
  (2327906, 6, 2),
  (2328354, 4, 2),
  (2329551, 1, 1),
  (2332258, 3, 3),
  (2333046, 2, 7),
  (2333500, 7, 0),
  (2337470, 4, 3),
  (2339279, 3, 3),
  (2346151, 5, 7),
  (2346155, 5, 4),
  (2346782, 6, 0),
  (2347699, 4, 3),
  (2350014, 4, 3),
  (2350851, 0, 0),
  (2354622, 4, 6),
  (2355207, 6, 3),
  (2357758, 7, 1),
  (2364430, 4, 3),
  (2366758, 5, 6),
  (2369488, 0, 3),
  (2372583, 3, 0),
  (2382802, 3, 7),
  (2383304, 2, 2),
  (2383417, 2, 4),
  (2392685, 2, 3),
  (2397947, 5, 2),
  (2404373, 1, 0),
  (2404439, 1, 3),
  (2405320, 7, 0),
  (2409210, 7, 0),
  (2411235, 3, 3),
  (2411903, 3, 7),
  (2413739, 2, 0),
  (2421861, 5, 3),
  (2426474, 6, 0),
  (2429547, 7, 6),
  (2431889, 4, 7),
  (2433698, 1, 1),
  (2433947, 6, 0),
  (2434294, 2, 2),
  (2436793, 3, 7),
  (2438808, 1, 7),
  (2439222, 0, 0),
  (2439976, 7, 3),
  (2441300, 6, 0),
  (2445772, 2, 3),
  (2447611, 3, 3),
  (2456044, 2, 3),
  (2457096, 3, 7),
  (2457637, 1, 2),
  (2458145, 2, 5),
  (2466501, 4, 6),
  (2467989, 5, 2),
  (2469899, 5, 3),
  (2478446, 7, 0),
  (2482384, 5, 3),
  (2484590, 4, 6),
  (2489773, 7, 3),
  (2495140, 4, 7),
  (2499891, 6, 7),
  (2502901, 0, 3),
  (2505931, 5, 2),
  (2511789, 1, 0),
  (2512085, 4, 3),
  (2515845, 2, 6),
  (2525653, 2, 2),
  (2531509, 7, 0),
  (2537207, 2, 0),
  (2539741, 2, 6),
  (2539981, 2, 7),
  (2542613, 3, 2),
  (2542746, 2, 3),
  (2548820, 4, 2),
  (2551869, 2, 3),
  (2553990, 6, 0),
  (2560277, 0, 7),
  (2561424, 2, 3),
  (2563345, 7, 3),
  (2566185, 7, 2),
  (2566581, 2, 2),
  (2566783, 0, 0),
  (2579201, 7, 0),
  (2579757, 0, 4),
  (2579853, 6, 7),
  (2594001, 7, 3),
  (2596903, 3, 3),
  (2597115, 4, 3),
  (2597583, 4, 4),
  (2598633, 0, 6),
  (2600515, 7, 0),
  (2605179, 7, 1),
  (2613803, 2, 6),
  (2614090, 6, 0),
  (2617057, 5, 3),
  (2618723, 3, 3),
  (2622358, 2, 3),
  (2622450, 1, 3),
  (2623706, 6, 5),
  (2631902, 0, 0),
  (2635988, 5, 6),
  (2641326, 5, 3),
  (2642441, 4, 3),
  (2642924, 1, 4),
  (2655444, 3, 3),
  (2655854, 1, 5),
  (2658829, 2, 6),
  (2666148, 7, 7),
  (2666330, 1, 7),
  (2666470, 4, 3),
  (2667283, 7, 1),
  (2667644, 5, 7),
  (2668742, 7, 0),
  (2668765, 2, 3),
  (2669063, 5, 3),
  (2669173, 4, 6),
  (2670496, 0, 0),
  (2675663, 5, 2),
  (2680360, 2, 7),
  (2682073, 5, 6),
  (2682428, 2, 7),
  (2683234, 6, 0),
  (2686742, 1, 0),
  (2687060, 5, 3),
  (2687977, 7, 0),
  (2690382, 7, 4),
  (2692479, 1, 0),
  (2704461, 5, 3),
  (2707592, 6, 0),
  (2708414, 0, 0),
  (2711228, 0, 5),
  (2715906, 6, 5),
  (2717129, 5, 1),
  (2718841, 6, 0),
  (2718853, 0, 7),
  (2719226, 0, 6),
  (2726751, 4, 7),
  (2732888, 2, 3),
  (2733173, 6, 3),
  (2734135, 6, 0),
  (2735211, 3, 3),
  (2735420, 3, 2),
  (2738237, 7, 0),
  (2738306, 3, 6),
  (2740204, 0, 2),
  (2743063, 3, 3),
  (2746898, 1, 0),
  (2749156, 6, 5),
  (2749825, 4, 7),
  (2751289, 4, 3),
  (2754212, 0, 0),
  (2758787, 6, 0),
  (2761535, 6, 0),
  (2763039, 0, 0),
  (2767807, 2, 1),
  (2769032, 0, 4),
  (2770481, 3, 3),
  (2774147, 2, 2),
  (2774575, 6, 4),
  (2775434, 2, 6),
  (2784311, 5, 3),
  (2784603, 6, 0),
  (2785546, 1, 0),
  (2785713, 1, 0),
  (2792604, 0, 0),
  (2799285, 3, 3),
  (2799736, 5, 7),
  (2801140, 4, 4),
  (2807158, 1, 0),
  (2813343, 4, 3),
  (2813465, 1, 0),
  (2813904, 3, 3),
  (2826348, 7, 0),
  (2829736, 4, 6),
  (2834498, 6, 0),
  (2834866, 1, 6),
  (2835563, 4, 3),
  (2836197, 1, 0),
  (2842199, 2, 4),
  (2842472, 5, 6),
  (2844281, 7, 3),
  (2845074, 7, 0),
  (2846842, 7, 0),
  (2848254, 6, 2),
  (2850204, 7, 4),
  (2850901, 3, 3),
  (2853710, 4, 7),
  (2857129, 0, 4),
  (2861223, 0, 0),
  (2869209, 3, 3),
  (2871858, 7, 5),
  (2875550, 4, 0),
  (2875875, 5, 7),
  (2880685, 0, 7),
  (2882973, 3, 3),
  (2885232, 6, 0),
  (2885766, 1, 7),
  (2891968, 3, 3),
  (2893148, 4, 3),
  (2894427, 5, 3),
  (2899212, 5, 5),
  (2899894, 7, 5),
  (2905219, 6, 0),
  (2907688, 1, 3),
  (2914128, 2, 3),
  (2919632, 3, 7),
  (2931452, 6, 1),
  (2932158, 2, 3),
  (2932320, 0, 5),
  (2938933, 7, 0),
  (2945948, 6, 0),
  (2947773, 1, 0),
  (2954065, 4, 2),
  (2954488, 7, 2),
  (2956304, 1, 0),
  (2961393, 3, 7),
  (2966224, 0, 0),
  (2966919, 4, 2),
  (2971404, 4, 0),
  (2975380, 6, 7),
  (2976032, 2, 3),
  (2976426, 5, 3),
  (2984124, 5, 3),
  (2988678, 0, 7),
  (2992067, 1, 0),
  (2992069, 7, 7),
  (2992435, 2, 0),
  (3002340, 5, 3),
  (3009815, 2, 0),
  (3019624, 4, 2),
  (3019997, 6, 0),
  (3020031, 5, 1),
  (3021985, 5, 3),
  (3023456, 0, 3),
  (3023590, 4, 2),
  (3026673, 5, 3),
  (3029677, 5, 3),
  (3030480, 7, 4),
  (3031203, 4, 3),
  (3044664, 7, 1),
  (3051730, 0, 0),
  (3052338, 0, 1),
  (3052349, 7, 0),
  (3060330, 3, 6),
  (3063721, 5, 6),
  (3067156, 2, 3),
  (3067662, 3, 6),
  (3070325, 4, 6),
  (3075903, 1, 4),
  (3085843, 6, 0),
  (3087157, 1, 4),
  (3087926, 6, 4),
  (3092962, 0, 0),
  (3094714, 0, 7),
  (3102031, 6, 0),
  (3102684, 1, 7),
  (3110184, 0, 2),
  (3110644, 0, 0),
  (3118618, 1, 7),
  (3119572, 5, 2),
  (3122277, 4, 0),
  (3122728, 7, 0),
  (3123264, 0, 4),
  (3125090, 7, 7),
  (3125272, 3, 7),
  (3128663, 1, 4),
  (3130006, 2, 3),
  (3134254, 0, 4),
  (3135286, 2, 6),
  (3135883, 5, 3),
  (3139935, 0, 4),
  (3141619, 0, 7),
  (3143458, 1, 0),
  (3149515, 7, 3),
  (3158479, 7, 7),
  (3160912, 0, 2),
  (3170977, 4, 3),
  (3172808, 6, 0),
  (3175812, 4, 3),
  (3181535, 5, 2),
  (3181778, 2, 3),
  (3182573, 1, 0),
  (3185286, 5, 2),
  (3187257, 1, 0),
  (3189887, 3, 3),
  (3191365, 0, 4),
  (3197670, 0, 7),
  (3201863, 0, 7),
  (3202032, 2, 2),
  (3202437, 5, 3),
  (3209997, 0, 5),
  (3212604, 7, 0),
  (3214086, 6, 0),
  (3215368, 3, 7),
  (3216199, 2, 7),
  (3216265, 1, 6),
  (3218682, 0, 0),
  (3221068, 6, 0),
  (3228850, 5, 6),
  (3234416, 4, 0),
  (3234587, 7, 0),
  (3235916, 7, 3),
  (3237904, 4, 3),
  (3238538, 1, 3),
  (3240083, 0, 0),
  (3241452, 2, 3),
  (3241701, 2, 7),
  (3246219, 5, 1),
  (3246592, 5, 3),
  (3255202, 4, 3),
  (3258455, 2, 2),
  (3262939, 5, 6),
  (3265948, 1, 0),
  (3271284, 7, 0),
  (3274828, 6, 6),
  (3279992, 2, 4),
  (3282682, 3, 3),
  (3282855, 7, 4),
  (3283638, 4, 3),
  (3283907, 4, 4),
  (3287777, 4, 6),
  (3290642, 4, 7),
  (3294881, 1, 7),
  (3295621, 4, 0),
  (3310019, 6, 7),
  (3311021, 7, 4),
  (3311966, 1, 4),
  (3313006, 5, 2),
  (3317796, 4, 0),
  (3322086, 4, 7),
  (3322237, 4, 6),
  (3322693, 7, 1),
  (3323133, 6, 6),
  (3332934, 6, 0),
  (3334823, 1, 1),
  (3338121, 5, 3),
  (3345684, 1, 0),
  (3351712, 1, 0),
  (3355408, 1, 0),
  (3357611, 1, 7),
  (3359236, 2, 2),
  (3359268, 3, 3),
  (3368646, 4, 1),
  (3371236, 6, 0),
  (3374622, 5, 5),
  (3375067, 6, 7),
  (3380061, 6, 3),
  (3380597, 4, 4),
  (3380866, 7, 4),
  (3384257, 4, 6),
  (3388377, 3, 0),
  (3390694, 4, 6),
  (3393775, 5, 2),
  (3395003, 4, 5),
  (3402224, 3, 3),
  (3405938, 4, 3),
  (3407964, 0, 0),
  (3409442, 4, 3),
  (3410918, 7, 0),
  (3413124, 7, 0),
  (3414864, 1, 0),
  (3415476, 7, 0),
  (3426235, 5, 3),
  (3427821, 7, 2),
  (3428535, 0, 6),
  (3428871, 6, 0),
  (3438438, 0, 0),
  (3438466, 2, 3),
  (3438798, 1, 0),
  (3443153, 3, 3),
  (3443276, 1, 5),
  (3445023, 0, 1),
  (3447504, 1, 4),
  (3453657, 1, 7),
  (3456556, 1, 0),
  (3459210, 1, 0),
  (3460782, 0, 7),
  (3463865, 2, 6),
  (3468039, 2, 3),
  (3478826, 0, 4),
  (3488154, 3, 7),
  (3492790, 1, 0),
  (3493501, 5, 3),
  (3494580, 0, 1),
  (3495254, 0, 0),
  (3498292, 0, 0),
  (3501950, 6, 0),
  (3503422, 2, 3),
  (3504319, 2, 2),
  (3509731, 5, 3),
  (3512319, 5, 6),
  (3513713, 3, 0),
  (3514267, 6, 0),
  (3515311, 5, 2),
  (3519030, 0, 5),
  (3519697, 4, 7),
  (3526169, 4, 2),
  (3526867, 5, 2),
  (3529074, 0, 1),
  (3538252, 6, 0),
  (3538577, 6, 0),
  (3543959, 7, 3),
  (3545035, 3, 0),
  (3552808, 0, 6),
  (3553255, 2, 3),
  (3554807, 6, 0),
  (3554811, 4, 2),
  (3559083, 2, 6),
  (3563437, 5, 1),
  (3564974, 3, 6),
  (3568242, 7, 4),
  (3570708, 2, 0),
  (3570747, 6, 0),
  (3573571, 4, 0),
  (3574121, 7, 5),
  (3574895, 1, 4),
  (3583407, 1, 7),
  (3585042, 7, 3),
  (3586747, 0, 3),
  (3587171, 5, 6),
  (3593396, 2, 7),
  (3594372, 6, 0),
  (3596606, 6, 7),
  (3597573, 0, 4),
])