from src.util import *
schedule = deque([
  (1609, 3, 1),
  (8311, 1, 1),
  (12402, 2, 2),
  (17542, 2, 1),
  (17624, 0, 1),
  (19575, 3, 1),
  (19957, 2, 0),
  (21092, 2, 2),
  (22303, 0, 1),
  (24894, 0, 0),
  (25708, 1, 0),
  (25759, 0, 2),
  (40714, 1, 2),
  (41203, 1, 1),
  (42820, 3, 1),
  (45853, 2, 1),
  (50228, 3, 2),
  (50856, 0, 2),
  (53681, 0, 0),
  (59512, 1, 1),
  (60392, 0, 1),
  (61464, 3, 1),
  (63216, 2, 2),
  (65930, 2, 1),
  (66107, 0, 0),
  (71168, 1, 1),
  (72578, 2, 1),
  (77312, 3, 2),
  (79140, 0, 0),
  (80706, 0, 0),
  (82486, 0, 1),
  (82723, 3, 2),
  (84317, 0, 1),
  (85840, 0, 1),
  (90149, 0, 0),
  (90982, 1, 1),
  (92475, 1, 2),
  (94470, 0, 0),
  (95503, 0, 1),
  (103106, 3, 1),
  (109057, 3, 2),
  (111807, 2, 2),
  (119103, 1, 1),
  (120182, 0, 2),
  (127920, 1, 1),
  (129141, 0, 1),
  (130239, 3, 1),
  (131561, 2, 0),
  (132165, 2, 0),
  (133202, 0, 1),
  (136329, 3, 2),
  (138288, 0, 2),
  (141760, 1, 2),
  (141971, 1, 2),
  (143969, 1, 0),
  (144417, 2, 0),
  (144775, 2, 1),
  (145781, 1, 2),
  (147791, 2, 0),
  (148966, 2, 0),
  (149032, 1, 2),
  (154972, 1, 1),
  (155996, 3, 0),
  (157827, 3, 2),
  (161091, 0, 1),
  (161399, 2, 1),
  (163073, 2, 1),
  (164205, 2, 1),
  (170091, 3, 2),
  (175235, 3, 1),
  (175675, 1, 0),
  (185599, 3, 2),
  (186936, 3, 1),
  (189346, 0, 0),
  (192635, 1, 2),
  (192692, 0, 2),
  (196402, 0, 1),
  (196635, 1, 0),
  (202999, 0, 1),
  (216933, 3, 2),
  (218492, 3, 0),
  (222567, 1, 0),
  (222958, 0, 2),
  (222959, 1, 0),
  (223331, 1, 0),
  (223580, 2, 1),
  (224642, 3, 0),
  (225222, 0, 0),
  (230122, 1, 2),
  (231200, 1, 0),
  (231790, 0, 2),
  (231941, 2, 1),
  (234815, 2, 0),
  (236620, 3, 0),
  (240868, 2, 2),
  (243549, 2, 0),
  (251861, 3, 1),
  (251918, 0, 2),
  (252121, 3, 1),
  (252965, 3, 1),
  (254051, 0, 1),
  (262844, 2, 1),
  (265269, 0, 0),
  (265796, 0, 0),
  (271930, 2, 1),
  (273893, 0, 1),
  (275024, 3, 2),
  (276929, 0, 2),
  (281765, 0, 1),
  (282254, 0, 0),
  (283337, 2, 1),
  (285448, 2, 1),
  (286180, 2, 1),
  (288533, 3, 0),
  (290112, 2, 0),
  (290515, 3, 1),
  (290696, 2, 2),
  (299032, 3, 2),
  (310826, 2, 2),
  (312494, 0, 2),
  (313273, 0, 1),
  (314745, 0, 0),
  (315203, 1, 1),
  (317651, 3, 0),
  (318609, 1, 1),
  (318859, 2, 0),
  (319751, 2, 1),
  (324207, 1, 2),
  (324234, 3, 1),
  (328036, 0, 0),
  (331022, 2, 2),
  (335369, 2, 0),
  (340144, 0, 1),
  (342961, 1, 2),
  (343930, 0, 2),
  (351570, 3, 1),
  (353345, 0, 1),
  (354005, 1, 1),
  (355825, 2, 2),
  (360603, 1, 1),
  (363296, 3, 2),
  (364936, 3, 2),
  (370617, 2, 0),
  (376951, 2, 0),
  (387066, 1, 0),
  (392130, 2, 2),
  (392444, 0, 0),
  (406417, 0, 2),
  (407371, 3, 0),
  (407589, 0, 2),
  (408628, 3, 1),
  (411628, 1, 0),
  (412451, 0, 0),
  (418395, 0, 0),
  (419778, 3, 2),
  (422438, 0, 1),
  (425460, 0, 1),
  (427322, 3, 1),
  (427653, 1, 2),
  (430514, 0, 2),
  (433575, 2, 1),
  (435211, 0, 1),
  (435408, 3, 0),
  (435539, 2, 0),
  (441117, 1, 0),
  (442841, 0, 1),
  (447857, 0, 0),
  (451077, 3, 2),
  (452896, 2, 1),
  (456468, 3, 2),
  (458675, 0, 0),
  (461742, 3, 0),
  (461799, 3, 2),
  (462791, 1, 1),
  (466090, 3, 0),
  (466380, 3, 2),
  (466743, 3, 2),
  (468987, 0, 1),
  (470409, 2, 0),
  (479322, 2, 0),
  (480596, 2, 2),
  (482574, 0, 2),
  (488749, 0, 0),
  (489752, 3, 1),
  (489956, 0, 0),
  (492004, 2, 1),
  (493926, 2, 0),
  (494601, 3, 0),
  (502842, 1, 1),
  (505150, 3, 0),
  (506729, 1, 1),
  (506903, 0, 0),
  (508754, 1, 2),
  (511876, 3, 1),
  (512973, 3, 2),
  (513500, 2, 2),
  (514027, 0, 1),
  (514235, 2, 1),
  (518956, 3, 2),
  (519016, 3, 1),
  (520068, 3, 1),
  (524799, 3, 1),
  (532375, 2, 0),
  (532509, 2, 1),
  (534874, 1, 1),
  (544255, 2, 2),
  (544331, 2, 2),
  (546454, 0, 0),
  (546916, 1, 0),
  (549140, 1, 0),
  (554976, 1, 0),
  (556518, 0, 0),
  (556924, 3, 1),
  (559159, 2, 2),
  (560348, 1, 0),
  (565106, 3, 2),
  (565521, 3, 2),
  (568633, 3, 0),
  (572401, 0, 2),
  (574665, 1, 0),
  (577241, 1, 1),
  (579182, 0, 0),
  (580145, 0, 2),
  (581266, 2, 2),
  (583864, 2, 2),
  (583978, 1, 2),
  (586282, 2, 2),
  (589627, 0, 1),
  (591259, 3, 1),
  (594576, 2, 0),
  (596849, 1, 1),
  (601826, 2, 0),
  (602304, 3, 2),
  (602382, 2, 0),
  (602536, 1, 2),
  (608661, 3, 2),
  (613187, 0, 1),
  (615097, 0, 2),
  (618233, 1, 2),
  (624218, 0, 1),
  (624589, 0, 2),
  (625202, 3, 0),
  (629979, 2, 1),
  (635262, 2, 2),
  (637651, 0, 2),
  (638125, 3, 2),
  (641123, 1, 1),
  (641172, 2, 0),
  (642905, 1, 0),
  (642985, 0, 2),
  (644410, 3, 1),
  (644665, 1, 2),
  (647348, 2, 2),
  (651500, 1, 0),
  (655431, 2, 2),
  (655539, 1, 2),
  (661685, 1, 1),
  (662418, 0, 1),
  (663148, 2, 1),
  (665282, 1, 0),
  (667931, 3, 2),
  (670914, 1, 2),
  (673383, 2, 1),
  (681782, 1, 0),
  (684817, 1, 1),
  (690613, 2, 1),
  (697258, 0, 1),
  (698518, 1, 0),
  (698872, 2, 1),
  (699753, 3, 1),
  (699985, 3, 1),
  (705978, 0, 0),
  (707766, 3, 1),
  (709401, 1, 2),
  (710212, 0, 0),
  (712360, 3, 2),
  (713259, 1, 0),
  (714760, 0, 0),
  (716824, 1, 1),
  (720408, 0, 0),
  (722514, 3, 0),
  (722552, 0, 1),
  (724765, 1, 0),
  (729430, 3, 1),
  (731063, 1, 0),
  (732074, 2, 1),
  (737332, 0, 0),
  (742704, 3, 2),
  (745735, 3, 2),
  (747586, 1, 2),
  (753606, 0, 0),
  (756719, 1, 2),
  (757347, 3, 0),
  (757728, 0, 1),
  (759775, 3, 0),
  (773035, 0, 0),
  (774337, 1, 1),
  (779869, 1, 2),
  (780889, 3, 1),
  (782020, 2, 2),
  (784784, 0, 2),
  (788181, 2, 2),
  (789566, 2, 1),
  (797635, 0, 0),
  (799096, 2, 2),
  (799423, 1, 1),
  (799584, 3, 2),
  (801025, 2, 1),
  (804838, 0, 1),
  (806745, 2, 1),
  (810037, 3, 1),
  (814016, 1, 1),
  (816854, 2, 2),
  (816880, 1, 2),
  (824225, 3, 1),
  (825447, 0, 1),
  (827770, 2, 2),
  (828783, 3, 1),
  (830360, 2, 1),
  (834380, 1, 1),
  (836347, 2, 2),
  (842370, 1, 1),
  (843094, 3, 1),
  (846502, 2, 0),
  (855401, 1, 1),
  (857478, 2, 1),
  (858077, 1, 1),
  (862715, 2, 1),
  (865440, 0, 2),
  (867653, 2, 2),
  (875316, 3, 2),
  (875474, 3, 2),
  (880092, 1, 1),
  (880515, 3, 2),
  (881629, 3, 1),
  (885328, 3, 0),
  (888391, 2, 2),
  (890875, 3, 1),
  (895036, 2, 0),
  (899935, 1, 0),
  (903487, 0, 2),
  (904413, 1, 2),
  (909125, 2, 2),
  (911691, 0, 2),
  (917223, 3, 1),
  (917414, 0, 0),
  (920715, 0, 0),
  (922719, 0, 1),
  (923659, 1, 1),
  (923717, 3, 2),
  (924855, 2, 2),
  (928709, 3, 0),
  (929564, 2, 1),
  (933694, 2, 2),
  (937472, 0, 2),
  (938124, 0, 1),
  (939872, 2, 1),
  (950265, 1, 2),
  (951734, 0, 2),
  (956401, 3, 1),
  (959396, 2, 2),
  (964804, 2, 1),
  (965197, 0, 1),
  (965520, 2, 2),
  (966003, 1, 1),
  (971657, 1, 0),
  (979556, 3, 1),
  (984949, 1, 1),
  (989530, 1, 1),
  (996085, 2, 1),
  (998129, 2, 0),
  (1002595, 3, 0),
  (1004155, 1, 1),
  (1007963, 0, 0),
  (1008935, 0, 2),
  (1008998, 0, 2),
  (1011580, 2, 2),
  (1016351, 2, 2),
  (1021570, 0, 0),
  (1024586, 2, 0),
  (1027747, 1, 0),
  (1034280, 3, 0),
  (1036762, 3, 2),
  (1046722, 0, 2),
  (1048928, 3, 1),
  (1057029, 1, 1),
  (1057516, 3, 2),
  (1061926, 2, 1),
  (1064912, 1, 0),
  (1066100, 0, 0),
  (1067364, 0, 2),
  (1068890, 3, 1),
  (1076868, 1, 0),
  (1078141, 2, 0),
  (1078163, 1, 0),
  (1078861, 2, 0),
  (1084682, 3, 0),
  (1084931, 1, 1),
  (1089873, 1, 0),
  (1089996, 3, 0),
  (1090387, 2, 0),
  (1091770, 1, 1),
  (1094232, 3, 1),
  (1095133, 3, 2),
  (1099086, 3, 1),
  (1104767, 0, 1),
  (1109287, 2, 2),
  (1110880, 2, 2),
  (1115245, 0, 1),
  (1123036, 0, 1),
  (1125896, 1, 1),
  (1126825, 2, 0),
  (1130848, 3, 1),
  (1131495, 1, 2),
  (1132755, 2, 2),
  (1133566, 0, 1),
  (1137023, 2, 0),
  (1137375, 1, 1),
  (1137807, 2, 1),
  (1147488, 0, 1),
  (1147591, 3, 2),
  (1151533, 0, 2),
  (1160760, 2, 1),
  (1161239, 1, 0),
  (1164971, 0, 0),
  (1169271, 1, 0),
  (1171243, 0, 2),
  (1171771, 1, 1),
  (1172260, 0, 1),
  (1172789, 0, 2),
  (1173176, 1, 0),
  (1179266, 2, 2),
  (1180609, 2, 1),
  (1187535, 2, 0),
  (1194697, 0, 0),
  (1194987, 0, 2),
  (1196340, 3, 2),
  (1196364, 3, 0),
  (1197667, 1, 1),
  (1200912, 1, 2),
  (1200979, 0, 1),
  (1201060, 0, 1),
  (1202415, 2, 2),
  (1202436, 1, 0),
  (1208611, 1, 0),
  (1209415, 0, 1),
  (1209494, 2, 0),
  (1212622, 0, 1),
  (1213958, 1, 2),
  (1214661, 1, 2),
  (1215634, 1, 0),
  (1216338, 0, 2),
  (1218612, 2, 0),
  (1219293, 0, 0),
  (1222404, 0, 1),
  (1228281, 2, 2),
  (1229243, 1, 0),
  (1230247, 0, 1),
  (1240408, 2, 0),
  (1240850, 0, 1),
  (1242331, 1, 1),
  (1258157, 0, 2),
  (1261482, 3, 1),
  (1262215, 0, 0),
  (1263339, 0, 1),
  (1263718, 0, 2),
  (1268116, 3, 0),
  (1272442, 3, 1),
  (1275646, 0, 2),
  (1279847, 2, 2),
  (1281154, 3, 1),
  (1282148, 2, 0),
  (1291761, 1, 1),
  (1296398, 1, 2),
  (1301464, 0, 2),
  (1308314, 1, 2),
  (1314626, 0, 1),
  (1316308, 3, 1),
  (1320779, 2, 2),
  (1325258, 3, 0),
  (1327200, 3, 2),
  (1327416, 0, 2),
  (1328408, 1, 0),
  (1333598, 2, 0),
  (1350354, 3, 0),
  (1350432, 1, 1),
  (1353570, 1, 0),
  (1355128, 0, 2),
  (1357199, 2, 0),
  (1357620, 3, 0),
  (1366478, 2, 2),
  (1366602, 0, 0),
  (1370058, 0, 2),
  (1372317, 1, 0),
  (1372556, 1, 0),
  (1373423, 2, 1),
  (1381903, 2, 0),
  (1390730, 0, 1),
  (1396354, 0, 0),
  (1396785, 0, 1),
  (1401713, 1, 0),
  (1402659, 1, 1),
  (1408545, 1, 1),
  (1410219, 1, 2),
  (1414796, 3, 2),
  (1416449, 3, 2),
  (1419682, 0, 1),
  (1420778, 0, 1),
  (1425638, 2, 0),
  (1426012, 3, 1),
  (1426416, 3, 0),
  (1427165, 0, 1),
  (1432896, 0, 0),
  (1439734, 1, 1),
  (1440371, 1, 2),
  (1441395, 2, 2),
  (1442839, 3, 1),
  (1446788, 1, 1),
  (1456209, 2, 1),
  (1457671, 2, 1),
  (1459099, 2, 2),
  (1460997, 3, 1),
  (1465978, 0, 0),
  (1470777, 0, 1),
  (1479186, 2, 0),
  (1480641, 3, 2),
  (1482429, 3, 0),
  (1484188, 1, 0),
  (1491505, 3, 0),
  (1496705, 2, 0),
  (1496906, 2, 0),
  (1504806, 2, 1),
  (1505021, 3, 2),
  (1514535, 2, 1),
  (1517486, 0, 2),
  (1522404, 1, 0),
  (1522511, 0, 2),
  (1528728, 1, 0),
  (1534670, 1, 2),
  (1534782, 1, 1),
  (1538316, 0, 1),
  (1540954, 3, 1),
  (1543450, 0, 1),
  (1544979, 0, 0),
  (1548141, 3, 0),
  (1552061, 1, 1),
  (1555723, 1, 1),
  (1561988, 3, 0),
  (1561991, 0, 1),
  (1564620, 1, 2),
  (1565066, 0, 0),
  (1566836, 3, 1),
  (1568792, 1, 1),
  (1571100, 0, 1),
  (1571223, 1, 0),
  (1575430, 3, 1),
  (1582864, 0, 0),
  (1584251, 0, 2),
  (1588592, 0, 2),
  (1589015, 3, 2),
  (1592766, 2, 1),
  (1596443, 1, 1),
  (1598517, 3, 1),
  (1599945, 3, 0),
  (1602323, 0, 1),
  (1604298, 2, 0),
  (1613182, 1, 2),
  (1614647, 2, 2),
  (1620731, 3, 1),
  (1621014, 0, 1),
  (1622818, 3, 0),
  (1628847, 2, 2),
  (1631497, 1, 1),
  (1632258, 0, 2),
  (1633366, 2, 2),
  (1633708, 3, 2),
  (1638451, 0, 1),
  (1645483, 2, 1),
  (1646433, 3, 1),
  (1650010, 3, 0),
  (1653675, 3, 2),
  (1653984, 2, 1),
  (1654050, 0, 0),
  (1658525, 2, 1),
  (1663339, 1, 1),
  (1666122, 1, 2),
  (1666260, 2, 2),
  (1667722, 2, 1),
  (1669227, 0, 1),
  (1669569, 0, 1),
  (1670830, 2, 0),
  (1675417, 0, 2),
  (1680677, 0, 2),
  (1685115, 3, 2),
  (1690413, 0, 1),
  (1692082, 3, 1),
  (1697506, 2, 0),
  (1705746, 3, 0),
  (1710237, 1, 0),
  (1710281, 0, 2),
  (1710524, 1, 1),
  (1712047, 3, 1),
  (1713322, 0, 2),
  (1714601, 0, 1),
  (1717541, 2, 0),
  (1720579, 0, 2),
  (1720640, 0, 2),
  (1720903, 2, 2),
  (1721049, 0, 2),
  (1722301, 3, 2),
  (1728468, 2, 2),
  (1728945, 0, 0),
  (1730039, 2, 2),
  (1731801, 1, 2),
  (1734229, 1, 2),
  (1738592, 3, 0),
  (1743730, 3, 2),
  (1744794, 0, 2),
  (1745478, 3, 0),
  (1746142, 1, 0),
  (1748497, 2, 1),
  (1751750, 2, 0),
  (1753062, 2, 1),
  (1754882, 0, 2),
  (1762354, 3, 0),
  (1764998, 3, 2),
  (1765447, 3, 1),
  (1767671, 1, 0),
  (1769688, 0, 2),
  (1769871, 3, 0),
  (1772645, 0, 1),
  (1777809, 2, 1),
  (1778600, 1, 2),
  (1785350, 2, 1),
  (1787518, 1, 2),
  (1787569, 1, 0),
  (1792300, 3, 0),
  (1795061, 3, 1),
  (1795435, 0, 1),
  (1797280, 3, 0),
  (1799296, 0, 0),
  (1799478, 3, 2),
  (1800208, 0, 1),
  (1806680, 0, 1),
  (1807828, 0, 0),
  (1808679, 0, 0),
  (1822309, 1, 1),
  (1833156, 3, 2),
  (1839926, 2, 1),
  (1840593, 3, 1),
  (1843790, 2, 2),
  (1846170, 1, 2),
  (1854705, 2, 2),
  (1861754, 0, 2),
  (1870594, 2, 1),
  (1873445, 2, 0),
  (1882678, 1, 0),
  (1884257, 2, 1),
  (1887038, 2, 1),
  (1887523, 1, 0),
  (1889664, 1, 1),
  (1889723, 3, 2),
  (1891417, 1, 0),
  (1892474, 1, 2),
  (1897201, 3, 0),
  (1898431, 1, 2),
  (1903008, 0, 2),
  (1907648, 1, 2),
  (1909642, 1, 1),
  (1910910, 3, 1),
  (1913593, 1, 1),
  (1913683, 3, 2),
  (1914163, 2, 1),
  (1929970, 2, 1),
  (1932831, 2, 2),
  (1933037, 2, 2),
  (1933384, 1, 1),
  (1934098, 0, 2),
  (1938099, 0, 1),
  (1946027, 3, 0),
  (1946301, 3, 0),
  (1947351, 0, 1),
  (1947762, 0, 2),
  (1949043, 2, 1),
  (1951752, 2, 0),
  (1952413, 3, 2),
  (1955683, 3, 2),
  (1955894, 1, 0),
  (1962916, 0, 1),
  (1963144, 0, 2),
  (1966913, 0, 2),
  (1969123, 2, 0),
  (1974315, 1, 1),
  (1974973, 1, 0),
  (1980354, 1, 2),
  (1989576, 1, 1),
  (1992414, 0, 0),
  (1994859, 2, 1),
  (2001889, 3, 1),
  (2003734, 1, 1),
  (2005268, 1, 0),
  (2007657, 2, 0),
  (2014918, 3, 1),
  (2015571, 2, 0),
  (2025406, 0, 1),
  (2031613, 3, 0),
  (2039960, 2, 0),
  (2045441, 1, 1),
  (2046615, 2, 1),
  (2051374, 2, 1),
  (2053133, 1, 2),
  (2063580, 1, 2),
  (2066606, 0, 0),
  (2072934, 3, 2),
  (2085856, 0, 1),
  (2089600, 2, 1),
  (2089771, 1, 2),
  (2091622, 2, 1),
  (2095954, 2, 2),
  (2099033, 0, 2),
  (2099177, 3, 0),
  (2099754, 2, 0),
  (2104557, 3, 0),
  (2109472, 3, 0),
  (2111669, 3, 1),
  (2113462, 1, 2),
  (2122340, 2, 2),
  (2125683, 2, 2),
  (2131398, 1, 0),
  (2131578, 3, 1),
  (2132130, 0, 1),
  (2140361, 3, 2),
  (2141388, 0, 1),
  (2148472, 0, 1),
  (2152482, 2, 1),
  (2155918, 1, 1),
  (2162824, 0, 0),
  (2163766, 0, 2),
  (2167871, 3, 2),
  (2180099, 3, 0),
  (2184849, 1, 2),
  (2191795, 2, 2),
  (2192517, 0, 0),
  (2194641, 2, 0),
  (2196916, 0, 2),
  (2201962, 3, 2),
  (2206567, 3, 2),
  (2209481, 2, 0),
  (2213445, 1, 1),
  (2216860, 2, 1),
  (2217752, 1, 2),
  (2218354, 2, 0),
  (2218429, 3, 1),
  (2225087, 2, 2),
  (2225279, 2, 1),
  (2226258, 1, 0),
  (2226777, 3, 1),
  (2229574, 0, 0),
  (2230547, 1, 0),
  (2232788, 0, 1),
  (2236386, 2, 2),
  (2238417, 0, 1),
  (2238555, 2, 2),
  (2240612, 3, 1),
  (2241077, 0, 1),
  (2247662, 2, 0),
  (2253436, 3, 1),
  (2256327, 0, 0),
  (2257986, 1, 2),
  (2259192, 3, 2),
  (2259813, 2, 2),
  (2270146, 1, 1),
  (2273037, 0, 0),
  (2274434, 0, 2),
  (2274997, 2, 1),
  (2275279, 1, 0),
  (2279846, 1, 1),
  (2280627, 3, 1),
  (2290384, 3, 0),
  (2294279, 0, 2),
  (2296293, 0, 0),
  (2298227, 2, 1),
  (2298673, 2, 1),
  (2304271, 3, 0),
  (2304476, 2, 1),
  (2306996, 0, 1),
  (2308582, 1, 0),
  (2308954, 1, 1),
  (2309981, 3, 0),
  (2311500, 1, 2),
  (2312902, 2, 0),
  (2316984, 0, 1),
  (2318763, 2, 1),
  (2321339, 2, 2),
  (2327931, 0, 1),
  (2328390, 0, 0),
  (2333424, 3, 2),
  (2334227, 0, 1),
  (2335499, 2, 1),
  (2357605, 2, 1),
  (2362211, 2, 0),
  (2367548, 0, 0),
  (2368725, 0, 1),
  (2372871, 0, 0),
  (2379419, 3, 0),
  (2382567, 0, 1),
  (2389974, 0, 0),
  (2394768, 0, 0),
  (2395193, 1, 1),
  (2398534, 0, 1),
  (2399092, 1, 0),
  (2400412, 3, 2),
  (2402512, 2, 0),
  (2409558, 3, 0),
  (2412407, 3, 1),
  (2412671, 3, 0),
  (2416110, 2, 2),
  (2423256, 3, 1),
  (2423726, 2, 2),
  (2425255, 1, 2),
  (2431091, 0, 1),
  (2432231, 1, 2),
  (2432366, 0, 2),
  (2432486, 3, 0),
  (2442500, 3, 1),
  (2444738, 2, 1),
  (2446873, 0, 0),
  (2453802, 3, 1),
  (2453908, 1, 0),
  (2455902, 2, 0),
  (2458480, 1, 2),
  (2462271, 3, 0),
  (2463989, 0, 1),
  (2467196, 3, 2),
  (2471885, 3, 2),
  (2472969, 1, 2),
  (2489115, 1, 1),
  (2491107, 0, 2),
  (2493017, 0, 0),
  (2494607, 3, 0),
  (2495427, 0, 2),
  (2501094, 0, 0),
  (2513301, 0, 2),
  (2517402, 2, 0),
  (2518318, 0, 2),
  (2520511, 2, 2),
  (2525548, 2, 0),
  (2534483, 2, 0),
  (2535920, 0, 0),
  (2539104, 1, 1),
  (2539368, 1, 2),
  (2542614, 2, 0),
  (2544448, 3, 2),
  (2548549, 0, 0),
  (2548854, 0, 2),
  (2549376, 2, 0),
  (2554045, 1, 0),
  (2554585, 2, 2),
  (2571986, 1, 2),
  (2572333, 2, 0),
  (2575175, 0, 2),
  (2582653, 0, 1),
  (2592766, 0, 2),
  (2598149, 2, 2),
  (2601542, 2, 2),
  (2602848, 3, 2),
  (2608244, 3, 1),
  (2609478, 2, 1),
  (2611985, 3, 1),
  (2612164, 3, 1),
  (2612507, 1, 1),
  (2613698, 3, 1),
  (2614033, 0, 1),
  (2615549, 3, 0),
  (2618955, 3, 1),
  (2619432, 3, 2),
  (2624914, 1, 1),
  (2628396, 2, 1),
  (2629156, 3, 0),
  (2630710, 1, 1),
  (2645724, 2, 1),
  (2649047, 1, 0),
  (2649735, 0, 1),
  (2649930, 3, 1),
  (2651732, 2, 2),
  (2656726, 3, 1),
  (2659863, 0, 2),
  (2663539, 0, 0),
  (2668410, 3, 0),
  (2668970, 1, 0),
  (2671664, 2, 0),
  (2671810, 1, 1),
  (2672963, 2, 2),
  (2673701, 1, 2),
  (2674353, 3, 0),
  (2696935, 0, 0),
  (2698904, 3, 0),
  (2703703, 0, 1),
  (2710280, 1, 1),
  (2721980, 0, 1),
  (2724936, 3, 1),
  (2726794, 0, 0),
  (2726974, 1, 2),
  (2728324, 3, 0),
  (2733598, 1, 0),
  (2738552, 2, 1),
  (2739042, 3, 2),
  (2739510, 3, 1),
  (2741195, 1, 2),
  (2743930, 0, 0),
  (2751476, 0, 0),
  (2752952, 3, 2),
  (2753168, 3, 0),
  (2756041, 0, 0),
  (2757509, 0, 0),
  (2769731, 1, 1),
  (2774990, 1, 2),
  (2777780, 1, 1),
  (2778705, 3, 0),
  (2778919, 0, 2),
  (2790698, 0, 0),
  (2792821, 2, 0),
  (2793658, 3, 0),
  (2798518, 0, 2),
  (2798566, 1, 2),
  (2798797, 0, 0),
  (2807846, 3, 1),
  (2811366, 2, 0),
  (2812659, 0, 1),
  (2819012, 1, 0),
  (2823890, 3, 2),
  (2825445, 3, 0),
  (2830116, 3, 2),
  (2837577, 0, 0),
  (2838640, 3, 0),
  (2838865, 1, 1),
  (2839511, 2, 2),
  (2844175, 3, 0),
  (2846257, 3, 1),
  (2850342, 3, 1),
  (2857401, 0, 2),
  (2861151, 2, 0),
  (2866079, 1, 1),
  (2874014, 1, 0),
  (2875346, 0, 2),
  (2877644, 3, 2),
  (2880549, 2, 2),
  (2893628, 3, 2),
  (2896490, 1, 2),
  (2900069, 3, 0),
  (2906984, 0, 2),
  (2911807, 2, 1),
  (2916144, 3, 2),
  (2918129, 3, 0),
  (2919753, 0, 0),
  (2920990, 1, 2),
  (2923978, 1, 2),
  (2925742, 2, 1),
  (2929638, 1, 2),
  (2935239, 0, 0),
  (2936773, 1, 2),
  (2937344, 0, 2),
  (2941462, 2, 0),
  (2946354, 3, 0),
  (2948053, 2, 2),
  (2948507, 3, 1),
  (2951646, 0, 0),
  (2953005, 0, 2),
  (2953025, 0, 0),
  (2953262, 2, 2),
  (2956385, 0, 1),
  (2963779, 2, 1),
  (2964344, 1, 1),
  (2969884, 1, 0),
  (2974930, 3, 2),
  (2977607, 3, 1),
  (2979190, 1, 0),
  (2979249, 3, 1),
  (2984520, 0, 0),
  (2988631, 3, 0),
  (2999006, 0, 0),
  (3002218, 0, 1),
  (3005822, 3, 1),
  (3014161, 0, 0),
  (3020293, 3, 1),
  (3023350, 3, 0),
  (3029019, 3, 2),
  (3029559, 1, 1),
  (3032226, 3, 2),
  (3033612, 3, 1),
  (3036613, 1, 1),
  (3041148, 2, 1),
  (3043925, 1, 0),
  (3049995, 1, 1),
  (3054196, 3, 0),
  (3054273, 3, 2),
  (3054453, 3, 2),
  (3056010, 3, 1),
  (3058046, 3, 0),
  (3066216, 3, 0),
  (3070793, 0, 0),
  (3070883, 2, 1),
  (3073111, 1, 0),
  (3075088, 2, 2),
  (3075244, 3, 2),
  (3075470, 0, 2),
  (3079535, 3, 0),
  (3087239, 0, 0),
  (3087581, 3, 1),
  (3091506, 3, 0),
  (3093014, 1, 0),
  (3096427, 2, 2),
  (3104517, 0, 2),
  (3108602, 0, 2),
  (3112492, 0, 2),
  (3114769, 1, 2),
  (3119315, 0, 0),
  (3119699, 0, 2),
  (3136695, 0, 1),
  (3137943, 0, 1),
  (3142893, 3, 0),
  (3148215, 2, 0),
  (3148477, 2, 2),
  (3149919, 1, 0),
  (3150358, 2, 1),
  (3151796, 3, 0),
  (3152291, 1, 2),
  (3153929, 3, 2),
  (3163861, 2, 0),
  (3164566, 3, 2),
  (3165034, 3, 1),
  (3166228, 1, 1),
  (3167905, 1, 2),
  (3168278, 3, 0),
  (3172323, 1, 2),
  (3179344, 2, 2),
  (3180455, 0, 1),
  (3182073, 3, 0),
  (3182832, 0, 0),
  (3190479, 1, 0),
  (3191230, 0, 0),
  (3192154, 0, 2),
  (3197203, 1, 0),
  (3199198, 0, 0),
  (3201226, 0, 1),
  (3206710, 1, 2),
  (3206839, 1, 0),
  (3208156, 2, 1),
  (3208787, 3, 2),
  (3210279, 2, 0),
  (3213756, 2, 0),
  (3217403, 1, 0),
  (3218588, 0, 0),
  (3219379, 1, 1),
  (3222116, 0, 0),
  (3227082, 3, 0),
  (3227184, 3, 0),
  (3227712, 1, 0),
  (3239070, 1, 2),
  (3244596, 1, 2),
  (3248802, 1, 2),
  (3254017, 2, 0),
  (3255693, 2, 0),
  (3256660, 3, 2),
  (3258090, 3, 1),
  (3260921, 2, 0),
  (3262949, 3, 1),
  (3264148, 0, 0),
  (3267605, 1, 2),
  (3268000, 1, 0),
  (3269782, 3, 1),
  (3275301, 3, 1),
  (3281617, 2, 0),
  (3282341, 3, 1),
  (3285300, 0, 0),
  (3290457, 2, 1),
  (3293897, 2, 1),
  (3295393, 1, 0),
  (3299099, 1, 2),
  (3301944, 3, 0),
  (3303222, 3, 2),
  (3306123, 1, 2),
  (3307801, 0, 0),
  (3314409, 1, 1),
  (3315297, 2, 2),
  (3324285, 2, 1),
  (3325458, 1, 2),
  (3329032, 0, 1),
  (3334558, 1, 0),
  (3334762, 3, 0),
  (3336130, 3, 0),
  (3339767, 3, 2),
  (3341495, 2, 2),
  (3343013, 3, 1),
  (3343810, 2, 1),
  (3346392, 2, 0),
  (3347420, 3, 1),
  (3347570, 3, 0),
  (3347978, 3, 2),
  (3348549, 2, 2),
  (3353514, 0, 0),
  (3354100, 0, 1),
  (3354222, 3, 0),
  (3356430, 3, 0),
  (3357526, 3, 0),
  (3360756, 0, 0),
  (3362143, 2, 0),
  (3362988, 2, 0),
  (3363529, 0, 1),
  (3365338, 0, 0),
  (3366511, 2, 0),
  (3367009, 2, 2),
  (3368444, 3, 2),
  (3368881, 1, 0),
  (3372429, 0, 2),
  (3375538, 2, 2),
  (3377361, 0, 1),
  (3382692, 1, 1),
  (3382855, 3, 2),
  (3382873, 1, 0),
  (3384028, 1, 0),
  (3385106, 2, 2),
  (3385826, 0, 1),
  (3388025, 2, 1),
  (3389327, 2, 1),
  (3390241, 0, 1),
  (3392142, 3, 1),
  (3394558, 2, 1),
  (3397630, 0, 1),
  (3397817, 3, 1),
  (3399464, 0, 0),
  (3402915, 1, 2),
  (3403400, 1, 2),
  (3403892, 1, 0),
  (3409173, 3, 1),
  (3413917, 3, 2),
  (3414796, 1, 2),
  (3414940, 1, 0),
  (3415740, 2, 1),
  (3432258, 1, 0),
  (3435464, 1, 1),
  (3439122, 0, 1),
  (3440569, 1, 0),
  (3444592, 2, 0),
  (3449536, 1, 2),
  (3450242, 3, 2),
  (3453762, 3, 2),
  (3456292, 1, 2),
  (3457335, 1, 1),
  (3462867, 0, 0),
  (3466811, 1, 2),
  (3473911, 1, 0),
  (3477769, 2, 1),
  (3479228, 0, 2),
  (3479264, 0, 1),
  (3484023, 2, 1),
  (3493717, 3, 0),
  (3497235, 1, 0),
  (3500531, 2, 0),
  (3500623, 1, 1),
  (3501679, 2, 2),
  (3504976, 2, 1),
  (3508292, 2, 0),
  (3510072, 0, 0),
  (3510192, 0, 1),
  (3511047, 3, 0),
  (3514437, 0, 0),
  (3516468, 1, 0),
  (3517850, 0, 0),
  (3518323, 0, 2),
  (3518840, 0, 1),
  (3520810, 2, 0),
  (3527436, 2, 0),
  (3527730, 3, 2),
  (3528164, 3, 2),
  (3531583, 1, 1),
  (3531888, 3, 1),
  (3533599, 3, 2),
  (3534153, 0, 0),
  (3536862, 1, 2),
  (3538792, 0, 1),
  (3540978, 0, 0),
  (3543333, 2, 1),
  (3545758, 3, 1),
  (3546611, 3, 0),
  (3557013, 2, 0),
  (3557750, 3, 1),
  (3561233, 3, 0),
  (3564051, 3, 0),
  (3565274, 1, 0),
  (3565395, 1, 2),
  (3567954, 0, 2),
  (3578550, 1, 2),
  (3580149, 0, 1),
  (3581514, 1, 0),
  (3583927, 0, 2),
  (3590453, 3, 1),
  (3590865, 1, 2),
  (3596549, 2, 0),
  (3596560, 3, 1),
])
