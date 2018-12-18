from src.util import *
schedule = deque([
  (5022, 0, 1),
  (6276, 3, 0),
  (7745, 0, 1),
  (10467, 1, 1),
  (12206, 1, 0),
  (17480, 0, 1),
  (20380, 2, 1),
  (21055, 2, 0),
  (33575, 1, 1),
  (36497, 3, 1),
  (38742, 0, 0),
  (40102, 1, 1),
  (52802, 3, 1),
  (57322, 2, 1),
  (60892, 3, 0),
  (61223, 2, 2),
  (63604, 3, 2),
  (65105, 2, 0),
  (74986, 1, 0),
  (75595, 2, 0),
  (82950, 2, 1),
  (85011, 1, 2),
  (86294, 0, 0),
  (89619, 0, 1),
  (91531, 0, 1),
  (93251, 0, 0),
  (98374, 0, 1),
  (98633, 2, 1),
  (101704, 0, 2),
  (101714, 0, 0),
  (106183, 3, 0),
  (108112, 3, 0),
  (109064, 2, 1),
  (112679, 1, 2),
  (116492, 1, 1),
  (118264, 2, 0),
  (118539, 0, 1),
  (118743, 2, 0),
  (119791, 0, 0),
  (125426, 3, 1),
  (127505, 3, 0),
  (130224, 0, 2),
  (131241, 2, 1),
  (135872, 3, 0),
  (139490, 3, 2),
  (141249, 2, 1),
  (144813, 2, 2),
  (145449, 1, 1),
  (145618, 2, 2),
  (147285, 3, 2),
  (151534, 0, 1),
  (151783, 3, 0),
  (151795, 1, 1),
  (156079, 3, 1),
  (157106, 1, 0),
  (159090, 1, 2),
  (162033, 3, 0),
  (162125, 2, 1),
  (163022, 1, 1),
  (165209, 1, 1),
  (165407, 2, 2),
  (170432, 3, 1),
  (171910, 2, 2),
  (173797, 2, 2),
  (174231, 3, 1),
  (174991, 3, 1),
  (179373, 3, 1),
  (179822, 2, 2),
  (184862, 2, 2),
  (185236, 3, 1),
  (187030, 3, 0),
  (194595, 0, 1),
  (195615, 3, 0),
  (214083, 3, 2),
  (221425, 1, 0),
  (225672, 2, 1),
  (226540, 3, 1),
  (227071, 3, 0),
  (227914, 1, 2),
  (229881, 3, 0),
  (230057, 3, 0),
  (231505, 2, 0),
  (233641, 2, 2),
  (233986, 3, 1),
  (234398, 0, 1),
  (240009, 3, 2),
  (241972, 1, 2),
  (246180, 1, 2),
  (251568, 2, 0),
  (252226, 3, 0),
  (254563, 2, 1),
  (255156, 0, 2),
  (256071, 3, 0),
  (256353, 1, 0),
  (259611, 1, 2),
  (261930, 1, 0),
  (265964, 1, 0),
  (267782, 1, 1),
  (270262, 0, 0),
  (272484, 1, 0),
  (276424, 1, 2),
  (281032, 2, 1),
  (284724, 2, 2),
  (285285, 0, 2),
  (288702, 2, 2),
  (289679, 1, 2),
  (294668, 2, 1),
  (296447, 1, 1),
  (297703, 1, 1),
  (297933, 2, 0),
  (299351, 3, 0),
  (301091, 0, 1),
  (301408, 2, 0),
  (304397, 0, 1),
  (304966, 3, 0),
  (305110, 0, 1),
  (310590, 2, 0),
  (316783, 2, 0),
  (317244, 0, 2),
  (328848, 3, 2),
  (331382, 1, 0),
  (333069, 2, 0),
  (337969, 0, 0),
  (338390, 0, 0),
  (338712, 1, 2),
  (345895, 1, 2),
  (348038, 0, 2),
  (351983, 3, 1),
  (357806, 3, 0),
  (362517, 0, 0),
  (365714, 3, 1),
  (367625, 1, 0),
  (370002, 0, 1),
  (370917, 0, 1),
  (373589, 1, 0),
  (377223, 3, 2),
  (378486, 2, 1),
  (380153, 1, 2),
  (387713, 1, 0),
  (388112, 3, 1),
  (390228, 0, 2),
  (391081, 1, 2),
  (398087, 2, 2),
  (400886, 2, 2),
  (402325, 3, 0),
  (403454, 0, 0),
  (411979, 3, 0),
  (417427, 1, 0),
  (418859, 3, 0),
  (423005, 3, 0),
  (431847, 1, 2),
  (435978, 2, 0),
  (441552, 0, 2),
  (441790, 1, 0),
  (445497, 1, 1),
  (450491, 3, 0),
  (453106, 1, 2),
  (454002, 3, 2),
  (454435, 3, 2),
  (457361, 1, 2),
  (465617, 2, 1),
  (466071, 1, 1),
  (468049, 1, 0),
  (469012, 0, 0),
  (474807, 0, 2),
  (475668, 2, 0),
  (478138, 2, 0),
  (478252, 1, 0),
  (481890, 1, 1),
  (485438, 0, 0),
  (488013, 3, 1),
  (488953, 3, 2),
  (489831, 3, 2),
  (491367, 3, 1),
  (491560, 3, 0),
  (506263, 1, 0),
  (506536, 1, 1),
  (507599, 0, 0),
  (508154, 0, 1),
  (512354, 1, 0),
  (512481, 1, 2),
  (512569, 2, 2),
  (514548, 1, 2),
  (519946, 3, 1),
  (521431, 1, 0),
  (523122, 2, 2),
  (524929, 3, 0),
  (526469, 3, 2),
  (530282, 3, 0),
  (533692, 3, 1),
  (534005, 1, 1),
  (535201, 2, 2),
  (537014, 2, 0),
  (541384, 3, 2),
  (543195, 2, 1),
  (549785, 0, 0),
  (552566, 2, 0),
  (552919, 0, 2),
  (553318, 1, 0),
  (555591, 0, 2),
  (556603, 2, 1),
  (557869, 1, 0),
  (559847, 0, 1),
  (562916, 2, 0),
  (563317, 0, 1),
  (567200, 2, 1),
  (571604, 2, 0),
  (572786, 2, 0),
  (576972, 2, 1),
  (578193, 2, 0),
  (581282, 0, 1),
  (581376, 1, 0),
  (588265, 3, 1),
  (588635, 0, 0),
  (594077, 3, 0),
  (596862, 1, 0),
  (597268, 2, 2),
  (597769, 1, 0),
  (604523, 1, 0),
  (607751, 3, 0),
  (609268, 2, 2),
  (609967, 2, 2),
  (612311, 1, 1),
  (612708, 3, 0),
  (613101, 0, 2),
  (617376, 2, 2),
  (627839, 2, 1),
  (630124, 3, 2),
  (635997, 3, 1),
  (638325, 0, 2),
  (640997, 0, 2),
  (642734, 0, 1),
  (646975, 1, 2),
  (648369, 2, 0),
  (649520, 3, 2),
  (650526, 2, 0),
  (650531, 2, 2),
  (650989, 0, 1),
  (653371, 0, 0),
  (654042, 2, 0),
  (660125, 2, 0),
  (663375, 2, 1),
  (665435, 3, 0),
  (667443, 1, 0),
  (673026, 1, 0),
  (683967, 0, 0),
  (685521, 2, 2),
  (689729, 2, 0),
  (690574, 2, 0),
  (691068, 3, 1),
  (697713, 2, 2),
  (698830, 3, 2),
  (699359, 1, 0),
  (707025, 0, 2),
  (717090, 0, 0),
  (717499, 3, 1),
  (719283, 0, 0),
  (721290, 2, 1),
  (725752, 0, 2),
  (728089, 0, 2),
  (729969, 3, 1),
  (730183, 1, 2),
  (730875, 2, 2),
  (740098, 2, 0),
  (743184, 3, 2),
  (746321, 2, 2),
  (747506, 2, 0),
  (747920, 2, 0),
  (750956, 0, 1),
  (752060, 1, 1),
  (755701, 1, 2),
  (760570, 0, 2),
  (760701, 0, 0),
  (761334, 1, 0),
  (762565, 1, 1),
  (762716, 2, 1),
  (762845, 3, 0),
  (771370, 2, 0),
  (771724, 1, 1),
  (773904, 3, 0),
  (776759, 2, 0),
  (779127, 1, 0),
  (781871, 0, 0),
  (786720, 2, 0),
  (789699, 2, 0),
  (790345, 2, 2),
  (793640, 1, 1),
  (794673, 0, 0),
  (799148, 0, 1),
  (803815, 1, 0),
  (804868, 1, 0),
  (809815, 1, 2),
  (821121, 2, 2),
  (825068, 3, 2),
  (829049, 2, 2),
  (833592, 3, 2),
  (839333, 0, 2),
  (845202, 3, 1),
  (847407, 0, 0),
  (852360, 0, 1),
  (853140, 2, 1),
  (853299, 3, 2),
  (857015, 2, 0),
  (860330, 0, 0),
  (861889, 0, 1),
  (863816, 3, 0),
  (868434, 0, 2),
  (869796, 3, 1),
  (872009, 0, 1),
  (872943, 0, 2),
  (874819, 0, 0),
  (877557, 2, 1),
  (877901, 2, 2),
  (881145, 1, 2),
  (882976, 1, 2),
  (885488, 1, 0),
  (885868, 1, 2),
  (887399, 3, 2),
  (890552, 1, 1),
  (892088, 1, 1),
  (909304, 1, 1),
  (910329, 1, 1),
  (910899, 3, 0),
  (918630, 0, 0),
  (920419, 1, 1),
  (921480, 2, 1),
  (921544, 2, 0),
  (929332, 0, 1),
  (932016, 2, 0),
  (936969, 3, 0),
  (937376, 2, 2),
  (937777, 2, 2),
  (938842, 2, 0),
  (939861, 3, 0),
  (940628, 0, 0),
  (943319, 2, 2),
  (943365, 2, 1),
  (943568, 3, 2),
  (953155, 1, 2),
  (958486, 0, 0),
  (958831, 2, 1),
  (959998, 3, 2),
  (960033, 1, 1),
  (964128, 3, 0),
  (971711, 3, 1),
  (972803, 1, 2),
  (973700, 1, 1),
  (978351, 2, 2),
  (981462, 3, 2),
  (982943, 2, 0),
  (984041, 3, 2),
  (984645, 3, 2),
  (988737, 3, 2),
  (990984, 3, 1),
  (1001934, 2, 2),
  (1014820, 2, 0),
  (1017798, 2, 0),
  (1023171, 3, 2),
  (1030696, 2, 0),
  (1035817, 3, 2),
  (1037671, 2, 1),
  (1037701, 0, 0),
  (1040690, 3, 0),
  (1040996, 2, 0),
  (1044122, 3, 2),
  (1049963, 2, 1),
  (1050398, 3, 0),
  (1051432, 3, 1),
  (1051588, 3, 2),
  (1060684, 1, 1),
  (1060863, 3, 1),
  (1067114, 2, 1),
  (1067551, 1, 0),
  (1078167, 0, 2),
  (1082246, 2, 0),
  (1085308, 2, 0),
  (1088511, 1, 1),
  (1091315, 3, 1),
  (1092419, 1, 2),
  (1093868, 1, 2),
  (1095580, 2, 2),
  (1099461, 0, 2),
  (1099994, 2, 1),
  (1104953, 0, 1),
  (1106537, 0, 0),
  (1107668, 1, 2),
  (1114475, 3, 1),
  (1115869, 1, 1),
  (1116481, 0, 2),
  (1122043, 0, 0),
  (1122536, 1, 2),
  (1123726, 2, 1),
  (1125312, 0, 2),
  (1126972, 0, 1),
  (1127197, 1, 0),
  (1135629, 2, 2),
  (1137105, 0, 1),
  (1137269, 3, 2),
  (1141717, 2, 1),
  (1142106, 0, 2),
  (1148179, 3, 1),
  (1153421, 0, 2),
  (1156490, 1, 2),
  (1162504, 1, 2),
  (1164565, 0, 1),
  (1170551, 0, 2),
  (1171045, 0, 2),
  (1173753, 0, 0),
  (1176687, 3, 2),
  (1185459, 3, 2),
  (1185705, 3, 1),
  (1191358, 0, 0),
  (1191570, 3, 2),
  (1194541, 1, 0),
  (1194817, 2, 1),
  (1196691, 2, 2),
  (1196905, 0, 2),
  (1201670, 2, 1),
  (1203850, 0, 0),
  (1204030, 3, 2),
  (1214610, 2, 1),
  (1228631, 1, 1),
  (1228662, 0, 1),
  (1231310, 3, 1),
  (1233104, 1, 0),
  (1233786, 1, 1),
  (1236862, 2, 1),
  (1238704, 3, 1),
  (1241576, 1, 1),
  (1245614, 3, 2),
  (1249853, 0, 2),
  (1250947, 2, 2),
  (1251695, 2, 1),
  (1254764, 1, 0),
  (1262206, 3, 1),
  (1266396, 0, 0),
  (1271957, 3, 2),
  (1272965, 0, 0),
  (1277500, 0, 1),
  (1278018, 0, 1),
  (1280160, 0, 0),
  (1282598, 1, 0),
  (1283092, 0, 1),
  (1284294, 0, 1),
  (1287402, 1, 1),
  (1288337, 1, 1),
  (1288467, 2, 0),
  (1291752, 0, 0),
  (1292106, 1, 0),
  (1293292, 1, 0),
  (1295129, 2, 2),
  (1295871, 1, 2),
  (1297366, 2, 1),
  (1298390, 0, 2),
  (1304534, 0, 0),
  (1314663, 0, 2),
  (1317698, 2, 1),
  (1325717, 0, 1),
  (1328428, 1, 2),
  (1330372, 2, 2),
  (1336010, 0, 1),
  (1339851, 0, 1),
  (1347227, 1, 0),
  (1347262, 3, 0),
  (1348741, 2, 2),
  (1352630, 0, 2),
  (1358709, 3, 1),
  (1364021, 0, 1),
  (1364151, 0, 1),
  (1366509, 0, 0),
  (1367936, 3, 0),
  (1369676, 3, 2),
  (1377001, 3, 1),
  (1377260, 3, 2),
  (1377456, 2, 1),
  (1378227, 0, 1),
  (1381362, 3, 2),
  (1381586, 0, 0),
  (1382589, 2, 2),
  (1385128, 0, 0),
  (1387672, 2, 2),
  (1389411, 3, 1),
  (1390039, 0, 1),
  (1390061, 2, 2),
  (1391253, 0, 1),
  (1398908, 3, 0),
  (1399887, 3, 1),
  (1402908, 2, 1),
  (1405627, 1, 0),
  (1412141, 3, 2),
  (1413646, 2, 0),
  (1416789, 3, 1),
  (1420363, 2, 0),
  (1424275, 0, 2),
  (1426194, 0, 1),
  (1428049, 2, 1),
  (1430759, 0, 1),
  (1433208, 0, 1),
  (1434487, 2, 2),
  (1434780, 3, 1),
  (1435957, 1, 0),
  (1439548, 3, 0),
  (1443044, 3, 1),
  (1446698, 3, 2),
  (1454704, 0, 1),
  (1462619, 1, 1),
  (1466905, 0, 1),
  (1467945, 0, 1),
  (1470983, 0, 0),
  (1472971, 2, 1),
  (1474170, 2, 0),
  (1476275, 0, 2),
  (1478930, 3, 1),
  (1481553, 0, 0),
  (1482445, 2, 0),
  (1485449, 0, 0),
  (1485717, 2, 0),
  (1486207, 1, 2),
  (1493186, 3, 2),
  (1493905, 0, 0),
  (1498764, 0, 0),
  (1500872, 0, 1),
  (1510310, 3, 2),
  (1512313, 3, 2),
  (1523541, 1, 2),
  (1529866, 2, 2),
  (1532733, 2, 2),
  (1537250, 1, 0),
  (1538452, 0, 2),
  (1545420, 2, 2),
  (1547639, 3, 0),
  (1548849, 0, 1),
  (1549032, 2, 1),
  (1550797, 1, 2),
  (1552646, 2, 2),
  (1558863, 1, 2),
  (1562283, 3, 2),
  (1562824, 1, 1),
  (1564017, 3, 0),
  (1569601, 3, 1),
  (1569755, 3, 0),
  (1572800, 2, 0),
  (1575189, 3, 0),
  (1586129, 1, 1),
  (1590830, 2, 0),
  (1595953, 2, 0),
  (1597933, 3, 0),
  (1602354, 3, 0),
  (1604848, 0, 1),
  (1605081, 2, 1),
  (1605601, 3, 2),
  (1611106, 0, 1),
  (1614344, 3, 2),
  (1617620, 2, 1),
  (1627779, 2, 2),
  (1630280, 3, 2),
  (1632575, 2, 2),
  (1636785, 2, 2),
  (1639022, 1, 1),
  (1639660, 0, 0),
  (1642347, 2, 0),
  (1642655, 1, 1),
  (1643855, 1, 0),
  (1647505, 2, 2),
  (1647794, 3, 1),
  (1651359, 3, 1),
  (1660177, 1, 1),
  (1666567, 2, 1),
  (1666778, 3, 1),
  (1676094, 3, 1),
  (1678712, 3, 2),
  (1679494, 3, 2),
  (1679598, 1, 2),
  (1685425, 1, 0),
  (1688487, 0, 2),
  (1688829, 0, 0),
  (1696892, 1, 1),
  (1697174, 3, 1),
  (1698311, 2, 0),
  (1698556, 0, 2),
  (1701226, 3, 2),
  (1712656, 1, 2),
  (1716040, 2, 1),
  (1716427, 1, 1),
  (1721325, 0, 1),
  (1721781, 0, 0),
  (1723495, 1, 1),
  (1724981, 0, 1),
  (1725991, 3, 0),
  (1726452, 2, 0),
  (1737456, 3, 2),
  (1737580, 1, 1),
  (1738785, 1, 2),
  (1740070, 1, 2),
  (1741062, 3, 1),
  (1741420, 3, 0),
  (1743365, 1, 0),
  (1744019, 3, 2),
  (1744560, 3, 1),
  (1746961, 3, 1),
  (1749637, 3, 1),
  (1750144, 0, 1),
  (1755962, 2, 0),
  (1756917, 3, 0),
  (1759453, 3, 2),
  (1762789, 1, 1),
  (1764358, 3, 2),
  (1764406, 2, 0),
  (1765701, 0, 1),
  (1769901, 2, 1),
  (1773540, 0, 1),
  (1775478, 0, 2),
  (1778517, 2, 0),
  (1779802, 2, 2),
  (1784317, 3, 2),
  (1798226, 1, 2),
  (1798672, 0, 1),
  (1807761, 2, 1),
  (1809383, 0, 2),
  (1814463, 1, 0),
  (1822345, 2, 2),
  (1825908, 3, 1),
  (1837696, 1, 1),
  (1845752, 0, 0),
  (1847457, 0, 2),
  (1847753, 1, 2),
  (1848501, 0, 2),
  (1849094, 0, 2),
  (1854228, 2, 2),
  (1854510, 0, 2),
  (1858775, 1, 1),
  (1863652, 0, 2),
  (1868114, 2, 1),
  (1871974, 3, 0),
  (1872485, 2, 2),
  (1873602, 1, 1),
  (1878968, 0, 2),
  (1882563, 2, 1),
  (1883914, 3, 1),
  (1888915, 0, 2),
  (1889569, 0, 1),
  (1891625, 2, 2),
  (1895479, 3, 0),
  (1897784, 2, 0),
  (1897797, 3, 2),
  (1898728, 3, 0),
  (1900142, 2, 1),
  (1901663, 2, 2),
  (1908257, 3, 1),
  (1912346, 1, 2),
  (1912640, 2, 1),
  (1913284, 3, 0),
  (1920341, 3, 0),
  (1921710, 3, 0),
  (1923237, 2, 2),
  (1923699, 2, 2),
  (1924936, 3, 2),
  (1926017, 3, 0),
  (1934256, 3, 0),
  (1934796, 3, 0),
  (1935573, 1, 2),
  (1937233, 0, 2),
  (1938752, 3, 0),
  (1940595, 0, 1),
  (1941277, 2, 2),
  (1943079, 2, 1),
  (1944951, 2, 0),
  (1946824, 0, 1),
  (1947631, 2, 1),
  (1948010, 2, 1),
  (1951157, 2, 1),
  (1955296, 1, 2),
  (1955721, 0, 1),
  (1956911, 3, 1),
  (1959451, 2, 1),
  (1961656, 0, 0),
  (1966498, 1, 0),
  (1971521, 1, 0),
  (1972728, 2, 0),
  (1973034, 3, 2),
  (1981847, 1, 2),
  (1984785, 0, 1),
  (1995485, 1, 1),
  (1996222, 2, 2),
  (1997381, 0, 1),
  (1997869, 0, 0),
  (2005693, 0, 2),
  (2023295, 2, 1),
  (2027939, 3, 0),
  (2028917, 1, 1),
  (2031042, 2, 0),
  (2031109, 2, 0),
  (2032224, 2, 1),
  (2033486, 3, 1),
  (2034723, 2, 1),
  (2035299, 2, 0),
  (2035415, 2, 0),
  (2042500, 1, 2),
  (2043071, 3, 1),
  (2048234, 3, 1),
  (2048954, 0, 0),
  (2050487, 2, 1),
  (2051437, 0, 2),
  (2057312, 1, 2),
  (2061712, 2, 0),
  (2062782, 0, 2),
  (2065077, 0, 1),
  (2069305, 0, 1),
  (2075916, 1, 1),
  (2083174, 3, 2),
  (2084785, 1, 1),
  (2089415, 3, 0),
  (2093178, 0, 2),
  (2107097, 0, 2),
  (2109104, 3, 2),
  (2110298, 2, 0),
  (2110751, 3, 1),
  (2122965, 1, 1),
  (2125912, 2, 1),
  (2127063, 3, 0),
  (2127495, 1, 0),
  (2147955, 1, 2),
  (2152307, 0, 1),
  (2155555, 0, 2),
  (2161666, 3, 2),
  (2164395, 0, 1),
  (2165126, 3, 1),
  (2169533, 0, 1),
  (2170878, 0, 0),
  (2170957, 3, 1),
  (2173221, 1, 2),
  (2175266, 1, 2),
  (2177331, 3, 1),
  (2182238, 2, 1),
  (2185540, 0, 1),
  (2187263, 0, 1),
  (2192421, 0, 2),
  (2203840, 1, 0),
  (2204598, 2, 1),
  (2206875, 0, 1),
  (2207318, 0, 2),
  (2211083, 2, 1),
  (2215223, 3, 2),
  (2217351, 1, 2),
  (2217380, 3, 2),
  (2219967, 3, 1),
  (2224504, 1, 2),
  (2226494, 3, 1),
  (2230210, 2, 2),
  (2238188, 0, 2),
  (2238463, 3, 0),
  (2240538, 0, 2),
  (2244393, 2, 0),
  (2244801, 0, 2),
  (2248918, 2, 2),
  (2249025, 1, 0),
  (2252779, 3, 0),
  (2261138, 3, 2),
  (2263502, 2, 2),
  (2266591, 1, 1),
  (2267540, 1, 1),
  (2267838, 0, 0),
  (2271182, 0, 1),
  (2273373, 3, 1),
  (2274893, 1, 0),
  (2276442, 1, 2),
  (2281581, 1, 1),
  (2284889, 3, 0),
  (2286556, 0, 0),
  (2300220, 1, 2),
  (2303236, 1, 1),
  (2304738, 2, 1),
  (2304984, 1, 2),
  (2305178, 3, 2),
  (2310887, 1, 1),
  (2311126, 3, 0),
  (2312464, 1, 2),
  (2319316, 3, 0),
  (2322967, 3, 1),
  (2324148, 3, 0),
  (2324772, 2, 1),
  (2326278, 1, 2),
  (2330909, 2, 0),
  (2332063, 0, 2),
  (2332251, 2, 2),
  (2338496, 1, 0),
  (2339126, 3, 2),
  (2342631, 2, 0),
  (2353738, 2, 1),
  (2353790, 2, 2),
  (2355345, 1, 2),
  (2356593, 0, 1),
  (2357357, 3, 0),
  (2357750, 1, 1),
  (2359345, 3, 0),
  (2363960, 1, 2),
  (2364679, 3, 2),
  (2365060, 3, 2),
  (2366066, 3, 1),
  (2366406, 1, 0),
  (2372356, 1, 1),
  (2375223, 2, 0),
  (2375318, 3, 0),
  (2378475, 2, 0),
  (2379674, 3, 0),
  (2388320, 2, 2),
  (2394515, 2, 0),
  (2394608, 2, 1),
  (2404952, 2, 1),
  (2409005, 3, 1),
  (2418953, 0, 0),
  (2418995, 2, 1),
  (2429557, 0, 1),
  (2432726, 0, 2),
  (2434321, 1, 0),
  (2439310, 1, 0),
  (2443160, 1, 2),
  (2448254, 2, 0),
  (2451989, 1, 0),
  (2452901, 0, 0),
  (2453466, 0, 2),
  (2459785, 2, 1),
  (2460247, 1, 0),
  (2462737, 2, 2),
  (2466816, 0, 2),
  (2467321, 3, 0),
  (2471619, 1, 2),
  (2477111, 3, 0),
  (2477112, 0, 1),
  (2484678, 0, 1),
  (2488269, 1, 2),
  (2490842, 1, 0),
  (2498886, 1, 0),
  (2502277, 2, 1),
  (2504549, 2, 0),
  (2508874, 1, 2),
  (2508959, 2, 0),
  (2512067, 0, 0),
  (2514140, 1, 2),
  (2527329, 2, 2),
  (2528153, 0, 1),
  (2530518, 1, 0),
  (2531539, 0, 2),
  (2531967, 3, 2),
  (2534182, 1, 1),
  (2534284, 3, 1),
  (2544082, 0, 0),
  (2547917, 1, 1),
  (2550116, 0, 1),
  (2550219, 1, 1),
  (2558047, 1, 1),
  (2558673, 3, 2),
  (2559476, 2, 2),
  (2559933, 2, 2),
  (2560127, 1, 1),
  (2567724, 1, 1),
  (2569862, 0, 1),
  (2570931, 3, 1),
  (2571148, 2, 2),
  (2575625, 3, 2),
  (2578055, 0, 1),
  (2578232, 3, 0),
  (2583729, 1, 1),
  (2587470, 2, 2),
  (2590069, 2, 2),
  (2594108, 1, 0),
  (2595535, 3, 2),
  (2598408, 0, 0),
  (2606086, 1, 2),
  (2610932, 3, 2),
  (2613437, 1, 1),
  (2620509, 2, 1),
  (2625191, 3, 0),
  (2625944, 2, 0),
  (2631718, 2, 0),
  (2637694, 1, 1),
  (2638451, 0, 1),
  (2639137, 2, 2),
  (2646173, 0, 1),
  (2651919, 3, 1),
  (2652462, 1, 0),
  (2661215, 3, 1),
  (2666749, 0, 1),
  (2669436, 2, 0),
  (2672129, 1, 2),
  (2679712, 3, 2),
  (2681459, 2, 0),
  (2683090, 3, 1),
  (2683158, 0, 0),
  (2683348, 1, 0),
  (2687884, 1, 0),
  (2691883, 2, 0),
  (2695920, 1, 1),
  (2698396, 1, 0),
  (2699431, 1, 0),
  (2700919, 2, 1),
  (2704701, 0, 2),
  (2707850, 2, 0),
  (2711616, 2, 2),
  (2712081, 3, 2),
  (2712316, 3, 0),
  (2726416, 1, 1),
  (2728909, 2, 2),
  (2732485, 1, 0),
  (2737379, 0, 0),
  (2740505, 2, 2),
  (2750247, 0, 2),
  (2753638, 1, 2),
  (2756529, 1, 2),
  (2758416, 1, 2),
  (2760925, 2, 0),
  (2767586, 1, 0),
  (2774307, 2, 0),
  (2775358, 2, 2),
  (2775780, 2, 1),
  (2776242, 1, 0),
  (2778899, 1, 2),
  (2784921, 2, 1),
  (2786255, 2, 1),
  (2787671, 1, 1),
  (2787923, 1, 0),
  (2788853, 0, 0),
  (2789611, 2, 2),
  (2793952, 1, 2),
  (2796234, 1, 0),
  (2796472, 3, 1),
  (2798593, 3, 2),
  (2801436, 0, 0),
  (2802216, 2, 2),
  (2806289, 1, 2),
  (2808290, 0, 2),
  (2810692, 0, 0),
  (2810947, 2, 1),
  (2811796, 2, 0),
  (2813698, 2, 2),
  (2817332, 2, 0),
  (2818791, 2, 2),
  (2819606, 3, 2),
  (2820986, 1, 2),
  (2824089, 0, 0),
  (2827841, 2, 2),
  (2829550, 1, 0),
  (2832066, 1, 2),
  (2833056, 0, 1),
  (2834262, 2, 1),
  (2835653, 0, 2),
  (2837924, 1, 1),
  (2838689, 2, 2),
  (2847537, 0, 1),
  (2851138, 3, 2),
  (2855583, 0, 1),
  (2855784, 3, 1),
  (2858316, 0, 2),
  (2860958, 2, 2),
  (2861607, 3, 2),
  (2862155, 2, 0),
  (2862958, 1, 0),
  (2865116, 1, 1),
  (2866878, 3, 0),
  (2866960, 1, 2),
  (2869919, 1, 1),
  (2869937, 0, 2),
  (2873529, 1, 2),
  (2876818, 0, 2),
  (2877053, 3, 0),
  (2877293, 1, 2),
  (2887569, 1, 1),
  (2896783, 3, 1),
  (2897103, 3, 0),
  (2902683, 3, 2),
  (2913620, 2, 1),
  (2915064, 1, 0),
  (2918385, 3, 0),
  (2928786, 0, 2),
  (2930902, 0, 0),
  (2931416, 2, 2),
  (2937415, 3, 0),
  (2937869, 0, 1),
  (2938937, 0, 1),
  (2940107, 3, 2),
  (2945740, 2, 0),
  (2949449, 1, 0),
  (2958414, 0, 0),
  (2960036, 0, 1),
  (2965466, 0, 2),
  (2967255, 2, 1),
  (2968792, 2, 0),
  (2974224, 1, 1),
  (2974921, 2, 1),
  (2978304, 1, 0),
  (2978536, 0, 2),
  (2978684, 1, 2),
  (2979762, 3, 1),
  (2985014, 2, 1),
  (2987157, 2, 1),
  (2987259, 3, 0),
  (2987940, 0, 1),
  (2988651, 3, 1),
  (2989042, 2, 0),
  (2989835, 2, 1),
  (2994381, 2, 1),
  (2996429, 1, 2),
  (2998758, 0, 1),
  (3000011, 2, 1),
  (3002281, 1, 1),
  (3008208, 3, 2),
  (3011304, 0, 0),
  (3011839, 2, 1),
  (3016293, 2, 2),
  (3016438, 3, 0),
  (3018752, 2, 1),
  (3019644, 0, 0),
  (3025646, 0, 0),
  (3026093, 2, 0),
  (3027036, 2, 1),
  (3031469, 2, 0),
  (3033857, 3, 2),
  (3034357, 2, 2),
  (3034427, 1, 1),
  (3039254, 1, 1),
  (3040159, 1, 1),
  (3040224, 1, 1),
  (3051554, 1, 1),
  (3053062, 2, 2),
  (3054438, 2, 1),
  (3057549, 2, 2),
  (3059212, 3, 0),
  (3061744, 2, 0),
  (3069413, 0, 2),
  (3069503, 0, 2),
  (3079185, 1, 1),
  (3081013, 2, 1),
  (3082936, 1, 1),
  (3082967, 3, 1),
  (3085730, 2, 1),
  (3087831, 1, 0),
  (3088642, 3, 0),
  (3089522, 3, 2),
  (3092594, 3, 0),
  (3094663, 0, 1),
  (3095078, 3, 1),
  (3097473, 3, 2),
  (3099449, 0, 0),
  (3108714, 1, 0),
  (3112468, 2, 0),
  (3115980, 1, 0),
  (3121993, 0, 1),
  (3123578, 1, 0),
  (3125326, 3, 1),
  (3130696, 0, 0),
  (3131391, 3, 0),
  (3133744, 2, 0),
  (3134028, 0, 0),
  (3137156, 0, 1),
  (3139279, 2, 0),
  (3140254, 2, 0),
  (3147912, 1, 0),
  (3147985, 0, 2),
  (3158321, 2, 0),
  (3159651, 2, 1),
  (3167304, 0, 0),
  (3171877, 2, 1),
  (3171901, 3, 1),
  (3171923, 2, 1),
  (3173953, 2, 2),
  (3178232, 2, 2),
  (3183074, 1, 0),
  (3184654, 1, 2),
  (3184944, 1, 1),
  (3187033, 0, 0),
  (3187157, 1, 1),
  (3187894, 3, 2),
  (3191025, 0, 1),
  (3194582, 2, 2),
  (3198043, 3, 2),
  (3198132, 3, 1),
  (3200067, 1, 0),
  (3203858, 1, 0),
  (3206656, 1, 0),
  (3208728, 1, 0),
  (3213236, 0, 1),
  (3214324, 2, 1),
  (3214469, 2, 1),
  (3217355, 2, 0),
  (3220097, 2, 0),
  (3221021, 1, 0),
  (3228999, 2, 0),
  (3229704, 2, 0),
  (3231594, 0, 1),
  (3239288, 2, 2),
  (3243732, 3, 0),
  (3249299, 1, 2),
  (3257267, 3, 1),
  (3265181, 2, 0),
  (3266473, 3, 2),
  (3268739, 1, 0),
  (3268970, 1, 2),
  (3272337, 1, 1),
  (3272738, 3, 1),
  (3275070, 0, 1),
  (3277629, 1, 2),
  (3283821, 1, 0),
  (3283823, 3, 0),
  (3289604, 1, 0),
  (3294179, 2, 1),
  (3298875, 0, 2),
  (3301537, 1, 0),
  (3303548, 2, 2),
  (3305654, 1, 2),
  (3307043, 1, 1),
  (3308354, 2, 2),
  (3311291, 3, 1),
  (3315233, 0, 0),
  (3316718, 0, 2),
  (3319114, 0, 0),
  (3335994, 1, 2),
  (3342339, 3, 1),
  (3342636, 2, 1),
  (3347001, 2, 0),
  (3349211, 1, 0),
  (3356612, 1, 0),
  (3359635, 3, 2),
  (3360058, 2, 1),
  (3365083, 0, 1),
  (3367012, 1, 1),
  (3371676, 2, 1),
  (3373685, 3, 0),
  (3378909, 2, 2),
  (3381102, 0, 0),
  (3385973, 2, 1),
  (3391441, 3, 0),
  (3393361, 2, 0),
  (3394440, 2, 1),
  (3397140, 1, 0),
  (3400563, 0, 2),
  (3400752, 0, 1),
  (3401088, 0, 2),
  (3402963, 3, 2),
  (3410303, 3, 1),
  (3416843, 3, 0),
  (3419196, 0, 2),
  (3420098, 0, 1),
  (3423435, 2, 1),
  (3423690, 1, 2),
  (3425337, 0, 0),
  (3432407, 0, 2),
  (3434912, 2, 2),
  (3441065, 2, 2),
  (3441141, 0, 2),
  (3443910, 0, 0),
  (3443926, 0, 2),
  (3444678, 2, 2),
  (3446372, 0, 1),
  (3448545, 1, 2),
  (3449668, 1, 1),
  (3450240, 1, 1),
  (3455428, 0, 0),
  (3456504, 2, 0),
  (3464202, 2, 2),
  (3467353, 2, 1),
  (3467414, 0, 0),
  (3468198, 1, 2),
  (3474713, 0, 2),
  (3480974, 2, 0),
  (3481170, 1, 1),
  (3489964, 1, 0),
  (3493351, 1, 0),
  (3493976, 3, 2),
  (3494012, 1, 1),
  (3495658, 2, 0),
  (3498172, 2, 2),
  (3506495, 0, 2),
  (3510419, 1, 0),
  (3511900, 3, 2),
  (3515317, 2, 0),
  (3515624, 3, 0),
  (3516795, 0, 0),
  (3516987, 0, 0),
  (3522567, 2, 2),
  (3526456, 2, 2),
  (3529710, 1, 2),
  (3530370, 1, 1),
  (3531132, 2, 1),
  (3532554, 0, 0),
  (3534160, 2, 0),
  (3534525, 3, 2),
  (3535251, 1, 0),
  (3536142, 3, 1),
  (3536605, 3, 0),
  (3547391, 1, 1),
  (3550476, 0, 0),
  (3564435, 1, 0),
  (3570443, 0, 0),
  (3572993, 1, 0),
  (3583262, 2, 1),
  (3586102, 0, 1),
  (3594500, 3, 2),
  (3595203, 3, 1),
  (3596981, 2, 0),
  (3598615, 0, 0),
])
