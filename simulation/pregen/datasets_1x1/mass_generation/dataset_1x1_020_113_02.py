from util import *
schedule = deque([
  (5959, 7, 3),
  (13296, 6, 6),
  (13709, 3, 2),
  (14787, 2, 3),
  (16316, 5, 7),
  (18958, 1, 7),
  (19410, 2, 3),
  (24673, 5, 7),
  (25040, 3, 6),
  (26364, 1, 0),
  (31430, 6, 7),
  (31757, 1, 5),
  (35054, 6, 0),
  (38707, 5, 7),
  (40413, 0, 7),
  (48936, 4, 7),
  (52942, 6, 0),
  (55418, 7, 0),
  (55551, 5, 2),
  (56534, 3, 5),
  (57536, 7, 7),
  (60085, 4, 6),
  (76836, 6, 6),
  (78646, 7, 7),
  (79142, 0, 0),
  (83436, 1, 7),
  (88605, 0, 7),
  (96254, 3, 1),
  (97342, 0, 0),
  (98126, 2, 2),
  (109475, 4, 6),
  (116955, 4, 2),
  (120453, 6, 7),
  (123806, 2, 7),
  (123971, 1, 7),
  (124217, 5, 6),
  (129920, 1, 0),
  (130390, 4, 7),
  (133133, 4, 3),
  (137988, 5, 7),
  (141360, 0, 7),
  (144695, 3, 7),
  (146115, 6, 4),
  (148591, 3, 7),
  (150450, 2, 6),
  (150550, 3, 7),
  (156684, 6, 4),
  (158621, 1, 3),
  (158974, 1, 6),
  (159893, 1, 0),
  (166972, 5, 6),
  (167987, 7, 3),
  (174735, 1, 0),
  (186661, 0, 7),
  (189026, 7, 6),
  (192012, 1, 3),
  (203066, 6, 3),
  (206435, 1, 7),
  (207279, 5, 3),
  (209994, 0, 0),
  (213245, 7, 7),
  (213604, 3, 7),
  (215706, 5, 6),
  (220562, 3, 3),
  (221394, 6, 4),
  (221955, 2, 2),
  (223050, 7, 1),
  (225152, 7, 6),
  (226220, 0, 0),
  (228089, 3, 7),
  (230966, 5, 7),
  (237489, 5, 5),
  (238632, 5, 3),
  (242329, 7, 7),
  (242338, 1, 5),
  (243020, 3, 6),
  (243415, 1, 2),
  (245868, 1, 0),
  (251445, 6, 2),
  (256763, 1, 3),
  (256842, 1, 7),
  (259670, 0, 7),
  (260090, 1, 0),
  (262802, 5, 2),
  (263486, 2, 3),
  (264380, 5, 6),
  (269865, 2, 6),
  (275483, 4, 7),
  (277085, 0, 6),
  (280486, 2, 6),
  (280608, 6, 0),
  (282385, 7, 3),
  (284148, 0, 4),
  (284653, 2, 6),
  (291545, 3, 7),
  (294674, 2, 3),
  (304836, 4, 7),
  (305072, 0, 3),
  (311197, 4, 6),
  (311659, 1, 7),
  (315763, 7, 7),
  (315802, 2, 7),
  (318568, 7, 7),
  (320052, 0, 7),
  (322862, 0, 7),
  (324840, 0, 0),
  (328403, 6, 4),
  (330171, 2, 2),
  (332557, 6, 7),
  (332817, 0, 0),
  (333366, 5, 5),
  (333956, 4, 7),
  (339221, 4, 3),
  (350363, 7, 0),
  (350397, 7, 0),
  (353685, 5, 7),
  (353956, 6, 3),
  (364037, 0, 3),
  (366280, 6, 6),
  (378067, 4, 3),
  (379358, 1, 4),
  (381370, 3, 5),
  (384083, 7, 4),
  (390765, 1, 7),
  (394363, 4, 3),
  (395628, 4, 7),
  (395769, 2, 5),
  (400804, 2, 7),
  (401829, 0, 7),
  (406795, 6, 7),
  (407734, 6, 7),
  (410927, 5, 3),
  (411941, 4, 7),
  (415168, 6, 4),
  (419343, 7, 0),
  (420043, 4, 7),
  (421566, 7, 3),
  (424547, 5, 7),
  (426188, 6, 7),
  (427068, 0, 7),
  (427366, 1, 7),
  (428517, 4, 7),
  (429479, 0, 7),
  (430000, 1, 3),
  (431995, 5, 7),
  (434836, 1, 4),
  (435957, 3, 5),
  (439068, 0, 4),
  (442794, 7, 6),
  (444146, 1, 3),
  (446489, 1, 0),
  (448149, 5, 7),
  (450032, 0, 3),
  (451128, 1, 0),
  (453904, 4, 3),
  (459784, 7, 4),
  (466144, 6, 4),
  (466642, 5, 7),
  (467217, 3, 7),
  (472531, 4, 4),
  (473021, 6, 0),
  (475006, 5, 4),
  (475108, 3, 0),
  (476366, 4, 7),
  (476867, 1, 7),
  (480355, 0, 0),
  (482000, 3, 3),
  (486206, 4, 2),
  (489656, 7, 7),
  (489880, 7, 0),
  (491784, 3, 7),
  (492513, 3, 7),
  (496069, 7, 6),
  (496499, 3, 3),
  (501393, 3, 3),
  (506447, 0, 4),
  (508487, 6, 4),
  (511399, 2, 2),
  (519340, 3, 7),
  (519888, 5, 2),
  (521860, 7, 7),
  (527452, 4, 4),
  (534857, 4, 7),
  (535787, 1, 4),
  (538775, 2, 2),
  (538839, 6, 7),
  (545096, 7, 3),
  (550410, 6, 7),
  (551501, 3, 5),
  (556165, 4, 3),
  (556405, 7, 3),
  (557646, 1, 3),
  (563448, 1, 6),
  (563920, 6, 4),
  (565961, 6, 3),
  (569571, 0, 3),
  (575726, 6, 7),
  (581295, 4, 7),
  (582864, 1, 7),
  (584589, 1, 5),
  (585013, 6, 4),
  (587457, 0, 3),
  (587578, 2, 7),
  (589156, 4, 7),
  (590724, 2, 2),
  (594028, 7, 3),
  (600332, 6, 7),
  (602085, 2, 6),
  (603409, 6, 3),
  (603465, 4, 3),
  (605594, 3, 7),
  (608711, 5, 7),
  (609268, 6, 7),
  (610905, 5, 6),
  (615774, 3, 3),
  (617460, 0, 7),
  (619924, 7, 0),
  (620748, 5, 7),
  (623056, 6, 7),
  (637880, 2, 7),
  (644397, 4, 7),
  (655331, 1, 7),
  (657174, 6, 4),
  (661020, 4, 3),
  (662404, 4, 3),
  (662748, 4, 3),
  (663773, 0, 7),
  (665405, 5, 7),
  (667780, 4, 6),
  (672053, 2, 7),
  (675826, 4, 3),
  (679795, 2, 6),
  (691704, 5, 5),
  (692713, 3, 3),
  (696358, 5, 3),
  (699611, 5, 7),
  (700106, 6, 7),
  (703376, 5, 4),
  (703598, 7, 3),
  (703985, 5, 7),
  (705646, 1, 0),
  (710587, 2, 6),
  (715908, 5, 7),
  (719929, 6, 0),
  (720534, 0, 0),
  (720833, 2, 3),
  (725250, 0, 3),
  (725531, 6, 4),
  (734833, 7, 3),
  (736869, 1, 7),
  (737680, 5, 7),
  (742203, 3, 6),
  (743504, 1, 4),
  (746677, 7, 0),
  (752297, 0, 7),
  (759775, 2, 4),
  (760811, 5, 7),
  (761960, 2, 7),
  (763410, 1, 4),
  (765359, 6, 7),
  (767701, 1, 5),
  (769709, 5, 3),
  (770962, 0, 5),
  (771346, 6, 2),
  (771371, 5, 2),
  (773121, 0, 3),
  (773688, 0, 6),
  (775156, 5, 7),
  (777939, 3, 7),
  (780213, 7, 7),
  (783166, 7, 0),
  (788173, 4, 7),
  (792640, 7, 3),
  (795636, 2, 7),
  (804828, 1, 6),
  (809294, 4, 7),
  (822392, 7, 4),
  (822742, 3, 2),
  (823784, 2, 7),
  (826692, 1, 3),
  (832526, 7, 7),
  (835120, 5, 1),
  (836345, 2, 2),
  (840210, 0, 3),
  (842605, 6, 0),
  (843629, 0, 7),
  (847592, 5, 7),
  (849793, 3, 7),
  (850722, 6, 7),
  (856897, 4, 7),
  (857019, 2, 7),
  (858849, 3, 7),
  (863297, 3, 7),
  (876474, 0, 7),
  (877766, 5, 5),
  (878898, 1, 4),
  (879444, 6, 0),
  (880052, 6, 7),
  (884875, 7, 0),
  (887851, 4, 3),
  (888155, 1, 7),
  (896229, 4, 3),
  (897544, 4, 7),
  (899921, 4, 3),
  (902051, 2, 7),
  (903179, 2, 6),
  (904195, 3, 5),
  (904532, 6, 5),
  (906131, 4, 3),
  (906727, 6, 4),
  (907023, 7, 4),
  (912302, 5, 7),
  (912417, 1, 2),
  (915695, 4, 3),
  (922338, 1, 7),
  (938238, 3, 2),
  (946978, 6, 5),
  (949146, 1, 3),
  (949691, 7, 0),
  (952181, 0, 7),
  (953575, 4, 3),
  (953895, 4, 7),
  (954940, 2, 7),
  (957181, 0, 7),
  (959143, 2, 7),
  (959511, 7, 6),
  (959837, 2, 2),
  (960777, 1, 3),
  (962029, 5, 7),
  (963652, 1, 3),
  (966958, 6, 7),
  (977689, 1, 7),
  (978793, 7, 0),
  (986114, 6, 7),
  (990242, 6, 2),
  (990374, 6, 7),
  (992605, 4, 3),
  (1004120, 5, 7),
  (1005337, 5, 7),
  (1006058, 6, 5),
  (1006953, 3, 5),
  (1008422, 3, 6),
  (1008703, 7, 7),
  (1013101, 3, 6),
  (1016030, 1, 0),
  (1016234, 6, 7),
  (1022470, 1, 2),
  (1024923, 2, 7),
  (1028626, 1, 3),
  (1029012, 6, 7),
  (1030576, 4, 7),
  (1033578, 1, 6),
  (1036186, 2, 7),
  (1036433, 1, 7),
  (1036874, 7, 6),
  (1040318, 5, 1),
  (1041705, 7, 7),
  (1042790, 7, 3),
  (1044151, 1, 3),
  (1044790, 2, 7),
  (1047872, 5, 6),
  (1048991, 0, 7),
  (1053172, 7, 7),
  (1070189, 4, 5),
  (1072650, 7, 3),
  (1073502, 0, 0),
  (1074279, 4, 6),
  (1078972, 3, 7),
  (1080463, 7, 7),
  (1080867, 0, 4),
  (1083242, 2, 3),
  (1083373, 2, 5),
  (1083868, 0, 7),
  (1084045, 4, 3),
  (1085446, 4, 2),
  (1086848, 4, 3),
  (1087443, 7, 7),
  (1093906, 4, 3),
  (1098203, 0, 0),
  (1099837, 1, 7),
  (1103743, 6, 3),
  (1104605, 6, 0),
  (1115059, 3, 7),
  (1116016, 6, 7),
  (1116444, 5, 3),
  (1119832, 5, 3),
  (1119832, 5, 6),
  (1121921, 7, 0),
  (1125209, 4, 3),
  (1127612, 4, 2),
  (1127770, 6, 7),
  (1128237, 7, 7),
  (1137064, 5, 6),
  (1140582, 7, 0),
  (1142074, 7, 7),
  (1144067, 6, 0),
  (1148556, 0, 6),
  (1150590, 0, 0),
  (1150889, 1, 6),
  (1151591, 4, 7),
  (1153025, 5, 6),
  (1154702, 3, 7),
  (1155224, 2, 7),
  (1155549, 3, 7),
  (1159428, 0, 3),
  (1160012, 3, 2),
  (1161629, 5, 7),
  (1162681, 1, 0),
  (1165818, 4, 7),
  (1165973, 6, 5),
  (1169485, 3, 7),
  (1172841, 1, 6),
  (1177219, 1, 7),
  (1181939, 2, 3),
  (1183240, 6, 0),
  (1183288, 1, 7),
  (1183312, 6, 0),
  (1185378, 7, 7),
  (1187341, 0, 0),
  (1190287, 4, 6),
  (1191706, 2, 5),
  (1195155, 3, 4),
  (1200337, 2, 3),
  (1200742, 0, 5),
  (1220087, 3, 3),
  (1225369, 7, 2),
  (1227349, 5, 5),
  (1230388, 5, 6),
  (1235335, 3, 3),
  (1238752, 6, 7),
  (1250245, 1, 3),
  (1253420, 2, 3),
  (1256744, 5, 6),
  (1256895, 2, 2),
  (1258034, 3, 7),
  (1259128, 5, 7),
  (1259741, 4, 7),
  (1259973, 5, 3),
  (1267204, 5, 3),
  (1268083, 7, 3),
  (1271651, 2, 2),
  (1273154, 0, 0),
  (1275297, 3, 3),
  (1278899, 2, 3),
  (1280524, 7, 4),
  (1280942, 6, 7),
  (1285656, 3, 2),
  (1287373, 3, 3),
  (1287540, 1, 0),
  (1288676, 3, 7),
  (1290638, 6, 3),
  (1294885, 2, 7),
  (1295597, 4, 3),
  (1299717, 5, 6),
  (1300966, 0, 7),
  (1301442, 5, 7),
  (1304678, 3, 3),
  (1307681, 5, 6),
  (1313549, 3, 7),
  (1315616, 5, 2),
  (1316817, 7, 7),
  (1317543, 6, 3),
  (1321944, 6, 0),
  (1322171, 6, 7),
  (1322840, 5, 2),
  (1326972, 3, 7),
  (1328368, 0, 7),
  (1334559, 4, 2),
  (1334648, 7, 7),
  (1341548, 4, 7),
  (1346122, 1, 0),
  (1348678, 5, 2),
  (1354305, 0, 0),
  (1355505, 4, 3),
  (1359246, 3, 3),
  (1379848, 3, 2),
  (1381412, 1, 3),
  (1385042, 6, 7),
  (1392891, 1, 6),
  (1398089, 1, 4),
  (1398496, 6, 0),
  (1400255, 6, 6),
  (1402298, 5, 7),
  (1404748, 1, 7),
  (1404866, 6, 3),
  (1405792, 7, 0),
  (1410171, 1, 3),
  (1411829, 6, 3),
  (1412422, 5, 3),
  (1414230, 0, 3),
  (1418551, 1, 7),
  (1421281, 5, 3),
  (1424322, 0, 7),
  (1424654, 3, 7),
  (1425615, 7, 7),
  (1425823, 3, 5),
  (1435014, 6, 7),
  (1436930, 5, 5),
  (1436936, 3, 7),
  (1437143, 1, 6),
  (1443240, 1, 7),
  (1445795, 3, 7),
  (1447200, 7, 7),
  (1447929, 6, 3),
  (1459187, 6, 0),
  (1462871, 3, 7),
  (1464200, 4, 6),
  (1464872, 1, 3),
  (1475512, 5, 7),
  (1477707, 1, 7),
  (1490453, 4, 7),
  (1495108, 7, 3),
  (1496653, 4, 5),
  (1506851, 5, 3),
  (1507366, 4, 3),
  (1509484, 2, 2),
  (1510427, 3, 3),
  (1519398, 5, 2),
  (1520430, 7, 3),
  (1524451, 5, 5),
  (1539284, 5, 2),
  (1542790, 4, 7),
  (1543368, 2, 2),
  (1546993, 0, 7),
  (1553694, 3, 5),
  (1554623, 1, 4),
  (1554902, 2, 6),
  (1558832, 2, 5),
  (1559953, 4, 3),
  (1562882, 6, 7),
  (1567301, 2, 6),
  (1567569, 4, 7),
  (1572237, 1, 3),
  (1574540, 6, 7),
  (1580970, 1, 4),
  (1587603, 1, 4),
  (1588861, 7, 7),
  (1593722, 4, 3),
  (1594100, 7, 7),
  (1596695, 4, 7),
  (1605210, 6, 0),
  (1606834, 3, 3),
  (1607976, 5, 7),
  (1608851, 0, 1),
  (1610421, 6, 4),
  (1611855, 6, 7),
  (1616660, 5, 3),
  (1619077, 3, 6),
  (1621135, 2, 6),
  (1621692, 6, 7),
  (1623338, 5, 7),
  (1624906, 6, 6),
  (1627505, 1, 1),
  (1629961, 0, 7),
  (1630175, 1, 3),
  (1632171, 4, 7),
  (1637009, 2, 7),
  (1643458, 2, 6),
  (1645098, 3, 3),
  (1655963, 7, 0),
  (1655976, 6, 7),
  (1656044, 3, 4),
  (1660366, 2, 3),
  (1660660, 2, 3),
  (1661848, 3, 5),
  (1662529, 4, 2),
  (1665746, 7, 0),
  (1666679, 7, 0),
  (1668945, 2, 3),
  (1669171, 1, 4),
  (1674272, 7, 7),
  (1681595, 0, 7),
  (1684507, 7, 3),
  (1688948, 7, 7),
  (1691454, 6, 7),
  (1692084, 0, 0),
  (1693294, 4, 7),
  (1695859, 4, 7),
  (1698554, 6, 7),
  (1699971, 1, 7),
  (1701776, 5, 7),
  (1702597, 7, 3),
  (1704493, 3, 0),
  (1705894, 4, 2),
  (1714208, 4, 7),
  (1722208, 7, 7),
  (1724626, 3, 6),
  (1726841, 2, 7),
  (1728109, 1, 7),
  (1742486, 7, 1),
  (1743570, 6, 0),
  (1743667, 2, 3),
  (1754120, 5, 5),
  (1754760, 2, 3),
  (1755099, 1, 3),
  (1755309, 4, 6),
  (1757493, 7, 4),
  (1761231, 7, 4),
  (1778600, 2, 7),
  (1781764, 5, 7),
  (1783762, 3, 3),
  (1787532, 5, 3),
  (1797844, 5, 7),
  (1798096, 1, 0),
  (1801034, 4, 3),
  (1802399, 7, 4),
  (1808964, 2, 3),
  (1812383, 7, 3),
  (1812440, 1, 7),
  (1816523, 4, 1),
  (1819044, 0, 4),
  (1821596, 4, 2),
  (1827184, 6, 4),
  (1831521, 3, 6),
  (1831677, 3, 3),
  (1836844, 6, 1),
  (1840048, 3, 5),
  (1846694, 2, 6),
  (1847218, 7, 7),
  (1848651, 4, 6),
  (1849583, 0, 4),
  (1851874, 7, 0),
  (1852162, 0, 0),
  (1853676, 5, 2),
  (1854291, 7, 6),
  (1856530, 4, 6),
  (1857993, 7, 6),
  (1858033, 0, 3),
  (1866189, 0, 7),
  (1874423, 2, 5),
  (1881355, 3, 6),
  (1883960, 5, 6),
  (1884149, 7, 7),
  (1884643, 0, 3),
  (1885229, 7, 1),
  (1892204, 0, 7),
  (1894233, 2, 3),
  (1895179, 4, 3),
  (1895494, 1, 4),
  (1898727, 3, 7),
  (1904946, 6, 3),
  (1906848, 5, 6),
  (1913657, 5, 5),
  (1918859, 2, 1),
  (1929301, 0, 0),
  (1931590, 3, 6),
  (1938742, 5, 2),
  (1940142, 5, 7),
  (1944369, 0, 6),
  (1954045, 0, 7),
  (1955011, 0, 0),
  (1955327, 7, 4),
  (1957648, 7, 7),
  (1957799, 3, 2),
  (1960754, 3, 7),
  (1970098, 7, 7),
  (1970439, 4, 2),
  (1972825, 3, 7),
  (1974112, 5, 7),
  (1975059, 7, 0),
  (1981616, 4, 5),
  (1984404, 7, 7),
  (1987964, 3, 6),
  (1988280, 3, 3),
  (1991778, 0, 7),
  (1994282, 2, 1),
  (2000994, 4, 7),
  (2013122, 4, 2),
  (2014225, 5, 6),
  (2017702, 0, 0),
  (2018814, 3, 6),
  (2021235, 6, 4),
  (2024974, 0, 0),
  (2025276, 0, 6),
  (2031733, 0, 3),
  (2031771, 1, 7),
  (2032616, 4, 3),
  (2033959, 4, 6),
  (2037374, 6, 0),
  (2037907, 2, 5),
  (2038668, 7, 4),
  (2039793, 6, 0),
  (2043321, 4, 2),
  (2043332, 3, 2),
  (2043828, 6, 7),
  (2047182, 1, 7),
  (2049546, 7, 6),
  (2052291, 3, 3),
  (2058964, 6, 5),
  (2063740, 2, 6),
  (2063742, 1, 6),
  (2067993, 5, 3),
  (2069407, 5, 7),
  (2076579, 2, 0),
  (2078728, 7, 3),
  (2079540, 1, 3),
  (2083119, 2, 2),
  (2083711, 3, 7),
  (2087488, 2, 6),
  (2088795, 3, 7),
  (2092398, 7, 6),
  (2093947, 2, 2),
  (2095879, 4, 2),
  (2096563, 0, 7),
  (2102868, 2, 7),
  (2103722, 3, 3),
  (2103930, 7, 7),
  (2110997, 3, 7),
  (2112435, 1, 5),
  (2114754, 7, 7),
  (2120905, 5, 2),
  (2123234, 7, 1),
  (2127482, 2, 3),
  (2131168, 7, 4),
  (2132670, 0, 3),
  (2136945, 3, 7),
  (2144025, 2, 6),
  (2147491, 6, 7),
  (2149891, 2, 5),
  (2153229, 5, 4),
  (2157739, 3, 7),
  (2158357, 0, 6),
  (2158675, 3, 6),
  (2159272, 5, 7),
  (2162216, 0, 0),
  (2162419, 4, 5),
  (2163049, 1, 7),
  (2163140, 3, 2),
  (2167283, 1, 0),
  (2168553, 6, 7),
  (2169966, 2, 3),
  (2172565, 4, 6),
  (2174246, 0, 4),
  (2184613, 6, 7),
  (2187218, 4, 2),
  (2193195, 6, 5),
  (2197786, 6, 7),
  (2199316, 7, 4),
  (2202551, 5, 3),
  (2209374, 0, 6),
  (2212947, 1, 3),
  (2218242, 6, 7),
  (2218443, 6, 0),
  (2221412, 4, 3),
  (2230583, 1, 2),
  (2231974, 7, 0),
  (2232073, 7, 3),
  (2237020, 6, 0),
  (2238808, 0, 7),
  (2243968, 7, 7),
  (2244937, 3, 6),
  (2246581, 3, 7),
  (2247562, 6, 2),
  (2250228, 4, 1),
  (2250668, 2, 7),
  (2250970, 3, 6),
  (2251770, 2, 2),
  (2252858, 2, 4),
  (2263723, 0, 2),
  (2266647, 5, 6),
  (2269488, 4, 7),
  (2269540, 7, 3),
  (2275416, 4, 2),
  (2277307, 2, 2),
  (2279729, 6, 7),
  (2290751, 0, 7),
  (2293249, 5, 3),
  (2297322, 4, 2),
  (2299534, 5, 3),
  (2301202, 2, 6),
  (2301501, 6, 0),
  (2304190, 0, 6),
  (2305248, 7, 0),
  (2308362, 6, 0),
  (2319856, 4, 7),
  (2322827, 2, 3),
  (2322956, 6, 4),
  (2322973, 6, 7),
  (2327484, 2, 2),
  (2335284, 3, 7),
  (2342549, 4, 3),
  (2343170, 1, 3),
  (2343557, 4, 2),
  (2347879, 4, 2),
  (2348314, 5, 7),
  (2354080, 6, 0),
  (2356407, 0, 0),
  (2359227, 0, 7),
  (2360107, 7, 0),
  (2361739, 7, 3),
  (2363064, 4, 3),
  (2369138, 6, 6),
  (2369970, 4, 7),
  (2370798, 1, 7),
  (2371042, 4, 6),
  (2380662, 1, 7),
  (2382894, 2, 7),
  (2382979, 6, 4),
  (2383541, 5, 2),
  (2383824, 3, 6),
  (2385264, 2, 2),
  (2389252, 0, 3),
  (2392457, 4, 4),
  (2407630, 2, 3),
  (2409016, 4, 3),
  (2412296, 4, 2),
  (2413626, 7, 7),
  (2413713, 6, 6),
  (2413943, 3, 6),
  (2416061, 3, 3),
  (2421298, 7, 7),
  (2429115, 3, 3),
  (2430566, 0, 3),
  (2435273, 0, 7),
  (2437645, 6, 0),
  (2440364, 3, 6),
  (2448257, 6, 7),
  (2448825, 0, 7),
  (2454577, 4, 7),
  (2455113, 5, 2),
  (2457151, 0, 7),
  (2462509, 4, 3),
  (2466198, 5, 7),
  (2467440, 3, 3),
  (2468322, 0, 7),
  (2469260, 6, 7),
  (2470129, 5, 3),
  (2472084, 4, 3),
  (2472827, 4, 7),
  (2473031, 0, 0),
  (2478148, 0, 7),
  (2479347, 6, 2),
  (2481796, 3, 7),
  (2492924, 0, 6),
  (2493114, 3, 3),
  (2497987, 2, 3),
  (2507481, 7, 0),
  (2507965, 6, 0),
  (2509673, 1, 7),
  (2509820, 3, 3),
  (2513271, 7, 2),
  (2517238, 1, 5),
  (2518852, 1, 7),
  (2519258, 7, 3),
  (2519385, 5, 3),
  (2521167, 7, 7),
  (2523953, 3, 2),
  (2524076, 1, 7),
  (2525827, 0, 6),
  (2529181, 0, 5),
  (2532290, 0, 7),
  (2535777, 6, 3),
  (2536619, 5, 7),
  (2539156, 7, 7),
  (2540838, 2, 6),
  (2543625, 3, 7),
  (2550142, 4, 6),
  (2551777, 1, 7),
  (2557353, 6, 1),
  (2559369, 0, 0),
  (2570091, 1, 0),
  (2571938, 0, 7),
  (2577330, 5, 3),
  (2578062, 6, 3),
  (2582374, 2, 2),
  (2585033, 7, 0),
  (2586279, 1, 7),
  (2591832, 7, 7),
  (2595643, 3, 3),
  (2598822, 7, 0),
  (2604553, 4, 6),
  (2607869, 4, 7),
  (2609689, 2, 5),
  (2612313, 0, 4),
  (2613279, 2, 7),
  (2616403, 5, 7),
  (2624620, 0, 0),
  (2624775, 0, 7),
  (2626143, 7, 4),
  (2628158, 6, 3),
  (2639400, 3, 6),
  (2641406, 0, 7),
  (2644209, 7, 3),
  (2645540, 7, 0),
  (2646588, 5, 6),
  (2648094, 1, 3),
  (2648096, 0, 0),
  (2650357, 7, 7),
  (2653255, 7, 3),
  (2656808, 7, 1),
  (2662720, 0, 4),
  (2665562, 3, 5),
  (2665608, 4, 5),
  (2666825, 1, 7),
  (2672277, 0, 0),
  (2675535, 1, 0),
  (2677518, 0, 7),
  (2677621, 7, 7),
  (2678463, 0, 0),
  (2679846, 5, 7),
  (2681407, 3, 3),
  (2684490, 7, 6),
  (2684912, 2, 4),
  (2702156, 5, 3),
  (2703565, 4, 3),
  (2707744, 1, 3),
  (2711143, 1, 6),
  (2723156, 1, 6),
  (2723585, 7, 0),
  (2727437, 4, 2),
  (2727822, 1, 7),
  (2731269, 7, 7),
  (2734493, 7, 0),
  (2741521, 6, 4),
  (2742500, 0, 7),
  (2751598, 6, 6),
  (2751764, 4, 7),
  (2755351, 4, 5),
  (2755879, 5, 7),
  (2756568, 7, 4),
  (2757225, 1, 6),
  (2757355, 6, 6),
  (2757982, 6, 0),
  (2759100, 2, 7),
  (2761527, 1, 7),
  (2761783, 7, 4),
  (2762573, 4, 7),
  (2763992, 7, 3),
  (2765186, 5, 1),
  (2766051, 3, 7),
  (2766925, 1, 4),
  (2767080, 7, 3),
  (2771172, 5, 3),
  (2772247, 3, 6),
  (2775637, 5, 3),
  (2777782, 6, 7),
  (2781938, 0, 5),
  (2800392, 7, 4),
  (2803574, 5, 7),
  (2807457, 0, 7),
  (2809232, 6, 0),
  (2809501, 4, 7),
  (2813774, 3, 7),
  (2815773, 1, 7),
  (2816713, 4, 6),
  (2818726, 7, 7),
  (2819906, 5, 7),
  (2826505, 1, 7),
  (2833554, 6, 4),
  (2833889, 3, 7),
  (2834657, 7, 3),
  (2838345, 4, 7),
  (2850433, 4, 2),
  (2858195, 1, 7),
  (2862709, 5, 5),
  (2864368, 5, 6),
  (2870085, 5, 6),
  (2875801, 4, 3),
  (2878530, 1, 0),
  (2881668, 4, 1),
  (2884056, 4, 2),
  (2890234, 5, 3),
  (2895383, 6, 7),
  (2898482, 6, 4),
  (2898912, 2, 7),
  (2901510, 3, 3),
  (2909039, 5, 6),
  (2911788, 0, 0),
  (2914715, 5, 7),
  (2915829, 7, 7),
  (2919290, 1, 4),
  (2925761, 3, 7),
  (2928601, 1, 3),
  (2928825, 1, 7),
  (2931240, 7, 0),
  (2937258, 3, 7),
  (2940635, 6, 7),
  (2942808, 5, 2),
  (2945590, 0, 7),
  (2949973, 4, 2),
  (2953087, 4, 6),
  (2954053, 4, 7),
  (2963050, 7, 7),
  (2976218, 4, 2),
  (2979842, 2, 2),
  (2979942, 3, 2),
  (2988857, 4, 7),
  (2990242, 2, 7),
  (2998710, 5, 7),
  (3001394, 7, 0),
  (3003312, 4, 7),
  (3004293, 7, 7),
  (3011995, 7, 0),
  (3016332, 4, 7),
  (3022801, 0, 2),
  (3026049, 2, 7),
  (3038811, 2, 6),
  (3039507, 3, 7),
  (3041490, 3, 1),
  (3043979, 2, 7),
  (3044330, 2, 7),
  (3044893, 2, 5),
  (3045322, 2, 7),
  (3052873, 2, 3),
  (3053731, 6, 7),
  (3055186, 1, 0),
  (3058380, 5, 3),
  (3060367, 2, 7),
  (3064761, 1, 5),
  (3071596, 4, 7),
  (3076890, 4, 3),
  (3077223, 4, 6),
  (3078342, 7, 7),
  (3078648, 5, 5),
  (3080035, 6, 0),
  (3081483, 5, 7),
  (3084875, 3, 7),
  (3086020, 0, 6),
  (3090818, 1, 0),
  (3092497, 3, 3),
  (3092950, 2, 3),
  (3099677, 1, 4),
  (3103940, 0, 7),
  (3104658, 2, 7),
  (3109252, 4, 4),
  (3117414, 2, 6),
  (3118971, 0, 7),
  (3119843, 7, 4),
  (3120980, 4, 5),
  (3122302, 0, 0),
  (3125092, 1, 0),
  (3129063, 1, 4),
  (3129957, 1, 0),
  (3130140, 1, 7),
  (3130352, 2, 7),
  (3131164, 2, 7),
  (3132112, 7, 7),
  (3134809, 2, 7),
  (3136066, 3, 7),
  (3137087, 5, 3),
  (3137382, 3, 7),
  (3137410, 2, 5),
  (3139590, 7, 6),
  (3141290, 0, 7),
  (3148236, 3, 7),
  (3149012, 6, 4),
  (3149290, 0, 3),
  (3149298, 6, 4),
  (3150779, 4, 7),
  (3155666, 3, 7),
  (3155738, 7, 0),
  (3157470, 6, 7),
  (3167447, 1, 6),
  (3167592, 5, 3),
  (3169822, 0, 7),
  (3175069, 1, 6),
  (3176589, 0, 3),
  (3181589, 2, 3),
  (3184492, 3, 5),
  (3185144, 1, 0),
  (3188557, 4, 4),
  (3190919, 7, 7),
  (3190959, 6, 7),
  (3191929, 7, 0),
  (3193862, 5, 1),
  (3197364, 1, 7),
  (3212268, 5, 7),
  (3215772, 0, 3),
  (3222436, 5, 6),
  (3224673, 6, 4),
  (3228413, 3, 7),
  (3238903, 5, 7),
  (3240680, 6, 4),
  (3240763, 0, 2),
  (3241150, 6, 4),
  (3244822, 1, 4),
  (3246102, 5, 2),
  (3247281, 0, 7),
  (3253150, 5, 7),
  (3253841, 1, 0),
  (3255502, 6, 3),
  (3263369, 7, 7),
  (3268824, 6, 0),
  (3269195, 7, 0),
  (3273274, 7, 4),
  (3276832, 5, 3),
  (3281163, 2, 3),
  (3287428, 3, 7),
  (3288724, 7, 0),
  (3289116, 7, 7),
  (3294810, 5, 6),
  (3295780, 0, 0),
  (3298190, 4, 3),
  (3301370, 7, 7),
  (3304942, 0, 3),
  (3315171, 7, 7),
  (3321263, 0, 3),
  (3321758, 2, 7),
  (3324178, 4, 7),
  (3326294, 3, 2),
  (3329017, 5, 7),
  (3334566, 0, 4),
  (3337872, 1, 2),
  (3338377, 4, 6),
  (3339421, 1, 0),
  (3340372, 4, 5),
  (3340641, 5, 2),
  (3344503, 7, 7),
  (3344545, 3, 5),
  (3345796, 2, 3),
  (3351447, 0, 7),
  (3362099, 6, 6),
  (3363840, 7, 0),
  (3364304, 6, 4),
  (3373032, 0, 4),
  (3374019, 1, 7),
  (3375827, 1, 3),
  (3376643, 5, 7),
  (3376750, 4, 7),
  (3379248, 1, 3),
  (3381110, 5, 7),
  (3381905, 7, 5),
  (3382289, 6, 7),
  (3384193, 0, 2),
  (3385719, 5, 3),
  (3386995, 4, 5),
  (3388224, 4, 7),
  (3389693, 4, 3),
  (3390992, 5, 4),
  (3391883, 3, 7),
  (3393389, 0, 3),
  (3397944, 2, 3),
  (3400357, 3, 7),
  (3401051, 4, 3),
  (3404097, 1, 7),
  (3404782, 7, 0),
  (3405487, 2, 3),
  (3413810, 3, 7),
  (3414001, 4, 7),
  (3417333, 6, 5),
  (3417750, 7, 7),
  (3419409, 6, 7),
  (3419554, 3, 7),
  (3422719, 7, 0),
  (3422794, 7, 7),
  (3425869, 3, 7),
  (3428961, 6, 0),
  (3430110, 3, 6),
  (3431423, 0, 4),
  (3433057, 2, 4),
  (3433072, 6, 3),
  (3438664, 2, 7),
  (3445608, 2, 6),
  (3447294, 3, 2),
  (3447476, 3, 7),
  (3449826, 2, 7),
  (3451371, 3, 2),
  (3452790, 0, 6),
  (3455997, 3, 7),
  (3458702, 0, 4),
  (3459779, 7, 2),
  (3464956, 5, 2),
  (3471583, 3, 7),
  (3471628, 2, 7),
  (3477744, 5, 3),
  (3479642, 5, 7),
  (3483701, 3, 3),
  (3485790, 2, 3),
  (3488029, 3, 7),
  (3497397, 4, 5),
  (3499131, 2, 7),
  (3504139, 7, 7),
  (3505587, 6, 0),
  (3506688, 1, 3),
  (3510786, 7, 0),
  (3511201, 1, 6),
  (3511836, 7, 6),
  (3519903, 6, 6),
  (3522784, 5, 7),
  (3524642, 0, 6),
  (3527059, 2, 6),
  (3529874, 1, 0),
  (3529920, 2, 7),
  (3535474, 2, 7),
  (3537246, 7, 3),
  (3542820, 6, 7),
  (3547580, 2, 3),
  (3549318, 1, 0),
  (3549688, 5, 7),
  (3551205, 2, 3),
  (3552463, 2, 4),
  (3553271, 0, 7),
  (3554184, 1, 4),
  (3556164, 4, 3),
  (3568728, 2, 2),
  (3579473, 2, 3),
  (3585594, 2, 2),
  (3586455, 2, 6),
  (3589580, 6, 0),
  (3596920, 3, 2),
])
