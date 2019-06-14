from src.util import *
schedule = deque([
  (1031, 3, 0),
  (2601, 2, 2),
  (3536, 3, 0),
  (4261, 0, 2),
  (6707, 3, 2),
  (10257, 2, 1),
  (12321, 1, 0),
  (12326, 2, 1),
  (12426, 0, 2),
  (15296, 0, 1),
  (19880, 0, 0),
  (21381, 0, 1),
  (34095, 1, 2),
  (37460, 0, 0),
  (41620, 3, 1),
  (43324, 1, 1),
  (44934, 0, 1),
  (46418, 0, 1),
  (54983, 1, 0),
  (55528, 1, 1),
  (56251, 2, 2),
  (60438, 0, 2),
  (60538, 1, 0),
  (62128, 1, 0),
  (62265, 0, 1),
  (62911, 0, 2),
  (64607, 1, 1),
  (64739, 1, 2),
  (67531, 2, 1),
  (70396, 3, 0),
  (72108, 1, 1),
  (72907, 0, 2),
  (73536, 2, 0),
  (74311, 3, 2),
  (75920, 1, 0),
  (85391, 3, 1),
  (91629, 2, 1),
  (92459, 0, 0),
  (98082, 0, 1),
  (103328, 0, 2),
  (103910, 0, 0),
  (115336, 2, 1),
  (119327, 3, 0),
  (120766, 0, 0),
  (122545, 0, 2),
  (125135, 0, 0),
  (133210, 3, 0),
  (136578, 3, 0),
  (138227, 0, 1),
  (138789, 2, 2),
  (140044, 1, 2),
  (142745, 0, 2),
  (151706, 3, 2),
  (155216, 0, 2),
  (157631, 0, 2),
  (157672, 3, 0),
  (158213, 0, 2),
  (160101, 0, 1),
  (162709, 3, 1),
  (163363, 3, 2),
  (165077, 2, 2),
  (167928, 0, 0),
  (169520, 0, 0),
  (173328, 3, 2),
  (176365, 1, 1),
  (177264, 0, 2),
  (177416, 2, 1),
  (179466, 2, 0),
  (183083, 3, 1),
  (191948, 0, 1),
  (195103, 1, 1),
  (198651, 1, 1),
  (200483, 2, 2),
  (206959, 1, 0),
  (208173, 0, 2),
  (208867, 0, 1),
  (209363, 1, 0),
  (209447, 2, 1),
  (210628, 0, 0),
  (211093, 2, 1),
  (218139, 1, 1),
  (218484, 2, 1),
  (218533, 2, 1),
  (219732, 0, 2),
  (223188, 3, 1),
  (228408, 2, 1),
  (229505, 2, 2),
  (230135, 0, 0),
  (236722, 2, 2),
  (245304, 1, 2),
  (253714, 0, 2),
  (260207, 3, 1),
  (260537, 1, 2),
  (262810, 3, 0),
  (269853, 1, 1),
  (275254, 3, 2),
  (275404, 0, 2),
  (288672, 0, 0),
  (294000, 1, 2),
  (294344, 0, 2),
  (295161, 0, 1),
  (297009, 2, 1),
  (297574, 1, 2),
  (299251, 0, 2),
  (300854, 0, 0),
  (303074, 0, 2),
  (306243, 0, 1),
  (309461, 2, 1),
  (309552, 1, 0),
  (318114, 3, 0),
  (320829, 2, 2),
  (322789, 1, 0),
  (326634, 0, 2),
  (327287, 1, 0),
  (328185, 1, 0),
  (332361, 3, 2),
  (340708, 0, 2),
  (341901, 2, 2),
  (343462, 0, 0),
  (351083, 3, 2),
  (351953, 3, 2),
  (352254, 3, 1),
  (354650, 1, 0),
  (362635, 1, 1),
  (364218, 1, 0),
  (365316, 0, 2),
  (365355, 0, 2),
  (366673, 0, 2),
  (368211, 0, 1),
  (372250, 2, 1),
  (372578, 0, 1),
  (390204, 1, 2),
  (390849, 1, 2),
  (391892, 1, 1),
  (392638, 2, 1),
  (394328, 0, 0),
  (396415, 1, 2),
  (402242, 0, 2),
  (403043, 1, 1),
  (403509, 2, 2),
  (407581, 2, 0),
  (409183, 0, 0),
  (410735, 2, 2),
  (413550, 0, 1),
  (415314, 3, 2),
  (417049, 0, 2),
  (418989, 0, 0),
  (419296, 2, 1),
  (424356, 2, 0),
  (425868, 2, 1),
  (427080, 0, 0),
  (430800, 3, 0),
  (434631, 3, 0),
  (435339, 1, 2),
  (449369, 3, 1),
  (451300, 1, 1),
  (451720, 3, 0),
  (455619, 2, 1),
  (455814, 0, 1),
  (458773, 2, 1),
  (458959, 0, 0),
  (459003, 3, 2),
  (461197, 2, 0),
  (462728, 1, 2),
  (472071, 0, 1),
  (473390, 2, 1),
  (473837, 0, 2),
  (477106, 0, 1),
  (480125, 2, 1),
  (485423, 3, 0),
  (488591, 0, 0),
  (489076, 1, 0),
  (489423, 2, 2),
  (492574, 0, 0),
  (497341, 1, 0),
  (498706, 3, 0),
  (498893, 3, 0),
  (508017, 2, 0),
  (510700, 1, 1),
  (514208, 0, 0),
  (516010, 3, 2),
  (516916, 1, 2),
  (517602, 1, 0),
  (517763, 0, 1),
  (518815, 2, 2),
  (522675, 2, 1),
  (526316, 0, 0),
  (527859, 1, 1),
  (529049, 3, 1),
  (534995, 3, 1),
  (536218, 1, 2),
  (538712, 3, 0),
  (542689, 0, 0),
  (543065, 1, 2),
  (546340, 3, 2),
  (553363, 3, 0),
  (559735, 3, 2),
  (561897, 3, 0),
  (566525, 3, 0),
  (569194, 2, 0),
  (571155, 0, 0),
  (571595, 2, 2),
  (573462, 1, 0),
  (576695, 1, 0),
  (580300, 2, 2),
  (586519, 2, 2),
  (586538, 1, 1),
  (591909, 1, 2),
  (595142, 3, 0),
  (596659, 1, 2),
  (596992, 3, 2),
  (599716, 3, 1),
  (599844, 2, 1),
  (601688, 1, 0),
  (604086, 1, 1),
  (604159, 2, 2),
  (608895, 0, 0),
  (609234, 0, 0),
  (612782, 1, 2),
  (612988, 3, 2),
  (613548, 0, 0),
  (625491, 1, 2),
  (626886, 0, 0),
  (629545, 1, 1),
  (638857, 3, 1),
  (658054, 0, 2),
  (658491, 3, 1),
  (659726, 3, 1),
  (661265, 1, 1),
  (661630, 0, 0),
  (669151, 3, 1),
  (671807, 1, 2),
  (673545, 3, 2),
  (678790, 1, 1),
  (680484, 3, 1),
  (682506, 3, 1),
  (685494, 3, 1),
  (691806, 1, 0),
  (693299, 3, 0),
  (693871, 1, 0),
  (696440, 2, 2),
  (700032, 3, 0),
  (704768, 0, 1),
  (711052, 2, 2),
  (713299, 2, 2),
  (719001, 3, 0),
  (723461, 1, 1),
  (733909, 2, 2),
  (736532, 2, 0),
  (737119, 1, 0),
  (737512, 1, 2),
  (740283, 3, 1),
  (742273, 1, 0),
  (748882, 2, 2),
  (749898, 2, 0),
  (751875, 0, 0),
  (752232, 0, 0),
  (754658, 0, 0),
  (755425, 1, 1),
  (758822, 0, 1),
  (759964, 0, 2),
  (760750, 2, 0),
  (761035, 0, 1),
  (770958, 3, 1),
  (777118, 0, 0),
  (780728, 1, 2),
  (782131, 0, 1),
  (782216, 3, 0),
  (782962, 1, 0),
  (787683, 2, 1),
  (795189, 1, 2),
  (798575, 0, 0),
  (801927, 0, 2),
  (802787, 1, 2),
  (813548, 3, 1),
  (815053, 0, 1),
  (815711, 0, 0),
  (817604, 3, 0),
  (820035, 3, 0),
  (820122, 3, 1),
  (839100, 1, 2),
  (842332, 1, 2),
  (845354, 2, 1),
  (845485, 0, 2),
  (846245, 3, 2),
  (851754, 1, 2),
  (853427, 2, 2),
  (856699, 2, 0),
  (859075, 0, 0),
  (864014, 0, 2),
  (865001, 1, 2),
  (868792, 0, 1),
  (869500, 1, 0),
  (870486, 0, 0),
  (871347, 0, 2),
  (873536, 0, 2),
  (874838, 2, 1),
  (877248, 1, 1),
  (880400, 2, 1),
  (882080, 2, 1),
  (884032, 0, 1),
  (885683, 1, 0),
  (885827, 0, 1),
  (885848, 1, 0),
  (886848, 2, 1),
  (890594, 0, 2),
  (893056, 0, 1),
  (894691, 0, 1),
  (898020, 3, 0),
  (902276, 2, 2),
  (903578, 0, 0),
  (910316, 2, 0),
  (910594, 0, 1),
  (913920, 2, 0),
  (914006, 1, 0),
  (918723, 3, 1),
  (924344, 0, 0),
  (925295, 0, 0),
  (926013, 3, 0),
  (928443, 2, 1),
  (934331, 1, 0),
  (938810, 3, 0),
  (940530, 2, 1),
  (942022, 3, 1),
  (942598, 3, 0),
  (942855, 1, 2),
  (945695, 2, 0),
  (947998, 1, 0),
  (949703, 1, 2),
  (950797, 3, 2),
  (956257, 0, 2),
  (957010, 2, 1),
  (961497, 1, 1),
  (968785, 3, 1),
  (970350, 0, 2),
  (970858, 1, 0),
  (974527, 0, 2),
  (975327, 0, 0),
  (976524, 3, 0),
  (976688, 1, 1),
  (978918, 3, 2),
  (986118, 1, 1),
  (986553, 1, 1),
  (988507, 1, 0),
  (990495, 3, 2),
  (990681, 1, 2),
  (995053, 0, 2),
  (999046, 3, 2),
  (999997, 3, 1),
  (1001454, 0, 1),
  (1004591, 0, 2),
  (1005353, 1, 1),
  (1008646, 0, 2),
  (1010435, 2, 2),
  (1010765, 3, 0),
  (1011823, 1, 1),
  (1021134, 2, 1),
  (1022355, 2, 0),
  (1024904, 2, 1),
  (1027581, 2, 0),
  (1027654, 1, 2),
  (1034887, 0, 2),
  (1039862, 2, 2),
  (1040698, 1, 1),
  (1045778, 2, 0),
  (1051389, 0, 0),
  (1052389, 2, 1),
  (1053528, 0, 0),
  (1064769, 2, 1),
  (1065515, 2, 1),
  (1066691, 3, 2),
  (1069458, 3, 0),
  (1069483, 3, 1),
  (1070235, 0, 1),
  (1070444, 2, 0),
  (1070445, 2, 2),
  (1072446, 1, 2),
  (1080248, 0, 2),
  (1081960, 3, 0),
  (1082798, 1, 0),
  (1082978, 1, 0),
  (1088142, 0, 0),
  (1090000, 3, 2),
  (1093498, 1, 0),
  (1107833, 3, 1),
  (1108772, 0, 0),
  (1110636, 0, 0),
  (1111103, 3, 0),
  (1111284, 3, 2),
  (1115370, 1, 2),
  (1119796, 1, 2),
  (1123880, 0, 0),
  (1123956, 0, 1),
  (1125068, 1, 0),
  (1126316, 0, 2),
  (1132361, 2, 1),
  (1132813, 3, 0),
  (1134837, 0, 2),
  (1136133, 3, 0),
  (1141210, 0, 1),
  (1143968, 3, 2),
  (1145870, 2, 1),
  (1149705, 1, 0),
  (1153002, 3, 1),
  (1156429, 2, 2),
  (1158034, 3, 0),
  (1158199, 3, 1),
  (1159301, 2, 0),
  (1161304, 2, 1),
  (1162520, 0, 2),
  (1165202, 0, 1),
  (1166348, 0, 0),
  (1166355, 3, 2),
  (1167503, 3, 0),
  (1173015, 1, 1),
  (1173441, 1, 2),
  (1174179, 2, 2),
  (1176247, 2, 2),
  (1178989, 2, 2),
  (1181133, 3, 2),
  (1187495, 1, 0),
  (1187498, 3, 0),
  (1189054, 2, 0),
  (1190524, 0, 2),
  (1191240, 3, 0),
  (1195794, 2, 2),
  (1204595, 1, 1),
  (1206505, 0, 2),
  (1207476, 3, 0),
  (1209192, 1, 2),
  (1211716, 1, 0),
  (1212736, 1, 1),
  (1213425, 2, 1),
  (1216945, 3, 1),
  (1217415, 0, 0),
  (1222455, 2, 1),
  (1224690, 1, 2),
  (1225466, 2, 1),
  (1230632, 1, 1),
  (1230741, 0, 1),
  (1232047, 2, 2),
  (1232846, 2, 2),
  (1233223, 1, 1),
  (1234420, 2, 2),
  (1234926, 3, 2),
  (1235204, 0, 1),
  (1236165, 1, 1),
  (1242669, 1, 2),
  (1244811, 1, 1),
  (1246874, 2, 2),
  (1250329, 3, 2),
  (1252707, 3, 2),
  (1252865, 0, 0),
  (1254769, 1, 1),
  (1261013, 3, 2),
  (1268679, 2, 0),
  (1273290, 3, 2),
  (1276857, 2, 0),
  (1277014, 1, 0),
  (1280633, 0, 2),
  (1283387, 0, 1),
  (1287659, 0, 2),
  (1290383, 1, 0),
  (1290428, 2, 1),
  (1291518, 2, 1),
  (1293935, 0, 1),
  (1294540, 3, 1),
  (1304508, 2, 2),
  (1308363, 1, 0),
  (1308818, 2, 2),
  (1310340, 0, 2),
  (1312977, 0, 1),
  (1314053, 1, 2),
  (1316146, 3, 0),
  (1317092, 0, 2),
  (1318814, 3, 1),
  (1322690, 2, 0),
  (1322772, 2, 0),
  (1323834, 1, 2),
  (1323938, 3, 0),
  (1331830, 2, 0),
  (1335670, 3, 1),
  (1339410, 3, 0),
  (1340947, 1, 0),
  (1341151, 0, 1),
  (1342511, 3, 1),
  (1349398, 0, 2),
  (1352238, 1, 0),
  (1358412, 1, 1),
  (1359317, 2, 1),
  (1363263, 2, 1),
  (1372120, 3, 2),
  (1373276, 0, 1),
  (1377417, 2, 0),
  (1387288, 2, 2),
  (1393542, 0, 0),
  (1394747, 2, 1),
  (1395546, 1, 1),
  (1395884, 1, 2),
  (1398278, 0, 2),
  (1403964, 0, 1),
  (1405305, 2, 0),
  (1417762, 1, 0),
  (1419122, 0, 1),
  (1424021, 3, 0),
  (1427085, 3, 1),
  (1433473, 0, 1),
  (1441937, 2, 1),
  (1446212, 2, 0),
  (1449947, 2, 2),
  (1459553, 0, 1),
  (1460062, 0, 0),
  (1460355, 2, 0),
  (1465114, 3, 1),
  (1465820, 1, 2),
  (1467017, 3, 2),
  (1470353, 0, 1),
  (1474205, 1, 2),
  (1481137, 1, 1),
  (1489849, 2, 0),
  (1493138, 0, 0),
  (1496975, 0, 1),
  (1499261, 1, 1),
  (1499779, 1, 1),
  (1503579, 2, 2),
  (1511635, 3, 2),
  (1511876, 2, 0),
  (1512001, 1, 0),
  (1512667, 3, 1),
  (1517949, 2, 1),
  (1519789, 2, 0),
  (1521127, 1, 1),
  (1524608, 1, 2),
  (1525079, 0, 1),
  (1529358, 2, 0),
  (1530356, 1, 2),
  (1533851, 0, 1),
  (1536845, 1, 1),
  (1540811, 2, 1),
  (1542785, 3, 1),
  (1543190, 1, 2),
  (1543931, 2, 2),
  (1550360, 0, 0),
  (1551107, 1, 0),
  (1554110, 1, 1),
  (1557297, 0, 0),
  (1561357, 1, 0),
  (1563074, 1, 2),
  (1566246, 3, 1),
  (1566563, 2, 1),
  (1567717, 1, 0),
  (1568152, 0, 0),
  (1570006, 0, 2),
  (1577950, 2, 1),
  (1582391, 0, 2),
  (1588794, 2, 2),
  (1591291, 1, 1),
  (1598843, 0, 1),
  (1599572, 3, 1),
  (1603317, 2, 2),
  (1605233, 3, 2),
  (1614351, 2, 2),
  (1614649, 2, 0),
  (1618929, 2, 2),
  (1620893, 2, 2),
  (1623584, 2, 1),
  (1625480, 0, 1),
  (1630369, 2, 0),
  (1634403, 0, 2),
  (1641084, 3, 2),
  (1643285, 0, 0),
  (1648889, 1, 1),
  (1650414, 1, 1),
  (1653736, 3, 2),
  (1663226, 3, 2),
  (1663813, 1, 0),
  (1670406, 1, 2),
  (1671943, 1, 0),
  (1673078, 1, 1),
  (1675643, 0, 2),
  (1677423, 1, 1),
  (1677600, 3, 0),
  (1688537, 2, 2),
  (1691353, 0, 1),
  (1691796, 0, 1),
  (1698448, 1, 0),
  (1698452, 2, 2),
  (1701301, 3, 2),
  (1707447, 1, 1),
  (1717173, 0, 0),
  (1717831, 2, 0),
  (1719307, 3, 0),
  (1732195, 1, 1),
  (1736958, 2, 0),
  (1742822, 3, 0),
  (1745310, 2, 0),
  (1745664, 3, 2),
  (1751529, 3, 0),
  (1757046, 1, 2),
  (1757139, 1, 0),
  (1757696, 2, 1),
  (1762696, 3, 1),
  (1765170, 1, 1),
  (1769472, 3, 1),
  (1777604, 0, 0),
  (1777609, 0, 1),
  (1784473, 3, 0),
  (1784788, 1, 1),
  (1787838, 1, 1),
  (1793559, 2, 1),
  (1798418, 1, 2),
  (1798736, 3, 2),
  (1802396, 2, 0),
  (1803282, 1, 1),
  (1803676, 3, 2),
  (1810094, 1, 0),
  (1810205, 2, 2),
  (1811574, 1, 0),
  (1815336, 2, 0),
  (1817229, 3, 1),
  (1818647, 2, 2),
  (1819190, 1, 0),
  (1820771, 3, 1),
  (1833191, 3, 0),
  (1835496, 0, 0),
  (1839447, 2, 2),
  (1840583, 3, 0),
  (1841989, 2, 0),
  (1842641, 1, 2),
  (1844876, 0, 1),
  (1846617, 1, 2),
  (1854345, 2, 2),
  (1865158, 3, 0),
  (1865931, 2, 1),
  (1873639, 3, 1),
  (1875931, 1, 0),
  (1891743, 1, 2),
  (1901523, 0, 2),
  (1906084, 1, 0),
  (1910174, 2, 0),
  (1911496, 3, 1),
  (1913769, 2, 2),
  (1918068, 1, 1),
  (1918390, 3, 0),
  (1924550, 1, 1),
  (1925087, 0, 2),
  (1932926, 0, 2),
  (1941710, 1, 1),
  (1942178, 2, 1),
  (1943796, 1, 1),
  (1947519, 1, 2),
  (1949206, 2, 1),
  (1950881, 0, 1),
  (1957132, 0, 1),
  (1962755, 1, 0),
  (1962986, 1, 0),
  (1970230, 2, 0),
  (1973533, 0, 0),
  (1973981, 0, 1),
  (1985111, 1, 1),
  (1989601, 3, 1),
  (1990393, 3, 1),
  (1990597, 2, 2),
  (1996279, 1, 0),
  (1999550, 1, 0),
  (2002564, 3, 2),
  (2006792, 2, 0),
  (2012737, 3, 0),
  (2014095, 2, 1),
  (2018066, 2, 2),
  (2019587, 0, 2),
  (2020477, 3, 0),
  (2024163, 0, 0),
  (2025898, 2, 0),
  (2026544, 2, 1),
  (2029739, 3, 1),
  (2034124, 2, 2),
  (2035612, 0, 0),
  (2036814, 3, 1),
  (2040134, 2, 0),
  (2046037, 3, 0),
  (2050926, 1, 0),
  (2057662, 3, 2),
  (2062031, 1, 2),
  (2062514, 2, 0),
  (2064445, 3, 1),
  (2065240, 2, 0),
  (2073245, 1, 1),
  (2075996, 1, 2),
  (2078242, 1, 1),
  (2079792, 3, 2),
  (2084434, 2, 2),
  (2084841, 2, 1),
  (2084940, 0, 2),
  (2085512, 3, 1),
  (2085945, 2, 0),
  (2089985, 3, 0),
  (2092231, 2, 1),
  (2092379, 3, 0),
  (2095722, 1, 2),
  (2096051, 1, 2),
  (2101445, 3, 1),
  (2102204, 2, 1),
  (2105694, 1, 0),
  (2107988, 2, 1),
  (2108013, 3, 2),
  (2109979, 3, 0),
  (2110625, 3, 2),
  (2113969, 3, 0),
  (2114606, 2, 1),
  (2115258, 3, 1),
  (2124347, 3, 2),
  (2125434, 2, 1),
  (2130404, 0, 0),
  (2136532, 3, 2),
  (2136935, 1, 1),
  (2147399, 2, 1),
  (2150038, 0, 1),
  (2150389, 0, 2),
  (2154111, 1, 0),
  (2159364, 0, 2),
  (2165438, 3, 0),
  (2167105, 3, 0),
  (2170070, 2, 1),
  (2171731, 2, 1),
  (2172505, 1, 2),
  (2180858, 1, 2),
  (2182525, 3, 2),
  (2183262, 2, 1),
  (2183396, 3, 0),
  (2187405, 1, 1),
  (2190694, 1, 1),
  (2197870, 2, 1),
  (2199490, 2, 1),
  (2200091, 1, 1),
  (2204855, 0, 1),
  (2207817, 3, 2),
  (2207965, 2, 1),
  (2209066, 2, 0),
  (2209896, 0, 0),
  (2210754, 1, 2),
  (2215986, 2, 2),
  (2216153, 0, 1),
  (2223930, 3, 0),
  (2226946, 0, 2),
  (2229496, 3, 1),
  (2232257, 0, 2),
  (2238138, 1, 1),
  (2238700, 1, 0),
  (2242530, 2, 1),
  (2244968, 1, 0),
  (2246294, 0, 2),
  (2249703, 2, 1),
  (2251185, 1, 0),
  (2252016, 0, 1),
  (2253197, 2, 2),
  (2263459, 3, 1),
  (2265844, 3, 0),
  (2271911, 3, 2),
  (2272080, 2, 1),
  (2272349, 2, 2),
  (2273378, 1, 2),
  (2274616, 1, 2),
  (2274863, 0, 0),
  (2277662, 2, 2),
  (2277995, 1, 1),
  (2278607, 1, 2),
  (2281489, 3, 0),
  (2281851, 0, 2),
  (2285740, 0, 1),
  (2288408, 2, 1),
  (2292076, 2, 1),
  (2297904, 1, 0),
  (2298008, 3, 1),
  (2310241, 3, 2),
  (2310947, 1, 2),
  (2312633, 1, 1),
  (2317660, 0, 0),
  (2319105, 0, 1),
  (2319319, 2, 0),
  (2321045, 1, 2),
  (2323507, 1, 1),
  (2324898, 3, 2),
  (2326620, 2, 1),
  (2334536, 2, 2),
  (2339695, 1, 1),
  (2344488, 3, 1),
  (2345987, 2, 0),
  (2347195, 0, 0),
  (2348393, 3, 2),
  (2358076, 0, 1),
  (2369199, 0, 1),
  (2378866, 0, 2),
  (2381471, 0, 1),
  (2382490, 2, 0),
  (2383028, 0, 0),
  (2395442, 0, 2),
  (2398757, 2, 1),
  (2401411, 1, 1),
  (2402421, 3, 2),
  (2407424, 2, 1),
  (2412182, 3, 0),
  (2415165, 2, 0),
  (2419054, 3, 2),
  (2419362, 1, 0),
  (2420751, 3, 2),
  (2422825, 1, 1),
  (2426496, 3, 0),
  (2430716, 2, 2),
  (2430907, 0, 2),
  (2431389, 3, 0),
  (2431661, 2, 0),
  (2432177, 1, 1),
  (2437077, 1, 2),
  (2441942, 3, 1),
  (2442455, 0, 1),
  (2446043, 1, 0),
  (2449497, 2, 0),
  (2453851, 3, 0),
  (2455666, 2, 2),
  (2457883, 3, 1),
  (2458103, 2, 1),
  (2459513, 2, 1),
  (2459732, 3, 1),
  (2460700, 1, 1),
  (2462430, 2, 0),
  (2463324, 1, 0),
  (2468531, 1, 1),
  (2472044, 1, 0),
  (2472703, 3, 2),
  (2473524, 0, 0),
  (2476535, 3, 2),
  (2482383, 3, 1),
  (2482699, 2, 2),
  (2483325, 3, 2),
  (2483488, 1, 1),
  (2485830, 2, 2),
  (2486710, 2, 1),
  (2488623, 3, 1),
  (2496447, 0, 0),
  (2498913, 3, 1),
  (2503693, 3, 2),
  (2505812, 2, 1),
  (2507404, 1, 0),
  (2509287, 2, 1),
  (2510297, 0, 0),
  (2517435, 3, 1),
  (2522391, 0, 2),
  (2524599, 3, 2),
  (2524682, 2, 1),
  (2525386, 0, 1),
  (2536634, 3, 0),
  (2536912, 2, 1),
  (2546388, 2, 1),
  (2547635, 3, 2),
  (2549468, 2, 1),
  (2550325, 2, 1),
  (2557938, 1, 2),
  (2561090, 2, 0),
  (2567177, 2, 2),
  (2568869, 3, 1),
  (2569417, 2, 0),
  (2571622, 0, 2),
  (2574551, 2, 2),
  (2575987, 2, 1),
  (2580512, 3, 2),
  (2580539, 0, 1),
  (2582235, 1, 0),
  (2584151, 0, 0),
  (2586627, 0, 2),
  (2587123, 0, 2),
  (2590991, 3, 0),
  (2591123, 2, 1),
  (2596709, 0, 1),
  (2597019, 2, 2),
  (2603711, 1, 2),
  (2604701, 1, 0),
  (2609867, 0, 2),
  (2610097, 0, 2),
  (2615317, 1, 0),
  (2618320, 1, 1),
  (2619846, 2, 1),
  (2629163, 1, 1),
  (2629319, 2, 2),
  (2630099, 1, 2),
  (2630531, 1, 2),
  (2637397, 3, 0),
  (2639881, 3, 0),
  (2640587, 1, 0),
  (2643307, 0, 2),
  (2649333, 2, 0),
  (2649899, 1, 0),
  (2651846, 3, 0),
  (2653767, 1, 1),
  (2656604, 0, 0),
  (2658535, 0, 0),
  (2659238, 2, 0),
  (2659281, 3, 1),
  (2660478, 3, 1),
  (2662417, 2, 0),
  (2663353, 2, 1),
  (2664348, 1, 2),
  (2665454, 2, 0),
  (2668539, 2, 2),
  (2679241, 3, 1),
  (2679397, 1, 1),
  (2680244, 2, 0),
  (2680852, 1, 1),
  (2683044, 1, 2),
  (2685531, 1, 0),
  (2685755, 2, 0),
  (2686122, 3, 2),
  (2686716, 2, 1),
  (2687813, 0, 1),
  (2690443, 1, 1),
  (2690468, 2, 0),
  (2697134, 1, 1),
  (2703113, 2, 2),
  (2704519, 3, 2),
  (2707058, 2, 0),
  (2709650, 1, 1),
  (2713742, 1, 1),
  (2715899, 2, 0),
  (2718184, 0, 2),
  (2719101, 2, 0),
  (2719539, 2, 1),
  (2731358, 1, 0),
  (2733388, 1, 1),
  (2733974, 0, 1),
  (2736153, 1, 2),
  (2740889, 1, 0),
  (2743704, 3, 2),
  (2746520, 2, 0),
  (2750681, 3, 1),
  (2754008, 3, 0),
  (2757562, 2, 0),
  (2762521, 2, 1),
  (2764354, 2, 1),
  (2769694, 2, 2),
  (2774443, 1, 0),
  (2777617, 2, 1),
  (2777926, 3, 2),
  (2778271, 1, 2),
  (2782829, 0, 0),
  (2789535, 2, 2),
  (2797113, 1, 1),
  (2797158, 2, 2),
  (2801457, 2, 1),
  (2803758, 3, 2),
  (2806944, 1, 1),
  (2814427, 2, 1),
  (2820606, 1, 1),
  (2821028, 1, 1),
  (2829143, 1, 2),
  (2835004, 3, 0),
  (2836228, 0, 1),
  (2840059, 3, 0),
  (2842520, 3, 0),
  (2843564, 1, 1),
  (2854058, 1, 0),
  (2854558, 1, 0),
  (2856647, 1, 2),
  (2856693, 1, 1),
  (2857046, 2, 0),
  (2859701, 2, 2),
  (2860380, 3, 0),
  (2861494, 0, 0),
  (2864390, 1, 1),
  (2865426, 1, 2),
  (2866061, 2, 0),
  (2867576, 3, 1),
  (2867958, 1, 1),
  (2871087, 2, 0),
  (2873599, 0, 0),
  (2876205, 0, 1),
  (2883317, 1, 2),
  (2883345, 0, 0),
  (2884626, 3, 1),
  (2884867, 2, 0),
  (2886258, 3, 1),
  (2893814, 3, 2),
  (2899011, 3, 1),
  (2899850, 3, 1),
  (2901574, 0, 2),
  (2912523, 1, 0),
  (2924224, 1, 1),
  (2925053, 1, 2),
  (2925179, 3, 2),
  (2927438, 1, 0),
  (2939940, 2, 1),
  (2945214, 0, 0),
  (2950373, 2, 1),
  (2951839, 3, 1),
  (2952329, 0, 2),
  (2956796, 0, 2),
  (2963338, 1, 0),
  (2969959, 1, 1),
  (2970871, 3, 1),
  (2970987, 1, 0),
  (2975592, 3, 2),
  (2978496, 3, 1),
  (2982829, 1, 0),
  (2984318, 1, 0),
  (2986979, 0, 0),
  (2988985, 2, 2),
  (2999165, 3, 1),
  (3012572, 3, 1),
  (3013359, 3, 2),
  (3018409, 1, 2),
  (3021057, 0, 1),
  (3022598, 0, 1),
  (3024562, 2, 0),
  (3027269, 1, 1),
  (3034565, 3, 2),
  (3036263, 2, 1),
  (3038539, 1, 0),
  (3039474, 2, 0),
  (3052005, 0, 1),
  (3055566, 1, 2),
  (3055765, 0, 0),
  (3055921, 3, 0),
  (3057329, 3, 2),
  (3059677, 0, 1),
  (3063306, 3, 2),
  (3063328, 1, 2),
  (3065437, 3, 2),
  (3067576, 3, 2),
  (3069076, 2, 2),
  (3070738, 3, 1),
  (3076098, 3, 1),
  (3076424, 0, 2),
  (3077900, 2, 2),
  (3082812, 0, 1),
  (3090477, 0, 0),
  (3094401, 0, 1),
  (3095062, 0, 2),
  (3097010, 0, 2),
  (3098858, 0, 0),
  (3099435, 2, 0),
  (3100991, 1, 2),
  (3108092, 2, 2),
  (3110129, 3, 2),
  (3117618, 2, 0),
  (3122313, 1, 1),
  (3123343, 2, 2),
  (3128477, 1, 1),
  (3136700, 3, 2),
  (3144195, 2, 1),
  (3145800, 1, 2),
  (3145849, 0, 1),
  (3150974, 1, 1),
  (3151634, 3, 1),
  (3154203, 0, 2),
  (3158100, 0, 0),
  (3160205, 3, 2),
  (3162044, 1, 1),
  (3171013, 0, 1),
  (3176266, 0, 2),
  (3177868, 3, 0),
  (3183908, 3, 1),
  (3190301, 0, 1),
  (3191088, 2, 0),
  (3193335, 1, 2),
  (3203807, 0, 2),
  (3204075, 1, 2),
  (3208840, 0, 2),
  (3209887, 2, 2),
  (3214419, 0, 0),
  (3219950, 0, 2),
  (3222585, 0, 0),
  (3224244, 0, 0),
  (3226218, 3, 0),
  (3230908, 0, 2),
  (3233856, 2, 1),
  (3238362, 1, 0),
  (3239709, 1, 1),
  (3239745, 1, 1),
  (3248175, 0, 1),
  (3248578, 1, 1),
  (3249411, 0, 0),
  (3251150, 0, 0),
  (3252481, 0, 2),
  (3263358, 0, 2),
  (3264921, 2, 2),
  (3268383, 1, 0),
  (3269864, 0, 0),
  (3274570, 0, 2),
  (3277130, 0, 0),
  (3277268, 0, 1),
  (3279284, 2, 2),
  (3287177, 0, 1),
  (3294431, 3, 1),
  (3294618, 1, 1),
  (3296120, 1, 0),
  (3297494, 0, 2),
  (3300227, 1, 0),
  (3301844, 3, 2),
  (3309200, 2, 0),
  (3316746, 3, 1),
  (3324127, 0, 1),
  (3324575, 3, 2),
  (3328982, 2, 2),
  (3334547, 0, 0),
  (3334862, 3, 1),
  (3337154, 3, 1),
  (3339533, 0, 0),
  (3344359, 1, 1),
  (3347980, 1, 2),
  (3352163, 3, 1),
  (3353573, 2, 2),
  (3356257, 3, 2),
  (3358375, 1, 2),
  (3359052, 1, 0),
  (3361248, 1, 1),
  (3362624, 2, 0),
  (3365339, 2, 1),
  (3372463, 2, 0),
  (3372557, 0, 0),
  (3374772, 1, 1),
  (3377581, 0, 1),
  (3384505, 1, 1),
  (3385071, 0, 0),
  (3387458, 3, 2),
  (3387521, 1, 1),
  (3390140, 2, 2),
  (3390868, 3, 0),
  (3395140, 1, 2),
  (3401757, 3, 0),
  (3402514, 2, 2),
  (3410619, 0, 2),
  (3411464, 2, 0),
  (3411514, 0, 0),
  (3414647, 0, 2),
  (3419253, 3, 0),
  (3424717, 1, 0),
  (3427885, 0, 0),
  (3429455, 0, 2),
  (3440276, 1, 0),
  (3441040, 1, 1),
  (3441373, 1, 2),
  (3445084, 1, 2),
  (3446721, 1, 2),
  (3446939, 2, 1),
  (3447768, 0, 1),
  (3449242, 1, 2),
  (3452066, 3, 2),
  (3455971, 3, 0),
  (3456051, 0, 2),
  (3460750, 2, 0),
  (3464516, 2, 0),
  (3472062, 0, 1),
  (3483082, 1, 1),
  (3483097, 3, 1),
  (3484366, 2, 1),
  (3498185, 0, 1),
  (3500691, 2, 0),
  (3505911, 3, 2),
  (3508526, 1, 1),
  (3512188, 3, 0),
  (3514616, 0, 1),
  (3516769, 0, 1),
  (3519480, 3, 2),
  (3520246, 0, 2),
  (3520369, 3, 1),
  (3520638, 2, 2),
  (3526099, 0, 1),
  (3528513, 1, 1),
  (3530122, 2, 1),
  (3530569, 3, 2),
  (3533996, 1, 1),
  (3534421, 3, 2),
  (3534827, 0, 0),
  (3535575, 0, 1),
  (3535662, 3, 1),
  (3536385, 1, 0),
  (3536906, 2, 1),
  (3537534, 1, 2),
  (3544048, 2, 0),
  (3548446, 0, 1),
  (3552623, 0, 1),
  (3557854, 1, 2),
  (3559053, 0, 0),
  (3559164, 0, 1),
  (3560460, 1, 2),
  (3562398, 1, 0),
  (3562688, 0, 2),
  (3563898, 1, 0),
  (3564297, 0, 2),
  (3567084, 2, 0),
  (3567088, 3, 0),
  (3567387, 0, 1),
  (3568713, 3, 1),
  (3572331, 2, 2),
  (3584874, 3, 0),
  (3586453, 0, 1),
  (3588373, 0, 0),
  (3588724, 0, 1),
  (3590737, 3, 1),
  (3592906, 1, 2),
  (3599301, 0, 1),
])