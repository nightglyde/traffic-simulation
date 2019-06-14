from src.util import *
schedule = deque([
  (2584, 3, 2),
  (3330, 3, 0),
  (3932, 0, 0),
  (4387, 2, 2),
  (5070, 1, 1),
  (8301, 0, 1),
  (8473, 3, 0),
  (9543, 3, 1),
  (17492, 2, 1),
  (21625, 0, 2),
  (24020, 1, 0),
  (29890, 3, 1),
  (34238, 3, 2),
  (34652, 1, 0),
  (35309, 2, 2),
  (45582, 3, 2),
  (47410, 0, 0),
  (48088, 1, 0),
  (49100, 3, 2),
  (54761, 2, 0),
  (68843, 2, 0),
  (71229, 3, 2),
  (71708, 0, 2),
  (72407, 2, 2),
  (74294, 0, 1),
  (74427, 2, 1),
  (79842, 0, 2),
  (80588, 2, 2),
  (87900, 0, 0),
  (89330, 1, 0),
  (89722, 2, 1),
  (95972, 2, 2),
  (97480, 3, 2),
  (98972, 1, 0),
  (102120, 3, 1),
  (102637, 3, 0),
  (104178, 2, 1),
  (104377, 2, 1),
  (108603, 3, 0),
  (108963, 3, 0),
  (113203, 0, 2),
  (113304, 0, 1),
  (122697, 3, 1),
  (131436, 2, 1),
  (131716, 2, 2),
  (132775, 3, 0),
  (134819, 2, 1),
  (136382, 2, 1),
  (137978, 0, 2),
  (140503, 1, 2),
  (144390, 2, 0),
  (144940, 2, 1),
  (148814, 2, 2),
  (150832, 1, 1),
  (152571, 3, 1),
  (156835, 3, 2),
  (159150, 0, 2),
  (159616, 3, 2),
  (160156, 0, 0),
  (160231, 3, 2),
  (160965, 0, 0),
  (161939, 3, 2),
  (166737, 0, 0),
  (168527, 3, 0),
  (175213, 3, 2),
  (175545, 0, 2),
  (176592, 3, 2),
  (178387, 1, 1),
  (179554, 3, 0),
  (180027, 1, 1),
  (181182, 0, 2),
  (181956, 1, 1),
  (186004, 3, 1),
  (191282, 0, 1),
  (192919, 0, 1),
  (199654, 1, 0),
  (203086, 2, 0),
  (204369, 3, 0),
  (211580, 1, 2),
  (211747, 3, 0),
  (217653, 1, 1),
  (217710, 3, 0),
  (218853, 2, 2),
  (219701, 1, 2),
  (224046, 2, 0),
  (226679, 2, 2),
  (228873, 2, 1),
  (230999, 2, 1),
  (231212, 0, 1),
  (231421, 1, 2),
  (231484, 0, 2),
  (231993, 0, 1),
  (232572, 3, 1),
  (235221, 1, 0),
  (236806, 2, 1),
  (239558, 2, 0),
  (239607, 3, 2),
  (243093, 3, 0),
  (250414, 1, 1),
  (253436, 0, 0),
  (253463, 2, 1),
  (253626, 1, 2),
  (256313, 2, 1),
  (258512, 0, 0),
  (258634, 2, 0),
  (262259, 1, 0),
  (263426, 3, 2),
  (266285, 2, 0),
  (270225, 2, 0),
  (272409, 2, 0),
  (275075, 1, 1),
  (276401, 3, 0),
  (278289, 0, 2),
  (279840, 1, 0),
  (280921, 1, 2),
  (282691, 1, 0),
  (288098, 3, 1),
  (288245, 1, 2),
  (289537, 1, 2),
  (291113, 1, 2),
  (298760, 3, 0),
  (299625, 0, 1),
  (305823, 1, 0),
  (307792, 2, 1),
  (319267, 2, 1),
  (323285, 0, 2),
  (325048, 2, 1),
  (328660, 1, 2),
  (339150, 0, 2),
  (342892, 3, 2),
  (343549, 3, 1),
  (349233, 3, 0),
  (351867, 3, 0),
  (352261, 2, 2),
  (354001, 3, 2),
  (358854, 3, 1),
  (359767, 0, 2),
  (360175, 3, 1),
  (363737, 1, 0),
  (363950, 1, 0),
  (365178, 1, 1),
  (365537, 0, 2),
  (366738, 2, 2),
  (372798, 1, 1),
  (375985, 2, 1),
  (377529, 2, 2),
  (377735, 3, 0),
  (381648, 0, 2),
  (383154, 0, 2),
  (384906, 0, 2),
  (395647, 2, 2),
  (397333, 2, 0),
  (404664, 3, 1),
  (407797, 2, 2),
  (408614, 2, 0),
  (411146, 2, 0),
  (417636, 2, 1),
  (420335, 2, 1),
  (421744, 3, 1),
  (422272, 0, 0),
  (431092, 3, 0),
  (431805, 2, 0),
  (432610, 0, 1),
  (441112, 3, 0),
  (444160, 3, 0),
  (446561, 3, 2),
  (446699, 2, 1),
  (466084, 0, 1),
  (467002, 3, 2),
  (467539, 1, 2),
  (471247, 2, 2),
  (471380, 1, 2),
  (473863, 3, 0),
  (477050, 2, 2),
  (477085, 2, 0),
  (481894, 2, 1),
  (486560, 0, 2),
  (487473, 1, 0),
  (488787, 2, 0),
  (497108, 1, 0),
  (499107, 3, 2),
  (500314, 1, 0),
  (502296, 2, 2),
  (505023, 0, 0),
  (507005, 3, 2),
  (508894, 3, 1),
  (510079, 1, 2),
  (510912, 2, 0),
  (511170, 3, 0),
  (512721, 0, 1),
  (513428, 1, 0),
  (514876, 0, 0),
  (516090, 2, 0),
  (517034, 1, 0),
  (517759, 0, 2),
  (518062, 0, 0),
  (520573, 1, 0),
  (523111, 2, 1),
  (524490, 1, 2),
  (525295, 0, 1),
  (525747, 0, 1),
  (526224, 1, 0),
  (527431, 0, 0),
  (529870, 0, 2),
  (530479, 3, 0),
  (532760, 1, 2),
  (539682, 1, 2),
  (539693, 3, 0),
  (548124, 0, 0),
  (551318, 1, 1),
  (553620, 3, 0),
  (554328, 2, 1),
  (557549, 1, 2),
  (557803, 1, 1),
  (558514, 3, 0),
  (562641, 0, 1),
  (562994, 1, 2),
  (565709, 0, 2),
  (567430, 0, 0),
  (568418, 0, 2),
  (568485, 3, 1),
  (571511, 0, 1),
  (574233, 3, 2),
  (580155, 0, 1),
  (580895, 2, 1),
  (582695, 1, 2),
  (584787, 1, 0),
  (589750, 1, 1),
  (596323, 1, 1),
  (602178, 0, 0),
  (605229, 0, 2),
  (611125, 3, 0),
  (611395, 3, 0),
  (611748, 2, 1),
  (612991, 3, 2),
  (613785, 3, 1),
  (615297, 3, 2),
  (616997, 3, 1),
  (617498, 0, 2),
  (622596, 1, 1),
  (626966, 2, 2),
  (632080, 1, 1),
  (632474, 2, 0),
  (633521, 2, 1),
  (636980, 3, 1),
  (644264, 1, 0),
  (648193, 3, 1),
  (650438, 0, 2),
  (650604, 1, 2),
  (652946, 3, 0),
  (654488, 1, 0),
  (663652, 1, 2),
  (675524, 3, 0),
  (677311, 0, 2),
  (678347, 1, 2),
  (683838, 1, 0),
  (685115, 0, 1),
  (686286, 3, 2),
  (686386, 3, 2),
  (686443, 3, 2),
  (686612, 1, 0),
  (688293, 3, 0),
  (689785, 2, 0),
  (699841, 0, 2),
  (705709, 2, 0),
  (706841, 1, 1),
  (709710, 0, 0),
  (717628, 3, 0),
  (719104, 2, 2),
  (721044, 3, 2),
  (725880, 3, 2),
  (739364, 3, 0),
  (741931, 3, 1),
  (742607, 0, 1),
  (746655, 0, 1),
  (749920, 2, 1),
  (751595, 3, 2),
  (752104, 2, 0),
  (754850, 0, 1),
  (759205, 2, 0),
  (760216, 1, 1),
  (769382, 3, 0),
  (771340, 1, 1),
  (781156, 0, 0),
  (781388, 2, 1),
  (782700, 3, 2),
  (784930, 0, 0),
  (786442, 2, 2),
  (791256, 3, 1),
  (793961, 3, 0),
  (794229, 1, 0),
  (797226, 0, 2),
  (800100, 3, 1),
  (807843, 0, 0),
  (811201, 3, 1),
  (812152, 1, 2),
  (812782, 1, 0),
  (826900, 2, 2),
  (829707, 3, 1),
  (844157, 3, 0),
  (849894, 0, 2),
  (851974, 1, 2),
  (857202, 2, 1),
  (864338, 2, 1),
  (865822, 0, 1),
  (867733, 0, 2),
  (891725, 1, 0),
  (894300, 1, 1),
  (894321, 1, 2),
  (895539, 1, 1),
  (901230, 0, 2),
  (911027, 3, 0),
  (911576, 2, 2),
  (915793, 0, 1),
  (917142, 1, 1),
  (918309, 0, 1),
  (918409, 2, 1),
  (918417, 3, 1),
  (919723, 3, 2),
  (929261, 2, 2),
  (930004, 3, 2),
  (935596, 3, 2),
  (937900, 0, 0),
  (953274, 1, 1),
  (955793, 3, 1),
  (957166, 1, 0),
  (957508, 0, 2),
  (958572, 3, 1),
  (965587, 1, 0),
  (971031, 2, 1),
  (975066, 1, 1),
  (977573, 1, 0),
  (981752, 2, 2),
  (983134, 1, 2),
  (988725, 2, 2),
  (990915, 1, 0),
  (997951, 3, 2),
  (1000999, 2, 0),
  (1002060, 1, 0),
  (1002769, 0, 0),
  (1007619, 1, 2),
  (1012847, 0, 0),
  (1013196, 0, 2),
  (1023155, 1, 2),
  (1024087, 2, 1),
  (1024166, 2, 2),
  (1034222, 3, 2),
  (1034444, 1, 1),
  (1034811, 1, 0),
  (1036550, 1, 2),
  (1038084, 1, 0),
  (1038606, 2, 2),
  (1039312, 3, 2),
  (1044272, 1, 2),
  (1045537, 0, 2),
  (1054385, 2, 1),
  (1058316, 0, 1),
  (1059223, 1, 2),
  (1066801, 1, 2),
  (1067681, 0, 0),
  (1070828, 3, 2),
  (1073230, 1, 1),
  (1074417, 3, 1),
  (1077925, 2, 2),
  (1079622, 1, 2),
  (1087354, 2, 0),
  (1087681, 1, 1),
  (1088973, 2, 0),
  (1089692, 3, 1),
  (1092530, 1, 0),
  (1092691, 2, 2),
  (1094472, 2, 0),
  (1097823, 0, 2),
  (1102756, 2, 1),
  (1105495, 3, 2),
  (1105543, 2, 0),
  (1108912, 0, 2),
  (1109938, 3, 1),
  (1116805, 2, 2),
  (1125687, 0, 0),
  (1125782, 1, 2),
  (1126614, 0, 1),
  (1129251, 0, 1),
  (1129428, 3, 0),
  (1129851, 0, 2),
  (1135952, 0, 2),
  (1140408, 3, 2),
  (1142964, 1, 2),
  (1146247, 3, 2),
  (1149756, 1, 2),
  (1150238, 3, 0),
  (1150567, 0, 1),
  (1151415, 1, 0),
  (1160327, 0, 0),
  (1163728, 1, 2),
  (1164600, 3, 1),
  (1164954, 3, 1),
  (1165386, 1, 1),
  (1173618, 2, 0),
  (1173823, 0, 0),
  (1174044, 0, 1),
  (1180488, 3, 0),
  (1182509, 0, 0),
  (1185008, 1, 2),
  (1185607, 2, 2),
  (1188611, 2, 1),
  (1195832, 1, 0),
  (1199892, 2, 0),
  (1202357, 2, 2),
  (1205037, 2, 2),
  (1217021, 1, 0),
  (1218206, 2, 2),
  (1231194, 2, 1),
  (1232450, 2, 1),
  (1234539, 2, 1),
  (1236089, 3, 2),
  (1250869, 0, 0),
  (1255094, 2, 1),
  (1257158, 3, 2),
  (1258431, 0, 1),
  (1268579, 3, 1),
  (1268676, 0, 0),
  (1271607, 2, 2),
  (1274733, 3, 0),
  (1275734, 1, 0),
  (1276652, 3, 1),
  (1277479, 2, 0),
  (1279647, 3, 2),
  (1280492, 1, 2),
  (1281243, 1, 1),
  (1289556, 1, 1),
  (1289692, 2, 0),
  (1291480, 1, 2),
  (1298695, 1, 1),
  (1303749, 1, 2),
  (1306920, 1, 1),
  (1313267, 0, 2),
  (1314383, 3, 2),
  (1314710, 0, 0),
  (1316991, 3, 2),
  (1318396, 1, 2),
  (1319004, 3, 0),
  (1325200, 1, 0),
  (1325473, 0, 2),
  (1325736, 2, 0),
  (1337739, 3, 2),
  (1339970, 0, 0),
  (1342344, 3, 2),
  (1343287, 2, 1),
  (1343679, 2, 0),
  (1349741, 0, 2),
  (1355121, 0, 2),
  (1356800, 1, 0),
  (1357863, 1, 1),
  (1362000, 1, 1),
  (1364079, 3, 2),
  (1368909, 2, 0),
  (1370912, 1, 1),
  (1374765, 1, 2),
  (1377279, 1, 2),
  (1379908, 1, 0),
  (1381795, 0, 0),
  (1381841, 0, 2),
  (1382277, 2, 2),
  (1385660, 3, 1),
  (1389327, 1, 0),
  (1394642, 0, 1),
  (1394890, 0, 1),
  (1399139, 0, 2),
  (1400955, 1, 1),
  (1402087, 3, 1),
  (1402719, 0, 2),
  (1404508, 3, 1),
  (1406019, 1, 1),
  (1413839, 2, 2),
  (1415216, 2, 0),
  (1421802, 2, 0),
  (1425136, 0, 0),
  (1429590, 1, 1),
  (1430384, 3, 0),
  (1434952, 3, 0),
  (1436724, 2, 1),
  (1437468, 2, 0),
  (1437514, 1, 1),
  (1444200, 0, 2),
  (1448600, 2, 1),
  (1450513, 2, 0),
  (1453614, 2, 2),
  (1460778, 2, 1),
  (1462891, 2, 2),
  (1464637, 1, 0),
  (1465212, 0, 0),
  (1465578, 0, 1),
  (1467867, 1, 1),
  (1471894, 2, 0),
  (1471909, 1, 2),
  (1474561, 1, 1),
  (1475646, 3, 2),
  (1483183, 1, 2),
  (1485902, 2, 0),
  (1486253, 3, 2),
  (1488430, 2, 2),
  (1491676, 2, 2),
  (1498672, 1, 2),
  (1500308, 2, 0),
  (1507236, 0, 0),
  (1507683, 3, 0),
  (1511835, 3, 1),
  (1511947, 0, 0),
  (1513896, 2, 2),
  (1515039, 2, 0),
  (1516274, 0, 1),
  (1517473, 0, 2),
  (1526584, 1, 2),
  (1531126, 2, 1),
  (1531941, 2, 0),
  (1534951, 2, 1),
  (1535855, 2, 0),
  (1535884, 1, 1),
  (1539965, 1, 0),
  (1542897, 0, 2),
  (1543766, 0, 0),
  (1553504, 0, 1),
  (1553884, 3, 2),
  (1557948, 0, 2),
  (1558394, 2, 1),
  (1558476, 1, 1),
  (1559404, 1, 2),
  (1562727, 1, 2),
  (1564043, 3, 2),
  (1565007, 3, 2),
  (1573100, 2, 1),
  (1578684, 1, 1),
  (1582597, 3, 1),
  (1589472, 3, 1),
  (1589533, 3, 0),
  (1591645, 2, 2),
  (1591923, 3, 0),
  (1592127, 3, 2),
  (1602243, 3, 0),
  (1605323, 3, 0),
  (1607739, 0, 1),
  (1611040, 1, 1),
  (1616462, 0, 1),
  (1617542, 1, 1),
  (1620985, 0, 0),
  (1621772, 0, 1),
  (1630311, 3, 1),
  (1631583, 0, 0),
  (1632127, 2, 1),
  (1632227, 1, 2),
  (1634108, 0, 1),
  (1638214, 0, 0),
  (1639123, 3, 2),
  (1645861, 3, 1),
  (1647010, 1, 2),
  (1648562, 3, 2),
  (1650491, 2, 1),
  (1650713, 1, 1),
  (1652778, 0, 1),
  (1661294, 1, 0),
  (1664102, 0, 1),
  (1667960, 1, 1),
  (1680581, 0, 0),
  (1682767, 2, 2),
  (1682864, 1, 1),
  (1685429, 0, 1),
  (1687652, 3, 2),
  (1690341, 0, 1),
  (1690662, 1, 2),
  (1691628, 0, 2),
  (1692461, 0, 1),
  (1697051, 0, 1),
  (1700605, 0, 2),
  (1702442, 3, 0),
  (1705626, 3, 0),
  (1718049, 3, 2),
  (1724126, 0, 2),
  (1728849, 3, 1),
  (1729252, 0, 0),
  (1729799, 3, 1),
  (1733476, 3, 0),
  (1739724, 3, 1),
  (1744595, 3, 1),
  (1745980, 0, 0),
  (1749594, 3, 1),
  (1754671, 2, 2),
  (1756820, 2, 0),
  (1757215, 0, 2),
  (1764213, 0, 1),
  (1766977, 2, 0),
  (1767190, 1, 1),
  (1769699, 2, 1),
  (1772187, 2, 1),
  (1772558, 2, 0),
  (1772832, 2, 2),
  (1775025, 1, 0),
  (1783814, 2, 2),
  (1784531, 1, 1),
  (1787535, 2, 0),
  (1788157, 3, 0),
  (1789284, 0, 2),
  (1794780, 0, 2),
  (1797331, 2, 0),
  (1803409, 3, 2),
  (1803501, 1, 1),
  (1804787, 3, 0),
  (1805946, 2, 2),
  (1810991, 3, 1),
  (1811946, 1, 0),
  (1813537, 3, 1),
  (1824389, 3, 2),
  (1825814, 3, 1),
  (1825986, 0, 2),
  (1826672, 1, 2),
  (1827521, 0, 0),
  (1829748, 1, 1),
  (1840266, 2, 0),
  (1844025, 1, 2),
  (1844653, 0, 0),
  (1848144, 3, 2),
  (1851153, 3, 0),
  (1854665, 2, 2),
  (1856413, 2, 0),
  (1858690, 2, 1),
  (1862205, 3, 2),
  (1862447, 0, 1),
  (1870148, 1, 1),
  (1870316, 2, 1),
  (1877527, 3, 2),
  (1880623, 2, 1),
  (1883845, 2, 2),
  (1884142, 0, 2),
  (1885306, 1, 0),
  (1886910, 3, 0),
  (1888534, 1, 1),
  (1889186, 3, 1),
  (1890302, 0, 2),
  (1893476, 2, 2),
  (1894583, 1, 0),
  (1894784, 1, 0),
  (1895332, 0, 1),
  (1895544, 2, 1),
  (1897015, 0, 0),
  (1898648, 1, 2),
  (1899836, 3, 2),
  (1902619, 2, 0),
  (1906514, 0, 1),
  (1907599, 2, 1),
  (1910715, 3, 1),
  (1917175, 1, 1),
  (1918224, 1, 1),
  (1920017, 2, 2),
  (1921594, 0, 2),
  (1923606, 0, 1),
  (1932982, 3, 2),
  (1933129, 0, 2),
  (1937779, 3, 2),
  (1947953, 2, 1),
  (1964988, 2, 1),
  (1966278, 2, 0),
  (1966998, 3, 0),
  (1968913, 1, 2),
  (1970524, 2, 1),
  (1977080, 0, 0),
  (1985325, 2, 0),
  (1985614, 1, 2),
  (1987807, 2, 1),
  (1989448, 1, 2),
  (1994136, 3, 2),
  (1994991, 0, 2),
  (2001895, 1, 1),
  (2003493, 0, 0),
  (2006794, 2, 0),
  (2011613, 1, 0),
  (2011726, 3, 2),
  (2012539, 2, 1),
  (2018988, 1, 0),
  (2023339, 2, 0),
  (2037195, 3, 2),
  (2042135, 1, 2),
  (2042659, 2, 2),
  (2043141, 3, 2),
  (2048083, 0, 1),
  (2051669, 0, 2),
  (2052077, 3, 2),
  (2054154, 1, 1),
  (2054247, 1, 1),
  (2057457, 0, 2),
  (2059513, 3, 2),
  (2064657, 0, 1),
  (2066952, 0, 1),
  (2068449, 1, 2),
  (2070153, 1, 1),
  (2071074, 1, 2),
  (2072299, 1, 0),
  (2075643, 1, 2),
  (2079343, 1, 1),
  (2081401, 3, 2),
  (2082832, 0, 2),
  (2096333, 3, 0),
  (2100644, 3, 1),
  (2100918, 1, 2),
  (2104084, 1, 2),
  (2123009, 0, 2),
  (2123017, 0, 0),
  (2123702, 2, 2),
  (2152758, 2, 0),
  (2153630, 2, 1),
  (2157414, 1, 0),
  (2164863, 3, 1),
  (2167342, 1, 2),
  (2169518, 3, 0),
  (2176299, 2, 0),
  (2176438, 1, 0),
  (2186061, 0, 0),
  (2186344, 3, 2),
  (2186915, 1, 1),
  (2191788, 1, 0),
  (2191866, 0, 2),
  (2195338, 1, 2),
  (2199054, 0, 1),
  (2201722, 1, 2),
  (2205375, 0, 1),
  (2205524, 1, 1),
  (2207763, 0, 2),
  (2208194, 0, 0),
  (2212734, 1, 0),
  (2215734, 1, 0),
  (2219417, 0, 0),
  (2220032, 2, 1),
  (2221444, 3, 2),
  (2223583, 0, 2),
  (2224898, 1, 2),
  (2227806, 1, 0),
  (2229577, 1, 0),
  (2233994, 3, 1),
  (2241986, 3, 2),
  (2242104, 0, 0),
  (2242771, 0, 1),
  (2250209, 1, 0),
  (2250954, 0, 2),
  (2250984, 3, 0),
  (2252436, 2, 2),
  (2253551, 3, 2),
  (2258217, 2, 2),
  (2260432, 1, 2),
  (2280439, 0, 1),
  (2285461, 1, 2),
  (2287279, 1, 1),
  (2287568, 3, 2),
  (2287693, 1, 0),
  (2293320, 3, 0),
  (2296976, 1, 1),
  (2298914, 1, 0),
  (2306496, 3, 2),
  (2308593, 2, 0),
  (2309186, 1, 0),
  (2311714, 1, 1),
  (2311741, 2, 1),
  (2316480, 2, 1),
  (2322033, 1, 2),
  (2322130, 3, 0),
  (2326521, 0, 0),
  (2326905, 1, 0),
  (2327114, 0, 0),
  (2330150, 0, 0),
  (2333387, 1, 2),
  (2333678, 0, 1),
  (2337839, 2, 2),
  (2346084, 2, 2),
  (2346137, 1, 0),
  (2353234, 2, 2),
  (2358679, 2, 1),
  (2358783, 3, 1),
  (2362311, 0, 1),
  (2363738, 1, 1),
  (2363843, 0, 0),
  (2366288, 0, 1),
  (2369218, 0, 1),
  (2369294, 1, 1),
  (2369977, 3, 1),
  (2375969, 1, 2),
  (2376236, 1, 1),
  (2379965, 0, 2),
  (2380716, 2, 2),
  (2390407, 2, 2),
  (2391857, 2, 1),
  (2393034, 2, 2),
  (2394528, 0, 0),
  (2399512, 3, 0),
  (2402421, 1, 2),
  (2419000, 1, 0),
  (2420383, 2, 1),
  (2421113, 2, 0),
  (2428132, 1, 1),
  (2431151, 2, 1),
  (2432763, 0, 1),
  (2432776, 2, 1),
  (2433159, 1, 2),
  (2437957, 3, 0),
  (2443396, 2, 1),
  (2443962, 3, 0),
  (2447436, 1, 2),
  (2454470, 0, 0),
  (2459328, 2, 1),
  (2470868, 0, 0),
  (2474067, 3, 2),
  (2479131, 2, 0),
  (2479217, 0, 2),
  (2479931, 1, 2),
  (2480750, 1, 1),
  (2481004, 1, 0),
  (2484009, 1, 1),
  (2488308, 3, 1),
  (2493172, 0, 1),
  (2503629, 1, 0),
  (2509448, 3, 1),
  (2512017, 3, 0),
  (2516771, 1, 0),
  (2519745, 3, 1),
  (2520547, 0, 1),
  (2521118, 2, 2),
  (2523353, 0, 1),
  (2523625, 3, 2),
  (2525470, 2, 1),
  (2531123, 1, 0),
  (2535769, 1, 1),
  (2537101, 3, 1),
  (2537798, 3, 2),
  (2539030, 2, 0),
  (2541385, 1, 0),
  (2550367, 3, 2),
  (2553173, 0, 1),
  (2554299, 3, 2),
  (2558127, 3, 0),
  (2566212, 3, 0),
  (2575047, 2, 1),
  (2577642, 1, 0),
  (2577715, 2, 2),
  (2583251, 0, 0),
  (2584983, 2, 2),
  (2594374, 1, 2),
  (2595795, 1, 1),
  (2598369, 0, 0),
  (2601645, 2, 1),
  (2606797, 3, 1),
  (2610066, 1, 0),
  (2613087, 3, 0),
  (2613795, 0, 1),
  (2614456, 1, 0),
  (2616161, 0, 2),
  (2617194, 2, 2),
  (2618684, 2, 1),
  (2627647, 1, 1),
  (2631533, 0, 1),
  (2632292, 1, 2),
  (2635115, 0, 0),
  (2643875, 3, 1),
  (2647208, 0, 1),
  (2650643, 0, 0),
  (2651321, 1, 2),
  (2658301, 1, 1),
  (2660437, 2, 0),
  (2661352, 0, 1),
  (2663763, 2, 0),
  (2664505, 0, 2),
  (2664656, 2, 0),
  (2665244, 2, 0),
  (2665454, 2, 0),
  (2666487, 2, 2),
  (2666749, 0, 1),
  (2666966, 1, 2),
  (2668093, 1, 0),
  (2669386, 0, 2),
  (2680146, 3, 2),
  (2681275, 2, 2),
  (2681756, 1, 0),
  (2683214, 1, 0),
  (2690056, 0, 2),
  (2691650, 3, 1),
  (2693823, 1, 2),
  (2695078, 3, 0),
  (2695752, 1, 1),
  (2701730, 1, 1),
  (2703663, 3, 2),
  (2707947, 0, 2),
  (2709460, 0, 1),
  (2714354, 2, 0),
  (2722694, 3, 2),
  (2726061, 0, 0),
  (2728324, 2, 2),
  (2728609, 3, 0),
  (2729302, 2, 0),
  (2729775, 2, 2),
  (2731433, 1, 0),
  (2735891, 2, 1),
  (2737363, 2, 0),
  (2739126, 2, 1),
  (2739990, 1, 0),
  (2740972, 1, 2),
  (2743863, 3, 0),
  (2745020, 3, 0),
  (2746355, 2, 2),
  (2749536, 0, 2),
  (2753466, 1, 0),
  (2757088, 3, 0),
  (2759982, 2, 2),
  (2762548, 1, 0),
  (2763011, 2, 2),
  (2766100, 1, 0),
  (2774673, 3, 0),
  (2776249, 2, 2),
  (2779044, 2, 0),
  (2783902, 1, 1),
  (2790511, 1, 2),
  (2797791, 0, 0),
  (2803523, 3, 1),
  (2811733, 1, 0),
  (2813520, 3, 0),
  (2813556, 3, 0),
  (2816664, 2, 0),
  (2825779, 3, 1),
  (2829756, 3, 1),
  (2831381, 0, 1),
  (2833256, 0, 0),
  (2836070, 3, 0),
  (2837006, 1, 1),
  (2837856, 0, 0),
  (2839189, 0, 2),
  (2840130, 1, 2),
  (2842211, 2, 2),
  (2842348, 1, 1),
  (2845241, 1, 2),
  (2846446, 0, 1),
  (2849911, 3, 1),
  (2852820, 1, 1),
  (2855913, 1, 0),
  (2865158, 1, 1),
  (2865337, 0, 2),
  (2865495, 1, 2),
  (2867555, 0, 1),
  (2871239, 1, 2),
  (2874126, 3, 2),
  (2881021, 3, 1),
  (2883011, 3, 0),
  (2883598, 1, 0),
  (2886323, 3, 1),
  (2894509, 3, 1),
  (2900544, 2, 2),
  (2904286, 2, 2),
  (2905610, 1, 0),
  (2906334, 1, 0),
  (2909737, 3, 2),
  (2913343, 0, 1),
  (2913569, 2, 2),
  (2914498, 3, 1),
  (2915891, 2, 0),
  (2920377, 3, 2),
  (2921003, 0, 0),
  (2921278, 3, 1),
  (2922080, 3, 2),
  (2933864, 2, 0),
  (2934962, 3, 1),
  (2940162, 3, 1),
  (2940950, 3, 2),
  (2942504, 1, 1),
  (2948849, 3, 0),
  (2949562, 1, 0),
  (2949910, 0, 2),
  (2949970, 1, 0),
  (2950446, 2, 2),
  (2950783, 3, 2),
  (2958868, 3, 1),
  (2962464, 3, 2),
  (2963925, 2, 0),
  (2970642, 1, 0),
  (2970841, 3, 0),
  (2974483, 3, 0),
  (2976762, 2, 1),
  (2986471, 0, 1),
  (2986541, 0, 1),
  (2988175, 1, 1),
  (2988985, 0, 0),
  (2989589, 3, 1),
  (2992469, 1, 2),
  (2994218, 2, 2),
  (2997498, 1, 0),
  (2997774, 2, 0),
  (3003186, 2, 1),
  (3005241, 0, 1),
  (3013992, 1, 1),
  (3015568, 3, 0),
  (3019335, 3, 2),
  (3020031, 1, 2),
  (3024387, 1, 0),
  (3031643, 3, 2),
  (3032219, 0, 2),
  (3038115, 0, 0),
  (3041286, 3, 0),
  (3041659, 0, 1),
  (3043747, 1, 2),
  (3046177, 2, 1),
  (3047770, 0, 1),
  (3048174, 0, 1),
  (3049222, 3, 0),
  (3057565, 1, 1),
  (3060586, 0, 2),
  (3061289, 1, 2),
  (3062514, 2, 1),
  (3074272, 3, 2),
  (3075310, 3, 0),
  (3077857, 1, 1),
  (3088614, 1, 0),
  (3092843, 1, 2),
  (3093646, 2, 1),
  (3094064, 1, 0),
  (3095271, 1, 2),
  (3098134, 1, 2),
  (3099459, 2, 0),
  (3105019, 1, 1),
  (3109228, 1, 2),
  (3111120, 1, 0),
  (3114765, 0, 2),
  (3122032, 1, 2),
  (3125938, 1, 2),
  (3127736, 2, 2),
  (3130689, 0, 2),
  (3132104, 1, 1),
  (3133251, 0, 1),
  (3133866, 3, 0),
  (3134036, 2, 2),
  (3137067, 1, 0),
  (3138516, 2, 1),
  (3143270, 0, 2),
  (3147281, 2, 0),
  (3151980, 0, 2),
  (3154332, 2, 0),
  (3155195, 2, 2),
  (3157589, 0, 0),
  (3159410, 0, 2),
  (3160024, 0, 1),
  (3161072, 2, 1),
  (3164141, 3, 0),
  (3169877, 1, 0),
  (3170419, 1, 0),
  (3174534, 1, 1),
  (3176381, 2, 2),
  (3177808, 0, 1),
  (3178400, 3, 1),
  (3179746, 0, 0),
  (3181306, 1, 2),
  (3184438, 3, 0),
  (3203822, 2, 2),
  (3207513, 3, 1),
  (3209217, 0, 0),
  (3209561, 3, 1),
  (3214429, 0, 0),
  (3214871, 0, 1),
  (3221027, 2, 2),
  (3222291, 1, 2),
  (3226205, 1, 2),
  (3226641, 3, 1),
  (3227281, 1, 2),
  (3231978, 1, 1),
  (3239221, 0, 2),
  (3242733, 2, 0),
  (3246434, 1, 1),
  (3251365, 3, 2),
  (3253618, 1, 2),
  (3256362, 2, 0),
  (3258344, 1, 0),
  (3262238, 0, 2),
  (3265810, 0, 2),
  (3266206, 2, 1),
  (3269009, 0, 0),
  (3270109, 0, 0),
  (3272373, 3, 1),
  (3272900, 2, 0),
  (3274506, 2, 2),
  (3276706, 0, 2),
  (3279548, 2, 1),
  (3286638, 1, 1),
  (3289640, 1, 0),
  (3290924, 0, 0),
  (3296077, 0, 2),
  (3299013, 3, 0),
  (3303060, 3, 2),
  (3303845, 1, 2),
  (3307769, 1, 0),
  (3307852, 3, 0),
  (3308132, 3, 2),
  (3311588, 2, 2),
  (3312433, 1, 0),
  (3317287, 2, 1),
  (3318022, 0, 1),
  (3324478, 0, 2),
  (3325362, 1, 0),
  (3326685, 0, 1),
  (3332162, 3, 1),
  (3332277, 3, 1),
  (3337405, 2, 1),
  (3339235, 2, 0),
  (3340462, 0, 2),
  (3346794, 2, 1),
  (3348557, 0, 0),
  (3351872, 2, 0),
  (3353085, 1, 0),
  (3353848, 0, 1),
  (3354245, 0, 0),
  (3356514, 1, 2),
  (3357368, 0, 1),
  (3358227, 3, 1),
  (3359564, 1, 2),
  (3361184, 2, 2),
  (3361891, 3, 1),
  (3373300, 0, 0),
  (3375050, 0, 1),
  (3379586, 3, 0),
  (3392030, 2, 2),
  (3392193, 3, 2),
  (3395124, 2, 2),
  (3399255, 1, 1),
  (3399990, 2, 2),
  (3402356, 1, 2),
  (3403529, 2, 0),
  (3409068, 0, 0),
  (3409275, 0, 2),
  (3411593, 3, 2),
  (3413114, 1, 1),
  (3413425, 1, 1),
  (3414429, 1, 1),
  (3420067, 2, 2),
  (3421826, 2, 2),
  (3422409, 1, 0),
  (3422736, 2, 0),
  (3423351, 0, 1),
  (3423828, 2, 0),
  (3431716, 3, 2),
  (3432475, 1, 2),
  (3435289, 1, 1),
  (3439946, 3, 1),
  (3440034, 0, 0),
  (3441768, 3, 0),
  (3442077, 1, 2),
  (3442823, 3, 1),
  (3446068, 1, 2),
  (3448589, 3, 2),
  (3450127, 2, 2),
  (3455302, 1, 2),
  (3457218, 2, 2),
  (3462619, 3, 0),
  (3464667, 0, 1),
  (3465219, 0, 1),
  (3465419, 1, 1),
  (3470823, 3, 1),
  (3471404, 1, 0),
  (3472996, 0, 1),
  (3480147, 0, 0),
  (3481768, 2, 2),
  (3487016, 2, 0),
  (3488039, 3, 2),
  (3490814, 2, 0),
  (3492147, 1, 1),
  (3495835, 3, 2),
  (3499583, 2, 1),
  (3500915, 0, 0),
  (3503687, 1, 2),
  (3503954, 1, 0),
  (3506042, 3, 1),
  (3506996, 3, 1),
  (3507879, 2, 2),
  (3508726, 1, 2),
  (3509965, 0, 1),
  (3510406, 1, 1),
  (3513835, 0, 2),
  (3514354, 0, 1),
  (3529788, 3, 2),
  (3531080, 2, 0),
  (3531152, 2, 2),
  (3536927, 1, 0),
  (3538731, 2, 2),
  (3551519, 2, 1),
  (3554757, 2, 2),
  (3556195, 2, 2),
  (3556942, 0, 0),
  (3557753, 0, 2),
  (3563476, 0, 2),
  (3566101, 0, 1),
  (3571832, 2, 2),
  (3575727, 1, 2),
  (3578110, 3, 1),
  (3578315, 2, 2),
  (3583723, 2, 1),
  (3585799, 2, 2),
  (3587093, 1, 0),
  (3587806, 3, 2),
  (3592185, 1, 0),
  (3592913, 1, 1),
  (3595516, 3, 1),
])