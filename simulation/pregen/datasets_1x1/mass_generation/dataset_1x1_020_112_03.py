from util import *
schedule = deque([
  (509, 1, 0),
  (1977, 3, 3),
  (6571, 2, 3),
  (6760, 4, 0),
  (12388, 6, 6),
  (13246, 6, 4),
  (15097, 5, 3),
  (15321, 7, 7),
  (17903, 4, 7),
  (18402, 7, 0),
  (22828, 5, 3),
  (23006, 3, 3),
  (24489, 1, 2),
  (41502, 2, 7),
  (48035, 2, 3),
  (49766, 2, 6),
  (52610, 3, 7),
  (58094, 1, 2),
  (62326, 7, 4),
  (66731, 4, 6),
  (71514, 3, 5),
  (73319, 4, 7),
  (74369, 1, 0),
  (76138, 7, 0),
  (77455, 4, 7),
  (81905, 6, 7),
  (82189, 1, 4),
  (84573, 0, 7),
  (88926, 7, 7),
  (92294, 3, 1),
  (94780, 1, 0),
  (95537, 7, 7),
  (96060, 1, 0),
  (97698, 7, 3),
  (105276, 7, 7),
  (107564, 3, 3),
  (107887, 3, 3),
  (112344, 0, 0),
  (115954, 5, 2),
  (116466, 5, 7),
  (119171, 1, 0),
  (119483, 4, 7),
  (120502, 7, 3),
  (122383, 3, 7),
  (126261, 2, 3),
  (126524, 3, 3),
  (128672, 3, 7),
  (129423, 3, 6),
  (130353, 1, 0),
  (134109, 0, 4),
  (136384, 1, 3),
  (137498, 1, 7),
  (138051, 7, 5),
  (140462, 0, 0),
  (142930, 5, 7),
  (144468, 4, 6),
  (144658, 3, 7),
  (150383, 0, 0),
  (150745, 3, 3),
  (152176, 5, 7),
  (153998, 5, 6),
  (156225, 7, 0),
  (164838, 2, 7),
  (167371, 3, 3),
  (168107, 3, 7),
  (168899, 3, 7),
  (172993, 4, 2),
  (174691, 2, 6),
  (175122, 5, 2),
  (176538, 5, 3),
  (178593, 7, 7),
  (180108, 6, 0),
  (181681, 6, 7),
  (184440, 5, 7),
  (186025, 2, 5),
  (186082, 0, 7),
  (186924, 0, 3),
  (189466, 3, 7),
  (192959, 7, 4),
  (193017, 1, 0),
  (195790, 3, 7),
  (201720, 6, 0),
  (202275, 3, 7),
  (204608, 4, 7),
  (207041, 4, 2),
  (213672, 5, 5),
  (215717, 7, 3),
  (222853, 1, 6),
  (227420, 3, 7),
  (228665, 7, 0),
  (228773, 1, 2),
  (229264, 5, 7),
  (232783, 1, 0),
  (233677, 5, 7),
  (234852, 2, 3),
  (245800, 4, 3),
  (247562, 2, 3),
  (249060, 7, 3),
  (253617, 2, 1),
  (258407, 6, 4),
  (260801, 0, 7),
  (262660, 6, 7),
  (265435, 4, 7),
  (267937, 1, 7),
  (268037, 5, 7),
  (269702, 6, 7),
  (271757, 6, 0),
  (278241, 4, 7),
  (279473, 3, 7),
  (279907, 0, 4),
  (282007, 5, 6),
  (287315, 7, 7),
  (288291, 7, 0),
  (290601, 7, 3),
  (294338, 6, 6),
  (295551, 4, 7),
  (302826, 1, 0),
  (305202, 3, 3),
  (306301, 1, 3),
  (309863, 6, 7),
  (311635, 5, 7),
  (319446, 1, 5),
  (327500, 7, 0),
  (330401, 5, 3),
  (330918, 6, 7),
  (332808, 7, 7),
  (335577, 3, 7),
  (337045, 1, 7),
  (337837, 2, 3),
  (340077, 5, 3),
  (341252, 3, 7),
  (342906, 7, 7),
  (343899, 0, 4),
  (347318, 4, 0),
  (348089, 1, 4),
  (348140, 7, 7),
  (348565, 3, 7),
  (348820, 5, 3),
  (351991, 1, 7),
  (352267, 4, 6),
  (353632, 3, 3),
  (356970, 6, 6),
  (357003, 0, 4),
  (359380, 0, 3),
  (359804, 2, 6),
  (360438, 3, 6),
  (364037, 1, 0),
  (365226, 1, 7),
  (372028, 6, 0),
  (375804, 4, 4),
  (375895, 7, 7),
  (376898, 6, 1),
  (379376, 4, 7),
  (382706, 1, 7),
  (383003, 3, 3),
  (384972, 1, 7),
  (388769, 0, 0),
  (390651, 6, 4),
  (391474, 4, 2),
  (397682, 3, 7),
  (400766, 0, 7),
  (402708, 4, 7),
  (404316, 1, 0),
  (404705, 2, 7),
  (407054, 7, 0),
  (408572, 6, 3),
  (412782, 6, 0),
  (413854, 3, 7),
  (419822, 5, 5),
  (423589, 5, 7),
  (435953, 0, 0),
  (440779, 5, 7),
  (440851, 6, 5),
  (442771, 0, 7),
  (443734, 3, 6),
  (444368, 0, 3),
  (445913, 2, 7),
  (445995, 7, 3),
  (451092, 4, 7),
  (453292, 7, 7),
  (456754, 2, 6),
  (457790, 5, 3),
  (469035, 7, 3),
  (469210, 3, 2),
  (491132, 2, 6),
  (491475, 1, 0),
  (502728, 2, 2),
  (504239, 5, 2),
  (506822, 5, 6),
  (507069, 4, 7),
  (507221, 2, 6),
  (511226, 3, 2),
  (516494, 1, 7),
  (518908, 6, 7),
  (519146, 1, 6),
  (520664, 7, 7),
  (527637, 4, 3),
  (527752, 1, 7),
  (530774, 7, 7),
  (533456, 1, 4),
  (534278, 1, 7),
  (534438, 2, 2),
  (536797, 5, 7),
  (537222, 4, 2),
  (538235, 5, 3),
  (538612, 1, 3),
  (540155, 5, 2),
  (543334, 0, 1),
  (550193, 3, 7),
  (552643, 5, 7),
  (553657, 5, 7),
  (556059, 6, 6),
  (556414, 5, 7),
  (559488, 2, 3),
  (560222, 5, 7),
  (566319, 5, 3),
  (569806, 4, 5),
  (571045, 7, 5),
  (571836, 7, 3),
  (578633, 6, 3),
  (583911, 0, 7),
  (584699, 6, 0),
  (587056, 6, 0),
  (590184, 0, 7),
  (594660, 7, 3),
  (595741, 3, 3),
  (600567, 0, 3),
  (600963, 4, 6),
  (601040, 1, 3),
  (612537, 3, 7),
  (614728, 4, 7),
  (618148, 4, 7),
  (619486, 6, 4),
  (620101, 6, 3),
  (633224, 6, 0),
  (638080, 6, 4),
  (645869, 2, 7),
  (646793, 4, 6),
  (648113, 5, 2),
  (649211, 3, 6),
  (658596, 1, 5),
  (659172, 7, 0),
  (661447, 4, 6),
  (667255, 0, 7),
  (680310, 3, 6),
  (681486, 6, 4),
  (690517, 7, 3),
  (693303, 2, 5),
  (695263, 4, 2),
  (696967, 6, 6),
  (697479, 4, 5),
  (699762, 3, 4),
  (699905, 3, 3),
  (700484, 4, 3),
  (708455, 1, 0),
  (710601, 6, 0),
  (712785, 1, 3),
  (713876, 7, 5),
  (718304, 4, 6),
  (719340, 3, 3),
  (719374, 1, 7),
  (722335, 2, 2),
  (723461, 2, 3),
  (731356, 4, 3),
  (738203, 6, 0),
  (738468, 3, 3),
  (739410, 2, 3),
  (743212, 5, 2),
  (744454, 7, 0),
  (744560, 5, 4),
  (744984, 4, 7),
  (749942, 1, 0),
  (750374, 6, 7),
  (759505, 0, 3),
  (760593, 4, 3),
  (760941, 5, 7),
  (761829, 7, 6),
  (767882, 6, 7),
  (768629, 6, 0),
  (771651, 0, 0),
  (774108, 5, 3),
  (780754, 1, 3),
  (781971, 4, 3),
  (784301, 2, 3),
  (786954, 4, 0),
  (786978, 5, 1),
  (793737, 2, 2),
  (795328, 7, 0),
  (798778, 2, 2),
  (800106, 1, 7),
  (800639, 2, 2),
  (807049, 0, 7),
  (807735, 1, 0),
  (809914, 5, 0),
  (813881, 7, 4),
  (815497, 1, 7),
  (815543, 0, 7),
  (816359, 6, 4),
  (816366, 1, 7),
  (822468, 4, 6),
  (825553, 3, 5),
  (830759, 0, 7),
  (837680, 2, 7),
  (838196, 5, 2),
  (844027, 4, 7),
  (844139, 5, 6),
  (844850, 3, 5),
  (846060, 6, 7),
  (847060, 6, 3),
  (848831, 4, 3),
  (851317, 3, 4),
  (852025, 2, 7),
  (855090, 6, 0),
  (858850, 7, 6),
  (860201, 0, 3),
  (862507, 4, 6),
  (863002, 4, 3),
  (864744, 2, 3),
  (867630, 6, 7),
  (868346, 0, 7),
  (870665, 1, 4),
  (877671, 5, 6),
  (880542, 1, 7),
  (882101, 5, 7),
  (882694, 4, 7),
  (886690, 3, 1),
  (889703, 4, 6),
  (897585, 6, 3),
  (901746, 2, 3),
  (905918, 1, 0),
  (914164, 5, 2),
  (919029, 2, 7),
  (919104, 2, 7),
  (919295, 6, 7),
  (926321, 2, 1),
  (940890, 2, 2),
  (942526, 2, 6),
  (942976, 4, 2),
  (943531, 5, 4),
  (945001, 0, 3),
  (949995, 0, 0),
  (963167, 4, 6),
  (968406, 1, 0),
  (968791, 1, 4),
  (972417, 6, 3),
  (975348, 4, 7),
  (977190, 2, 7),
  (979487, 4, 5),
  (979654, 2, 6),
  (982088, 6, 0),
  (984344, 2, 6),
  (985455, 5, 7),
  (989099, 7, 7),
  (989956, 1, 0),
  (993577, 5, 3),
  (994747, 1, 0),
  (1002626, 4, 6),
  (1003212, 1, 4),
  (1003647, 6, 7),
  (1019987, 0, 5),
  (1030697, 5, 7),
  (1034535, 6, 6),
  (1039475, 7, 4),
  (1049720, 0, 1),
  (1053297, 6, 6),
  (1060436, 1, 6),
  (1061831, 0, 7),
  (1063383, 6, 7),
  (1066992, 2, 2),
  (1074437, 2, 2),
  (1079455, 2, 3),
  (1081143, 6, 4),
  (1086966, 3, 3),
  (1094737, 3, 2),
  (1095813, 5, 3),
  (1104483, 1, 2),
  (1107889, 3, 6),
  (1112505, 4, 7),
  (1114102, 6, 7),
  (1117008, 6, 0),
  (1117947, 5, 7),
  (1120473, 6, 7),
  (1122979, 7, 7),
  (1123971, 0, 5),
  (1124322, 2, 6),
  (1124490, 6, 7),
  (1126905, 7, 4),
  (1127223, 2, 7),
  (1130712, 7, 7),
  (1132764, 6, 0),
  (1133574, 4, 3),
  (1137264, 6, 6),
  (1138138, 7, 0),
  (1139978, 6, 1),
  (1142594, 0, 6),
  (1143104, 5, 3),
  (1143801, 7, 0),
  (1145046, 7, 3),
  (1146069, 5, 6),
  (1146787, 3, 3),
  (1149990, 7, 1),
  (1150208, 3, 7),
  (1150281, 5, 7),
  (1153529, 2, 7),
  (1156623, 7, 0),
  (1159930, 5, 7),
  (1162314, 4, 7),
  (1162355, 5, 3),
  (1168232, 2, 6),
  (1168489, 4, 6),
  (1169088, 5, 2),
  (1169179, 7, 4),
  (1177250, 5, 5),
  (1177465, 3, 2),
  (1184916, 3, 6),
  (1185642, 6, 3),
  (1187420, 4, 0),
  (1191742, 7, 1),
  (1193350, 7, 3),
  (1195553, 5, 5),
  (1196706, 6, 7),
  (1199304, 4, 6),
  (1199527, 2, 3),
  (1200783, 4, 7),
  (1201058, 3, 0),
  (1205373, 1, 3),
  (1210880, 1, 6),
  (1218037, 6, 7),
  (1221312, 7, 6),
  (1225117, 2, 2),
  (1227254, 3, 2),
  (1233419, 2, 6),
  (1236676, 7, 4),
  (1239725, 1, 7),
  (1260718, 3, 4),
  (1262409, 7, 3),
  (1263758, 7, 7),
  (1264428, 3, 5),
  (1266946, 0, 1),
  (1268720, 2, 3),
  (1271430, 0, 3),
  (1272759, 3, 3),
  (1273896, 7, 7),
  (1274591, 3, 3),
  (1279630, 4, 7),
  (1282147, 5, 3),
  (1283452, 4, 7),
  (1288902, 7, 6),
  (1291640, 2, 7),
  (1293355, 1, 0),
  (1294004, 5, 3),
  (1294052, 4, 3),
  (1298600, 0, 7),
  (1299924, 5, 3),
  (1300874, 6, 3),
  (1301661, 6, 7),
  (1302794, 2, 3),
  (1312359, 3, 3),
  (1314580, 2, 3),
  (1320297, 2, 7),
  (1327229, 6, 7),
  (1327611, 4, 6),
  (1327867, 4, 3),
  (1328057, 2, 3),
  (1328203, 7, 0),
  (1328816, 6, 5),
  (1330653, 4, 3),
  (1340677, 6, 7),
  (1340811, 2, 3),
  (1343930, 6, 4),
  (1348458, 2, 2),
  (1349483, 0, 3),
  (1354317, 4, 7),
  (1360605, 0, 5),
  (1363702, 0, 7),
  (1364487, 5, 3),
  (1365508, 3, 6),
  (1368669, 2, 2),
  (1370850, 2, 0),
  (1378049, 2, 2),
  (1381759, 4, 4),
  (1387144, 0, 0),
  (1387210, 0, 6),
  (1390024, 7, 0),
  (1395251, 7, 0),
  (1398778, 4, 5),
  (1400029, 6, 5),
  (1405273, 5, 7),
  (1406163, 0, 0),
  (1407971, 7, 7),
  (1414313, 3, 2),
  (1416164, 4, 6),
  (1417079, 3, 3),
  (1427432, 4, 5),
  (1429371, 6, 1),
  (1432850, 7, 3),
  (1435324, 1, 7),
  (1444008, 0, 7),
  (1448532, 6, 3),
  (1452808, 3, 6),
  (1454170, 1, 0),
  (1455169, 1, 7),
  (1458730, 1, 4),
  (1463293, 2, 6),
  (1464012, 0, 3),
  (1467484, 0, 0),
  (1469290, 3, 7),
  (1469379, 6, 6),
  (1472564, 5, 6),
  (1477995, 3, 3),
  (1480310, 1, 4),
  (1481006, 7, 0),
  (1482626, 5, 2),
  (1484803, 7, 0),
  (1487938, 4, 3),
  (1492187, 2, 5),
  (1493327, 1, 0),
  (1493343, 4, 3),
  (1493587, 7, 0),
  (1507406, 5, 7),
  (1513082, 2, 1),
  (1525200, 4, 1),
  (1526731, 5, 2),
  (1529632, 6, 7),
  (1540263, 1, 0),
  (1540400, 2, 6),
  (1541369, 0, 0),
  (1542237, 1, 0),
  (1543872, 3, 2),
  (1552345, 2, 7),
  (1555174, 4, 3),
  (1556947, 2, 3),
  (1561127, 5, 3),
  (1564523, 1, 4),
  (1567229, 5, 7),
  (1575832, 7, 0),
  (1576460, 6, 7),
  (1580617, 1, 3),
  (1582098, 1, 7),
  (1582806, 2, 3),
  (1589288, 5, 3),
  (1592697, 3, 6),
  (1595853, 2, 2),
  (1597922, 0, 7),
  (1601640, 1, 3),
  (1604367, 7, 3),
  (1605280, 5, 6),
  (1608233, 7, 3),
  (1610632, 6, 0),
  (1611291, 3, 3),
  (1613011, 1, 7),
  (1613437, 6, 4),
  (1615016, 2, 6),
  (1618736, 6, 7),
  (1619387, 6, 7),
  (1621123, 0, 4),
  (1622181, 2, 7),
  (1625685, 1, 7),
  (1625797, 1, 7),
  (1632074, 1, 4),
  (1633527, 0, 2),
  (1636120, 7, 7),
  (1636986, 5, 3),
  (1637009, 0, 4),
  (1638728, 4, 7),
  (1639637, 6, 3),
  (1642269, 4, 2),
  (1644009, 3, 2),
  (1645162, 7, 0),
  (1646295, 2, 6),
  (1648245, 4, 7),
  (1652539, 1, 0),
  (1654096, 3, 1),
  (1661803, 4, 3),
  (1669541, 4, 3),
  (1670937, 6, 0),
  (1684385, 2, 2),
  (1684575, 3, 7),
  (1685431, 5, 2),
  (1691357, 4, 5),
  (1693200, 7, 0),
  (1699190, 0, 7),
  (1699331, 2, 7),
  (1709192, 2, 0),
  (1709786, 4, 2),
  (1710150, 2, 3),
  (1711498, 2, 3),
  (1712532, 4, 7),
  (1718194, 1, 4),
  (1730756, 5, 3),
  (1731205, 2, 3),
  (1737837, 1, 0),
  (1739606, 5, 7),
  (1740583, 6, 0),
  (1746052, 0, 6),
  (1746278, 2, 6),
  (1746970, 2, 6),
  (1747049, 6, 3),
  (1748193, 4, 3),
  (1754753, 5, 7),
  (1757008, 4, 4),
  (1757532, 6, 7),
  (1758480, 0, 7),
  (1758743, 7, 7),
  (1760207, 0, 7),
  (1760686, 7, 7),
  (1760924, 6, 6),
  (1761122, 3, 5),
  (1763529, 5, 7),
  (1769011, 6, 0),
  (1771370, 4, 4),
  (1772341, 2, 7),
  (1773325, 2, 7),
  (1779514, 3, 7),
  (1780181, 2, 3),
  (1781518, 6, 0),
  (1782408, 5, 3),
  (1782928, 1, 7),
  (1783016, 0, 3),
  (1789938, 6, 3),
  (1792024, 7, 3),
  (1793839, 6, 4),
  (1799053, 2, 7),
  (1803286, 0, 0),
  (1806138, 2, 7),
  (1807838, 7, 3),
  (1810829, 4, 2),
  (1811326, 6, 7),
  (1812901, 3, 3),
  (1818955, 4, 3),
  (1820704, 5, 3),
  (1822812, 7, 3),
  (1825303, 4, 6),
  (1829188, 5, 6),
  (1837601, 7, 7),
  (1841447, 4, 2),
  (1845419, 2, 7),
  (1847706, 2, 7),
  (1849257, 3, 3),
  (1851759, 4, 5),
  (1856714, 0, 1),
  (1857786, 0, 0),
  (1861105, 5, 3),
  (1871849, 3, 4),
  (1873482, 3, 3),
  (1874458, 0, 4),
  (1882874, 6, 7),
  (1892647, 2, 2),
  (1894029, 2, 7),
  (1898507, 1, 0),
  (1899411, 1, 4),
  (1904323, 7, 0),
  (1915470, 4, 3),
  (1915963, 7, 4),
  (1920091, 7, 0),
  (1924218, 6, 6),
  (1924723, 7, 0),
  (1926609, 3, 2),
  (1933526, 5, 3),
  (1936283, 0, 4),
  (1938731, 3, 3),
  (1940583, 4, 6),
  (1941398, 2, 7),
  (1942120, 0, 4),
  (1942783, 0, 0),
  (1947452, 1, 7),
  (1949232, 4, 2),
  (1954784, 4, 5),
  (1956706, 4, 7),
  (1968002, 6, 1),
  (1968791, 2, 3),
  (1971213, 3, 3),
  (1973275, 7, 6),
  (1976743, 5, 2),
  (1976959, 3, 3),
  (1979785, 6, 5),
  (1991522, 1, 0),
  (2002581, 1, 7),
  (2003248, 6, 0),
  (2010636, 6, 4),
  (2010810, 6, 5),
  (2012754, 0, 7),
  (2015873, 1, 3),
  (2016936, 2, 2),
  (2019873, 6, 7),
  (2027012, 1, 0),
  (2028660, 5, 3),
  (2029234, 1, 7),
  (2032185, 7, 4),
  (2038689, 4, 2),
  (2040047, 3, 3),
  (2044613, 1, 4),
  (2045575, 1, 4),
  (2053598, 0, 7),
  (2058020, 3, 6),
  (2061422, 6, 7),
  (2065017, 3, 7),
  (2067048, 5, 7),
  (2069358, 6, 0),
  (2077018, 5, 3),
  (2079262, 6, 3),
  (2082907, 5, 6),
  (2083145, 4, 6),
  (2083877, 7, 6),
  (2083963, 4, 4),
  (2091814, 3, 3),
  (2093135, 7, 7),
  (2093878, 3, 2),
  (2096144, 2, 6),
  (2097425, 6, 1),
  (2108700, 7, 7),
  (2110939, 4, 5),
  (2113531, 2, 7),
  (2118639, 1, 4),
  (2120512, 2, 3),
  (2129803, 1, 7),
  (2130850, 7, 0),
  (2135397, 0, 0),
  (2136107, 2, 3),
  (2149396, 4, 7),
  (2150004, 7, 3),
  (2161514, 0, 0),
  (2162588, 1, 7),
  (2162960, 7, 7),
  (2167640, 6, 7),
  (2174327, 4, 3),
  (2175049, 4, 7),
  (2182755, 7, 5),
  (2189488, 0, 4),
  (2191466, 0, 7),
  (2198276, 6, 2),
  (2202333, 6, 3),
  (2204071, 7, 4),
  (2210921, 1, 3),
  (2215767, 2, 6),
  (2220701, 4, 3),
  (2222333, 6, 3),
  (2222759, 0, 7),
  (2237127, 0, 7),
  (2237131, 0, 4),
  (2239268, 1, 0),
  (2250395, 3, 3),
  (2253134, 3, 7),
  (2257895, 4, 2),
  (2261759, 6, 4),
  (2263575, 3, 7),
  (2264569, 5, 2),
  (2270007, 3, 7),
  (2272581, 4, 1),
  (2278364, 2, 5),
  (2280349, 5, 3),
  (2280394, 2, 6),
  (2282443, 2, 5),
  (2283826, 1, 7),
  (2284910, 4, 3),
  (2286485, 6, 7),
  (2288671, 2, 7),
  (2290744, 5, 6),
  (2296882, 6, 7),
  (2304601, 3, 1),
  (2306378, 0, 0),
  (2308999, 2, 3),
  (2309225, 6, 0),
  (2311651, 0, 7),
  (2312581, 1, 0),
  (2320086, 4, 3),
  (2324487, 3, 3),
  (2324681, 5, 5),
  (2328885, 1, 1),
  (2329105, 0, 4),
  (2329478, 1, 3),
  (2331604, 6, 7),
  (2332456, 2, 7),
  (2332537, 3, 3),
  (2333590, 1, 4),
  (2339733, 2, 7),
  (2341509, 0, 4),
  (2341824, 3, 5),
  (2345175, 0, 3),
  (2345408, 5, 3),
  (2347186, 6, 6),
  (2347852, 1, 7),
  (2355109, 6, 0),
  (2363379, 3, 3),
  (2364658, 6, 4),
  (2366705, 6, 0),
  (2375934, 3, 6),
  (2380840, 3, 6),
  (2390471, 4, 3),
  (2392425, 7, 0),
  (2404175, 0, 1),
  (2410611, 4, 2),
  (2411059, 4, 7),
  (2413570, 7, 7),
  (2415243, 2, 3),
  (2418924, 7, 6),
  (2422328, 7, 3),
  (2422664, 5, 7),
  (2429647, 7, 7),
  (2429940, 2, 3),
  (2433020, 7, 4),
  (2433239, 6, 7),
  (2435821, 0, 7),
  (2435860, 0, 3),
  (2442969, 5, 6),
  (2443645, 3, 3),
  (2453386, 4, 7),
  (2453647, 2, 5),
  (2455066, 1, 7),
  (2455998, 4, 2),
  (2457857, 5, 2),
  (2462675, 4, 7),
  (2463505, 7, 0),
  (2464222, 5, 7),
  (2468167, 4, 3),
  (2473588, 6, 4),
  (2474119, 7, 0),
  (2479493, 6, 7),
  (2480115, 7, 5),
  (2485669, 3, 7),
  (2485745, 3, 5),
  (2487091, 1, 7),
  (2491360, 6, 7),
  (2495488, 0, 7),
  (2498833, 4, 3),
  (2503577, 0, 6),
  (2507304, 2, 3),
  (2511253, 3, 3),
  (2520826, 6, 7),
  (2521836, 5, 5),
  (2527119, 5, 3),
  (2531170, 4, 6),
  (2537042, 1, 0),
  (2543976, 1, 7),
  (2544581, 2, 3),
  (2548391, 0, 7),
  (2549746, 0, 1),
  (2550087, 1, 3),
  (2552065, 3, 5),
  (2553631, 5, 3),
  (2553641, 6, 0),
  (2558850, 2, 3),
  (2560092, 7, 7),
  (2565066, 5, 6),
  (2565841, 2, 2),
  (2570545, 6, 0),
  (2571401, 0, 0),
  (2571568, 3, 7),
  (2574146, 2, 6),
  (2581478, 4, 7),
  (2583264, 4, 4),
  (2585120, 5, 6),
  (2586168, 5, 5),
  (2592597, 6, 7),
  (2596214, 0, 3),
  (2598836, 4, 4),
  (2601994, 1, 7),
  (2603431, 6, 0),
  (2603734, 4, 7),
  (2604156, 3, 6),
  (2605842, 6, 0),
  (2607889, 1, 0),
  (2611774, 4, 3),
  (2612265, 1, 3),
  (2612359, 1, 0),
  (2616869, 1, 3),
  (2624183, 1, 4),
  (2626733, 3, 6),
  (2628185, 3, 3),
  (2638873, 7, 5),
  (2639200, 6, 3),
  (2643530, 3, 3),
  (2645313, 1, 6),
  (2647597, 3, 7),
  (2649103, 7, 0),
  (2653896, 6, 7),
  (2654875, 5, 7),
  (2657168, 4, 2),
  (2657514, 3, 7),
  (2660571, 6, 0),
  (2664290, 4, 1),
  (2669577, 1, 0),
  (2670099, 0, 0),
  (2677418, 2, 6),
  (2682825, 5, 2),
  (2683571, 3, 6),
  (2700487, 6, 0),
  (2700735, 0, 4),
  (2702753, 7, 0),
  (2703797, 1, 7),
  (2704944, 0, 7),
  (2716781, 5, 7),
  (2726011, 1, 3),
  (2729227, 5, 5),
  (2732873, 5, 7),
  (2736742, 0, 4),
  (2737882, 2, 5),
  (2739658, 0, 6),
  (2742700, 3, 3),
  (2743091, 6, 0),
  (2752436, 3, 2),
  (2753912, 2, 7),
  (2754020, 0, 7),
  (2754567, 4, 5),
  (2758093, 4, 7),
  (2762109, 3, 6),
  (2763494, 4, 6),
  (2764441, 1, 4),
  (2767224, 5, 5),
  (2768160, 7, 4),
  (2780270, 3, 6),
  (2780277, 4, 7),
  (2781886, 5, 1),
  (2782544, 1, 0),
  (2785763, 4, 7),
  (2788707, 4, 3),
  (2788757, 2, 7),
  (2793369, 6, 5),
  (2797476, 2, 7),
  (2801008, 2, 3),
  (2802485, 0, 7),
  (2802698, 7, 7),
  (2805400, 4, 3),
  (2806180, 5, 2),
  (2806182, 3, 3),
  (2806701, 3, 2),
  (2811631, 5, 2),
  (2812659, 0, 3),
  (2813922, 1, 4),
  (2817075, 5, 2),
  (2818170, 2, 3),
  (2825302, 0, 3),
  (2827608, 5, 7),
  (2827831, 7, 7),
  (2830525, 7, 0),
  (2831153, 0, 3),
  (2834263, 0, 7),
  (2836723, 1, 7),
  (2838987, 3, 3),
  (2845429, 3, 7),
  (2845875, 1, 7),
  (2847597, 4, 7),
  (2848783, 1, 7),
  (2849408, 7, 4),
  (2849453, 1, 0),
  (2851724, 2, 6),
  (2855671, 7, 7),
  (2858078, 2, 7),
  (2860894, 3, 3),
  (2862531, 5, 3),
  (2863442, 0, 7),
  (2863677, 2, 2),
  (2866137, 2, 3),
  (2867205, 0, 6),
  (2869360, 0, 3),
  (2870295, 6, 7),
  (2875159, 0, 0),
  (2876081, 3, 7),
  (2876160, 5, 2),
  (2878055, 0, 5),
  (2881272, 4, 2),
  (2884761, 1, 4),
  (2885029, 6, 4),
  (2889912, 3, 5),
  (2899425, 2, 3),
  (2902217, 6, 6),
  (2906336, 1, 7),
  (2907951, 4, 6),
  (2909530, 5, 7),
  (2911971, 2, 2),
  (2911975, 2, 3),
  (2914475, 6, 7),
  (2917758, 5, 7),
  (2920919, 6, 3),
  (2924482, 5, 2),
  (2926270, 3, 6),
  (2927611, 3, 3),
  (2930452, 2, 3),
  (2930955, 7, 7),
  (2934359, 1, 3),
  (2934395, 0, 0),
  (2938000, 6, 7),
  (2938445, 2, 3),
  (2943549, 0, 6),
  (2945949, 6, 4),
  (2953719, 7, 7),
  (2956518, 7, 4),
  (2957186, 2, 6),
  (2958188, 6, 6),
  (2959191, 7, 7),
  (2962103, 0, 6),
  (2963626, 5, 7),
  (2970913, 4, 3),
  (2974004, 7, 4),
  (2977505, 1, 0),
  (2977947, 0, 7),
  (2984788, 2, 3),
  (3004783, 7, 0),
  (3008332, 6, 0),
  (3009532, 4, 3),
  (3012446, 4, 7),
  (3013209, 1, 6),
  (3015590, 4, 7),
  (3019032, 2, 2),
  (3020663, 5, 4),
  (3021682, 7, 0),
  (3023495, 3, 3),
  (3025002, 0, 6),
  (3026061, 2, 3),
  (3026188, 1, 7),
  (3029378, 6, 0),
  (3032667, 4, 3),
  (3034799, 2, 2),
  (3035318, 3, 3),
  (3042196, 3, 0),
  (3045307, 4, 6),
  (3051077, 4, 3),
  (3054138, 5, 2),
  (3054158, 3, 3),
  (3055480, 5, 7),
  (3056900, 4, 7),
  (3065798, 1, 0),
  (3067795, 0, 4),
  (3073821, 0, 5),
  (3075416, 3, 5),
  (3078556, 7, 7),
  (3079326, 0, 4),
  (3080398, 7, 3),
  (3081547, 2, 3),
  (3085220, 6, 7),
  (3087091, 7, 7),
  (3093011, 5, 7),
  (3103676, 5, 3),
  (3108773, 6, 3),
  (3109709, 5, 3),
  (3115329, 4, 2),
  (3117469, 3, 3),
  (3117744, 4, 3),
  (3118128, 1, 4),
  (3125060, 3, 6),
  (3128791, 6, 7),
  (3130674, 2, 1),
  (3132108, 6, 0),
  (3135901, 3, 3),
  (3138093, 6, 3),
  (3141844, 3, 3),
  (3142453, 4, 6),
  (3142486, 1, 6),
  (3145070, 1, 3),
  (3148023, 5, 7),
  (3149491, 5, 5),
  (3150095, 0, 7),
  (3151842, 6, 7),
  (3156478, 7, 6),
  (3157367, 0, 2),
  (3170856, 7, 7),
  (3188217, 6, 3),
  (3188414, 2, 2),
  (3199912, 0, 3),
  (3204691, 4, 7),
  (3205795, 2, 7),
  (3210594, 3, 5),
  (3211858, 7, 4),
  (3212044, 4, 5),
  (3217257, 7, 0),
  (3220271, 4, 5),
  (3220961, 5, 3),
  (3224910, 1, 0),
  (3228139, 5, 3),
  (3230724, 4, 3),
  (3231644, 7, 5),
  (3235681, 0, 4),
  (3236202, 0, 0),
  (3237858, 2, 7),
  (3238742, 5, 7),
  (3239133, 0, 0),
  (3241224, 2, 3),
  (3241491, 0, 7),
  (3243370, 1, 0),
  (3246734, 4, 3),
  (3249049, 0, 0),
  (3249450, 1, 4),
  (3252428, 5, 6),
  (3254354, 2, 6),
  (3254601, 6, 4),
  (3263650, 2, 3),
  (3265558, 7, 5),
  (3269210, 4, 7),
  (3270688, 2, 2),
  (3274435, 0, 7),
  (3276446, 0, 0),
  (3278654, 5, 6),
  (3279522, 0, 7),
  (3283922, 4, 6),
  (3293504, 6, 7),
  (3293733, 0, 7),
  (3296879, 6, 4),
  (3297230, 0, 7),
  (3299856, 6, 4),
  (3301104, 0, 7),
  (3305566, 1, 7),
  (3307355, 1, 0),
  (3307383, 5, 3),
  (3307708, 6, 4),
  (3315369, 6, 4),
  (3316866, 6, 7),
  (3317745, 3, 6),
  (3318894, 6, 5),
  (3321034, 5, 2),
  (3321402, 4, 3),
  (3337329, 1, 4),
  (3337577, 1, 7),
  (3344834, 2, 6),
  (3351445, 5, 3),
  (3354337, 0, 0),
  (3354771, 5, 4),
  (3354901, 6, 7),
  (3357134, 6, 0),
  (3359930, 3, 7),
  (3366221, 2, 7),
  (3366350, 2, 5),
  (3368192, 4, 7),
  (3376022, 0, 6),
  (3377177, 6, 7),
  (3377682, 7, 0),
  (3383381, 1, 0),
  (3385218, 4, 5),
  (3385575, 1, 0),
  (3387244, 1, 7),
  (3390659, 7, 3),
  (3396723, 3, 2),
  (3398838, 1, 5),
  (3405806, 0, 6),
  (3406913, 6, 0),
  (3411112, 2, 4),
  (3420099, 7, 3),
  (3423290, 6, 4),
  (3427467, 4, 6),
  (3430654, 3, 1),
  (3431899, 3, 7),
  (3432193, 4, 3),
  (3437988, 1, 7),
  (3443615, 1, 7),
  (3444467, 7, 6),
  (3445440, 6, 6),
  (3446798, 3, 1),
  (3449515, 4, 7),
  (3449743, 1, 4),
  (3452634, 3, 3),
  (3458968, 3, 6),
  (3461116, 6, 6),
  (3462714, 6, 7),
  (3462736, 3, 7),
  (3464313, 3, 3),
  (3464495, 6, 0),
  (3465881, 6, 6),
  (3466666, 6, 0),
  (3470078, 1, 7),
  (3473776, 3, 3),
  (3477331, 0, 0),
  (3477497, 1, 7),
  (3477630, 0, 0),
  (3481069, 0, 3),
  (3481949, 3, 1),
  (3487052, 3, 6),
  (3487430, 2, 2),
  (3489616, 7, 0),
  (3489618, 4, 2),
  (3489654, 5, 5),
  (3491655, 4, 7),
  (3492474, 2, 3),
  (3493787, 0, 2),
  (3496679, 3, 7),
  (3498730, 4, 6),
  (3500450, 5, 4),
  (3507450, 6, 7),
  (3508491, 5, 3),
  (3513927, 5, 7),
  (3521832, 7, 3),
  (3522049, 5, 3),
  (3522558, 1, 3),
  (3532248, 0, 4),
  (3560228, 4, 2),
  (3560908, 3, 3),
  (3565108, 6, 2),
  (3567093, 5, 6),
  (3568490, 1, 0),
  (3570519, 5, 6),
  (3572222, 0, 7),
  (3572356, 5, 3),
  (3573726, 2, 3),
  (3581980, 5, 6),
  (3583843, 1, 3),
  (3589011, 3, 3),
  (3593250, 1, 7),
  (3594027, 6, 0),
  (3596400, 3, 3),
  (3596890, 0, 7),
  (3597366, 1, 0),
  (3598264, 0, 0),
])