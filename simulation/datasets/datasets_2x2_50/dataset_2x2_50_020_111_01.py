from src.util import *
schedule = deque([
  (1242, 9, 18),
  (3958, 8, 14),
  (5725, 7, 1),
  (12606, 0, 0),
  (17491, 8, 7),
  (17620, 0, 22),
  (18261, 7, 10),
  (19967, 6, 10),
  (21895, 3, 10),
  (22004, 2, 3),
  (25477, 3, 3),
  (25863, 4, 4),
  (27694, 3, 11),
  (32106, 10, 0),
  (36128, 6, 10),
  (36206, 2, 0),
  (36780, 4, 10),
  (39291, 4, 9),
  (40038, 3, 13),
  (50000, 0, 0),
  (50811, 9, 18),
  (53256, 6, 9),
  (54135, 8, 4),
  (55189, 4, 14),
  (56107, 6, 22),
  (60176, 3, 0),
  (61240, 7, 10),
  (64940, 0, 8),
  (65208, 1, 10),
  (65236, 5, 17),
  (66211, 11, 0),
  (70112, 11, 18),
  (71707, 3, 13),
  (73856, 8, 10),
  (77562, 4, 17),
  (79142, 3, 3),
  (81822, 11, 18),
  (86278, 2, 3),
  (86281, 0, 20),
  (87630, 5, 17),
  (91405, 0, 4),
  (91406, 11, 11),
  (92134, 1, 0),
  (93049, 1, 0),
  (98318, 7, 17),
  (100428, 4, 10),
  (102495, 11, 0),
  (106049, 6, 17),
  (108263, 10, 0),
  (110854, 4, 0),
  (112448, 1, 0),
  (112571, 8, 14),
  (113317, 9, 4),
  (117340, 9, 13),
  (119024, 11, 0),
  (120221, 4, 17),
  (122951, 3, 13),
  (123909, 9, 7),
  (125702, 10, 0),
  (129184, 6, 10),
  (131065, 4, 21),
  (138289, 2, 18),
  (139525, 2, 10),
  (142131, 3, 7),
  (144189, 9, 5),
  (149289, 7, 17),
  (153577, 3, 7),
  (153639, 0, 0),
  (159321, 4, 10),
  (163952, 2, 3),
  (164047, 7, 17),
  (168177, 10, 0),
  (173638, 9, 15),
  (173993, 3, 17),
  (175005, 6, 10),
  (179735, 11, 17),
  (182564, 3, 4),
  (184867, 1, 0),
  (185840, 1, 0),
  (186402, 5, 10),
  (189517, 6, 10),
  (190471, 6, 17),
  (196745, 1, 0),
  (200174, 3, 11),
  (200399, 2, 18),
  (200682, 7, 10),
  (203899, 8, 1),
  (204533, 0, 11),
  (223343, 11, 12),
  (224773, 3, 7),
  (225292, 10, 0),
  (225764, 11, 13),
  (226292, 2, 10),
  (229683, 4, 17),
  (230894, 10, 0),
  (234402, 10, 11),
  (238229, 3, 10),
  (238377, 0, 22),
  (241287, 3, 7),
  (245227, 10, 11),
  (246406, 8, 2),
  (246538, 7, 9),
  (253508, 4, 5),
  (255453, 4, 10),
  (257857, 11, 18),
  (263829, 4, 10),
  (276500, 10, 19),
  (280525, 11, 3),
  (281532, 1, 22),
  (290583, 1, 0),
  (295427, 0, 10),
  (298328, 6, 11),
  (303097, 2, 10),
  (305398, 4, 19),
  (310364, 2, 3),
  (315346, 1, 11),
  (321404, 4, 10),
  (322898, 0, 21),
  (328486, 1, 22),
  (332708, 6, 21),
  (335852, 1, 0),
  (336886, 10, 0),
  (337798, 4, 10),
  (345474, 3, 7),
  (348973, 8, 7),
  (353035, 10, 0),
  (354204, 0, 6),
  (355524, 1, 0),
  (356428, 11, 10),
  (362746, 8, 7),
  (364816, 6, 22),
  (365172, 4, 10),
  (366658, 5, 10),
  (366802, 6, 10),
  (366864, 3, 7),
  (368615, 6, 10),
  (372370, 10, 18),
  (376714, 4, 13),
  (378069, 3, 10),
  (388285, 1, 0),
  (391053, 8, 4),
  (393128, 6, 10),
  (396142, 6, 16),
  (412258, 5, 18),
  (415261, 10, 11),
  (415626, 8, 3),
  (415859, 4, 10),
  (421937, 4, 10),
  (424457, 8, 3),
  (435470, 11, 0),
  (436324, 4, 10),
  (438469, 5, 9),
  (446385, 7, 10),
  (450790, 5, 17),
  (453456, 1, 10),
  (453903, 7, 10),
  (457731, 2, 3),
  (457841, 3, 10),
  (459053, 0, 0),
  (465749, 3, 3),
  (471862, 7, 10),
  (474000, 6, 10),
  (478408, 11, 0),
  (483222, 8, 0),
  (484312, 11, 22),
  (484793, 11, 11),
  (486853, 0, 6),
  (486997, 9, 1),
  (487141, 0, 0),
  (487652, 9, 17),
  (488073, 11, 0),
  (488691, 5, 20),
  (490777, 6, 17),
  (494740, 4, 6),
  (495894, 2, 3),
  (496038, 9, 10),
  (500527, 0, 0),
  (506804, 10, 0),
  (507109, 8, 13),
  (515008, 3, 5),
  (518366, 6, 22),
  (522665, 5, 21),
  (522716, 9, 3),
  (525010, 9, 18),
  (526523, 11, 18),
  (529744, 3, 7),
  (530990, 8, 7),
  (533929, 5, 10),
  (542257, 10, 15),
  (548126, 10, 18),
  (552355, 8, 13),
  (554042, 7, 9),
  (556925, 6, 10),
  (560301, 8, 13),
  (562323, 5, 10),
  (566639, 3, 1),
  (567184, 1, 0),
  (569739, 1, 0),
  (572477, 4, 22),
  (572769, 3, 7),
  (579915, 8, 16),
  (583557, 1, 3),
  (587714, 7, 17),
  (588161, 1, 0),
  (591682, 5, 10),
  (596637, 11, 0),
  (600987, 5, 10),
  (601557, 1, 13),
  (602029, 0, 22),
  (604176, 8, 12),
  (604337, 5, 10),
  (605322, 4, 10),
  (613394, 1, 0),
  (614024, 2, 7),
  (615571, 4, 17),
  (616146, 2, 3),
  (616801, 3, 3),
  (617230, 11, 3),
  (618187, 0, 7),
  (622817, 9, 1),
  (624081, 6, 10),
  (631876, 7, 10),
  (634305, 6, 10),
  (642407, 2, 3),
  (642668, 11, 0),
  (647784, 7, 12),
  (649073, 3, 0),
  (651084, 11, 10),
  (651462, 8, 7),
  (652269, 0, 0),
  (654734, 3, 5),
  (655797, 11, 0),
  (659998, 3, 10),
  (667553, 3, 4),
  (670442, 2, 18),
  (674581, 9, 13),
  (675443, 0, 0),
  (676236, 6, 22),
  (680673, 1, 14),
  (682373, 3, 7),
  (683650, 4, 6),
  (685367, 2, 8),
  (685553, 11, 11),
  (685604, 7, 10),
  (685898, 1, 0),
  (688135, 6, 5),
  (693026, 8, 3),
  (693359, 0, 0),
  (693803, 3, 3),
  (694944, 3, 0),
  (696951, 7, 10),
  (701881, 7, 17),
  (702522, 0, 0),
  (707117, 8, 5),
  (708076, 10, 10),
  (711050, 2, 7),
  (714825, 6, 10),
  (717106, 5, 6),
  (718720, 9, 18),
  (723067, 10, 0),
  (723068, 6, 21),
  (723102, 0, 22),
  (728589, 2, 3),
  (729384, 1, 0),
  (732668, 1, 22),
  (734527, 0, 11),
  (736016, 5, 21),
  (740355, 2, 7),
  (741310, 5, 5),
  (742096, 5, 10),
  (743411, 9, 6),
  (745081, 7, 22),
  (748422, 6, 10),
  (754149, 2, 7),
  (756083, 2, 3),
  (761001, 1, 0),
  (762406, 5, 10),
  (768811, 11, 11),
  (769624, 2, 0),
  (771759, 1, 3),
  (776606, 4, 11),
  (778861, 0, 0),
  (782151, 9, 14),
  (784397, 8, 0),
  (785623, 8, 0),
  (785671, 6, 10),
  (786227, 0, 0),
  (787200, 7, 10),
  (787823, 4, 10),
  (787856, 9, 16),
  (789511, 3, 7),
  (790364, 6, 10),
  (791227, 9, 16),
  (791514, 11, 0),
  (793370, 0, 11),
  (796260, 8, 13),
  (796320, 2, 7),
  (796497, 11, 22),
  (801984, 11, 18),
  (802475, 10, 22),
  (804411, 11, 11),
  (810051, 9, 18),
  (814377, 2, 3),
  (826565, 2, 3),
  (826760, 2, 1),
  (833337, 9, 17),
  (834648, 3, 7),
  (840110, 7, 9),
  (840391, 6, 17),
  (841045, 5, 6),
  (842848, 6, 17),
  (848152, 0, 0),
  (851801, 6, 10),
  (855686, 7, 10),
  (856188, 10, 19),
  (860030, 10, 0),
  (861054, 6, 1),
  (865543, 2, 16),
  (871334, 6, 10),
  (878960, 7, 10),
  (880025, 11, 18),
  (883149, 9, 7),
  (885434, 6, 17),
  (887379, 3, 4),
  (889233, 1, 11),
  (901646, 8, 7),
  (902432, 6, 10),
  (902643, 5, 10),
  (903247, 6, 10),
  (904597, 1, 0),
  (906220, 7, 10),
  (910968, 9, 3),
  (920341, 10, 0),
  (921198, 10, 10),
  (922171, 1, 0),
  (922424, 11, 22),
  (922987, 4, 22),
  (926840, 9, 13),
  (929776, 5, 17),
  (930310, 3, 0),
  (931947, 2, 3),
  (939363, 11, 0),
  (939985, 3, 3),
  (942287, 7, 10),
  (944369, 5, 10),
  (947234, 8, 8),
  (947630, 8, 18),
  (948761, 2, 3),
  (950265, 3, 3),
  (954354, 3, 7),
  (955002, 1, 0),
  (956299, 5, 10),
  (957057, 7, 16),
  (957331, 7, 10),
  (962640, 2, 6),
  (963522, 2, 7),
  (965471, 7, 10),
  (967397, 4, 9),
  (972432, 5, 10),
  (972792, 7, 17),
  (978442, 2, 15),
  (979017, 1, 6),
  (984475, 2, 7),
  (988749, 4, 9),
  (992290, 7, 10),
  (993114, 11, 11),
  (993359, 6, 17),
  (994422, 7, 17),
  (1001643, 2, 3),
  (1003583, 3, 4),
  (1010269, 11, 0),
  (1010877, 10, 0),
  (1012870, 11, 22),
  (1018152, 8, 3),
  (1019925, 9, 1),
  (1025891, 8, 10),
  (1026451, 3, 7),
  (1026466, 4, 17),
  (1027129, 2, 7),
  (1035447, 3, 7),
  (1040500, 8, 17),
  (1042031, 3, 3),
  (1042926, 1, 14),
  (1044056, 1, 0),
  (1047084, 10, 18),
  (1048075, 11, 10),
  (1052326, 9, 3),
  (1054408, 9, 1),
  (1060078, 3, 3),
  (1060744, 4, 17),
  (1061398, 2, 3),
  (1063228, 0, 0),
  (1066484, 9, 12),
  (1079247, 4, 10),
  (1079877, 8, 18),
  (1081356, 6, 6),
  (1087953, 1, 4),
  (1091273, 10, 10),
  (1092140, 0, 8),
  (1096978, 0, 0),
  (1100262, 4, 10),
  (1102036, 4, 10),
  (1104342, 6, 22),
  (1120509, 3, 7),
  (1127355, 6, 21),
  (1129987, 9, 4),
  (1131016, 8, 13),
  (1132828, 11, 0),
  (1133448, 7, 10),
  (1137587, 2, 15),
  (1138921, 6, 17),
  (1146086, 5, 10),
  (1146309, 6, 10),
  (1146879, 10, 0),
  (1149687, 4, 10),
  (1150442, 1, 0),
  (1156861, 8, 17),
  (1161281, 1, 11),
  (1163038, 2, 0),
  (1168894, 8, 7),
  (1169933, 1, 11),
  (1171779, 9, 7),
  (1182358, 10, 11),
  (1182507, 7, 10),
  (1183052, 0, 11),
  (1183452, 2, 3),
  (1184010, 8, 4),
  (1184959, 0, 7),
  (1188225, 3, 6),
  (1189536, 0, 11),
  (1192289, 6, 10),
  (1195134, 11, 0),
  (1200261, 3, 10),
  (1201409, 8, 9),
  (1205510, 4, 10),
  (1206679, 8, 18),
  (1216739, 6, 10),
  (1218546, 3, 3),
  (1219037, 0, 0),
  (1221122, 4, 10),
  (1222937, 0, 0),
  (1231373, 1, 0),
  (1232990, 2, 10),
  (1233253, 4, 10),
  (1235380, 10, 0),
  (1241359, 9, 12),
  (1241652, 11, 0),
  (1242505, 7, 10),
  (1243228, 6, 6),
  (1249077, 4, 17),
  (1249518, 9, 10),
  (1250778, 11, 0),
  (1251272, 6, 10),
  (1258304, 9, 3),
  (1259782, 5, 13),
  (1268084, 8, 7),
  (1269729, 6, 10),
  (1269837, 0, 18),
  (1271787, 4, 10),
  (1273788, 4, 9),
  (1277620, 1, 0),
  (1279479, 10, 14),
  (1282474, 11, 0),
  (1284512, 0, 0),
  (1289868, 8, 7),
  (1291736, 8, 8),
  (1293880, 3, 18),
  (1296314, 11, 0),
  (1300314, 3, 10),
  (1301336, 6, 17),
  (1306164, 4, 10),
  (1312830, 8, 10),
  (1319455, 6, 10),
  (1320238, 5, 2),
  (1320300, 3, 18),
  (1321265, 2, 7),
  (1325248, 4, 20),
  (1328906, 3, 15),
  (1334773, 9, 18),
  (1335623, 1, 0),
  (1336708, 7, 21),
  (1337576, 7, 17),
  (1344419, 8, 7),
  (1348698, 0, 0),
  (1348820, 7, 10),
  (1351487, 3, 9),
  (1354718, 8, 3),
  (1361601, 4, 17),
  (1364272, 9, 4),
  (1364978, 4, 17),
  (1365637, 11, 0),
  (1368874, 5, 10),
  (1369652, 1, 11),
  (1370601, 8, 11),
  (1371269, 7, 10),
  (1376534, 6, 10),
  (1377792, 4, 9),
  (1379870, 10, 6),
  (1381494, 4, 10),
  (1384295, 10, 6),
  (1387835, 2, 10),
  (1388981, 1, 11),
  (1390185, 11, 0),
  (1391714, 3, 13),
  (1395030, 5, 10),
  (1395614, 10, 0),
  (1397504, 1, 0),
  (1400610, 7, 17),
  (1402856, 10, 0),
  (1404240, 4, 10),
  (1407035, 4, 9),
  (1408133, 8, 14),
  (1408320, 1, 11),
  (1409628, 7, 22),
  (1410812, 0, 0),
  (1413335, 9, 0),
  (1417429, 0, 0),
  (1420279, 5, 6),
  (1421452, 3, 5),
  (1423423, 2, 7),
  (1428109, 3, 7),
  (1439998, 7, 10),
  (1445939, 3, 3),
  (1446359, 11, 0),
  (1447752, 6, 10),
  (1448094, 11, 17),
  (1449800, 11, 0),
  (1453339, 1, 0),
  (1454054, 10, 11),
  (1457540, 4, 10),
  (1462706, 0, 0),
  (1472417, 11, 18),
  (1473532, 0, 5),
  (1475903, 3, 13),
  (1476936, 9, 3),
  (1477059, 6, 10),
  (1477898, 3, 16),
  (1480193, 6, 10),
  (1485884, 8, 18),
  (1486346, 5, 10),
  (1489718, 7, 18),
  (1492130, 11, 11),
  (1497819, 6, 10),
  (1499356, 6, 22),
  (1502981, 4, 6),
  (1508072, 2, 3),
  (1510657, 6, 20),
  (1510778, 7, 10),
  (1510910, 3, 1),
  (1513762, 8, 18),
  (1526127, 8, 3),
  (1526357, 8, 9),
  (1527278, 7, 10),
  (1528588, 8, 4),
  (1532738, 11, 1),
  (1536252, 3, 3),
  (1539406, 7, 10),
  (1555839, 11, 0),
  (1555861, 11, 3),
  (1556782, 7, 17),
  (1557625, 7, 5),
  (1559795, 5, 22),
  (1559858, 10, 11),
  (1560151, 11, 11),
  (1563733, 3, 3),
  (1567483, 7, 7),
  (1573007, 7, 17),
  (1579376, 4, 17),
  (1588464, 11, 18),
  (1593006, 2, 3),
  (1598561, 2, 3),
  (1600205, 6, 0),
  (1609774, 6, 10),
  (1610337, 9, 4),
  (1610731, 8, 0),
  (1612635, 9, 7),
  (1612860, 6, 17),
  (1623162, 11, 0),
  (1631449, 7, 17),
  (1632223, 2, 3),
  (1643166, 10, 22),
  (1646094, 1, 18),
  (1649016, 3, 7),
  (1650615, 10, 0),
  (1652138, 7, 18),
  (1653326, 9, 10),
  (1658864, 10, 2),
  (1661049, 4, 10),
  (1665132, 2, 7),
  (1666260, 5, 17),
  (1666488, 4, 10),
  (1667920, 3, 3),
  (1671999, 5, 10),
  (1673259, 0, 11),
  (1676488, 0, 0),
  (1678534, 6, 10),
  (1680876, 5, 10),
  (1682290, 11, 10),
  (1688614, 9, 14),
  (1689758, 2, 17),
  (1691612, 9, 3),
  (1692372, 10, 0),
  (1693742, 10, 10),
  (1697535, 0, 7),
  (1697764, 3, 7),
  (1698737, 1, 3),
  (1698857, 0, 22),
  (1705371, 10, 0),
  (1711325, 3, 13),
  (1712417, 6, 10),
  (1715585, 3, 6),
  (1717236, 3, 0),
  (1718942, 4, 17),
  (1720050, 0, 10),
  (1736706, 2, 7),
  (1744404, 7, 10),
  (1747919, 6, 10),
  (1749769, 7, 10),
  (1750200, 8, 7),
  (1750373, 6, 4),
  (1753070, 11, 11),
  (1756832, 1, 0),
  (1760066, 4, 5),
  (1763511, 2, 9),
  (1767640, 7, 11),
  (1769256, 8, 7),
  (1773647, 0, 11),
  (1781220, 1, 0),
  (1782480, 10, 11),
  (1788140, 9, 6),
  (1790401, 7, 10),
  (1790856, 3, 7),
  (1796333, 4, 17),
  (1798651, 2, 4),
  (1802319, 0, 3),
  (1807354, 11, 13),
  (1810337, 6, 10),
  (1811241, 8, 4),
  (1812781, 8, 10),
  (1818229, 9, 7),
  (1828397, 6, 10),
  (1832012, 11, 0),
  (1837386, 6, 4),
  (1845400, 0, 11),
  (1847681, 8, 10),
  (1852486, 7, 17),
  (1853006, 11, 0),
  (1856020, 7, 10),
  (1856663, 6, 10),
  (1858977, 8, 0),
  (1873307, 1, 0),
  (1878242, 0, 13),
  (1881774, 7, 13),
  (1882602, 2, 0),
  (1883624, 1, 0),
  (1884065, 5, 9),
  (1884724, 1, 11),
  (1885307, 7, 10),
  (1887200, 2, 10),
  (1887782, 0, 0),
  (1889661, 5, 9),
  (1890067, 11, 19),
  (1890398, 0, 11),
  (1899915, 1, 11),
  (1902519, 8, 7),
  (1902724, 1, 16),
  (1914632, 5, 10),
  (1916445, 2, 10),
  (1916817, 8, 0),
  (1920646, 5, 10),
  (1920878, 8, 15),
  (1923155, 1, 11),
  (1933271, 6, 10),
  (1936065, 10, 3),
  (1943367, 4, 10),
  (1947917, 7, 10),
  (1950631, 10, 0),
  (1952312, 7, 10),
  (1963023, 2, 18),
  (1963063, 4, 12),
  (1965837, 11, 4),
  (1965940, 7, 10),
  (1969370, 0, 0),
  (1969571, 9, 4),
  (1972513, 4, 10),
  (1972929, 5, 10),
  (1976541, 1, 9),
  (1978386, 7, 17),
  (1978806, 1, 0),
  (1982964, 2, 3),
  (1983959, 8, 0),
  (1984110, 6, 10),
  (1985801, 9, 7),
  (1992720, 4, 10),
  (1996179, 7, 18),
  (2002143, 4, 9),
  (2006712, 4, 18),
  (2009935, 5, 10),
  (2018315, 3, 15),
  (2030249, 0, 0),
  (2038614, 11, 10),
  (2039099, 9, 3),
  (2039828, 9, 3),
  (2045845, 9, 3),
  (2046878, 3, 8),
  (2050615, 7, 10),
  (2053617, 3, 7),
  (2056917, 3, 3),
  (2058048, 4, 9),
  (2059115, 7, 22),
  (2061414, 5, 22),
  (2063417, 8, 3),
  (2065765, 0, 18),
  (2066098, 10, 0),
  (2067256, 9, 17),
  (2069549, 10, 0),
  (2071085, 10, 0),
  (2072194, 11, 0),
  (2076099, 1, 0),
  (2078830, 11, 11),
  (2080100, 8, 7),
  (2080755, 8, 10),
  (2080834, 2, 3),
  (2080863, 10, 0),
  (2082386, 10, 22),
  (2092366, 11, 0),
  (2092670, 4, 10),
  (2092883, 2, 7),
  (2096691, 6, 10),
  (2102002, 9, 18),
  (2103119, 0, 0),
  (2105483, 9, 3),
  (2114435, 10, 0),
  (2117885, 0, 0),
  (2117895, 4, 10),
  (2122544, 9, 11),
  (2123353, 3, 17),
  (2127757, 2, 4),
  (2129284, 1, 10),
  (2134519, 9, 18),
  (2139974, 10, 0),
  (2142806, 0, 11),
  (2145642, 4, 10),
  (2150450, 0, 0),
  (2152322, 8, 7),
  (2157410, 1, 0),
  (2158062, 10, 11),
  (2163795, 0, 0),
  (2165230, 8, 4),
  (2166238, 8, 7),
  (2169904, 5, 10),
  (2173722, 3, 4),
  (2177983, 4, 10),
  (2189448, 5, 10),
  (2193233, 8, 0),
  (2203836, 2, 13),
  (2204331, 3, 3),
  (2204525, 8, 10),
  (2204576, 3, 12),
  (2208636, 10, 3),
  (2212148, 8, 7),
  (2213259, 7, 22),
  (2215401, 3, 7),
  (2217234, 8, 15),
  (2217361, 10, 0),
  (2222054, 1, 10),
  (2230856, 1, 0),
  (2232066, 7, 17),
  (2241603, 6, 22),
  (2245086, 9, 18),
  (2245689, 0, 11),
  (2246210, 7, 10),
  (2248957, 10, 10),
  (2250527, 5, 10),
  (2256184, 10, 14),
  (2260478, 9, 1),
  (2264959, 1, 0),
  (2279785, 11, 11),
  (2285463, 1, 1),
  (2285492, 0, 0),
  (2287132, 2, 4),
  (2305111, 0, 10),
  (2308450, 10, 11),
  (2308579, 6, 21),
  (2311159, 8, 3),
  (2321914, 8, 0),
  (2322876, 1, 10),
  (2325950, 6, 10),
  (2327516, 6, 10),
  (2327587, 6, 6),
  (2327636, 10, 17),
  (2328641, 6, 17),
  (2332655, 1, 7),
  (2338849, 6, 10),
  (2341418, 8, 3),
  (2344605, 5, 10),
  (2350528, 10, 19),
  (2356953, 11, 22),
  (2360772, 1, 0),
  (2362608, 7, 10),
  (2365921, 0, 0),
  (2371362, 11, 0),
  (2372317, 2, 0),
  (2375693, 3, 9),
  (2378832, 11, 0),
  (2379258, 1, 22),
  (2381975, 8, 10),
  (2389353, 6, 15),
  (2402790, 9, 3),
  (2403071, 1, 0),
  (2409353, 1, 11),
  (2410097, 3, 13),
  (2410278, 4, 9),
  (2410829, 0, 0),
  (2412862, 4, 10),
  (2415125, 9, 3),
  (2421404, 8, 3),
  (2424345, 5, 0),
  (2424390, 4, 10),
  (2425112, 8, 11),
  (2425518, 3, 0),
  (2429621, 1, 0),
  (2430714, 2, 10),
  (2432156, 10, 0),
  (2433280, 2, 10),
  (2433717, 7, 10),
  (2434259, 2, 9),
  (2437641, 6, 2),
  (2438095, 1, 11),
  (2440266, 4, 10),
  (2441383, 0, 0),
  (2446769, 11, 0),
  (2458145, 1, 7),
  (2458516, 8, 6),
  (2461369, 5, 10),
  (2463309, 8, 0),
  (2466205, 10, 12),
  (2473242, 1, 0),
  (2473594, 4, 6),
  (2475701, 10, 11),
  (2476879, 6, 5),
  (2479689, 7, 0),
  (2482507, 10, 0),
  (2492037, 1, 16),
  (2497849, 2, 3),
  (2499932, 11, 0),
  (2503172, 3, 1),
  (2507461, 1, 16),
  (2508340, 10, 10),
  (2509315, 5, 10),
  (2510551, 1, 18),
  (2516518, 7, 22),
  (2517214, 8, 14),
  (2519318, 5, 13),
  (2528597, 1, 0),
  (2528665, 8, 17),
  (2528870, 8, 13),
  (2534378, 7, 13),
  (2536247, 1, 0),
  (2541690, 0, 11),
  (2548101, 9, 3),
  (2552338, 0, 0),
  (2554989, 9, 3),
  (2557250, 1, 15),
  (2569043, 11, 7),
  (2569772, 9, 12),
  (2570202, 3, 10),
  (2571615, 6, 10),
  (2580954, 2, 8),
  (2582039, 10, 0),
  (2585791, 4, 17),
  (2597968, 2, 13),
  (2601210, 0, 0),
  (2602452, 4, 10),
  (2602703, 4, 9),
  (2604175, 0, 10),
  (2604482, 1, 18),
  (2605395, 6, 9),
  (2606670, 5, 10),
  (2608580, 0, 0),
  (2608721, 1, 11),
  (2611045, 2, 1),
  (2618149, 11, 6),
  (2623011, 1, 11),
  (2625605, 1, 10),
  (2629848, 7, 10),
  (2630345, 1, 11),
  (2633416, 5, 10),
  (2634472, 4, 10),
  (2640627, 2, 7),
  (2641021, 2, 4),
  (2643167, 2, 13),
  (2644114, 7, 10),
  (2651582, 11, 0),
  (2653726, 11, 18),
  (2661530, 0, 17),
  (2663366, 11, 18),
  (2667844, 0, 0),
  (2669314, 3, 13),
  (2674982, 1, 0),
  (2675038, 1, 0),
  (2675456, 4, 10),
  (2677058, 6, 10),
  (2677231, 3, 4),
  (2677534, 11, 0),
  (2678908, 5, 17),
  (2680692, 10, 0),
  (2690761, 10, 2),
  (2693319, 3, 3),
  (2697967, 0, 11),
  (2698527, 8, 7),
  (2698707, 1, 0),
  (2699425, 10, 0),
  (2703216, 4, 10),
  (2706329, 2, 10),
  (2706429, 1, 0),
  (2709816, 9, 10),
  (2711026, 7, 22),
  (2717478, 6, 10),
  (2719662, 9, 10),
  (2721338, 7, 21),
  (2721549, 11, 0),
  (2722471, 2, 15),
  (2726113, 11, 11),
  (2726981, 8, 1),
  (2727433, 8, 7),
  (2731479, 6, 10),
  (2733626, 1, 10),
  (2733801, 0, 11),
  (2733964, 1, 18),
  (2735134, 7, 10),
  (2736474, 4, 10),
  (2738278, 10, 5),
  (2738811, 0, 10),
  (2739153, 7, 10),
  (2740678, 10, 0),
  (2741726, 8, 7),
  (2753150, 3, 10),
  (2754908, 1, 0),
  (2757477, 4, 10),
  (2765483, 7, 17),
  (2773254, 0, 0),
  (2774035, 11, 17),
  (2774738, 8, 8),
  (2779088, 1, 0),
  (2779310, 7, 17),
  (2789746, 4, 7),
  (2790956, 4, 22),
  (2792663, 5, 9),
  (2793078, 6, 6),
  (2793635, 1, 19),
  (2796756, 8, 10),
  (2799545, 0, 6),
  (2802841, 4, 10),
  (2803924, 0, 0),
  (2814608, 0, 18),
  (2818710, 11, 11),
  (2824695, 7, 10),
  (2825857, 8, 7),
  (2828706, 2, 7),
  (2831284, 10, 18),
  (2838918, 4, 17),
  (2839168, 9, 4),
  (2847729, 10, 17),
  (2852959, 8, 3),
  (2853968, 7, 6),
  (2866933, 6, 10),
  (2867903, 7, 10),
  (2874359, 9, 3),
  (2878397, 3, 2),
  (2879030, 1, 22),
  (2881152, 5, 10),
  (2881428, 6, 10),
  (2886137, 1, 0),
  (2886292, 3, 16),
  (2886643, 9, 18),
  (2889134, 6, 20),
  (2891137, 11, 0),
  (2894677, 11, 11),
  (2897303, 9, 0),
  (2904244, 8, 7),
  (2906906, 4, 10),
  (2909472, 6, 2),
  (2912753, 2, 3),
  (2913700, 0, 0),
  (2919099, 2, 15),
  (2922134, 4, 10),
  (2924598, 4, 10),
  (2925028, 0, 0),
  (2926450, 7, 10),
  (2938766, 6, 6),
  (2941055, 4, 21),
  (2943810, 4, 10),
  (2945484, 7, 3),
  (2954160, 4, 9),
  (2954536, 5, 22),
  (2954885, 5, 17),
  (2958572, 7, 13),
  (2961139, 8, 7),
  (2972920, 0, 19),
  (2977452, 10, 0),
  (2980614, 8, 3),
  (2984042, 11, 0),
  (2986068, 9, 7),
  (2989260, 8, 3),
  (2994948, 9, 18),
  (2995152, 3, 13),
  (2997048, 9, 7),
  (3001567, 2, 6),
  (3007768, 9, 7),
  (3008851, 0, 19),
  (3017861, 2, 4),
  (3019024, 4, 17),
  (3020393, 4, 10),
  (3021099, 0, 2),
  (3025296, 4, 16),
  (3025325, 1, 6),
  (3028559, 5, 10),
  (3044097, 2, 2),
  (3045404, 1, 0),
  (3045468, 1, 0),
  (3046375, 1, 18),
  (3047677, 5, 10),
  (3050382, 1, 8),
  (3052914, 2, 7),
  (3056776, 6, 10),
  (3057946, 9, 3),
  (3058810, 5, 2),
  (3067390, 10, 22),
  (3069630, 2, 7),
  (3071878, 10, 11),
  (3074327, 11, 0),
  (3079386, 5, 10),
  (3086329, 3, 0),
  (3091415, 8, 8),
  (3091744, 7, 6),
  (3097129, 5, 21),
  (3103005, 8, 7),
  (3104734, 9, 4),
  (3109764, 8, 0),
  (3112220, 9, 10),
  (3114777, 7, 17),
  (3114785, 4, 10),
  (3114901, 4, 17),
  (3115485, 10, 0),
  (3116031, 3, 3),
  (3117755, 11, 11),
  (3121215, 8, 14),
  (3121562, 2, 7),
  (3122849, 10, 7),
  (3123324, 7, 10),
  (3123563, 8, 13),
  (3133520, 5, 10),
  (3135493, 0, 1),
  (3136786, 5, 21),
  (3140612, 11, 0),
  (3143008, 6, 22),
  (3147779, 10, 0),
  (3149246, 3, 7),
  (3149740, 1, 11),
  (3153528, 4, 10),
  (3154217, 8, 3),
  (3168953, 9, 3),
  (3171119, 2, 7),
  (3172123, 8, 12),
  (3172387, 7, 9),
  (3173108, 9, 3),
  (3174338, 4, 11),
  (3180661, 1, 10),
  (3180671, 2, 18),
  (3186645, 0, 5),
  (3188201, 8, 2),
  (3192987, 8, 18),
  (3193474, 6, 21),
  (3193555, 11, 11),
  (3195597, 0, 0),
  (3195753, 7, 17),
  (3195791, 11, 18),
  (3198772, 4, 2),
  (3202881, 0, 13),
  (3208770, 0, 0),
  (3215627, 5, 10),
  (3215656, 10, 21),
  (3218000, 4, 18),
  (3220233, 6, 10),
  (3225952, 4, 10),
  (3229120, 7, 10),
  (3231011, 2, 3),
  (3232477, 4, 10),
  (3234433, 6, 9),
  (3254398, 5, 22),
  (3263944, 7, 9),
  (3264587, 0, 0),
  (3269722, 6, 10),
  (3272372, 7, 5),
  (3273311, 9, 10),
  (3275077, 11, 11),
  (3275630, 6, 10),
  (3277758, 6, 17),
  (3280331, 4, 6),
  (3283338, 2, 14),
  (3291009, 3, 7),
  (3291278, 4, 17),
  (3292195, 11, 3),
  (3292545, 7, 10),
  (3299094, 6, 9),
  (3301205, 1, 11),
  (3309636, 6, 9),
  (3310258, 5, 10),
  (3320455, 11, 10),
  (3321635, 1, 17),
  (3322572, 5, 10),
  (3332779, 3, 7),
  (3335558, 11, 21),
  (3336670, 5, 10),
  (3342211, 4, 17),
  (3343196, 6, 18),
  (3348652, 11, 11),
  (3350130, 6, 17),
  (3354001, 0, 11),
  (3358472, 2, 4),
  (3360105, 6, 17),
  (3362781, 0, 0),
  (3363244, 10, 0),
  (3365608, 4, 10),
  (3368254, 1, 15),
  (3373850, 4, 18),
  (3374157, 8, 13),
  (3377832, 5, 17),
  (3379035, 1, 18),
  (3379790, 6, 1),
  (3382504, 10, 11),
  (3383093, 4, 17),
  (3386463, 11, 18),
  (3386687, 6, 10),
  (3388689, 1, 11),
  (3391967, 1, 0),
  (3393492, 6, 10),
  (3395578, 3, 9),
  (3396904, 11, 11),
  (3402665, 6, 10),
  (3403382, 7, 17),
  (3403949, 1, 1),
  (3416623, 9, 3),
  (3418382, 0, 11),
  (3419005, 4, 21),
  (3423127, 11, 10),
  (3424801, 7, 17),
  (3431637, 6, 6),
  (3435141, 11, 11),
  (3435831, 8, 3),
  (3443464, 4, 10),
  (3459438, 10, 0),
  (3461193, 6, 10),
  (3461953, 10, 0),
  (3463035, 1, 0),
  (3466034, 3, 13),
  (3466174, 3, 10),
  (3470558, 7, 6),
  (3473931, 2, 15),
  (3477997, 6, 6),
  (3481057, 5, 10),
  (3485188, 2, 2),
  (3486903, 0, 18),
  (3489641, 2, 11),
  (3492136, 4, 10),
  (3493596, 5, 10),
  (3496888, 10, 0),
  (3497250, 9, 3),
  (3502017, 3, 18),
  (3502377, 10, 0),
  (3503592, 8, 13),
  (3504744, 11, 0),
  (3508628, 8, 7),
  (3508716, 2, 18),
  (3508855, 9, 7),
  (3515394, 9, 13),
  (3515655, 4, 17),
  (3519542, 6, 18),
  (3523918, 7, 10),
  (3524142, 2, 2),
  (3528730, 6, 10),
  (3536022, 9, 18),
  (3541038, 5, 22),
  (3546812, 3, 18),
  (3548738, 4, 21),
  (3556316, 2, 7),
  (3558330, 4, 10),
  (3566226, 4, 10),
  (3570224, 9, 7),
  (3571714, 11, 0),
  (3572561, 5, 10),
  (3573543, 11, 0),
  (3574147, 6, 1),
  (3575034, 0, 0),
  (3585907, 10, 11),
  (3586304, 9, 18),
  (3590574, 0, 7),
  (3594525, 0, 18),
  (3595493, 5, 21),
])