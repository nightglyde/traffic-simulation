from util import *
schedule = deque([
  (1017, 5, 7),
  (2243, 1, 3),
  (7811, 1, 0),
  (9171, 6, 0),
  (12599, 4, 3),
  (17552, 1, 7),
  (17797, 2, 7),
  (30814, 5, 3),
  (32755, 4, 6),
  (33835, 0, 0),
  (38350, 4, 3),
  (39426, 3, 7),
  (42239, 4, 7),
  (46538, 2, 7),
  (47406, 4, 7),
  (48515, 5, 3),
  (54954, 0, 0),
  (57662, 4, 7),
  (58600, 6, 7),
  (59154, 5, 2),
  (67535, 5, 2),
  (73379, 5, 6),
  (78993, 6, 7),
  (83588, 2, 3),
  (86347, 5, 3),
  (91002, 7, 6),
  (96000, 6, 0),
  (97215, 2, 3),
  (99336, 6, 5),
  (110589, 2, 7),
  (113342, 5, 3),
  (121263, 4, 3),
  (121910, 7, 0),
  (122242, 7, 4),
  (131204, 6, 0),
  (134074, 2, 2),
  (140690, 5, 7),
  (141857, 1, 7),
  (143784, 2, 7),
  (145787, 1, 6),
  (146939, 4, 7),
  (148382, 6, 7),
  (148614, 0, 6),
  (150119, 4, 2),
  (156074, 5, 3),
  (162399, 1, 3),
  (165435, 3, 7),
  (165805, 3, 3),
  (166708, 3, 3),
  (168883, 0, 7),
  (169389, 7, 7),
  (169785, 7, 3),
  (173444, 2, 3),
  (174698, 6, 4),
  (179826, 6, 3),
  (181532, 1, 7),
  (183542, 1, 0),
  (186089, 2, 2),
  (188038, 4, 2),
  (190573, 3, 7),
  (190810, 0, 6),
  (191150, 0, 2),
  (197521, 0, 7),
  (200196, 4, 2),
  (200391, 2, 2),
  (204039, 3, 7),
  (204262, 3, 3),
  (209614, 5, 2),
  (210613, 3, 7),
  (218070, 3, 1),
  (218805, 0, 4),
  (232698, 5, 5),
  (242389, 1, 5),
  (243361, 6, 0),
  (247728, 2, 2),
  (248507, 0, 7),
  (251224, 5, 7),
  (253631, 0, 7),
  (253727, 5, 7),
  (255495, 5, 3),
  (261509, 4, 7),
  (263174, 6, 0),
  (273988, 0, 0),
  (274192, 3, 7),
  (280726, 4, 2),
  (280991, 4, 3),
  (285245, 4, 7),
  (286700, 1, 0),
  (288984, 1, 4),
  (291953, 6, 3),
  (294532, 7, 7),
  (297306, 7, 5),
  (298234, 1, 0),
  (300533, 1, 1),
  (302322, 3, 7),
  (304078, 6, 7),
  (305997, 6, 0),
  (307403, 5, 7),
  (312729, 6, 3),
  (322355, 5, 7),
  (325778, 6, 7),
  (328239, 7, 6),
  (332583, 7, 7),
  (333785, 3, 3),
  (339245, 5, 4),
  (340057, 3, 2),
  (344094, 4, 7),
  (345571, 4, 3),
  (352282, 1, 7),
  (352414, 0, 0),
  (353688, 5, 3),
  (356714, 5, 7),
  (368612, 1, 2),
  (370231, 4, 7),
  (370867, 7, 0),
  (372033, 4, 6),
  (372997, 0, 7),
  (375040, 4, 6),
  (376495, 7, 7),
  (379820, 4, 6),
  (383569, 4, 6),
  (384957, 0, 2),
  (386707, 4, 5),
  (387882, 1, 3),
  (390768, 5, 7),
  (391726, 3, 3),
  (397591, 5, 6),
  (398289, 6, 0),
  (399168, 7, 5),
  (401229, 2, 3),
  (404597, 1, 7),
  (405279, 4, 7),
  (406145, 1, 3),
  (410640, 4, 3),
  (413313, 0, 7),
  (417352, 2, 6),
  (418649, 6, 7),
  (419082, 2, 7),
  (420813, 2, 3),
  (421893, 5, 3),
  (422319, 3, 2),
  (423672, 2, 3),
  (428894, 0, 4),
  (429281, 4, 5),
  (431871, 0, 2),
  (432498, 0, 7),
  (434155, 7, 0),
  (434448, 1, 4),
  (435305, 3, 2),
  (436712, 7, 3),
  (438242, 3, 7),
  (438909, 6, 7),
  (444605, 1, 4),
  (446256, 5, 6),
  (446904, 3, 7),
  (448263, 3, 6),
  (454650, 3, 3),
  (455047, 7, 0),
  (455750, 2, 3),
  (460502, 4, 6),
  (467749, 1, 3),
  (469851, 7, 7),
  (471448, 6, 3),
  (471793, 4, 3),
  (474152, 0, 7),
  (476220, 4, 0),
  (478151, 6, 2),
  (480595, 0, 6),
  (480970, 4, 3),
  (483422, 7, 3),
  (484993, 0, 7),
  (491443, 3, 2),
  (491573, 2, 3),
  (494085, 5, 2),
  (495801, 7, 0),
  (503038, 7, 6),
  (507739, 6, 0),
  (509746, 4, 3),
  (512015, 4, 2),
  (512632, 5, 5),
  (513596, 2, 2),
  (514131, 0, 6),
  (522020, 0, 7),
  (523458, 0, 0),
  (524673, 1, 0),
  (525043, 6, 7),
  (526327, 4, 7),
  (527934, 3, 7),
  (530893, 6, 7),
  (533625, 3, 3),
  (541676, 5, 7),
  (542648, 6, 3),
  (546365, 3, 3),
  (547654, 2, 7),
  (549001, 5, 3),
  (551302, 5, 2),
  (552564, 2, 3),
  (559266, 4, 7),
  (561592, 5, 2),
  (570377, 4, 6),
  (571425, 0, 7),
  (575920, 7, 0),
  (581670, 7, 4),
  (584753, 6, 6),
  (584849, 0, 7),
  (590684, 1, 4),
  (590772, 1, 3),
  (594458, 3, 6),
  (595873, 3, 7),
  (597154, 5, 3),
  (600793, 2, 6),
  (607795, 0, 0),
  (608454, 4, 4),
  (608497, 6, 5),
  (609511, 6, 4),
  (609544, 6, 7),
  (613697, 3, 7),
  (618552, 0, 6),
  (620093, 6, 0),
  (630206, 3, 3),
  (634496, 0, 7),
  (636794, 0, 7),
  (643992, 3, 6),
  (645688, 6, 4),
  (651061, 0, 7),
  (654464, 5, 7),
  (655726, 2, 6),
  (655794, 0, 0),
  (657635, 4, 3),
  (659094, 1, 4),
  (660085, 1, 4),
  (661541, 5, 2),
  (664378, 1, 5),
  (666620, 0, 0),
  (668715, 0, 0),
  (670584, 2, 3),
  (675061, 5, 7),
  (684713, 1, 0),
  (685424, 7, 7),
  (686802, 0, 1),
  (689291, 5, 3),
  (689593, 5, 5),
  (690500, 3, 6),
  (697927, 2, 7),
  (697962, 6, 0),
  (700487, 6, 3),
  (704267, 3, 3),
  (705841, 4, 7),
  (707649, 1, 0),
  (707934, 7, 3),
  (710641, 2, 7),
  (710936, 0, 3),
  (711588, 6, 3),
  (713982, 1, 3),
  (718234, 4, 7),
  (722443, 4, 7),
  (730499, 2, 7),
  (732183, 0, 7),
  (736037, 3, 7),
  (737784, 7, 1),
  (740622, 7, 3),
  (741090, 7, 3),
  (744915, 6, 7),
  (746753, 3, 7),
  (748845, 0, 0),
  (748921, 6, 2),
  (749382, 3, 3),
  (753912, 4, 6),
  (760168, 6, 4),
  (762157, 6, 7),
  (762560, 4, 3),
  (763032, 5, 7),
  (771929, 3, 7),
  (772600, 7, 0),
  (778539, 7, 7),
  (780772, 4, 6),
  (792280, 1, 4),
  (792450, 5, 2),
  (794172, 2, 4),
  (795448, 3, 3),
  (798154, 1, 7),
  (800853, 3, 7),
  (802031, 5, 6),
  (802442, 3, 2),
  (802788, 0, 0),
  (803735, 2, 5),
  (807478, 4, 3),
  (818735, 7, 7),
  (818814, 4, 6),
  (825086, 4, 5),
  (830571, 5, 3),
  (832533, 6, 3),
  (836161, 3, 7),
  (842560, 1, 7),
  (848913, 6, 4),
  (851055, 1, 3),
  (858202, 1, 4),
  (862827, 3, 5),
  (865642, 5, 3),
  (865817, 6, 7),
  (868598, 4, 5),
  (869043, 5, 2),
  (875531, 2, 7),
  (875746, 5, 6),
  (878541, 5, 2),
  (881968, 7, 6),
  (882472, 5, 4),
  (883947, 0, 6),
  (893663, 0, 7),
  (894237, 5, 1),
  (897805, 7, 0),
  (898210, 0, 7),
  (912226, 5, 6),
  (918618, 4, 7),
  (919885, 2, 7),
  (920936, 7, 5),
  (924779, 6, 0),
  (928673, 2, 3),
  (929624, 5, 4),
  (931028, 6, 0),
  (931033, 6, 3),
  (932174, 0, 3),
  (934015, 7, 0),
  (937298, 3, 7),
  (937553, 4, 3),
  (941753, 2, 3),
  (942060, 2, 5),
  (947089, 7, 0),
  (947698, 0, 7),
  (947773, 7, 6),
  (950296, 2, 1),
  (956595, 0, 0),
  (967169, 7, 7),
  (972990, 2, 6),
  (973968, 3, 3),
  (974719, 0, 0),
  (974923, 1, 3),
  (983905, 1, 4),
  (990463, 2, 3),
  (990792, 7, 2),
  (992969, 1, 7),
  (994644, 7, 0),
  (999366, 0, 0),
  (1001037, 7, 3),
  (1001720, 3, 3),
  (1005037, 2, 3),
  (1015397, 6, 3),
  (1015905, 5, 3),
  (1017395, 2, 7),
  (1021989, 2, 7),
  (1023425, 7, 7),
  (1024597, 2, 7),
  (1025168, 5, 3),
  (1025894, 0, 0),
  (1030221, 6, 7),
  (1030474, 6, 4),
  (1033237, 3, 7),
  (1035584, 7, 0),
  (1037097, 2, 3),
  (1037183, 6, 0),
  (1037833, 3, 1),
  (1042172, 2, 3),
  (1046031, 7, 6),
  (1051595, 6, 0),
  (1060115, 3, 3),
  (1063826, 5, 1),
  (1064759, 3, 3),
  (1067346, 1, 5),
  (1067871, 0, 3),
  (1073678, 2, 7),
  (1078196, 2, 7),
  (1081723, 4, 2),
  (1082936, 5, 3),
  (1083477, 6, 7),
  (1085196, 5, 2),
  (1094539, 3, 6),
  (1095897, 5, 7),
  (1096800, 2, 7),
  (1103840, 5, 6),
  (1104543, 0, 4),
  (1110619, 4, 2),
  (1112723, 0, 7),
  (1118619, 5, 6),
  (1121225, 2, 6),
  (1124193, 0, 0),
  (1125694, 7, 7),
  (1127007, 3, 3),
  (1133799, 2, 6),
  (1139059, 0, 6),
  (1147193, 4, 2),
  (1147704, 4, 3),
  (1148678, 1, 0),
  (1149315, 5, 3),
  (1151890, 1, 0),
  (1155386, 7, 0),
  (1157487, 5, 7),
  (1162347, 6, 0),
  (1164863, 7, 4),
  (1176634, 5, 3),
  (1177594, 5, 1),
  (1182899, 2, 5),
  (1183186, 0, 0),
  (1185131, 4, 2),
  (1186764, 6, 3),
  (1187462, 1, 0),
  (1191308, 0, 0),
  (1199920, 5, 2),
  (1206257, 3, 6),
  (1208279, 0, 7),
  (1209873, 4, 6),
  (1215345, 7, 0),
  (1215483, 3, 7),
  (1215658, 3, 3),
  (1226444, 2, 7),
  (1227343, 2, 3),
  (1231121, 0, 5),
  (1231182, 2, 7),
  (1231389, 6, 7),
  (1236425, 3, 7),
  (1238358, 0, 7),
  (1244992, 6, 7),
  (1245864, 5, 7),
  (1246343, 0, 0),
  (1246756, 0, 0),
  (1250445, 4, 6),
  (1250642, 0, 2),
  (1276028, 5, 6),
  (1279815, 0, 5),
  (1280477, 0, 3),
  (1285788, 1, 7),
  (1289963, 6, 0),
  (1291164, 0, 0),
  (1302969, 7, 0),
  (1303153, 6, 6),
  (1307272, 7, 0),
  (1307883, 2, 3),
  (1309553, 5, 3),
  (1314110, 4, 0),
  (1316417, 7, 7),
  (1317655, 1, 0),
  (1318662, 2, 3),
  (1321729, 3, 3),
  (1325746, 0, 3),
  (1327201, 0, 0),
  (1330916, 5, 3),
  (1332635, 2, 5),
  (1335346, 4, 7),
  (1335977, 0, 7),
  (1345348, 3, 6),
  (1355537, 0, 3),
  (1356461, 1, 0),
  (1359425, 5, 3),
  (1361923, 4, 7),
  (1362720, 2, 7),
  (1370061, 1, 7),
  (1371567, 2, 7),
  (1372252, 6, 0),
  (1372486, 3, 7),
  (1372936, 4, 6),
  (1373477, 7, 6),
  (1382702, 0, 3),
  (1394305, 6, 0),
  (1396598, 4, 3),
  (1398485, 3, 7),
  (1399316, 1, 0),
  (1399894, 3, 7),
  (1402946, 2, 7),
  (1405291, 0, 5),
  (1405832, 5, 2),
  (1407520, 6, 3),
  (1415559, 6, 0),
  (1415647, 6, 6),
  (1415804, 4, 3),
  (1417569, 3, 4),
  (1420190, 5, 3),
  (1424805, 4, 2),
  (1425606, 7, 7),
  (1427040, 2, 3),
  (1431215, 5, 3),
  (1432015, 0, 0),
  (1432958, 3, 7),
  (1435734, 7, 4),
  (1437912, 0, 0),
  (1438688, 3, 7),
  (1444429, 3, 7),
  (1445783, 4, 2),
  (1458035, 1, 7),
  (1469369, 3, 3),
  (1483440, 7, 7),
  (1484669, 2, 2),
  (1488033, 7, 0),
  (1491044, 5, 7),
  (1493473, 4, 7),
  (1495205, 6, 7),
  (1496829, 3, 1),
  (1497199, 5, 1),
  (1498459, 5, 1),
  (1504055, 1, 0),
  (1504954, 3, 7),
  (1507035, 5, 6),
  (1507257, 4, 3),
  (1510405, 4, 5),
  (1518640, 2, 2),
  (1520011, 2, 7),
  (1520987, 2, 2),
  (1521655, 3, 3),
  (1524308, 2, 6),
  (1526983, 3, 7),
  (1527855, 4, 5),
  (1531221, 5, 3),
  (1532786, 3, 7),
  (1533734, 7, 0),
  (1535201, 1, 3),
  (1539116, 3, 3),
  (1539255, 2, 1),
  (1551632, 2, 7),
  (1553058, 7, 0),
  (1554711, 6, 7),
  (1554831, 2, 7),
  (1566581, 4, 7),
  (1567540, 3, 3),
  (1567732, 7, 0),
  (1572836, 4, 3),
  (1574159, 3, 2),
  (1577339, 3, 6),
  (1577814, 5, 3),
  (1579078, 3, 3),
  (1580113, 1, 7),
  (1583229, 6, 0),
  (1588036, 6, 3),
  (1588315, 5, 3),
  (1589405, 5, 7),
  (1590520, 6, 1),
  (1595747, 5, 7),
  (1601651, 5, 2),
  (1602759, 3, 0),
  (1603021, 7, 0),
  (1604098, 1, 7),
  (1604938, 4, 7),
  (1605121, 3, 3),
  (1607124, 6, 7),
  (1610358, 3, 5),
  (1611277, 1, 0),
  (1616119, 7, 0),
  (1617881, 0, 5),
  (1617933, 1, 7),
  (1623575, 4, 7),
  (1624428, 0, 7),
  (1626956, 1, 7),
  (1633783, 5, 5),
  (1637590, 2, 3),
  (1640351, 2, 3),
  (1640670, 1, 7),
  (1644977, 4, 3),
  (1650166, 6, 0),
  (1651705, 0, 7),
  (1652109, 3, 6),
  (1653790, 2, 2),
  (1658277, 0, 7),
  (1659367, 0, 7),
  (1662055, 1, 4),
  (1665664, 0, 3),
  (1665928, 7, 3),
  (1668520, 6, 7),
  (1670316, 6, 4),
  (1670753, 3, 3),
  (1672456, 3, 2),
  (1679751, 6, 7),
  (1681740, 7, 0),
  (1683181, 3, 2),
  (1684055, 0, 3),
  (1684753, 1, 0),
  (1684765, 7, 1),
  (1686169, 7, 4),
  (1688060, 4, 3),
  (1688732, 2, 7),
  (1690354, 4, 7),
  (1692059, 2, 3),
  (1693701, 0, 0),
  (1696119, 1, 0),
  (1699561, 3, 6),
  (1700645, 7, 2),
  (1707535, 5, 3),
  (1721334, 0, 7),
  (1728254, 3, 7),
  (1732043, 2, 3),
  (1733689, 5, 7),
  (1734045, 0, 7),
  (1735308, 6, 0),
  (1737058, 0, 7),
  (1742171, 2, 7),
  (1743339, 7, 7),
  (1743681, 3, 7),
  (1743874, 5, 3),
  (1743896, 2, 6),
  (1744042, 4, 7),
  (1746165, 2, 4),
  (1748177, 2, 2),
  (1748669, 7, 6),
  (1750503, 0, 7),
  (1750869, 0, 0),
  (1752076, 6, 3),
  (1755560, 0, 7),
  (1757175, 4, 4),
  (1758623, 6, 6),
  (1762878, 3, 7),
  (1764151, 2, 2),
  (1764217, 2, 7),
  (1767173, 3, 3),
  (1769261, 3, 3),
  (1772422, 4, 7),
  (1773444, 2, 7),
  (1777980, 0, 0),
  (1781040, 4, 7),
  (1785189, 6, 1),
  (1789352, 5, 3),
  (1796088, 3, 3),
  (1797212, 3, 6),
  (1809284, 2, 7),
  (1811782, 1, 0),
  (1813023, 6, 4),
  (1814890, 1, 0),
  (1815047, 5, 3),
  (1817090, 7, 4),
  (1824216, 1, 7),
  (1832879, 0, 2),
  (1833489, 1, 7),
  (1834098, 7, 3),
  (1836069, 2, 5),
  (1836720, 1, 0),
  (1839766, 2, 3),
  (1844169, 6, 7),
  (1848060, 4, 2),
  (1856027, 1, 7),
  (1856785, 7, 7),
  (1859990, 3, 7),
  (1864781, 4, 3),
  (1871622, 3, 6),
  (1874827, 7, 7),
  (1876884, 3, 6),
  (1878408, 3, 6),
  (1881723, 5, 7),
  (1883798, 6, 3),
  (1884796, 4, 2),
  (1888213, 6, 0),
  (1892199, 1, 3),
  (1896132, 5, 7),
  (1900853, 5, 7),
  (1903349, 6, 7),
  (1903719, 6, 0),
  (1906221, 6, 6),
  (1909216, 3, 2),
  (1909497, 3, 3),
  (1914637, 1, 4),
  (1915166, 3, 3),
  (1918209, 4, 1),
  (1921003, 1, 0),
  (1924971, 3, 3),
  (1933263, 7, 0),
  (1933637, 3, 3),
  (1934384, 7, 0),
  (1934716, 5, 7),
  (1938268, 6, 7),
  (1940301, 3, 1),
  (1940710, 5, 3),
  (1954410, 7, 7),
  (1960057, 1, 4),
  (1961596, 1, 4),
  (1963162, 6, 0),
  (1968290, 2, 0),
  (1976433, 0, 3),
  (1978334, 2, 2),
  (1983943, 1, 0),
  (1986899, 4, 2),
  (1989527, 6, 0),
  (1990589, 3, 6),
  (1991164, 3, 3),
  (1994015, 0, 0),
  (1997924, 5, 7),
  (1999949, 4, 3),
  (2003981, 2, 6),
  (2004057, 2, 6),
  (2006114, 3, 5),
  (2011484, 6, 7),
  (2014051, 0, 7),
  (2015644, 2, 3),
  (2017038, 6, 7),
  (2018419, 5, 1),
  (2020397, 2, 3),
  (2022068, 5, 5),
  (2023283, 3, 6),
  (2039126, 4, 3),
  (2039955, 6, 0),
  (2041140, 5, 3),
  (2049850, 6, 7),
  (2049878, 0, 0),
  (2050009, 6, 4),
  (2053659, 1, 0),
  (2058012, 4, 4),
  (2061936, 6, 3),
  (2072435, 3, 2),
  (2073386, 3, 6),
  (2074876, 4, 4),
  (2077450, 2, 1),
  (2080602, 3, 5),
  (2081636, 7, 7),
  (2082189, 2, 7),
  (2088687, 2, 5),
  (2088710, 4, 4),
  (2091456, 5, 6),
  (2096638, 2, 4),
  (2099147, 1, 7),
  (2102151, 3, 7),
  (2102232, 1, 0),
  (2103272, 1, 3),
  (2112098, 0, 4),
  (2112297, 1, 6),
  (2114408, 6, 0),
  (2116687, 2, 5),
  (2118747, 7, 7),
  (2124941, 0, 7),
  (2126846, 0, 4),
  (2128993, 3, 1),
  (2129515, 6, 3),
  (2130596, 7, 0),
  (2134315, 2, 3),
  (2137081, 2, 0),
  (2142818, 5, 7),
  (2145459, 4, 2),
  (2147416, 5, 2),
  (2157492, 2, 3),
  (2159675, 6, 1),
  (2170869, 4, 3),
  (2173357, 3, 3),
  (2176514, 6, 4),
  (2183947, 5, 7),
  (2187819, 0, 6),
  (2188761, 0, 6),
  (2192320, 7, 4),
  (2194542, 7, 4),
  (2196149, 5, 3),
  (2196889, 6, 0),
  (2200303, 4, 3),
  (2201816, 7, 4),
  (2203504, 3, 3),
  (2205974, 4, 6),
  (2208324, 2, 3),
  (2211858, 2, 3),
  (2214916, 5, 3),
  (2217845, 2, 1),
  (2218694, 0, 7),
  (2219543, 1, 0),
  (2222569, 1, 0),
  (2224509, 7, 7),
  (2234702, 5, 7),
  (2240176, 6, 0),
  (2240616, 0, 3),
  (2245629, 1, 0),
  (2251843, 2, 7),
  (2253228, 0, 3),
  (2266000, 5, 7),
  (2267620, 7, 0),
  (2270964, 1, 6),
  (2274256, 6, 4),
  (2275983, 5, 3),
  (2281003, 7, 0),
  (2284872, 6, 0),
  (2286356, 4, 3),
  (2291553, 0, 5),
  (2293747, 3, 7),
  (2294769, 1, 7),
  (2295950, 0, 4),
  (2297128, 7, 4),
  (2298904, 4, 3),
  (2301485, 4, 7),
  (2301495, 5, 7),
  (2302929, 2, 5),
  (2309388, 5, 3),
  (2310107, 2, 7),
  (2310818, 0, 7),
  (2311078, 5, 7),
  (2314490, 0, 7),
  (2326895, 2, 7),
  (2327643, 6, 3),
  (2329213, 2, 7),
  (2330287, 3, 7),
  (2332648, 0, 0),
  (2333228, 3, 5),
  (2333664, 2, 2),
  (2342740, 5, 7),
  (2345174, 3, 2),
  (2354375, 4, 2),
  (2355112, 5, 2),
  (2359459, 5, 1),
  (2363801, 1, 0),
  (2379843, 0, 0),
  (2393473, 4, 7),
  (2394836, 5, 2),
  (2402137, 6, 7),
  (2402776, 2, 6),
  (2404309, 1, 5),
  (2407290, 6, 0),
  (2412980, 4, 3),
  (2414543, 4, 2),
  (2419937, 4, 5),
  (2420164, 6, 0),
  (2421111, 1, 3),
  (2422144, 6, 6),
  (2422243, 7, 7),
  (2423920, 3, 5),
  (2425517, 7, 0),
  (2427771, 7, 4),
  (2436512, 5, 2),
  (2439650, 4, 2),
  (2448701, 5, 2),
  (2450226, 5, 7),
  (2452720, 7, 0),
  (2455904, 7, 0),
  (2458339, 3, 3),
  (2458878, 7, 7),
  (2465942, 2, 7),
  (2478713, 3, 7),
  (2478857, 3, 3),
  (2479784, 2, 3),
  (2484364, 2, 7),
  (2484594, 1, 0),
  (2485832, 1, 2),
  (2487106, 2, 3),
  (2487914, 2, 6),
  (2487977, 1, 7),
  (2488863, 0, 0),
  (2493549, 3, 7),
  (2497115, 1, 2),
  (2502000, 5, 3),
  (2507361, 3, 2),
  (2509998, 0, 7),
  (2510181, 1, 7),
  (2512930, 0, 1),
  (2518691, 5, 2),
  (2523683, 5, 7),
  (2524413, 6, 7),
  (2529879, 6, 4),
  (2534428, 6, 7),
  (2534985, 1, 0),
  (2537789, 5, 7),
  (2543388, 4, 3),
  (2544376, 6, 3),
  (2546299, 2, 7),
  (2547865, 5, 7),
  (2552125, 6, 4),
  (2553041, 2, 7),
  (2558331, 0, 0),
  (2558984, 6, 6),
  (2561046, 2, 0),
  (2567810, 0, 7),
  (2568662, 1, 6),
  (2573091, 0, 3),
  (2574892, 0, 4),
  (2576371, 4, 7),
  (2578041, 2, 7),
  (2580998, 4, 7),
  (2583350, 2, 6),
  (2589332, 6, 7),
  (2592520, 2, 7),
  (2593043, 6, 0),
  (2596924, 5, 2),
  (2601434, 3, 3),
  (2602980, 4, 4),
  (2603730, 6, 3),
  (2606865, 1, 2),
  (2611800, 4, 5),
  (2612754, 0, 7),
  (2613244, 2, 5),
  (2613680, 2, 6),
  (2615827, 7, 7),
  (2621443, 1, 7),
  (2621520, 6, 0),
  (2627458, 6, 7),
  (2627517, 2, 2),
  (2629120, 1, 4),
  (2634334, 4, 3),
  (2640504, 3, 6),
  (2649004, 3, 3),
  (2652296, 6, 3),
  (2652778, 4, 7),
  (2655352, 7, 7),
  (2661942, 2, 3),
  (2676643, 1, 5),
  (2678102, 4, 2),
  (2680772, 6, 0),
  (2682451, 0, 0),
  (2682607, 2, 4),
  (2691211, 0, 7),
  (2696137, 3, 0),
  (2697736, 0, 4),
  (2698588, 3, 3),
  (2704392, 5, 3),
  (2712759, 5, 4),
  (2719968, 1, 5),
  (2722922, 3, 3),
  (2727318, 7, 0),
  (2731105, 2, 6),
  (2731931, 4, 3),
  (2745051, 3, 6),
  (2753204, 2, 7),
  (2757640, 2, 6),
  (2759869, 2, 2),
  (2764068, 4, 7),
  (2768579, 6, 0),
  (2773553, 1, 0),
  (2776700, 1, 0),
  (2777508, 5, 6),
  (2779594, 2, 2),
  (2780986, 1, 7),
  (2781634, 3, 5),
  (2782001, 5, 6),
  (2784515, 0, 0),
  (2788066, 5, 5),
  (2788143, 4, 7),
  (2796317, 5, 0),
  (2800829, 0, 0),
  (2805044, 0, 6),
  (2806089, 2, 1),
  (2806362, 6, 0),
  (2807921, 2, 6),
  (2809973, 1, 5),
  (2810430, 1, 0),
  (2812445, 0, 0),
  (2827149, 5, 3),
  (2835165, 7, 7),
  (2836073, 2, 2),
  (2839041, 5, 7),
  (2841658, 4, 6),
  (2843977, 7, 4),
  (2847193, 6, 0),
  (2850003, 0, 0),
  (2852182, 5, 2),
  (2854395, 6, 5),
  (2855637, 0, 3),
  (2857326, 5, 7),
  (2857876, 5, 2),
  (2858228, 3, 7),
  (2869770, 7, 3),
  (2870465, 0, 7),
  (2871267, 5, 3),
  (2872954, 6, 7),
  (2874901, 3, 3),
  (2875513, 0, 7),
  (2875942, 6, 0),
  (2878737, 5, 5),
  (2882135, 1, 7),
  (2885111, 7, 7),
  (2886111, 2, 7),
  (2894179, 1, 7),
  (2898068, 6, 7),
  (2908400, 7, 7),
  (2909342, 2, 7),
  (2910697, 2, 3),
  (2914084, 6, 7),
  (2914837, 0, 4),
  (2916512, 3, 7),
  (2917208, 3, 7),
  (2919585, 3, 7),
  (2921287, 5, 3),
  (2921515, 4, 1),
  (2921902, 1, 4),
  (2929062, 5, 6),
  (2933816, 5, 7),
  (2940162, 5, 3),
  (2943848, 3, 6),
  (2944200, 3, 2),
  (2945111, 4, 3),
  (2946571, 5, 3),
  (2956758, 0, 7),
  (2962480, 3, 3),
  (2964390, 4, 2),
  (2972212, 2, 2),
  (2975761, 4, 7),
  (2987764, 2, 7),
  (2989601, 6, 6),
  (2993116, 6, 6),
  (2994673, 3, 6),
  (2996203, 4, 6),
  (3005887, 6, 0),
  (3007189, 4, 6),
  (3015410, 7, 7),
  (3015853, 5, 7),
  (3020031, 4, 2),
  (3020529, 5, 2),
  (3023118, 4, 5),
  (3025059, 4, 3),
  (3028659, 5, 7),
  (3028804, 1, 2),
  (3033220, 3, 7),
  (3036835, 1, 0),
  (3039099, 1, 0),
  (3039748, 3, 7),
  (3041644, 1, 5),
  (3044840, 1, 2),
  (3045609, 7, 3),
  (3059365, 3, 7),
  (3065356, 0, 6),
  (3065502, 0, 7),
  (3068354, 5, 2),
  (3069214, 0, 7),
  (3069370, 2, 3),
  (3069618, 0, 3),
  (3071261, 0, 0),
  (3071419, 4, 3),
  (3073721, 1, 0),
  (3074164, 2, 3),
  (3079590, 6, 3),
  (3081450, 6, 0),
  (3083580, 4, 6),
  (3084184, 6, 3),
  (3084370, 6, 7),
  (3084697, 4, 3),
  (3085573, 4, 5),
  (3089949, 2, 2),
  (3089955, 7, 6),
  (3092164, 4, 2),
  (3094954, 5, 4),
  (3100635, 1, 4),
  (3106487, 3, 2),
  (3107970, 0, 7),
  (3111606, 0, 7),
  (3113935, 6, 7),
  (3116968, 0, 0),
  (3118731, 5, 6),
  (3120735, 4, 3),
  (3123177, 4, 6),
  (3134592, 2, 7),
  (3137477, 3, 7),
  (3141041, 7, 7),
  (3141964, 4, 3),
  (3145419, 4, 3),
  (3149436, 3, 2),
  (3150349, 5, 3),
  (3152947, 6, 0),
  (3160291, 3, 2),
  (3164070, 6, 7),
  (3167054, 0, 7),
  (3168403, 6, 7),
  (3170498, 5, 5),
  (3170761, 0, 3),
  (3175788, 6, 7),
  (3181497, 2, 3),
  (3182778, 3, 5),
  (3183808, 7, 4),
  (3184828, 6, 0),
  (3187412, 6, 0),
  (3189036, 2, 7),
  (3189589, 2, 3),
  (3201808, 2, 7),
  (3206729, 7, 5),
  (3211078, 2, 7),
  (3212438, 7, 0),
  (3212933, 1, 7),
  (3215128, 5, 2),
  (3221562, 5, 7),
  (3224776, 5, 2),
  (3226482, 3, 7),
  (3229422, 6, 7),
  (3230012, 5, 2),
  (3232582, 5, 7),
  (3233068, 3, 6),
  (3246151, 4, 5),
  (3248436, 0, 4),
  (3251071, 2, 5),
  (3252598, 2, 7),
  (3253939, 1, 0),
  (3260853, 7, 0),
  (3261252, 7, 7),
  (3266610, 6, 6),
  (3266867, 4, 3),
  (3274892, 6, 3),
  (3277245, 5, 5),
  (3278829, 2, 4),
  (3279258, 5, 7),
  (3279800, 5, 7),
  (3281652, 7, 7),
  (3281926, 2, 3),
  (3283770, 5, 7),
  (3286737, 1, 3),
  (3287104, 5, 7),
  (3287548, 0, 3),
  (3289692, 0, 7),
  (3291944, 3, 1),
  (3294855, 6, 3),
  (3295661, 2, 7),
  (3299172, 7, 7),
  (3301302, 1, 0),
  (3311849, 1, 0),
  (3312613, 2, 5),
  (3317640, 6, 6),
  (3319412, 3, 7),
  (3326688, 5, 2),
  (3328553, 7, 3),
  (3331543, 1, 2),
  (3331939, 0, 0),
  (3331968, 7, 7),
  (3332045, 0, 0),
  (3334278, 7, 0),
  (3334289, 2, 5),
  (3337732, 6, 7),
  (3337803, 5, 2),
  (3341476, 7, 7),
  (3342012, 0, 3),
  (3347931, 2, 7),
  (3349108, 0, 0),
  (3352083, 0, 3),
  (3352463, 0, 4),
  (3356710, 1, 0),
  (3359565, 2, 6),
  (3360281, 3, 3),
  (3362468, 4, 2),
  (3364989, 3, 2),
  (3365022, 3, 6),
  (3368119, 7, 0),
  (3373191, 3, 7),
  (3375173, 5, 3),
  (3377280, 4, 3),
  (3379151, 5, 2),
  (3379239, 3, 7),
  (3379934, 6, 6),
  (3383817, 2, 4),
  (3387409, 6, 3),
  (3387487, 0, 7),
  (3391268, 0, 7),
  (3392546, 3, 2),
  (3394220, 1, 3),
  (3394892, 4, 7),
  (3397199, 1, 4),
  (3398237, 2, 2),
  (3398590, 6, 7),
  (3399130, 0, 7),
  (3402713, 2, 7),
  (3404927, 0, 3),
  (3406279, 4, 2),
  (3408563, 5, 3),
  (3410512, 1, 0),
  (3416248, 2, 3),
  (3416504, 5, 7),
  (3417835, 7, 7),
  (3419805, 6, 7),
  (3420004, 3, 7),
  (3426134, 5, 1),
  (3427046, 6, 0),
  (3429724, 5, 3),
  (3429731, 6, 4),
  (3439602, 0, 0),
  (3441691, 4, 4),
  (3441984, 5, 3),
  (3445514, 3, 7),
  (3449796, 2, 3),
  (3451112, 5, 3),
  (3461233, 0, 3),
  (3464975, 0, 3),
  (3467420, 3, 7),
  (3473365, 4, 7),
  (3475340, 6, 3),
  (3481147, 6, 7),
  (3488485, 4, 7),
  (3488729, 4, 6),
  (3491404, 6, 7),
  (3491522, 2, 7),
  (3493572, 5, 6),
  (3495247, 4, 1),
  (3496201, 4, 6),
  (3497641, 7, 7),
  (3503610, 3, 6),
  (3507902, 1, 0),
  (3510180, 6, 0),
  (3512167, 6, 0),
  (3512217, 3, 5),
  (3516137, 1, 7),
  (3524007, 3, 7),
  (3526184, 6, 4),
  (3532518, 2, 1),
  (3545230, 4, 4),
  (3547142, 7, 4),
  (3560206, 7, 7),
  (3562713, 6, 6),
  (3569241, 7, 0),
  (3570434, 6, 4),
  (3572775, 7, 0),
  (3575497, 0, 2),
  (3577129, 6, 7),
  (3577494, 4, 3),
  (3578379, 0, 2),
  (3579105, 1, 5),
  (3581441, 7, 7),
  (3586855, 1, 0),
  (3590430, 5, 3),
  (3593546, 4, 7),
  (3595152, 2, 6),
  (3596778, 4, 6),
  (3598611, 2, 7),
  (3598839, 3, 3),
  (3599652, 6, 0),
])