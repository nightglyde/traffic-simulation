from src.util import *
schedule = deque([
  (4533, 2, 1),
  (9261, 1, 2),
  (10236, 1, 2),
  (10951, 1, 2),
  (11901, 3, 1),
  (18184, 1, 0),
  (19801, 2, 2),
  (23778, 2, 2),
  (25228, 2, 1),
  (26289, 3, 0),
  (28925, 1, 0),
  (39862, 0, 1),
  (49436, 2, 2),
  (51413, 1, 1),
  (55050, 3, 0),
  (57489, 0, 1),
  (58882, 1, 1),
  (59092, 0, 1),
  (63539, 2, 2),
  (64307, 2, 2),
  (65086, 2, 2),
  (68847, 2, 2),
  (73515, 0, 2),
  (75670, 2, 1),
  (77007, 3, 1),
  (80904, 1, 1),
  (81002, 3, 2),
  (83815, 0, 1),
  (84017, 2, 0),
  (87861, 3, 2),
  (89798, 0, 0),
  (91953, 0, 2),
  (93477, 1, 0),
  (94275, 0, 2),
  (95615, 3, 2),
  (95949, 0, 0),
  (96203, 3, 0),
  (101377, 0, 1),
  (102421, 1, 1),
  (105813, 1, 2),
  (108571, 1, 1),
  (114514, 1, 1),
  (117114, 3, 2),
  (119575, 1, 2),
  (124141, 0, 2),
  (125244, 2, 1),
  (128053, 1, 1),
  (128512, 0, 2),
  (130491, 1, 2),
  (149613, 2, 2),
  (149685, 2, 1),
  (152573, 0, 1),
  (152693, 0, 2),
  (153369, 0, 1),
  (155833, 2, 0),
  (156822, 0, 2),
  (158298, 3, 2),
  (158818, 2, 2),
  (160634, 0, 2),
  (167275, 1, 1),
  (169013, 3, 1),
  (170054, 1, 2),
  (172160, 0, 1),
  (177022, 2, 2),
  (178871, 1, 0),
  (179008, 2, 0),
  (179843, 1, 1),
  (181797, 3, 0),
  (182428, 3, 0),
  (184196, 0, 0),
  (185837, 0, 0),
  (186511, 0, 2),
  (190007, 2, 0),
  (191134, 1, 2),
  (191691, 0, 2),
  (192304, 3, 1),
  (192941, 2, 2),
  (194718, 1, 0),
  (197289, 1, 2),
  (199918, 1, 1),
  (200052, 0, 2),
  (200492, 2, 1),
  (201914, 0, 1),
  (205276, 1, 2),
  (207681, 2, 0),
  (209002, 1, 2),
  (210054, 3, 1),
  (213704, 0, 0),
  (217253, 1, 2),
  (217664, 3, 2),
  (220991, 2, 1),
  (230043, 3, 0),
  (234027, 0, 0),
  (238288, 1, 2),
  (243011, 3, 0),
  (244019, 0, 0),
  (253958, 2, 1),
  (257425, 3, 0),
  (258311, 1, 1),
  (261609, 3, 2),
  (264139, 0, 2),
  (264505, 0, 0),
  (264950, 3, 1),
  (268417, 1, 2),
  (270113, 0, 1),
  (270783, 1, 1),
  (270859, 1, 2),
  (272485, 3, 1),
  (274342, 3, 1),
  (276231, 1, 1),
  (277903, 1, 0),
  (279914, 0, 0),
  (284413, 2, 1),
  (290288, 1, 1),
  (290728, 1, 0),
  (294280, 0, 0),
  (298437, 1, 2),
  (300832, 0, 2),
  (301458, 3, 2),
  (303655, 2, 0),
  (309614, 0, 1),
  (314813, 3, 2),
  (316922, 3, 1),
  (328951, 0, 0),
  (332179, 0, 1),
  (342037, 1, 2),
  (342599, 2, 2),
  (348426, 0, 0),
  (352118, 1, 2),
  (352455, 0, 2),
  (353664, 3, 1),
  (354368, 1, 2),
  (355236, 0, 2),
  (367040, 2, 1),
  (371395, 2, 0),
  (372644, 3, 2),
  (375723, 0, 0),
  (378501, 2, 0),
  (378680, 1, 2),
  (382454, 1, 1),
  (382749, 1, 2),
  (398114, 3, 1),
  (403294, 1, 1),
  (408203, 2, 1),
  (408209, 0, 2),
  (413983, 1, 1),
  (421280, 1, 1),
  (422195, 2, 1),
  (424418, 0, 1),
  (424432, 0, 2),
  (436943, 3, 0),
  (450143, 3, 0),
  (452711, 1, 0),
  (452743, 1, 2),
  (453427, 3, 0),
  (463432, 2, 1),
  (469806, 1, 2),
  (472064, 0, 0),
  (472070, 2, 0),
  (472137, 0, 1),
  (474357, 2, 1),
  (476465, 1, 1),
  (481086, 3, 1),
  (486078, 3, 2),
  (487404, 3, 2),
  (487525, 0, 1),
  (492663, 1, 0),
  (493698, 0, 1),
  (494473, 1, 0),
  (496411, 1, 2),
  (503908, 3, 2),
  (507327, 3, 2),
  (514361, 2, 2),
  (517445, 2, 0),
  (517811, 1, 1),
  (519812, 3, 2),
  (521252, 0, 2),
  (526442, 1, 2),
  (531121, 3, 1),
  (534653, 0, 1),
  (536686, 0, 0),
  (547893, 3, 2),
  (548567, 1, 2),
  (549007, 2, 1),
  (554369, 1, 1),
  (557339, 0, 2),
  (562928, 0, 2),
  (569704, 0, 0),
  (570418, 0, 1),
  (577660, 2, 0),
  (583844, 0, 0),
  (584895, 1, 2),
  (586191, 1, 0),
  (591739, 0, 2),
  (593275, 2, 2),
  (594371, 2, 0),
  (596092, 1, 1),
  (596253, 0, 2),
  (601442, 2, 0),
  (601593, 0, 0),
  (602688, 3, 0),
  (605748, 2, 1),
  (611784, 2, 1),
  (611867, 0, 1),
  (612769, 3, 0),
  (615667, 2, 1),
  (616167, 3, 0),
  (618211, 3, 2),
  (618601, 2, 0),
  (620396, 2, 2),
  (623759, 3, 2),
  (625333, 3, 1),
  (627049, 2, 2),
  (628703, 1, 0),
  (628740, 1, 2),
  (633326, 1, 0),
  (634760, 3, 2),
  (635575, 1, 2),
  (638369, 0, 0),
  (648846, 2, 1),
  (652203, 2, 1),
  (656277, 2, 2),
  (657795, 0, 2),
  (659126, 0, 0),
  (667942, 1, 0),
  (668826, 1, 2),
  (671420, 3, 1),
  (677073, 1, 2),
  (686882, 2, 2),
  (687219, 2, 1),
  (688036, 3, 0),
  (688703, 0, 2),
  (691278, 0, 1),
  (697893, 2, 2),
  (699513, 3, 2),
  (702904, 3, 2),
  (703519, 2, 2),
  (704628, 3, 0),
  (705643, 1, 1),
  (707579, 1, 1),
  (708468, 0, 2),
  (718042, 3, 0),
  (719383, 0, 2),
  (720790, 3, 1),
  (724524, 0, 0),
  (724663, 3, 1),
  (728175, 3, 1),
  (729718, 3, 0),
  (730621, 3, 2),
  (733007, 3, 2),
  (733759, 2, 2),
  (735239, 3, 2),
  (738121, 0, 2),
  (743882, 1, 0),
  (745340, 0, 2),
  (751443, 3, 2),
  (753551, 3, 0),
  (753640, 2, 1),
  (754220, 0, 0),
  (754818, 2, 1),
  (756145, 2, 1),
  (763298, 1, 0),
  (764445, 2, 0),
  (770787, 3, 0),
  (780070, 0, 1),
  (781957, 3, 1),
  (787672, 3, 2),
  (787769, 1, 1),
  (789987, 2, 2),
  (797620, 1, 2),
  (797893, 0, 1),
  (799175, 3, 2),
  (813932, 3, 2),
  (825946, 0, 0),
  (827278, 3, 1),
  (837748, 1, 1),
  (839822, 1, 1),
  (841576, 1, 0),
  (841984, 1, 2),
  (842648, 1, 0),
  (845124, 0, 2),
  (847899, 3, 0),
  (849772, 2, 1),
  (850343, 3, 2),
  (852603, 3, 2),
  (857196, 2, 1),
  (857639, 3, 2),
  (863299, 3, 0),
  (868720, 1, 0),
  (870470, 2, 1),
  (875183, 0, 1),
  (879233, 3, 0),
  (884956, 2, 1),
  (884978, 2, 1),
  (891489, 1, 0),
  (894005, 0, 2),
  (894852, 1, 2),
  (895806, 0, 2),
  (896141, 1, 1),
  (897608, 3, 0),
  (900378, 0, 1),
  (900399, 0, 2),
  (901951, 0, 1),
  (905350, 0, 0),
  (910311, 1, 0),
  (910877, 2, 2),
  (910882, 3, 1),
  (918779, 3, 0),
  (925873, 1, 0),
  (927221, 2, 0),
  (934120, 3, 1),
  (934601, 1, 1),
  (938715, 0, 2),
  (940226, 1, 0),
  (941849, 0, 0),
  (942230, 2, 1),
  (944624, 2, 1),
  (944682, 3, 1),
  (945755, 3, 2),
  (946052, 3, 1),
  (950297, 2, 2),
  (952284, 3, 0),
  (952619, 0, 0),
  (960734, 0, 1),
  (971506, 2, 1),
  (974708, 1, 2),
  (977684, 2, 2),
  (979556, 3, 0),
  (980257, 1, 0),
  (981823, 1, 0),
  (982106, 3, 1),
  (983904, 3, 2),
  (983977, 1, 1),
  (984885, 2, 2),
  (987484, 0, 2),
  (989184, 3, 0),
  (995439, 1, 2),
  (995788, 2, 1),
  (997136, 2, 1),
  (998035, 0, 1),
  (998373, 3, 0),
  (1003011, 2, 0),
  (1008712, 0, 1),
  (1009053, 3, 2),
  (1009757, 3, 0),
  (1023746, 1, 1),
  (1025003, 1, 1),
  (1028477, 1, 1),
  (1029426, 3, 0),
  (1033854, 2, 2),
  (1033920, 3, 2),
  (1035467, 3, 2),
  (1036565, 2, 2),
  (1039382, 3, 0),
  (1042943, 3, 2),
  (1043500, 1, 2),
  (1046153, 3, 1),
  (1047292, 2, 1),
  (1049064, 3, 1),
  (1049565, 0, 2),
  (1051777, 2, 2),
  (1053880, 2, 0),
  (1055559, 1, 0),
  (1058659, 1, 0),
  (1061068, 3, 2),
  (1065467, 2, 2),
  (1067858, 0, 1),
  (1070706, 2, 2),
  (1072953, 1, 2),
  (1073720, 0, 2),
  (1079275, 2, 1),
  (1081307, 3, 0),
  (1084976, 3, 1),
  (1085205, 0, 0),
  (1086058, 2, 1),
  (1086150, 1, 0),
  (1095872, 0, 0),
  (1096479, 2, 1),
  (1097830, 0, 2),
  (1108314, 0, 2),
  (1108435, 3, 0),
  (1109994, 0, 0),
  (1110053, 2, 0),
  (1113000, 2, 2),
  (1113370, 2, 2),
  (1127091, 2, 2),
  (1128874, 0, 0),
  (1129994, 1, 0),
  (1133406, 1, 2),
  (1135575, 2, 1),
  (1135964, 1, 0),
  (1138271, 3, 1),
  (1141418, 2, 2),
  (1141909, 0, 2),
  (1143299, 2, 2),
  (1143745, 3, 1),
  (1151869, 2, 2),
  (1152124, 0, 1),
  (1154212, 0, 0),
  (1158994, 0, 2),
  (1159751, 0, 0),
  (1161595, 2, 2),
  (1165617, 2, 0),
  (1165975, 2, 2),
  (1176308, 3, 2),
  (1176872, 0, 0),
  (1178188, 1, 2),
  (1179000, 1, 1),
  (1179253, 0, 2),
  (1184360, 0, 2),
  (1191552, 1, 1),
  (1193967, 3, 0),
  (1194515, 1, 0),
  (1197335, 3, 2),
  (1199501, 0, 1),
  (1201965, 2, 2),
  (1206694, 1, 2),
  (1207989, 0, 0),
  (1210452, 1, 1),
  (1217735, 1, 2),
  (1220936, 0, 1),
  (1224236, 3, 2),
  (1228727, 0, 0),
  (1231560, 0, 0),
  (1233416, 0, 0),
  (1236101, 0, 1),
  (1237822, 1, 1),
  (1241278, 0, 1),
  (1244911, 2, 1),
  (1247559, 0, 2),
  (1251243, 2, 1),
  (1259258, 2, 2),
  (1260971, 3, 1),
  (1265716, 1, 0),
  (1267248, 0, 0),
  (1267516, 0, 2),
  (1267560, 2, 2),
  (1269844, 3, 1),
  (1270854, 0, 2),
  (1272114, 1, 1),
  (1273563, 1, 0),
  (1274834, 0, 0),
  (1278769, 0, 2),
  (1282014, 3, 2),
  (1283460, 3, 2),
  (1289803, 3, 2),
  (1291565, 3, 0),
  (1292489, 0, 0),
  (1295888, 0, 2),
  (1302297, 2, 2),
  (1307376, 0, 2),
  (1309014, 0, 2),
  (1309635, 2, 0),
  (1311181, 0, 1),
  (1312130, 2, 0),
  (1316554, 2, 1),
  (1320102, 3, 1),
  (1324228, 1, 2),
  (1325550, 2, 0),
  (1327763, 3, 1),
  (1333530, 2, 2),
  (1337078, 0, 0),
  (1345669, 1, 2),
  (1346938, 0, 0),
  (1361551, 0, 2),
  (1366367, 3, 1),
  (1367007, 1, 0),
  (1367707, 1, 2),
  (1370988, 3, 1),
  (1371344, 1, 0),
  (1373440, 0, 0),
  (1375768, 0, 0),
  (1376336, 3, 0),
  (1378360, 0, 2),
  (1378998, 3, 2),
  (1389693, 3, 0),
  (1389988, 3, 2),
  (1390512, 2, 2),
  (1397831, 3, 2),
  (1407836, 0, 2),
  (1408813, 1, 1),
  (1412333, 0, 2),
  (1413150, 0, 0),
  (1414740, 1, 0),
  (1416040, 3, 1),
  (1418438, 0, 0),
  (1422286, 2, 1),
  (1423824, 1, 0),
  (1425923, 0, 0),
  (1428187, 1, 2),
  (1438364, 0, 1),
  (1438933, 1, 0),
  (1440373, 1, 1),
  (1451215, 3, 0),
  (1455336, 0, 1),
  (1458242, 3, 0),
  (1461936, 2, 1),
  (1462135, 2, 2),
  (1463466, 3, 1),
  (1465217, 1, 1),
  (1465639, 2, 0),
  (1469287, 3, 2),
  (1471711, 3, 0),
  (1473218, 3, 0),
  (1476569, 1, 0),
  (1483716, 3, 2),
  (1492791, 1, 1),
  (1494904, 1, 2),
  (1495117, 3, 0),
  (1495826, 1, 2),
  (1496883, 2, 1),
  (1504953, 0, 0),
  (1520372, 1, 0),
  (1524562, 2, 0),
  (1527623, 2, 1),
  (1527704, 3, 1),
  (1528111, 2, 2),
  (1528194, 1, 2),
  (1535948, 0, 1),
  (1536610, 2, 0),
  (1538413, 3, 2),
  (1540229, 1, 1),
  (1541757, 2, 2),
  (1548592, 3, 2),
  (1549557, 2, 0),
  (1552796, 3, 0),
  (1555932, 2, 1),
  (1562198, 3, 0),
  (1567223, 2, 2),
  (1567692, 1, 1),
  (1567812, 1, 1),
  (1575837, 0, 2),
  (1580283, 3, 0),
  (1588947, 1, 1),
  (1590303, 2, 1),
  (1593873, 0, 1),
  (1595266, 1, 2),
  (1595470, 0, 2),
  (1602411, 1, 1),
  (1608589, 2, 2),
  (1609483, 3, 1),
  (1609809, 3, 0),
  (1611211, 3, 0),
  (1614703, 0, 2),
  (1614869, 3, 0),
  (1620499, 0, 0),
  (1623940, 3, 0),
  (1629230, 0, 2),
  (1636552, 2, 1),
  (1639059, 0, 2),
  (1645974, 2, 1),
  (1648458, 2, 0),
  (1648518, 1, 0),
  (1650538, 1, 1),
  (1650647, 0, 1),
  (1651364, 1, 2),
  (1652687, 1, 0),
  (1653371, 0, 1),
  (1654076, 1, 0),
  (1654534, 0, 0),
  (1655888, 0, 2),
  (1657530, 3, 0),
  (1658516, 3, 0),
  (1665751, 1, 2),
  (1669901, 2, 2),
  (1677369, 2, 2),
  (1679455, 3, 0),
  (1679801, 3, 1),
  (1682098, 0, 2),
  (1688961, 0, 1),
  (1691355, 3, 2),
  (1694853, 0, 2),
  (1699077, 3, 1),
  (1703081, 3, 1),
  (1703117, 3, 2),
  (1704136, 0, 1),
  (1707385, 1, 0),
  (1708625, 2, 2),
  (1709121, 0, 0),
  (1709125, 2, 1),
  (1712909, 3, 2),
  (1715211, 0, 0),
  (1718492, 1, 1),
  (1722981, 2, 0),
  (1728022, 0, 1),
  (1728075, 1, 1),
  (1728970, 0, 1),
  (1729847, 2, 0),
  (1739485, 3, 0),
  (1742415, 2, 1),
  (1743861, 0, 1),
  (1748432, 0, 1),
  (1749088, 2, 2),
  (1759717, 3, 0),
  (1762053, 2, 0),
  (1762420, 3, 2),
  (1765374, 3, 0),
  (1766722, 2, 2),
  (1768142, 1, 0),
  (1768352, 0, 1),
  (1770450, 1, 0),
  (1776349, 3, 0),
  (1780953, 0, 1),
  (1784266, 0, 1),
  (1784674, 1, 2),
  (1785902, 0, 2),
  (1788888, 3, 2),
  (1790937, 3, 0),
  (1791049, 2, 2),
  (1791107, 2, 1),
  (1791341, 3, 2),
  (1793074, 2, 0),
  (1795755, 0, 0),
  (1796895, 0, 1),
  (1799304, 0, 0),
  (1802760, 0, 2),
  (1803244, 1, 1),
  (1804614, 3, 0),
  (1805085, 0, 1),
  (1808910, 1, 2),
  (1818925, 0, 0),
  (1820191, 3, 0),
  (1825612, 1, 0),
  (1829890, 3, 2),
  (1836952, 3, 1),
  (1839730, 3, 0),
  (1840456, 0, 1),
  (1842940, 1, 0),
  (1846433, 1, 0),
  (1855354, 1, 1),
  (1861806, 1, 1),
  (1863902, 0, 0),
  (1866527, 0, 1),
  (1866697, 3, 1),
  (1867308, 0, 0),
  (1879838, 1, 1),
  (1882092, 3, 0),
  (1884124, 3, 2),
  (1889053, 0, 1),
  (1889171, 0, 0),
  (1889657, 0, 0),
  (1892221, 0, 0),
  (1892455, 2, 0),
  (1906513, 1, 2),
  (1914560, 3, 0),
  (1918149, 0, 0),
  (1918383, 0, 0),
  (1919751, 3, 0),
  (1921598, 3, 0),
  (1928319, 3, 0),
  (1931997, 0, 1),
  (1936102, 2, 2),
  (1937085, 3, 1),
  (1940067, 0, 2),
  (1941209, 1, 1),
  (1943109, 1, 2),
  (1952875, 0, 2),
  (1954190, 2, 0),
  (1961216, 2, 0),
  (1967329, 3, 1),
  (1968036, 3, 0),
  (1975061, 0, 0),
  (1976856, 0, 0),
  (1978919, 1, 2),
  (1981025, 2, 1),
  (1982929, 2, 0),
  (1984872, 3, 2),
  (1987692, 3, 1),
  (1988882, 3, 0),
  (1992115, 1, 1),
  (1993897, 3, 0),
  (1996086, 0, 2),
  (2000832, 2, 2),
  (2001560, 1, 2),
  (2004689, 0, 2),
  (2012542, 0, 2),
  (2015923, 2, 1),
  (2021006, 3, 0),
  (2027160, 2, 2),
  (2035536, 3, 1),
  (2036534, 3, 2),
  (2036553, 2, 1),
  (2043597, 2, 2),
  (2045582, 2, 2),
  (2047925, 0, 1),
  (2051269, 3, 0),
  (2052810, 1, 0),
  (2054448, 0, 0),
  (2055028, 0, 0),
  (2056879, 0, 2),
  (2060244, 0, 2),
  (2061328, 0, 1),
  (2065382, 0, 1),
  (2066422, 0, 2),
  (2069824, 0, 2),
  (2073025, 0, 0),
  (2073046, 0, 2),
  (2080386, 1, 2),
  (2087016, 3, 0),
  (2088232, 3, 0),
  (2088968, 0, 0),
  (2090027, 3, 0),
  (2097831, 1, 1),
  (2100710, 1, 1),
  (2106711, 0, 2),
  (2109125, 3, 1),
  (2114556, 3, 1),
  (2114889, 1, 0),
  (2118185, 0, 1),
  (2120263, 0, 0),
  (2122388, 0, 1),
  (2122428, 0, 0),
  (2129246, 2, 0),
  (2133736, 0, 0),
  (2135729, 3, 0),
  (2135889, 1, 1),
  (2138337, 3, 0),
  (2146559, 0, 1),
  (2149050, 3, 1),
  (2149743, 3, 0),
  (2156205, 0, 2),
  (2158400, 1, 2),
  (2159662, 3, 2),
  (2159877, 2, 2),
  (2161045, 1, 0),
  (2162021, 3, 1),
  (2162473, 1, 1),
  (2164440, 0, 1),
  (2170077, 0, 1),
  (2174474, 0, 0),
  (2174734, 3, 2),
  (2179886, 3, 0),
  (2180987, 1, 0),
  (2184409, 2, 1),
  (2184453, 1, 2),
  (2184642, 3, 1),
  (2189273, 2, 2),
  (2189689, 3, 2),
  (2190251, 0, 1),
  (2190702, 3, 1),
  (2200056, 3, 2),
  (2204482, 1, 0),
  (2208073, 3, 0),
  (2208588, 0, 0),
  (2220452, 2, 0),
  (2220916, 0, 0),
  (2228368, 3, 1),
  (2240779, 0, 1),
  (2241201, 0, 1),
  (2241604, 1, 1),
  (2245063, 0, 0),
  (2245841, 2, 0),
  (2250202, 1, 0),
  (2254738, 2, 1),
  (2256066, 2, 2),
  (2256817, 1, 2),
  (2258881, 0, 0),
  (2259632, 3, 0),
  (2263392, 3, 2),
  (2265737, 2, 2),
  (2272404, 3, 2),
  (2272770, 3, 0),
  (2275694, 0, 1),
  (2276488, 0, 1),
  (2281968, 2, 1),
  (2284693, 3, 2),
  (2284855, 3, 0),
  (2287513, 0, 0),
  (2288091, 0, 1),
  (2291011, 3, 2),
  (2292169, 0, 1),
  (2294026, 1, 0),
  (2297374, 2, 0),
  (2300059, 3, 2),
  (2300600, 2, 0),
  (2301438, 3, 0),
  (2312877, 2, 1),
  (2313094, 1, 1),
  (2313733, 0, 1),
  (2315097, 0, 0),
  (2315149, 1, 0),
  (2316420, 3, 1),
  (2317211, 2, 0),
  (2324466, 2, 0),
  (2324474, 1, 0),
  (2324847, 3, 1),
  (2326120, 3, 0),
  (2328557, 2, 2),
  (2328832, 1, 1),
  (2329762, 2, 2),
  (2333827, 0, 0),
  (2334304, 2, 0),
  (2336973, 1, 1),
  (2339862, 1, 2),
  (2343121, 1, 0),
  (2345047, 1, 1),
  (2347983, 2, 0),
  (2353043, 3, 0),
  (2357596, 0, 1),
  (2357977, 0, 1),
  (2361964, 2, 1),
  (2367596, 0, 2),
  (2369275, 0, 2),
  (2370976, 3, 0),
  (2373371, 0, 0),
  (2381472, 2, 0),
  (2383313, 0, 0),
  (2385034, 1, 2),
  (2388218, 3, 1),
  (2389109, 2, 1),
  (2391903, 3, 2),
  (2392390, 0, 0),
  (2393016, 0, 2),
  (2397794, 0, 2),
  (2401861, 0, 2),
  (2406019, 3, 2),
  (2407448, 2, 0),
  (2408278, 0, 0),
  (2411131, 3, 1),
  (2416112, 0, 1),
  (2416211, 1, 1),
  (2416952, 1, 1),
  (2419429, 3, 0),
  (2427744, 0, 1),
  (2433115, 0, 1),
  (2437463, 0, 1),
  (2439739, 1, 0),
  (2440566, 3, 2),
  (2445604, 3, 2),
  (2448638, 0, 1),
  (2448753, 0, 1),
  (2450565, 0, 1),
  (2454476, 1, 1),
  (2457436, 0, 1),
  (2457820, 2, 0),
  (2458670, 2, 0),
  (2464181, 1, 0),
  (2464487, 0, 2),
  (2468080, 1, 2),
  (2468183, 0, 1),
  (2469751, 3, 2),
  (2472786, 0, 1),
  (2482028, 3, 2),
  (2485895, 0, 0),
  (2486014, 1, 1),
  (2486030, 3, 0),
  (2487278, 1, 1),
  (2488078, 1, 1),
  (2500082, 1, 0),
  (2500958, 2, 0),
  (2503082, 2, 1),
  (2507255, 3, 0),
  (2507882, 2, 0),
  (2510629, 0, 0),
  (2513992, 3, 1),
  (2520834, 1, 1),
  (2521917, 1, 2),
  (2522767, 2, 1),
  (2524497, 3, 1),
  (2525293, 1, 1),
  (2526039, 2, 0),
  (2526117, 0, 0),
  (2528605, 3, 0),
  (2530493, 0, 2),
  (2533670, 2, 2),
  (2544598, 3, 1),
  (2545967, 3, 1),
  (2550090, 3, 0),
  (2551453, 2, 2),
  (2552715, 0, 0),
  (2553846, 1, 0),
  (2555074, 1, 2),
  (2559339, 2, 2),
  (2564519, 3, 0),
  (2564537, 3, 0),
  (2570148, 0, 2),
  (2571091, 0, 1),
  (2581576, 1, 1),
  (2582817, 1, 1),
  (2589929, 1, 2),
  (2592641, 1, 2),
  (2593834, 1, 1),
  (2595873, 3, 2),
  (2595954, 0, 0),
  (2597183, 1, 1),
  (2598026, 2, 2),
  (2601220, 3, 1),
  (2602738, 2, 0),
  (2603137, 3, 0),
  (2603340, 2, 0),
  (2603393, 3, 2),
  (2604955, 2, 1),
  (2612734, 2, 2),
  (2613820, 3, 1),
  (2615967, 0, 1),
  (2621065, 2, 2),
  (2626706, 3, 2),
  (2627745, 1, 0),
  (2628392, 2, 2),
  (2628719, 0, 2),
  (2634769, 3, 2),
  (2638335, 0, 0),
  (2638980, 2, 2),
  (2641612, 1, 2),
  (2647407, 2, 0),
  (2651823, 1, 2),
  (2652123, 1, 1),
  (2653584, 1, 2),
  (2653702, 3, 1),
  (2654766, 2, 0),
  (2654844, 1, 2),
  (2661842, 3, 2),
  (2664258, 0, 0),
  (2672221, 0, 2),
  (2678473, 0, 1),
  (2679981, 2, 1),
  (2681172, 3, 0),
  (2681663, 2, 2),
  (2685642, 3, 1),
  (2685745, 2, 1),
  (2700483, 1, 2),
  (2703355, 2, 1),
  (2710045, 2, 2),
  (2711355, 1, 2),
  (2711776, 2, 1),
  (2716719, 1, 2),
  (2718286, 1, 2),
  (2721691, 1, 1),
  (2722845, 0, 0),
  (2725599, 0, 1),
  (2731540, 2, 0),
  (2732170, 0, 0),
  (2736614, 3, 2),
  (2737386, 0, 1),
  (2737394, 2, 2),
  (2744847, 1, 2),
  (2745180, 0, 1),
  (2746440, 3, 2),
  (2746527, 2, 1),
  (2754461, 0, 2),
  (2754813, 3, 0),
  (2756611, 2, 2),
  (2757574, 0, 2),
  (2765425, 1, 2),
  (2767049, 1, 1),
  (2776213, 2, 1),
  (2785450, 2, 1),
  (2788365, 0, 2),
  (2796213, 0, 2),
  (2799208, 3, 2),
  (2814511, 2, 0),
  (2815516, 2, 2),
  (2816157, 0, 2),
  (2818197, 3, 1),
  (2819166, 1, 1),
  (2821911, 1, 0),
  (2836167, 2, 2),
  (2837398, 0, 0),
  (2848145, 0, 2),
  (2849248, 3, 2),
  (2850745, 3, 0),
  (2852450, 3, 1),
  (2852606, 2, 0),
  (2857169, 2, 1),
  (2860184, 3, 0),
  (2861549, 0, 0),
  (2865224, 0, 0),
  (2875200, 1, 1),
  (2880093, 1, 0),
  (2882007, 0, 1),
  (2882634, 3, 2),
  (2883629, 2, 2),
  (2886278, 0, 1),
  (2886965, 3, 2),
  (2890186, 1, 2),
  (2890702, 3, 0),
  (2902367, 3, 1),
  (2902398, 0, 0),
  (2912598, 1, 2),
  (2913889, 1, 1),
  (2921100, 3, 2),
  (2925058, 2, 2),
  (2926060, 1, 1),
  (2934693, 0, 1),
  (2935044, 3, 2),
  (2935075, 0, 0),
  (2940600, 1, 1),
  (2941095, 3, 1),
  (2942212, 3, 1),
  (2944226, 1, 1),
  (2945172, 1, 0),
  (2945886, 0, 0),
  (2946216, 3, 0),
  (2949536, 3, 2),
  (2951546, 0, 2),
  (2951845, 1, 1),
  (2968937, 1, 0),
  (2972456, 3, 1),
  (2973202, 2, 2),
  (2976907, 0, 0),
  (2982141, 3, 2),
  (2989321, 2, 1),
  (2990180, 0, 2),
  (2992878, 2, 1),
  (2995237, 3, 0),
  (2995566, 2, 1),
  (2995763, 0, 0),
  (2996211, 1, 0),
  (2998090, 3, 1),
  (3006611, 0, 0),
  (3012990, 0, 0),
  (3016224, 3, 2),
  (3020938, 1, 2),
  (3022312, 0, 0),
  (3025283, 1, 1),
  (3028776, 3, 0),
  (3034490, 0, 2),
  (3046679, 0, 2),
  (3047942, 2, 2),
  (3049592, 2, 2),
  (3050186, 1, 0),
  (3055175, 3, 2),
  (3060220, 3, 0),
  (3061495, 1, 1),
  (3061832, 3, 0),
  (3063389, 1, 0),
  (3063463, 2, 2),
  (3066255, 3, 1),
  (3067449, 0, 2),
  (3068268, 0, 1),
  (3069662, 0, 1),
  (3079690, 1, 0),
  (3082324, 3, 0),
  (3082333, 3, 1),
  (3082650, 0, 0),
  (3088031, 3, 1),
  (3088596, 3, 1),
  (3089948, 2, 2),
  (3091946, 0, 1),
  (3092204, 0, 2),
  (3095878, 0, 1),
  (3095946, 2, 1),
  (3097312, 3, 2),
  (3097505, 0, 2),
  (3099455, 1, 0),
  (3100413, 0, 1),
  (3105479, 3, 1),
  (3109298, 1, 2),
  (3110159, 2, 0),
  (3111402, 3, 1),
  (3113536, 1, 1),
  (3114715, 1, 0),
  (3115104, 0, 1),
  (3119204, 1, 2),
  (3126546, 1, 1),
  (3127589, 0, 0),
  (3129025, 1, 1),
  (3132808, 1, 2),
  (3133500, 3, 2),
  (3134586, 1, 2),
  (3153951, 3, 0),
  (3159143, 2, 0),
  (3162604, 0, 2),
  (3164232, 0, 1),
  (3165231, 0, 0),
  (3170299, 0, 0),
  (3173325, 1, 0),
  (3176629, 2, 2),
  (3183021, 3, 1),
  (3183889, 1, 2),
  (3185133, 3, 0),
  (3185603, 3, 1),
  (3186032, 0, 0),
  (3186176, 1, 2),
  (3187145, 1, 0),
  (3187769, 2, 1),
  (3188360, 3, 2),
  (3189542, 3, 2),
  (3189570, 1, 2),
  (3189676, 1, 0),
  (3210805, 1, 0),
  (3212574, 1, 1),
  (3214693, 3, 1),
  (3216887, 2, 1),
  (3217466, 1, 2),
  (3221149, 1, 1),
  (3225100, 2, 0),
  (3229805, 3, 0),
  (3231525, 3, 2),
  (3234433, 1, 0),
  (3237642, 3, 2),
  (3240986, 0, 2),
  (3242764, 2, 1),
  (3245595, 1, 1),
  (3251939, 0, 0),
  (3252947, 2, 0),
  (3253434, 3, 0),
  (3254991, 0, 2),
  (3256075, 1, 1),
  (3263429, 1, 0),
  (3266276, 2, 2),
  (3266716, 0, 2),
  (3268578, 2, 2),
  (3269533, 1, 1),
  (3269686, 3, 0),
  (3272093, 2, 0),
  (3281425, 3, 1),
  (3281762, 0, 1),
  (3290874, 1, 1),
  (3291128, 0, 1),
  (3305296, 0, 2),
  (3307911, 2, 2),
  (3308436, 3, 2),
  (3313587, 0, 0),
  (3313843, 0, 0),
  (3318182, 3, 0),
  (3320484, 1, 0),
  (3325072, 3, 0),
  (3326793, 1, 0),
  (3330360, 0, 2),
  (3332268, 2, 2),
  (3334860, 2, 0),
  (3336788, 3, 0),
  (3337247, 2, 1),
  (3338704, 1, 1),
  (3343751, 0, 1),
  (3348590, 1, 1),
  (3349259, 3, 1),
  (3352487, 0, 1),
  (3364812, 2, 0),
  (3368550, 1, 2),
  (3368619, 0, 0),
  (3371304, 3, 2),
  (3383948, 1, 0),
  (3386192, 1, 2),
  (3389442, 2, 0),
  (3390333, 0, 1),
  (3395509, 0, 2),
  (3398204, 3, 0),
  (3400048, 2, 2),
  (3402005, 2, 2),
  (3403201, 3, 0),
  (3404571, 1, 0),
  (3410814, 2, 1),
  (3414701, 0, 1),
  (3418560, 1, 0),
  (3419374, 0, 0),
  (3421480, 1, 2),
  (3422822, 3, 0),
  (3423497, 3, 1),
  (3432093, 3, 2),
  (3432272, 3, 1),
  (3432332, 0, 0),
  (3432463, 3, 1),
  (3436522, 0, 1),
  (3442079, 0, 0),
  (3454138, 3, 1),
  (3457560, 0, 0),
  (3457630, 0, 2),
  (3460933, 3, 0),
  (3461925, 3, 0),
  (3466189, 3, 2),
  (3466598, 0, 0),
  (3470330, 3, 0),
  (3475492, 0, 1),
  (3475959, 2, 0),
  (3482598, 1, 2),
  (3483160, 1, 1),
  (3485609, 0, 0),
  (3489297, 1, 1),
  (3489955, 3, 1),
  (3492958, 1, 0),
  (3494021, 2, 1),
  (3494896, 1, 0),
  (3495479, 2, 0),
  (3498624, 2, 0),
  (3504115, 3, 2),
  (3511840, 2, 1),
  (3515970, 2, 0),
  (3522710, 3, 2),
  (3523771, 0, 2),
  (3523921, 0, 1),
  (3531039, 3, 1),
  (3532724, 0, 1),
  (3533310, 3, 0),
  (3537453, 0, 2),
  (3539734, 1, 0),
  (3549439, 3, 2),
  (3552018, 3, 1),
  (3559134, 3, 1),
  (3566387, 3, 0),
  (3573925, 3, 1),
  (3576887, 3, 0),
  (3578875, 0, 1),
  (3579499, 0, 2),
  (3582099, 0, 1),
  (3583878, 1, 0),
  (3588455, 1, 2),
  (3590263, 3, 1),
  (3595811, 0, 2),
])