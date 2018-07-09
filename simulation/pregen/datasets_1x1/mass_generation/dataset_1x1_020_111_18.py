from util import *
schedule = deque([
  (8859, 5, 2),
  (14479, 6, 0),
  (15355, 7, 4),
  (28776, 0, 7),
  (28984, 6, 7),
  (29110, 6, 3),
  (34826, 0, 4),
  (35177, 7, 7),
  (44144, 2, 4),
  (48499, 2, 3),
  (49772, 1, 7),
  (49858, 3, 2),
  (52624, 1, 0),
  (54034, 3, 3),
  (57658, 1, 0),
  (58325, 3, 2),
  (60983, 4, 3),
  (61798, 5, 3),
  (63205, 5, 3),
  (67068, 0, 7),
  (74017, 1, 0),
  (75008, 4, 3),
  (76429, 4, 7),
  (82833, 4, 1),
  (84007, 0, 0),
  (91116, 6, 7),
  (92486, 3, 6),
  (93150, 2, 4),
  (94658, 5, 2),
  (94807, 0, 3),
  (95794, 3, 3),
  (95805, 2, 5),
  (96407, 7, 4),
  (96886, 2, 2),
  (99050, 2, 3),
  (104220, 3, 6),
  (105725, 5, 3),
  (106016, 6, 0),
  (107404, 0, 0),
  (107900, 1, 0),
  (108283, 4, 1),
  (109139, 6, 0),
  (112375, 0, 0),
  (115964, 1, 5),
  (116343, 7, 3),
  (117714, 3, 2),
  (122772, 2, 3),
  (130566, 1, 0),
  (134134, 2, 5),
  (138016, 6, 4),
  (141330, 1, 4),
  (142693, 3, 0),
  (144544, 3, 7),
  (145142, 3, 7),
  (146408, 7, 0),
  (147569, 4, 6),
  (151887, 0, 4),
  (153572, 6, 6),
  (155507, 6, 3),
  (163925, 3, 7),
  (165355, 3, 2),
  (165669, 0, 7),
  (165712, 3, 7),
  (167001, 5, 0),
  (169112, 7, 4),
  (170162, 6, 4),
  (170634, 4, 5),
  (170970, 3, 5),
  (172901, 3, 7),
  (176464, 2, 5),
  (187415, 1, 0),
  (187537, 7, 0),
  (189515, 4, 7),
  (194860, 2, 5),
  (197750, 6, 0),
  (209238, 2, 6),
  (212496, 1, 4),
  (214887, 2, 3),
  (219878, 5, 4),
  (221999, 3, 3),
  (222009, 3, 3),
  (225887, 1, 4),
  (226597, 0, 0),
  (230057, 1, 2),
  (236218, 4, 6),
  (236777, 2, 6),
  (241113, 5, 6),
  (245302, 0, 0),
  (245753, 6, 7),
  (245781, 7, 3),
  (251394, 1, 0),
  (252788, 4, 7),
  (253517, 5, 7),
  (257684, 4, 7),
  (257859, 0, 0),
  (257871, 1, 2),
  (261769, 1, 0),
  (266186, 0, 0),
  (268678, 1, 3),
  (269959, 0, 7),
  (270999, 6, 4),
  (271150, 0, 7),
  (271625, 1, 7),
  (274290, 1, 3),
  (278512, 7, 6),
  (278825, 3, 6),
  (279227, 1, 0),
  (280957, 6, 0),
  (291396, 3, 6),
  (296853, 0, 4),
  (301410, 6, 7),
  (302819, 6, 0),
  (309683, 5, 3),
  (310424, 1, 0),
  (312060, 5, 6),
  (316244, 3, 3),
  (318995, 1, 0),
  (336568, 2, 7),
  (337462, 7, 0),
  (341266, 1, 0),
  (347670, 2, 3),
  (350767, 3, 3),
  (352311, 6, 3),
  (354219, 6, 0),
  (366765, 4, 2),
  (367480, 1, 5),
  (368717, 3, 3),
  (370526, 7, 4),
  (373870, 1, 3),
  (374691, 0, 0),
  (374716, 0, 3),
  (377859, 4, 7),
  (378227, 4, 2),
  (381881, 6, 7),
  (383143, 4, 3),
  (384705, 6, 4),
  (385755, 0, 3),
  (387036, 7, 6),
  (390474, 1, 0),
  (391205, 0, 7),
  (393697, 0, 7),
  (397790, 6, 3),
  (398857, 7, 7),
  (404208, 6, 0),
  (405964, 7, 3),
  (409894, 5, 6),
  (412090, 4, 6),
  (414274, 1, 3),
  (417502, 7, 0),
  (419282, 2, 3),
  (420204, 5, 3),
  (424470, 7, 3),
  (427227, 6, 5),
  (432759, 2, 6),
  (433147, 6, 0),
  (434695, 4, 2),
  (443972, 4, 6),
  (452738, 3, 6),
  (454529, 2, 3),
  (454744, 3, 3),
  (458705, 6, 0),
  (459987, 3, 6),
  (463226, 3, 4),
  (463460, 1, 0),
  (463959, 0, 0),
  (465853, 0, 7),
  (470739, 6, 0),
  (471806, 4, 0),
  (473566, 6, 0),
  (474055, 0, 0),
  (475387, 5, 7),
  (479404, 6, 4),
  (484183, 6, 0),
  (487710, 3, 6),
  (489866, 3, 6),
  (491036, 3, 5),
  (491892, 2, 0),
  (492999, 7, 0),
  (495685, 3, 5),
  (497810, 5, 2),
  (500052, 0, 7),
  (500103, 1, 3),
  (501620, 6, 0),
  (501662, 2, 0),
  (502549, 4, 6),
  (502669, 6, 7),
  (507726, 6, 0),
  (508124, 5, 3),
  (511922, 0, 0),
  (512112, 0, 0),
  (513015, 3, 3),
  (514079, 3, 3),
  (514433, 1, 4),
  (516632, 4, 3),
  (531994, 5, 5),
  (535126, 2, 1),
  (537598, 1, 4),
  (538608, 0, 6),
  (539711, 0, 6),
  (539793, 3, 3),
  (540379, 0, 4),
  (542148, 6, 0),
  (543799, 2, 6),
  (545755, 6, 6),
  (546409, 3, 3),
  (557404, 6, 0),
  (560774, 4, 2),
  (561085, 2, 6),
  (561481, 6, 2),
  (562612, 0, 3),
  (563339, 1, 4),
  (565701, 1, 7),
  (567304, 4, 3),
  (569246, 7, 4),
  (570848, 3, 3),
  (574219, 6, 5),
  (576797, 7, 7),
  (588015, 4, 3),
  (588562, 5, 3),
  (591598, 1, 0),
  (597678, 6, 4),
  (601324, 6, 0),
  (601792, 5, 2),
  (602445, 3, 2),
  (602536, 3, 3),
  (610725, 4, 3),
  (611255, 0, 1),
  (617886, 3, 3),
  (622498, 1, 7),
  (622771, 5, 3),
  (622784, 3, 4),
  (627221, 7, 7),
  (627484, 4, 7),
  (630811, 3, 4),
  (632863, 7, 7),
  (633028, 4, 2),
  (635865, 2, 5),
  (637694, 3, 6),
  (639888, 0, 0),
  (642763, 5, 3),
  (643202, 7, 6),
  (643308, 6, 0),
  (644183, 6, 0),
  (651368, 4, 3),
  (651708, 1, 4),
  (652159, 1, 7),
  (656364, 7, 3),
  (658974, 5, 3),
  (660736, 2, 3),
  (660969, 6, 1),
  (664377, 1, 0),
  (664539, 6, 7),
  (672976, 6, 0),
  (674319, 4, 3),
  (675455, 5, 4),
  (675563, 4, 3),
  (677148, 7, 0),
  (677672, 3, 3),
  (679166, 1, 3),
  (679454, 4, 3),
  (683179, 5, 7),
  (685414, 3, 3),
  (685826, 1, 0),
  (698706, 7, 0),
  (699713, 0, 1),
  (702913, 3, 3),
  (703723, 6, 2),
  (704012, 3, 2),
  (704640, 5, 2),
  (706705, 0, 4),
  (708905, 4, 2),
  (716591, 4, 3),
  (723292, 1, 0),
  (724083, 7, 0),
  (724385, 1, 3),
  (725693, 5, 2),
  (730713, 1, 0),
  (731802, 0, 2),
  (732370, 0, 1),
  (734515, 1, 3),
  (746578, 4, 2),
  (747751, 2, 3),
  (754308, 1, 5),
  (754853, 4, 3),
  (756655, 5, 3),
  (765557, 5, 3),
  (767449, 7, 0),
  (767476, 5, 2),
  (774578, 5, 4),
  (778345, 1, 0),
  (782552, 3, 3),
  (784646, 4, 3),
  (792800, 0, 0),
  (794705, 0, 0),
  (799574, 5, 2),
  (800786, 1, 4),
  (802411, 0, 1),
  (803796, 2, 6),
  (805427, 2, 0),
  (809734, 0, 0),
  (813031, 5, 5),
  (813451, 5, 3),
  (814591, 0, 7),
  (818255, 0, 7),
  (821218, 1, 0),
  (822972, 7, 7),
  (823193, 6, 2),
  (826358, 1, 0),
  (826861, 7, 4),
  (829423, 6, 7),
  (833846, 6, 0),
  (837703, 5, 5),
  (841364, 6, 0),
  (844621, 5, 3),
  (848572, 5, 3),
  (856278, 3, 6),
  (858093, 1, 0),
  (860174, 6, 5),
  (862668, 0, 3),
  (862923, 3, 3),
  (864283, 4, 2),
  (865565, 4, 3),
  (868835, 0, 7),
  (871802, 1, 5),
  (876459, 6, 2),
  (879275, 4, 3),
  (886146, 5, 3),
  (890736, 6, 6),
  (891508, 6, 7),
  (903986, 4, 7),
  (904148, 3, 3),
  (921555, 7, 3),
  (922013, 4, 5),
  (925184, 5, 3),
  (926292, 6, 4),
  (927159, 3, 7),
  (928800, 4, 7),
  (929220, 6, 3),
  (932783, 3, 3),
  (934899, 3, 3),
  (936274, 3, 3),
  (944973, 1, 7),
  (958785, 1, 3),
  (960619, 0, 0),
  (962852, 7, 0),
  (963611, 7, 0),
  (965316, 2, 0),
  (970263, 5, 5),
  (972568, 6, 2),
  (974501, 7, 0),
  (977836, 4, 7),
  (979358, 2, 6),
  (981651, 7, 1),
  (984966, 7, 0),
  (985933, 2, 0),
  (987527, 6, 0),
  (990013, 5, 0),
  (992077, 4, 3),
  (997742, 1, 0),
  (998388, 4, 3),
  (1001272, 2, 3),
  (1007842, 3, 3),
  (1008039, 2, 6),
  (1013440, 5, 7),
  (1015050, 2, 5),
  (1024223, 1, 7),
  (1025334, 7, 2),
  (1028240, 7, 4),
  (1028446, 3, 5),
  (1031255, 4, 6),
  (1032737, 2, 3),
  (1033784, 6, 4),
  (1037863, 4, 2),
  (1038991, 6, 0),
  (1039427, 3, 0),
  (1040125, 0, 7),
  (1051176, 4, 3),
  (1055555, 1, 0),
  (1056424, 7, 0),
  (1061952, 0, 2),
  (1065263, 4, 2),
  (1065763, 6, 4),
  (1066077, 2, 2),
  (1068637, 0, 0),
  (1069730, 4, 3),
  (1071229, 0, 0),
  (1073302, 2, 2),
  (1073911, 5, 3),
  (1075145, 4, 0),
  (1075797, 1, 7),
  (1076043, 4, 3),
  (1078633, 6, 3),
  (1078815, 4, 3),
  (1081872, 6, 0),
  (1082727, 6, 7),
  (1088298, 0, 3),
  (1089937, 2, 2),
  (1092073, 4, 2),
  (1092394, 7, 4),
  (1093180, 4, 2),
  (1094189, 1, 7),
  (1095783, 1, 0),
  (1101326, 1, 7),
  (1104396, 1, 4),
  (1105696, 4, 2),
  (1106356, 0, 4),
  (1112531, 6, 3),
  (1116262, 3, 2),
  (1119029, 0, 0),
  (1123210, 6, 4),
  (1126192, 2, 4),
  (1126887, 7, 3),
  (1127020, 4, 6),
  (1134462, 1, 0),
  (1135126, 3, 2),
  (1135796, 1, 0),
  (1146611, 1, 0),
  (1150164, 4, 7),
  (1151831, 2, 2),
  (1153642, 1, 7),
  (1153882, 7, 6),
  (1157343, 2, 2),
  (1161958, 3, 3),
  (1163063, 3, 3),
  (1163671, 6, 0),
  (1165533, 7, 0),
  (1172709, 7, 7),
  (1174458, 1, 0),
  (1180661, 7, 4),
  (1190577, 4, 4),
  (1193593, 5, 7),
  (1197737, 2, 1),
  (1199037, 5, 7),
  (1201419, 0, 0),
  (1201732, 3, 6),
  (1206467, 5, 3),
  (1207708, 1, 4),
  (1214220, 2, 4),
  (1215509, 1, 0),
  (1222402, 6, 0),
  (1222765, 0, 3),
  (1227326, 7, 6),
  (1229036, 5, 3),
  (1229659, 5, 3),
  (1239046, 3, 3),
  (1247007, 5, 3),
  (1248089, 1, 3),
  (1250462, 5, 3),
  (1251798, 0, 0),
  (1254071, 6, 5),
  (1255865, 4, 7),
  (1256696, 7, 4),
  (1257497, 7, 0),
  (1259998, 2, 7),
  (1261621, 6, 7),
  (1261706, 7, 1),
  (1262618, 7, 4),
  (1268476, 7, 0),
  (1270471, 2, 5),
  (1274590, 0, 3),
  (1276633, 6, 5),
  (1285673, 7, 7),
  (1289022, 1, 0),
  (1290011, 6, 7),
  (1292786, 0, 0),
  (1295477, 3, 3),
  (1298420, 0, 3),
  (1299793, 4, 3),
  (1300807, 3, 3),
  (1303839, 4, 3),
  (1309687, 0, 3),
  (1318463, 1, 0),
  (1319273, 4, 6),
  (1321841, 7, 7),
  (1321868, 0, 0),
  (1323438, 5, 5),
  (1327535, 6, 7),
  (1341573, 6, 0),
  (1350153, 0, 0),
  (1352281, 0, 2),
  (1352779, 4, 6),
  (1355055, 3, 6),
  (1356540, 1, 2),
  (1356992, 4, 6),
  (1359626, 6, 0),
  (1362560, 5, 3),
  (1365358, 0, 2),
  (1366416, 1, 0),
  (1367247, 2, 3),
  (1368746, 0, 7),
  (1369524, 7, 5),
  (1370129, 0, 2),
  (1370536, 0, 5),
  (1376450, 5, 0),
  (1380652, 6, 3),
  (1381227, 0, 7),
  (1382035, 2, 6),
  (1385828, 6, 5),
  (1385979, 1, 2),
  (1392681, 2, 3),
  (1396141, 6, 4),
  (1398133, 7, 0),
  (1400851, 5, 7),
  (1411294, 2, 7),
  (1414115, 6, 4),
  (1416691, 5, 3),
  (1420103, 3, 0),
  (1421689, 6, 0),
  (1422250, 4, 3),
  (1422736, 1, 0),
  (1422763, 5, 7),
  (1424070, 5, 3),
  (1430812, 4, 3),
  (1431213, 6, 1),
  (1431699, 5, 5),
  (1434987, 6, 0),
  (1441399, 2, 2),
  (1446094, 1, 3),
  (1446736, 1, 0),
  (1447329, 1, 0),
  (1452931, 1, 2),
  (1454485, 3, 3),
  (1454943, 2, 1),
  (1456243, 2, 1),
  (1477344, 2, 6),
  (1481409, 3, 2),
  (1483552, 0, 0),
  (1484731, 6, 4),
  (1489661, 5, 3),
  (1498912, 4, 2),
  (1509357, 7, 2),
  (1516066, 6, 3),
  (1518148, 0, 7),
  (1521817, 6, 2),
  (1523333, 5, 3),
  (1526719, 0, 2),
  (1531680, 3, 7),
  (1534772, 3, 2),
  (1544142, 7, 0),
  (1546194, 2, 6),
  (1555089, 5, 3),
  (1555926, 1, 1),
  (1557197, 1, 3),
  (1558141, 5, 7),
  (1562684, 4, 2),
  (1563947, 3, 3),
  (1565000, 7, 3),
  (1565052, 6, 0),
  (1565127, 2, 2),
  (1566962, 6, 7),
  (1570045, 6, 7),
  (1572059, 5, 3),
  (1576526, 0, 3),
  (1579608, 4, 3),
  (1582895, 5, 3),
  (1583222, 1, 4),
  (1591856, 6, 3),
  (1593552, 4, 7),
  (1600169, 6, 0),
  (1600702, 2, 2),
  (1608319, 7, 3),
  (1617066, 2, 3),
  (1621438, 4, 6),
  (1625575, 5, 3),
  (1625668, 3, 6),
  (1627369, 2, 0),
  (1628728, 2, 7),
  (1631677, 1, 5),
  (1637211, 4, 3),
  (1642247, 2, 4),
  (1643880, 6, 1),
  (1644808, 5, 3),
  (1645819, 0, 4),
  (1646867, 2, 3),
  (1649743, 4, 4),
  (1650221, 2, 3),
  (1650243, 5, 6),
  (1653672, 7, 0),
  (1658121, 6, 0),
  (1664177, 1, 0),
  (1665767, 3, 2),
  (1669518, 0, 4),
  (1670248, 6, 1),
  (1670554, 2, 3),
  (1670623, 5, 7),
  (1670849, 6, 0),
  (1670982, 1, 2),
  (1672417, 7, 0),
  (1672897, 0, 3),
  (1676645, 6, 0),
  (1680403, 2, 3),
  (1688310, 3, 2),
  (1688562, 5, 6),
  (1693640, 2, 2),
  (1695302, 0, 0),
  (1702512, 2, 3),
  (1705978, 6, 0),
  (1706951, 5, 3),
  (1708450, 1, 0),
  (1712106, 6, 7),
  (1713918, 1, 3),
  (1719558, 6, 0),
  (1722553, 6, 3),
  (1723090, 4, 3),
  (1729615, 1, 6),
  (1734802, 7, 5),
  (1735119, 2, 7),
  (1738898, 5, 3),
  (1739125, 5, 3),
  (1745734, 6, 3),
  (1751355, 4, 1),
  (1753071, 0, 1),
  (1755491, 6, 4),
  (1756140, 5, 1),
  (1763160, 7, 7),
  (1763937, 5, 3),
  (1765545, 3, 3),
  (1766054, 6, 0),
  (1767700, 1, 0),
  (1775014, 7, 4),
  (1777306, 1, 7),
  (1778739, 2, 2),
  (1780946, 2, 3),
  (1788399, 1, 2),
  (1791446, 2, 3),
  (1793739, 4, 2),
  (1801182, 7, 4),
  (1804313, 1, 4),
  (1806866, 4, 4),
  (1812644, 5, 3),
  (1818720, 1, 0),
  (1820869, 0, 0),
  (1822577, 3, 6),
  (1823568, 6, 0),
  (1825726, 0, 3),
  (1826804, 7, 0),
  (1826854, 1, 0),
  (1834525, 6, 7),
  (1840710, 4, 2),
  (1842052, 0, 3),
  (1849075, 3, 0),
  (1850618, 7, 3),
  (1851971, 7, 2),
  (1853343, 1, 0),
  (1857624, 3, 2),
  (1865728, 2, 5),
  (1866237, 2, 6),
  (1873643, 1, 4),
  (1874925, 5, 6),
  (1877246, 1, 3),
  (1877800, 3, 3),
  (1879017, 0, 0),
  (1885459, 7, 5),
  (1896036, 0, 0),
  (1896255, 4, 7),
  (1897330, 0, 0),
  (1904106, 3, 3),
  (1906702, 1, 0),
  (1907039, 6, 4),
  (1911957, 5, 6),
  (1916689, 2, 4),
  (1917105, 3, 3),
  (1917545, 3, 0),
  (1918834, 5, 2),
  (1927739, 4, 6),
  (1928978, 7, 7),
  (1930454, 4, 3),
  (1930537, 1, 5),
  (1931668, 3, 2),
  (1931752, 3, 3),
  (1933024, 6, 0),
  (1936706, 7, 0),
  (1940901, 0, 7),
  (1957119, 1, 3),
  (1958969, 5, 3),
  (1965702, 6, 0),
  (1974759, 3, 3),
  (1976726, 7, 4),
  (1980494, 0, 7),
  (1981506, 6, 4),
  (1983572, 3, 3),
  (1988576, 4, 3),
  (1991702, 2, 5),
  (1994633, 4, 3),
  (2000660, 5, 3),
  (2003209, 4, 4),
  (2004071, 6, 5),
  (2012021, 1, 0),
  (2014052, 2, 3),
  (2015757, 3, 7),
  (2027410, 4, 3),
  (2030313, 6, 3),
  (2034052, 3, 7),
  (2035164, 0, 3),
  (2036197, 0, 3),
  (2041283, 7, 3),
  (2045699, 2, 7),
  (2050132, 5, 7),
  (2051930, 7, 0),
  (2055350, 3, 3),
  (2056386, 1, 7),
  (2056616, 5, 3),
  (2061777, 5, 0),
  (2067029, 3, 7),
  (2068513, 3, 6),
  (2075605, 3, 0),
  (2089390, 6, 0),
  (2096285, 3, 3),
  (2099055, 7, 0),
  (2105330, 4, 6),
  (2105412, 7, 0),
  (2111307, 7, 0),
  (2117846, 6, 4),
  (2120153, 0, 7),
  (2121152, 1, 0),
  (2124956, 6, 4),
  (2131504, 5, 3),
  (2132539, 3, 0),
  (2138238, 3, 3),
  (2142131, 4, 7),
  (2144342, 5, 2),
  (2148048, 5, 1),
  (2148322, 5, 3),
  (2156174, 2, 3),
  (2157683, 6, 0),
  (2157823, 5, 3),
  (2159025, 5, 0),
  (2169774, 3, 3),
  (2171887, 3, 3),
  (2174858, 7, 7),
  (2176567, 5, 6),
  (2178801, 6, 1),
  (2183280, 7, 3),
  (2183929, 7, 1),
  (2195598, 1, 0),
  (2196816, 6, 3),
  (2197967, 6, 0),
  (2199721, 6, 0),
  (2208356, 5, 2),
  (2209418, 2, 3),
  (2219462, 7, 0),
  (2223462, 4, 3),
  (2223949, 3, 3),
  (2226338, 4, 3),
  (2229632, 2, 5),
  (2231153, 7, 4),
  (2232915, 7, 2),
  (2236612, 5, 2),
  (2238855, 5, 6),
  (2239670, 5, 3),
  (2248373, 4, 2),
  (2248491, 7, 3),
  (2250201, 5, 4),
  (2252661, 3, 3),
  (2256406, 5, 4),
  (2259623, 7, 5),
  (2270948, 2, 3),
  (2273902, 6, 3),
  (2278764, 0, 7),
  (2280811, 2, 1),
  (2301667, 1, 7),
  (2302259, 2, 3),
  (2307157, 3, 3),
  (2307887, 4, 7),
  (2308265, 1, 6),
  (2314197, 7, 0),
  (2314776, 3, 7),
  (2320560, 6, 0),
  (2322504, 3, 3),
  (2324059, 7, 7),
  (2324802, 0, 3),
  (2329961, 4, 7),
  (2330570, 3, 6),
  (2331386, 4, 7),
  (2333294, 3, 3),
  (2334833, 5, 2),
  (2336272, 6, 0),
  (2341304, 5, 2),
  (2342510, 0, 7),
  (2344213, 4, 3),
  (2344507, 3, 3),
  (2344983, 4, 6),
  (2346148, 3, 7),
  (2346785, 5, 3),
  (2347115, 3, 3),
  (2350395, 1, 4),
  (2353620, 2, 6),
  (2355615, 4, 6),
  (2356667, 3, 3),
  (2358926, 3, 7),
  (2359323, 2, 3),
  (2359690, 3, 2),
  (2366114, 1, 1),
  (2366587, 6, 0),
  (2367803, 6, 0),
  (2374696, 1, 3),
  (2375661, 2, 6),
  (2378212, 5, 3),
  (2379750, 3, 6),
  (2379900, 4, 3),
  (2382304, 6, 2),
  (2382657, 5, 7),
  (2382945, 2, 3),
  (2385836, 2, 3),
  (2387514, 5, 7),
  (2389130, 4, 3),
  (2389406, 7, 3),
  (2395845, 0, 4),
  (2398860, 2, 5),
  (2399943, 1, 7),
  (2406806, 2, 2),
  (2409841, 2, 6),
  (2411784, 5, 2),
  (2412798, 5, 2),
  (2414232, 7, 7),
  (2416020, 1, 4),
  (2416503, 1, 5),
  (2420593, 7, 4),
  (2423316, 3, 3),
  (2423429, 5, 2),
  (2428332, 6, 7),
  (2428347, 4, 1),
  (2429462, 0, 0),
  (2434047, 6, 0),
  (2439883, 1, 0),
  (2439959, 0, 7),
  (2444638, 6, 0),
  (2446191, 2, 2),
  (2449213, 7, 0),
  (2454677, 3, 5),
  (2457672, 1, 7),
  (2458435, 0, 7),
  (2461377, 4, 3),
  (2462494, 5, 3),
  (2468796, 6, 0),
  (2469904, 4, 7),
  (2470317, 3, 7),
  (2470578, 0, 0),
  (2472413, 1, 2),
  (2472655, 1, 7),
  (2478433, 1, 0),
  (2482506, 3, 7),
  (2490840, 3, 5),
  (2493877, 7, 0),
  (2495278, 3, 2),
  (2496826, 5, 3),
  (2512011, 6, 0),
  (2512331, 6, 0),
  (2516258, 7, 7),
  (2518130, 6, 5),
  (2519869, 1, 7),
  (2520647, 1, 0),
  (2520758, 7, 0),
  (2523720, 0, 0),
  (2530556, 1, 0),
  (2535818, 6, 0),
  (2541911, 0, 0),
  (2545049, 6, 7),
  (2551297, 1, 0),
  (2551562, 4, 4),
  (2551595, 6, 7),
  (2553582, 3, 3),
  (2557015, 7, 7),
  (2560008, 0, 4),
  (2563845, 6, 1),
  (2570454, 6, 4),
  (2571458, 1, 4),
  (2571885, 3, 1),
  (2576967, 3, 7),
  (2582312, 4, 2),
  (2584797, 1, 7),
  (2588494, 5, 7),
  (2589044, 5, 2),
  (2590161, 5, 3),
  (2593383, 3, 6),
  (2596514, 3, 3),
  (2600352, 1, 4),
  (2608524, 5, 0),
  (2616702, 4, 2),
  (2619315, 3, 3),
  (2621121, 1, 7),
  (2625209, 5, 7),
  (2627366, 4, 7),
  (2627943, 7, 4),
  (2628342, 4, 3),
  (2628584, 4, 7),
  (2630627, 0, 0),
  (2636843, 7, 3),
  (2651783, 7, 7),
  (2655177, 7, 2),
  (2656668, 5, 7),
  (2657096, 7, 4),
  (2657420, 3, 3),
  (2662514, 1, 3),
  (2669594, 7, 7),
  (2670783, 7, 5),
  (2673940, 2, 2),
  (2679980, 1, 0),
  (2681964, 2, 6),
  (2681975, 1, 0),
  (2683811, 4, 6),
  (2687972, 2, 3),
  (2696315, 2, 3),
  (2706479, 2, 7),
  (2707868, 7, 0),
  (2708712, 1, 0),
  (2711403, 2, 3),
  (2712783, 0, 0),
  (2716822, 1, 2),
  (2718047, 2, 2),
  (2724007, 5, 3),
  (2724320, 3, 3),
  (2724322, 0, 0),
  (2724336, 5, 3),
  (2732675, 5, 3),
  (2735385, 2, 6),
  (2737858, 6, 3),
  (2740545, 6, 5),
  (2741974, 2, 3),
  (2742759, 6, 3),
  (2743943, 2, 2),
  (2747468, 6, 5),
  (2749628, 5, 2),
  (2752989, 6, 0),
  (2754419, 6, 4),
  (2755843, 3, 3),
  (2755884, 1, 0),
  (2758656, 3, 3),
  (2764662, 2, 3),
  (2765730, 7, 0),
  (2777060, 1, 7),
  (2779045, 1, 0),
  (2780627, 6, 0),
  (2784258, 3, 5),
  (2785771, 3, 7),
  (2788114, 0, 3),
  (2788133, 7, 7),
  (2791054, 6, 4),
  (2792403, 7, 4),
  (2793911, 5, 2),
  (2794292, 0, 4),
  (2797912, 5, 3),
  (2798380, 3, 7),
  (2800267, 5, 2),
  (2800518, 2, 3),
  (2803274, 0, 0),
  (2805191, 6, 7),
  (2806639, 0, 3),
  (2815875, 5, 0),
  (2819880, 4, 3),
  (2824629, 7, 0),
  (2825192, 2, 0),
  (2825588, 2, 1),
  (2827536, 6, 4),
  (2831651, 5, 3),
  (2837182, 2, 1),
  (2839918, 6, 6),
  (2841458, 1, 0),
  (2846195, 1, 0),
  (2849895, 7, 6),
  (2852906, 7, 2),
  (2854920, 7, 4),
  (2856412, 6, 0),
  (2856775, 6, 7),
  (2857507, 6, 0),
  (2858742, 0, 4),
  (2859153, 3, 6),
  (2859296, 5, 6),
  (2863769, 7, 4),
  (2868680, 5, 1),
  (2870524, 1, 0),
  (2870749, 7, 6),
  (2873801, 6, 3),
  (2876431, 7, 5),
  (2876870, 5, 2),
  (2877114, 3, 3),
  (2878503, 5, 6),
  (2881864, 6, 0),
  (2882620, 3, 3),
  (2884371, 4, 2),
  (2888840, 4, 7),
  (2889220, 6, 7),
  (2889984, 0, 0),
  (2890780, 3, 3),
  (2898933, 1, 0),
  (2900956, 1, 4),
  (2901403, 5, 6),
  (2901660, 4, 3),
  (2904300, 7, 0),
  (2907505, 4, 2),
  (2916060, 4, 4),
  (2917056, 4, 2),
  (2919608, 2, 3),
  (2920697, 6, 0),
  (2922121, 6, 7),
  (2922724, 4, 3),
  (2933807, 4, 3),
  (2935290, 3, 3),
  (2937500, 1, 5),
  (2943494, 7, 0),
  (2951362, 2, 2),
  (2952723, 2, 6),
  (2955124, 0, 3),
  (2958319, 3, 6),
  (2959749, 0, 0),
  (2960018, 6, 0),
  (2962594, 6, 3),
  (2966309, 5, 3),
  (2974539, 2, 7),
  (2977527, 2, 5),
  (2979576, 3, 6),
  (2987864, 7, 2),
  (2991511, 1, 4),
  (2992177, 7, 4),
  (2993906, 4, 2),
  (2996992, 7, 4),
  (2998335, 7, 0),
  (3001265, 1, 4),
  (3001611, 5, 2),
  (3001721, 4, 1),
  (3007187, 4, 3),
  (3007952, 5, 2),
  (3029040, 4, 2),
  (3030253, 6, 3),
  (3035514, 4, 5),
  (3039669, 4, 3),
  (3043501, 7, 3),
  (3044537, 5, 5),
  (3045262, 6, 0),
  (3046590, 0, 4),
  (3058375, 4, 7),
  (3058439, 3, 3),
  (3058769, 4, 4),
  (3061768, 2, 3),
  (3065302, 2, 1),
  (3085888, 4, 7),
  (3086106, 5, 3),
  (3091131, 3, 1),
  (3091688, 6, 7),
  (3093323, 4, 3),
  (3107410, 3, 6),
  (3108259, 3, 2),
  (3112219, 5, 3),
  (3113984, 6, 0),
  (3115285, 5, 3),
  (3115451, 6, 4),
  (3118685, 2, 6),
  (3122554, 0, 0),
  (3122691, 1, 0),
  (3125789, 7, 0),
  (3127771, 3, 3),
  (3129142, 0, 3),
  (3130749, 1, 7),
  (3140705, 4, 3),
  (3146125, 2, 3),
  (3146719, 2, 5),
  (3146826, 7, 0),
  (3147233, 6, 1),
  (3148621, 4, 3),
  (3149756, 7, 0),
  (3150396, 0, 4),
  (3154474, 0, 6),
  (3159057, 1, 2),
  (3162001, 1, 0),
  (3162634, 3, 7),
  (3168761, 0, 1),
  (3169623, 2, 7),
  (3171036, 0, 0),
  (3172436, 6, 3),
  (3173364, 6, 7),
  (3174281, 5, 7),
  (3180443, 1, 4),
  (3181251, 6, 0),
  (3181943, 5, 3),
  (3183641, 0, 0),
  (3187227, 5, 2),
  (3187738, 0, 3),
  (3188760, 3, 3),
  (3190718, 6, 0),
  (3193421, 6, 1),
  (3197710, 0, 2),
  (3198476, 6, 7),
  (3198787, 7, 3),
  (3202892, 7, 0),
  (3207869, 6, 0),
  (3211174, 5, 2),
  (3211884, 1, 0),
  (3212819, 4, 1),
  (3213331, 2, 6),
  (3220852, 2, 4),
  (3232029, 4, 3),
  (3232586, 7, 4),
  (3234937, 0, 7),
  (3239411, 6, 7),
  (3241040, 0, 0),
  (3241716, 0, 2),
  (3247038, 2, 1),
  (3252852, 2, 2),
  (3255268, 5, 3),
  (3256706, 0, 7),
  (3262545, 5, 2),
  (3273772, 0, 4),
  (3274035, 5, 3),
  (3287244, 0, 6),
  (3290052, 5, 3),
  (3290501, 1, 7),
  (3290723, 5, 6),
  (3291083, 2, 7),
  (3294485, 5, 7),
  (3295148, 3, 3),
  (3306179, 0, 0),
  (3306713, 3, 3),
  (3313920, 7, 2),
  (3317769, 2, 7),
  (3319289, 0, 0),
  (3319423, 5, 3),
  (3327493, 0, 6),
  (3330602, 1, 0),
  (3332660, 0, 3),
  (3333165, 1, 0),
  (3334807, 2, 3),
  (3337985, 5, 3),
  (3343019, 4, 2),
  (3345424, 4, 3),
  (3347346, 3, 4),
  (3347722, 3, 6),
  (3348075, 3, 7),
  (3355189, 1, 0),
  (3356383, 3, 2),
  (3359794, 7, 0),
  (3361404, 3, 1),
  (3378088, 1, 0),
  (3386717, 4, 6),
  (3389091, 4, 3),
  (3392412, 4, 3),
  (3396286, 0, 7),
  (3398868, 2, 3),
  (3400673, 2, 3),
  (3402035, 3, 3),
  (3406419, 0, 0),
  (3408251, 2, 5),
  (3413823, 3, 3),
  (3414539, 2, 6),
  (3417353, 0, 0),
  (3424684, 0, 2),
  (3425493, 4, 3),
  (3430695, 5, 5),
  (3432242, 3, 6),
  (3435495, 0, 0),
  (3435629, 6, 1),
  (3443449, 4, 7),
  (3446697, 6, 4),
  (3450180, 4, 3),
  (3451197, 6, 4),
  (3453013, 6, 6),
  (3454771, 6, 0),
  (3459897, 6, 0),
  (3460684, 4, 1),
  (3470149, 4, 6),
  (3470221, 7, 0),
  (3473004, 5, 5),
  (3478649, 3, 1),
  (3479912, 3, 5),
  (3481960, 6, 0),
  (3482493, 0, 3),
  (3483180, 6, 3),
  (3486609, 0, 0),
  (3492664, 5, 7),
  (3492891, 1, 0),
  (3494338, 0, 0),
  (3496617, 3, 3),
  (3507877, 6, 0),
  (3508311, 4, 3),
  (3510014, 2, 3),
  (3510527, 2, 2),
  (3512797, 1, 0),
  (3517313, 6, 3),
  (3526321, 6, 3),
  (3527004, 6, 4),
  (3540742, 5, 3),
  (3541018, 7, 0),
  (3542710, 0, 3),
  (3548200, 0, 0),
  (3548292, 7, 3),
  (3549175, 3, 3),
  (3550255, 5, 4),
  (3552909, 4, 3),
  (3552929, 1, 4),
  (3557376, 5, 6),
  (3568232, 2, 2),
  (3569555, 5, 0),
  (3570250, 4, 3),
  (3573568, 7, 0),
  (3574542, 0, 1),
  (3575348, 4, 7),
  (3576024, 5, 6),
  (3578396, 6, 3),
  (3586578, 1, 0),
  (3597467, 5, 6),
  (3597803, 5, 6),
])
