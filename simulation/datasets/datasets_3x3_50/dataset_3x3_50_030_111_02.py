from src.util import *
schedule = deque([
  (309, 4, 19),
  (3057, 1, 73),
  (5643, 12, 0),
  (6535, 13, 19),
  (7494, 6, 56),
  (11679, 8, 56),
  (13532, 9, 56),
  (14981, 14, 0),
  (16994, 12, 48),
  (18017, 0, 35),
  (18599, 14, 36),
  (20191, 3, 4),
  (33916, 8, 35),
  (36885, 10, 36),
  (38987, 6, 68),
  (40872, 14, 0),
  (43103, 15, 36),
  (44222, 10, 19),
  (44940, 0, 54),
  (47223, 1, 0),
  (52778, 5, 0),
  (53778, 11, 6),
  (53818, 5, 19),
  (55388, 13, 16),
  (56462, 1, 35),
  (58934, 7, 34),
  (59296, 2, 20),
  (65235, 6, 35),
  (65757, 1, 0),
  (69631, 7, 60),
  (70719, 6, 67),
  (74000, 2, 23),
  (75673, 5, 33),
  (79450, 9, 35),
  (86335, 3, 19),
  (86727, 10, 17),
  (87893, 15, 0),
  (89797, 9, 35),
  (90123, 0, 0),
  (101959, 10, 48),
  (102722, 7, 56),
  (105712, 11, 16),
  (111063, 3, 4),
  (111326, 7, 35),
  (112426, 11, 19),
  (112815, 9, 35),
  (115987, 11, 14),
  (117052, 2, 36),
  (118041, 12, 20),
  (119228, 5, 14),
  (122643, 7, 35),
  (122672, 5, 19),
  (123266, 10, 19),
  (127224, 15, 0),
  (130643, 9, 35),
  (132345, 1, 73),
  (134366, 0, 0),
  (137461, 9, 35),
  (139688, 6, 16),
  (140974, 9, 35),
  (141416, 15, 0),
  (146247, 15, 0),
  (148965, 7, 12),
  (150525, 14, 0),
  (150762, 11, 15),
  (151838, 12, 23),
  (152095, 2, 4),
  (153093, 8, 56),
  (154277, 15, 36),
  (158109, 5, 19),
  (161295, 3, 19),
  (162568, 2, 36),
  (162847, 3, 30),
  (162898, 4, 33),
  (164485, 5, 19),
  (167634, 2, 33),
  (168630, 2, 23),
  (175913, 4, 48),
  (176514, 1, 36),
  (180647, 1, 56),
  (182343, 1, 0),
  (183748, 12, 4),
  (185400, 13, 27),
  (187563, 13, 23),
  (192980, 1, 0),
  (195569, 9, 55),
  (195743, 13, 23),
  (196227, 4, 15),
  (197722, 4, 3),
  (198947, 11, 19),
  (200417, 8, 56),
  (207021, 10, 22),
  (207107, 10, 8),
  (212015, 12, 19),
  (212832, 13, 30),
  (213029, 3, 23),
  (213523, 14, 0),
  (216391, 15, 0),
  (222169, 6, 47),
  (222826, 0, 0),
  (225796, 11, 16),
  (226568, 6, 67),
  (227863, 13, 43),
  (231589, 3, 21),
  (231855, 7, 35),
  (233191, 3, 4),
  (233373, 13, 4),
  (236103, 13, 0),
  (237675, 6, 48),
  (237771, 4, 19),
  (238541, 8, 56),
  (245348, 0, 36),
  (247320, 3, 4),
  (248370, 10, 33),
  (249495, 7, 56),
  (253083, 7, 35),
  (255870, 7, 35),
  (258490, 5, 19),
  (259427, 7, 67),
  (260139, 10, 15),
  (261689, 15, 0),
  (264302, 3, 0),
  (267181, 11, 42),
  (267797, 2, 27),
  (270153, 12, 26),
  (272513, 6, 9),
  (273595, 1, 0),
  (274537, 1, 0),
  (274981, 14, 13),
  (276167, 3, 20),
  (278170, 2, 19),
  (278380, 7, 56),
  (278569, 11, 19),
  (282456, 2, 43),
  (283487, 9, 67),
  (286782, 2, 41),
  (286888, 10, 14),
  (288554, 9, 35),
  (291095, 15, 0),
  (293932, 7, 56),
  (294578, 1, 0),
  (296220, 9, 35),
  (296455, 6, 34),
  (298975, 12, 4),
  (301583, 1, 0),
  (303906, 10, 19),
  (304602, 4, 19),
  (305188, 10, 19),
  (306008, 8, 67),
  (307922, 4, 6),
  (310888, 11, 27),
  (316751, 4, 19),
  (318232, 3, 15),
  (320727, 7, 35),
  (321478, 3, 19),
  (322226, 0, 0),
  (324407, 5, 29),
  (325515, 3, 4),
  (326585, 13, 34),
  (327424, 13, 20),
  (327425, 11, 22),
  (328068, 15, 36),
  (328274, 15, 0),
  (330386, 3, 0),
  (332283, 11, 28),
  (332701, 5, 15),
  (332890, 8, 35),
  (332937, 9, 28),
  (333316, 10, 15),
  (333638, 10, 19),
  (339108, 1, 0),
  (340049, 11, 48),
  (340626, 12, 29),
  (348824, 5, 3),
  (350986, 2, 4),
  (351702, 6, 35),
  (351926, 8, 35),
  (353532, 15, 36),
  (355897, 1, 0),
  (358931, 7, 56),
  (362873, 5, 19),
  (363412, 13, 19),
  (363847, 10, 29),
  (364345, 14, 0),
  (367309, 9, 56),
  (368782, 13, 3),
  (369500, 5, 21),
  (372587, 14, 44),
  (372685, 1, 24),
  (375579, 14, 0),
  (375697, 12, 4),
  (380980, 2, 36),
  (381206, 1, 0),
  (384628, 12, 23),
  (386467, 14, 17),
  (390765, 6, 35),
  (398124, 12, 10),
  (401156, 0, 0),
  (401642, 11, 10),
  (411188, 14, 0),
  (413844, 15, 36),
  (414556, 12, 16),
  (415176, 14, 0),
  (417123, 6, 35),
  (420004, 1, 0),
  (420855, 8, 35),
  (422064, 2, 4),
  (423048, 15, 0),
  (423249, 11, 19),
  (424531, 15, 0),
  (426404, 7, 35),
  (426712, 5, 19),
  (428040, 14, 36),
  (433119, 12, 32),
  (434442, 1, 47),
  (434848, 6, 35),
  (437853, 8, 35),
  (439147, 5, 29),
  (439240, 4, 40),
  (444193, 1, 20),
  (451215, 9, 35),
  (452062, 4, 2),
  (453170, 4, 14),
  (455392, 14, 0),
  (458536, 9, 35),
  (463305, 7, 35),
  (463843, 12, 45),
  (467747, 10, 33),
  (469241, 7, 35),
  (471130, 6, 35),
  (471688, 13, 36),
  (474129, 10, 44),
  (475546, 8, 56),
  (479030, 11, 10),
  (480662, 8, 35),
  (481167, 1, 0),
  (481997, 8, 35),
  (482868, 11, 42),
  (483065, 14, 36),
  (483491, 0, 0),
  (484231, 10, 22),
  (485787, 9, 15),
  (486107, 1, 0),
  (488084, 11, 10),
  (488305, 8, 56),
  (488466, 12, 48),
  (488481, 10, 16),
  (489432, 3, 0),
  (495031, 14, 0),
  (495809, 8, 45),
  (497815, 7, 19),
  (505705, 4, 19),
  (506920, 11, 15),
  (507196, 11, 45),
  (507879, 11, 1),
  (509121, 15, 36),
  (510197, 12, 23),
  (510497, 4, 19),
  (512703, 0, 36),
  (513133, 3, 48),
  (514510, 10, 19),
  (514876, 10, 33),
  (514946, 10, 14),
  (515399, 6, 35),
  (516636, 2, 48),
  (517750, 2, 12),
  (518224, 6, 57),
  (519294, 14, 57),
  (522220, 7, 35),
  (527702, 4, 11),
  (532002, 4, 33),
  (532436, 7, 35),
  (534582, 14, 0),
  (538121, 13, 36),
  (539922, 8, 56),
  (547197, 13, 8),
  (548776, 2, 36),
  (555318, 5, 24),
  (557535, 6, 35),
  (557982, 8, 8),
  (558804, 13, 48),
  (566560, 13, 48),
  (567305, 1, 0),
  (569097, 8, 6),
  (569373, 3, 4),
  (573995, 6, 67),
  (574465, 11, 33),
  (574588, 1, 0),
  (575657, 5, 19),
  (576575, 9, 35),
  (578099, 3, 36),
  (580171, 0, 0),
  (583550, 13, 4),
  (583824, 15, 0),
  (584370, 0, 0),
  (588009, 3, 16),
  (588341, 6, 35),
  (589411, 14, 36),
  (591343, 11, 14),
  (598531, 8, 56),
  (599482, 4, 19),
  (599541, 11, 14),
  (600972, 8, 63),
  (601882, 8, 35),
  (602725, 3, 19),
  (603662, 9, 35),
  (605736, 7, 35),
  (606039, 7, 51),
  (606704, 1, 0),
  (607736, 12, 33),
  (607996, 12, 44),
  (608944, 3, 4),
  (609605, 13, 39),
  (611882, 14, 0),
  (614116, 3, 4),
  (616564, 3, 31),
  (620141, 2, 1),
  (620194, 13, 1),
  (622217, 2, 19),
  (622694, 6, 35),
  (623874, 2, 21),
  (624787, 9, 35),
  (626812, 0, 31),
  (627266, 14, 56),
  (629417, 13, 19),
  (634460, 13, 48),
  (639420, 3, 36),
  (649126, 11, 19),
  (650700, 13, 4),
  (652441, 11, 19),
  (654554, 11, 14),
  (654850, 0, 0),
  (661156, 14, 53),
  (661647, 1, 57),
  (663296, 2, 23),
  (664353, 11, 10),
  (667006, 7, 67),
  (669052, 15, 0),
  (669193, 10, 10),
  (669281, 14, 36),
  (670100, 5, 33),
  (670716, 8, 35),
  (676771, 11, 19),
  (683638, 13, 33),
  (684889, 2, 48),
  (687328, 13, 4),
  (688670, 2, 27),
  (689973, 6, 35),
  (693005, 0, 36),
  (693173, 7, 73),
  (693349, 14, 36),
  (695151, 13, 4),
  (698601, 7, 60),
  (698857, 2, 19),
  (699987, 3, 48),
  (701505, 7, 35),
  (702735, 15, 29),
  (702885, 8, 41),
  (703705, 8, 56),
  (704415, 12, 4),
  (705945, 0, 21),
  (708089, 5, 24),
  (708376, 7, 35),
  (709232, 4, 25),
  (711375, 3, 33),
  (712147, 12, 31),
  (715446, 5, 19),
  (723827, 3, 23),
  (727102, 15, 0),
  (727466, 9, 53),
  (727584, 1, 0),
  (731058, 14, 0),
  (731151, 5, 7),
  (731276, 2, 17),
  (731403, 8, 67),
  (731600, 10, 19),
  (733161, 14, 0),
  (734169, 9, 67),
  (735752, 8, 67),
  (738466, 9, 60),
  (738725, 14, 0),
  (742713, 9, 67),
  (743932, 15, 42),
  (749021, 11, 46),
  (750370, 15, 0),
  (751255, 8, 35),
  (752074, 6, 35),
  (752835, 2, 27),
  (754047, 11, 17),
  (755364, 13, 4),
  (756915, 3, 26),
  (757531, 12, 4),
  (758146, 0, 69),
  (769277, 5, 33),
  (769809, 10, 15),
  (769838, 12, 2),
  (770786, 0, 0),
  (772463, 0, 0),
  (773303, 10, 15),
  (774993, 10, 14),
  (775513, 1, 36),
  (775803, 2, 33),
  (777783, 3, 19),
  (785426, 8, 51),
  (787453, 4, 19),
  (788611, 11, 14),
  (790875, 2, 19),
  (791083, 1, 0),
  (792554, 14, 36),
  (796434, 2, 19),
  (798870, 14, 0),
  (801555, 8, 35),
  (802192, 13, 15),
  (803198, 9, 72),
  (806144, 7, 35),
  (806309, 3, 20),
  (816471, 7, 35),
  (816542, 7, 35),
  (816704, 2, 4),
  (816811, 11, 30),
  (816956, 12, 48),
  (820186, 14, 35),
  (821069, 10, 29),
  (822267, 15, 0),
  (822578, 13, 19),
  (823277, 14, 36),
  (826614, 4, 15),
  (826869, 5, 11),
  (832280, 4, 15),
  (834477, 0, 0),
  (837918, 9, 35),
  (838568, 12, 4),
  (839138, 9, 35),
  (839236, 12, 4),
  (839724, 8, 35),
  (842222, 11, 3),
  (844779, 3, 4),
  (846815, 15, 36),
  (847154, 9, 35),
  (854275, 4, 38),
  (854454, 11, 33),
  (856431, 5, 6),
  (856754, 10, 14),
  (858003, 8, 56),
  (858581, 12, 4),
  (860098, 13, 1),
  (862474, 4, 3),
  (868459, 4, 11),
  (870780, 15, 57),
  (871301, 6, 38),
  (871575, 9, 35),
  (871917, 13, 48),
  (872649, 15, 0),
  (873494, 7, 35),
  (874314, 15, 0),
  (876304, 4, 14),
  (877429, 3, 15),
  (879012, 2, 43),
  (879982, 15, 0),
  (880968, 6, 35),
  (881591, 11, 14),
  (882211, 0, 0),
  (885879, 0, 0),
  (886493, 12, 19),
  (890686, 14, 0),
  (891735, 7, 35),
  (894820, 8, 35),
  (900802, 10, 33),
  (902220, 0, 36),
  (905296, 13, 39),
  (906902, 4, 19),
  (907563, 3, 4),
  (907997, 12, 4),
  (908638, 8, 35),
  (910739, 14, 0),
  (911781, 12, 42),
  (915511, 8, 35),
  (916791, 7, 35),
  (917793, 10, 33),
  (918709, 11, 15),
  (922738, 7, 35),
  (930205, 5, 39),
  (930598, 11, 14),
  (932354, 8, 35),
  (932702, 11, 33),
  (933638, 10, 14),
  (935690, 12, 4),
  (936155, 8, 35),
  (936688, 7, 35),
  (938315, 4, 3),
  (941387, 11, 3),
  (942720, 11, 19),
  (944425, 0, 0),
  (944857, 9, 56),
  (945394, 3, 44),
  (945847, 15, 24),
  (945997, 4, 19),
  (951189, 12, 0),
  (951400, 1, 48),
  (952432, 0, 0),
  (955463, 1, 0),
  (958948, 4, 19),
  (960278, 2, 4),
  (975992, 5, 47),
  (977306, 9, 73),
  (980082, 10, 41),
  (981271, 6, 35),
  (985597, 5, 19),
  (986378, 5, 14),
  (987598, 0, 0),
  (989227, 6, 35),
  (991403, 13, 30),
  (993661, 3, 4),
  (994027, 12, 4),
  (998866, 7, 35),
  (1003159, 12, 0),
  (1003504, 14, 0),
  (1003899, 0, 36),
  (1004007, 2, 48),
  (1005734, 8, 35),
  (1009237, 12, 4),
  (1014764, 1, 0),
  (1019246, 10, 44),
  (1019761, 5, 6),
  (1023189, 9, 35),
  (1024220, 2, 3),
  (1024385, 5, 33),
  (1027974, 4, 18),
  (1033849, 0, 36),
  (1035496, 2, 21),
  (1038320, 2, 0),
  (1040016, 6, 35),
  (1049187, 11, 14),
  (1050637, 10, 14),
  (1055156, 12, 0),
  (1058349, 4, 19),
  (1059285, 6, 35),
  (1061947, 9, 35),
  (1072374, 14, 0),
  (1073562, 6, 35),
  (1075276, 2, 4),
  (1075684, 2, 0),
  (1075751, 4, 19),
  (1077008, 14, 20),
  (1077590, 14, 0),
  (1079842, 1, 68),
  (1080689, 4, 15),
  (1086961, 10, 19),
  (1089710, 15, 0),
  (1091845, 11, 14),
  (1091850, 10, 19),
  (1091998, 11, 14),
  (1092974, 12, 29),
  (1095790, 3, 4),
  (1096462, 11, 15),
  (1096853, 2, 0),
  (1097571, 5, 19),
  (1099866, 12, 23),
  (1102461, 14, 0),
  (1104101, 11, 11),
  (1104653, 9, 6),
  (1106465, 7, 35),
  (1106532, 14, 0),
  (1109145, 15, 0),
  (1110632, 5, 19),
  (1118868, 6, 56),
  (1122957, 3, 33),
  (1132644, 9, 0),
  (1135329, 3, 4),
  (1137240, 12, 4),
  (1139245, 11, 9),
  (1141674, 13, 11),
  (1141682, 9, 57),
  (1146196, 13, 1),
  (1147054, 5, 19),
  (1148276, 7, 35),
  (1149265, 14, 0),
  (1149317, 8, 56),
  (1152943, 12, 4),
  (1156399, 1, 36),
  (1158999, 15, 36),
  (1160683, 0, 50),
  (1160801, 1, 0),
  (1161448, 5, 9),
  (1165123, 6, 56),
  (1166184, 4, 43),
  (1170356, 11, 14),
  (1170896, 12, 8),
  (1171242, 6, 34),
  (1171863, 0, 3),
  (1172402, 14, 36),
  (1172928, 5, 15),
  (1174268, 13, 20),
  (1176156, 8, 35),
  (1177706, 9, 35),
  (1179684, 15, 0),
  (1181428, 12, 4),
  (1181629, 12, 0),
  (1184551, 12, 4),
  (1186854, 0, 0),
  (1189936, 13, 4),
  (1190877, 4, 48),
  (1195073, 15, 0),
  (1203816, 14, 0),
  (1205357, 14, 0),
  (1207213, 12, 4),
  (1207957, 5, 33),
  (1211778, 15, 36),
  (1212910, 5, 6),
  (1214221, 15, 36),
  (1214223, 5, 14),
  (1214692, 9, 56),
  (1219003, 7, 67),
  (1220174, 10, 19),
  (1222288, 8, 35),
  (1224999, 8, 35),
  (1225227, 6, 72),
  (1226782, 12, 42),
  (1228971, 15, 0),
  (1231415, 14, 36),
  (1231454, 14, 28),
  (1235251, 6, 35),
  (1235257, 7, 56),
  (1235799, 11, 19),
  (1237743, 6, 35),
  (1239067, 9, 35),
  (1239096, 3, 5),
  (1241204, 1, 0),
  (1246194, 11, 19),
  (1247575, 12, 48),
  (1250430, 2, 23),
  (1250505, 14, 0),
  (1259621, 7, 35),
  (1260302, 8, 56),
  (1261240, 10, 46),
  (1266049, 13, 36),
  (1267022, 7, 35),
  (1270405, 10, 19),
  (1271087, 0, 0),
  (1271935, 4, 33),
  (1272109, 8, 35),
  (1274203, 13, 30),
  (1276987, 2, 4),
  (1277020, 6, 67),
  (1277452, 10, 48),
  (1279699, 8, 67),
  (1280935, 8, 56),
  (1282981, 12, 36),
  (1284862, 1, 0),
  (1288822, 8, 35),
  (1289275, 0, 0),
  (1289426, 7, 35),
  (1292605, 6, 72),
  (1294064, 7, 67),
  (1294390, 0, 20),
  (1295576, 2, 4),
  (1299301, 7, 35),
  (1301449, 11, 19),
  (1303623, 4, 29),
  (1305481, 13, 4),
  (1306366, 12, 4),
  (1308306, 4, 19),
  (1309312, 12, 19),
  (1310458, 14, 36),
  (1310806, 3, 4),
  (1310965, 15, 36),
  (1312719, 1, 0),
  (1317238, 1, 0),
  (1318993, 5, 19),
  (1320842, 9, 35),
  (1321235, 14, 36),
  (1321342, 9, 56),
  (1322831, 14, 0),
  (1323124, 15, 0),
  (1323264, 6, 56),
  (1323779, 0, 0),
  (1325771, 11, 15),
  (1326256, 9, 35),
  (1328768, 1, 0),
  (1329390, 1, 36),
  (1329793, 15, 36),
  (1332884, 9, 55),
  (1335103, 2, 15),
  (1339551, 6, 35),
  (1339761, 13, 43),
  (1340709, 10, 1),
  (1342499, 15, 61),
  (1343167, 15, 57),
  (1344417, 10, 19),
  (1345118, 12, 4),
  (1346983, 8, 56),
  (1350420, 12, 4),
  (1351879, 6, 35),
  (1362821, 8, 30),
  (1363283, 5, 19),
  (1363454, 3, 22),
  (1366044, 5, 6),
  (1366837, 1, 0),
  (1367701, 6, 35),
  (1371306, 7, 35),
  (1374260, 9, 56),
  (1375374, 6, 35),
  (1375699, 1, 0),
  (1376476, 5, 19),
  (1377330, 4, 19),
  (1378936, 15, 0),
  (1379107, 9, 35),
  (1384371, 12, 18),
  (1386414, 8, 35),
  (1387295, 9, 35),
  (1392456, 6, 41),
  (1395238, 4, 30),
  (1397534, 0, 57),
  (1398061, 15, 0),
  (1401754, 3, 23),
  (1404801, 0, 37),
  (1406439, 10, 19),
  (1410132, 13, 4),
  (1413846, 12, 17),
  (1414254, 3, 4),
  (1415067, 1, 0),
  (1417693, 12, 33),
  (1417757, 10, 14),
  (1417917, 13, 4),
  (1420990, 8, 72),
  (1423254, 12, 29),
  (1428835, 13, 3),
  (1429788, 1, 0),
  (1432285, 6, 35),
  (1432971, 3, 15),
  (1433768, 3, 42),
  (1433996, 11, 42),
  (1435042, 2, 36),
  (1435524, 8, 72),
  (1436160, 12, 0),
  (1439332, 6, 68),
  (1439743, 2, 4),
  (1440141, 3, 21),
  (1441315, 2, 15),
  (1441458, 15, 36),
  (1442181, 11, 33),
  (1445158, 5, 42),
  (1448109, 11, 17),
  (1448893, 5, 16),
  (1450215, 6, 35),
  (1452131, 14, 36),
  (1452449, 15, 0),
  (1459125, 6, 35),
  (1459236, 2, 0),
  (1460014, 14, 36),
  (1460751, 12, 8),
  (1462337, 2, 30),
  (1462415, 6, 35),
  (1462501, 0, 35),
  (1462725, 6, 35),
  (1465139, 3, 35),
  (1465505, 12, 19),
  (1468609, 3, 19),
  (1471248, 1, 0),
  (1471400, 15, 36),
  (1479223, 3, 1),
  (1481973, 5, 18),
  (1482614, 8, 71),
  (1484547, 11, 30),
  (1485095, 10, 30),
  (1489781, 8, 35),
  (1494832, 8, 35),
  (1496658, 10, 14),
  (1496807, 12, 30),
  (1499827, 10, 30),
  (1501024, 0, 68),
  (1503219, 15, 0),
  (1503757, 4, 15),
  (1504934, 1, 0),
  (1505013, 7, 56),
  (1505741, 10, 19),
  (1506320, 2, 20),
  (1506845, 3, 2),
  (1507000, 0, 68),
  (1507099, 3, 44),
  (1508227, 13, 4),
  (1509006, 11, 25),
  (1509384, 11, 10),
  (1510541, 3, 0),
  (1510859, 7, 56),
  (1512485, 4, 30),
  (1515420, 9, 35),
  (1515842, 14, 36),
  (1516007, 10, 33),
  (1519366, 3, 8),
  (1519690, 3, 40),
  (1519704, 2, 4),
  (1521170, 12, 32),
  (1524013, 2, 0),
  (1527399, 11, 19),
  (1531180, 2, 22),
  (1531363, 4, 19),
  (1532568, 11, 14),
  (1532990, 6, 16),
  (1534129, 9, 35),
  (1535054, 0, 0),
  (1535972, 14, 36),
  (1538121, 12, 23),
  (1540571, 13, 23),
  (1540635, 9, 19),
  (1542431, 10, 3),
  (1543597, 13, 0),
  (1545351, 10, 39),
  (1550617, 7, 35),
  (1551056, 0, 0),
  (1552373, 8, 35),
  (1553917, 15, 0),
  (1558710, 4, 19),
  (1562665, 10, 40),
  (1564565, 12, 15),
  (1565145, 5, 6),
  (1566332, 5, 22),
  (1566507, 0, 0),
  (1567841, 0, 0),
  (1570379, 13, 10),
  (1574027, 10, 19),
  (1574178, 5, 15),
  (1575970, 11, 16),
  (1576414, 10, 19),
  (1578593, 3, 23),
  (1580297, 9, 67),
  (1582030, 15, 0),
  (1582103, 0, 36),
  (1583182, 0, 36),
  (1584802, 7, 35),
  (1584857, 11, 48),
  (1585101, 3, 4),
  (1585226, 11, 19),
  (1586548, 3, 4),
  (1588153, 10, 19),
  (1589784, 4, 15),
  (1591467, 4, 9),
  (1605922, 6, 35),
  (1606392, 11, 15),
  (1606740, 7, 35),
  (1607794, 13, 4),
  (1608394, 12, 23),
  (1609615, 1, 0),
  (1615252, 1, 0),
  (1615324, 6, 35),
  (1615923, 11, 10),
  (1621570, 1, 0),
  (1622313, 5, 30),
  (1625672, 3, 4),
  (1628665, 3, 19),
  (1629831, 13, 20),
  (1635940, 5, 46),
  (1636161, 10, 19),
  (1637658, 13, 33),
  (1640177, 6, 35),
  (1642266, 14, 36),
  (1643973, 7, 67),
  (1645992, 15, 57),
  (1646278, 2, 4),
  (1648197, 11, 19),
  (1648494, 8, 34),
  (1650500, 0, 24),
  (1651586, 2, 21),
  (1655850, 0, 36),
  (1656727, 11, 19),
  (1657397, 10, 26),
  (1658972, 0, 0),
  (1659349, 0, 0),
  (1660884, 13, 19),
  (1663016, 12, 4),
  (1666016, 7, 35),
  (1672426, 14, 0),
  (1673819, 0, 36),
  (1675871, 5, 19),
  (1677973, 8, 63),
  (1678239, 8, 56),
  (1683961, 11, 19),
  (1689814, 10, 19),
  (1695053, 14, 0),
  (1696608, 6, 35),
  (1698341, 6, 56),
  (1701460, 2, 23),
  (1702480, 11, 33),
  (1704794, 12, 22),
  (1709778, 7, 34),
  (1711984, 14, 0),
  (1712332, 15, 0),
  (1715699, 9, 67),
  (1721627, 3, 1),
  (1721676, 10, 33),
  (1723289, 15, 73),
  (1724102, 10, 14),
  (1728784, 14, 0),
  (1732703, 7, 67),
  (1733322, 5, 29),
  (1735921, 8, 56),
  (1738711, 9, 73),
  (1745467, 3, 4),
  (1748910, 12, 19),
  (1749774, 3, 31),
  (1750016, 7, 35),
  (1750924, 13, 0),
  (1752507, 3, 19),
  (1752803, 12, 19),
  (1753402, 6, 35),
  (1753748, 10, 33),
  (1755599, 4, 33),
  (1757414, 5, 19),
  (1759712, 14, 0),
  (1760772, 12, 0),
  (1761965, 15, 0),
  (1766430, 15, 36),
  (1766921, 12, 23),
  (1773276, 14, 36),
  (1775347, 8, 35),
  (1776252, 9, 35),
  (1776769, 11, 10),
  (1778886, 15, 56),
  (1779323, 11, 19),
  (1784045, 14, 0),
  (1785903, 9, 35),
  (1787769, 8, 27),
  (1790045, 9, 34),
  (1791054, 12, 23),
  (1793703, 3, 5),
  (1795118, 11, 33),
  (1795758, 0, 36),
  (1798712, 12, 20),
  (1799461, 9, 67),
  (1800598, 0, 36),
  (1800869, 6, 34),
  (1801508, 10, 33),
  (1805162, 5, 7),
  (1806854, 1, 0),
  (1808220, 1, 36),
  (1808660, 6, 35),
  (1809572, 12, 8),
  (1811355, 2, 20),
  (1811635, 8, 34),
  (1813074, 1, 0),
  (1813302, 6, 35),
  (1820113, 7, 67),
  (1820785, 2, 15),
  (1821807, 6, 56),
  (1822874, 13, 0),
  (1823111, 13, 4),
  (1825719, 6, 56),
  (1825733, 5, 48),
  (1829190, 8, 56),
  (1829387, 4, 19),
  (1832013, 15, 69),
  (1832525, 4, 14),
  (1832590, 6, 56),
  (1833227, 1, 0),
  (1836802, 5, 38),
  (1836855, 8, 12),
  (1836925, 8, 35),
  (1836933, 6, 73),
  (1837180, 12, 8),
  (1837361, 9, 35),
  (1840327, 13, 33),
  (1841003, 0, 35),
  (1842605, 9, 35),
  (1843150, 2, 26),
  (1844476, 8, 67),
  (1844535, 2, 36),
  (1848265, 1, 36),
  (1848951, 15, 0),
  (1851089, 8, 35),
  (1853015, 12, 4),
  (1857074, 7, 35),
  (1861198, 11, 19),
  (1863715, 9, 63),
  (1866422, 8, 35),
  (1867325, 6, 72),
  (1869830, 0, 0),
  (1870004, 5, 42),
  (1872983, 6, 35),
  (1874151, 12, 35),
  (1877058, 11, 40),
  (1877382, 6, 35),
  (1877500, 1, 57),
  (1880383, 8, 35),
  (1880698, 4, 33),
  (1881411, 9, 19),
  (1882164, 4, 15),
  (1886797, 2, 20),
  (1891042, 5, 27),
  (1893663, 11, 19),
  (1896866, 5, 33),
  (1897562, 15, 0),
  (1897769, 7, 35),
  (1899900, 1, 0),
  (1902088, 1, 0),
  (1904876, 10, 11),
  (1905034, 15, 0),
  (1905543, 4, 16),
  (1909260, 0, 36),
  (1910955, 12, 48),
  (1911032, 15, 0),
  (1912551, 15, 57),
  (1918283, 0, 0),
  (1921326, 14, 0),
  (1922813, 8, 45),
  (1925309, 11, 47),
  (1925849, 12, 11),
  (1926168, 7, 56),
  (1928252, 9, 35),
  (1930075, 9, 56),
  (1937523, 2, 4),
  (1937533, 4, 19),
  (1940712, 3, 4),
  (1940810, 3, 4),
  (1945532, 9, 35),
  (1945693, 14, 73),
  (1947580, 9, 35),
  (1952532, 0, 0),
  (1954704, 6, 56),
  (1955546, 10, 19),
  (1961000, 6, 56),
  (1962692, 9, 35),
  (1962764, 15, 36),
  (1963235, 4, 19),
  (1966756, 2, 19),
  (1968249, 2, 43),
  (1969204, 15, 0),
  (1971329, 2, 48),
  (1973531, 15, 10),
  (1976619, 13, 4),
  (1978588, 8, 35),
  (1980078, 4, 15),
  (1982594, 1, 0),
  (1983953, 11, 15),
  (1985693, 0, 57),
  (1986384, 6, 68),
  (1990280, 7, 35),
  (1992993, 4, 19),
  (1996476, 7, 35),
  (1999584, 8, 56),
  (1999918, 15, 36),
  (2002338, 1, 0),
  (2002370, 10, 46),
  (2004336, 14, 0),
  (2005324, 12, 4),
  (2006478, 4, 29),
  (2007111, 9, 56),
  (2010474, 1, 36),
  (2010900, 7, 56),
  (2014326, 14, 73),
  (2014823, 13, 26),
  (2015577, 8, 73),
  (2020896, 0, 0),
  (2022046, 11, 33),
  (2023400, 7, 73),
  (2027031, 1, 0),
  (2027189, 5, 33),
  (2031139, 0, 0),
  (2031759, 0, 36),
  (2034460, 0, 0),
  (2040941, 4, 2),
  (2043699, 2, 42),
  (2044421, 14, 0),
  (2046471, 1, 0),
  (2048024, 8, 35),
  (2048257, 9, 35),
  (2049385, 11, 14),
  (2049941, 9, 35),
  (2052472, 5, 19),
  (2052640, 5, 19),
  (2065537, 13, 4),
  (2065926, 11, 45),
  (2069124, 15, 0),
  (2071742, 13, 1),
  (2075225, 9, 35),
  (2075328, 0, 24),
  (2076985, 3, 23),
  (2077217, 0, 0),
  (2081117, 6, 35),
  (2081943, 14, 46),
  (2082742, 7, 67),
  (2085125, 9, 56),
  (2089098, 14, 36),
  (2089126, 6, 67),
  (2089947, 7, 68),
  (2090716, 12, 19),
  (2093143, 10, 14),
  (2093243, 2, 48),
  (2094720, 7, 73),
  (2095245, 5, 19),
  (2099993, 6, 35),
  (2101011, 1, 31),
  (2102670, 6, 35),
  (2104319, 15, 0),
  (2104607, 7, 35),
  (2114789, 3, 19),
  (2116124, 3, 17),
  (2118394, 8, 56),
  (2119205, 15, 0),
  (2120899, 13, 36),
  (2126305, 9, 56),
  (2128951, 12, 1),
  (2131492, 15, 0),
  (2133437, 5, 3),
  (2136023, 1, 35),
  (2138056, 7, 35),
  (2139477, 14, 31),
  (2144201, 5, 33),
  (2144905, 11, 47),
  (2152098, 14, 0),
  (2152779, 15, 35),
  (2157784, 5, 33),
  (2157812, 3, 4),
  (2161721, 1, 36),
  (2161843, 11, 20),
  (2164364, 10, 16),
  (2164466, 4, 15),
  (2167039, 2, 0),
  (2169355, 8, 35),
  (2169744, 6, 35),
  (2170229, 8, 67),
  (2174749, 6, 35),
  (2174807, 9, 56),
  (2176302, 11, 3),
  (2177418, 13, 4),
  (2177573, 8, 35),
  (2178100, 6, 35),
  (2178584, 15, 0),
  (2184393, 14, 36),
  (2184659, 15, 0),
  (2188174, 14, 0),
  (2189553, 5, 10),
  (2191978, 5, 14),
  (2196319, 7, 55),
  (2196530, 7, 56),
  (2197904, 15, 36),
  (2202183, 3, 15),
  (2202952, 12, 29),
  (2204306, 1, 69),
  (2211751, 11, 17),
  (2213836, 5, 15),
  (2216309, 6, 35),
  (2216865, 14, 24),
  (2218170, 15, 36),
  (2218185, 14, 0),
  (2222299, 0, 36),
  (2223071, 8, 35),
  (2223823, 2, 3),
  (2226044, 4, 10),
  (2226728, 15, 0),
  (2227006, 4, 16),
  (2227141, 9, 35),
  (2228113, 1, 0),
  (2228157, 13, 4),
  (2229077, 8, 56),
  (2230967, 7, 35),
  (2232508, 2, 16),
  (2232950, 8, 29),
  (2235438, 1, 0),
  (2240416, 14, 0),
  (2241209, 4, 6),
  (2247330, 9, 37),
  (2249081, 10, 19),
  (2249197, 12, 0),
  (2249588, 1, 36),
  (2250241, 10, 19),
  (2250955, 14, 0),
  (2255856, 5, 29),
  (2258700, 2, 23),
  (2259377, 6, 72),
  (2262466, 1, 1),
  (2262740, 13, 4),
  (2263390, 5, 48),
  (2264831, 9, 35),
  (2268939, 15, 19),
  (2269984, 4, 19),
  (2270134, 9, 35),
  (2271920, 5, 3),
  (2273231, 9, 35),
  (2275376, 15, 36),
  (2277143, 13, 0),
  (2281932, 13, 19),
  (2290343, 15, 0),
  (2291746, 0, 0),
  (2294113, 14, 36),
  (2294426, 1, 0),
  (2294800, 11, 10),
  (2302943, 15, 0),
  (2313170, 0, 0),
  (2317417, 0, 0),
  (2318299, 11, 36),
  (2320268, 13, 4),
  (2322489, 6, 68),
  (2323129, 13, 5),
  (2323630, 15, 0),
  (2326625, 9, 35),
  (2328336, 6, 56),
  (2328903, 10, 10),
  (2332273, 7, 35),
  (2332848, 14, 0),
  (2336028, 13, 34),
  (2336751, 0, 0),
  (2338554, 11, 29),
  (2342402, 7, 35),
  (2342989, 11, 42),
  (2343577, 8, 35),
  (2343606, 2, 48),
  (2344575, 14, 57),
  (2346266, 3, 4),
  (2349802, 12, 30),
  (2352877, 0, 36),
  (2364167, 14, 36),
  (2368814, 0, 36),
  (2369787, 12, 0),
  (2370081, 8, 35),
  (2370112, 3, 20),
  (2371883, 4, 19),
  (2372672, 14, 57),
  (2373132, 15, 35),
  (2375206, 6, 56),
  (2375971, 2, 21),
  (2383444, 5, 46),
  (2384383, 2, 18),
  (2386500, 15, 0),
  (2392014, 10, 33),
  (2392032, 13, 4),
  (2396701, 4, 40),
  (2401489, 9, 10),
  (2402706, 12, 19),
  (2404806, 9, 30),
  (2406479, 10, 19),
  (2406610, 14, 47),
  (2408042, 12, 19),
  (2410418, 2, 4),
  (2413116, 15, 0),
  (2418331, 9, 35),
  (2418873, 3, 4),
  (2419046, 7, 72),
  (2420233, 3, 5),
  (2421669, 9, 38),
  (2422259, 6, 34),
  (2423183, 12, 4),
  (2423384, 13, 0),
  (2424254, 15, 0),
  (2424800, 12, 45),
  (2426336, 9, 35),
  (2428235, 7, 35),
  (2431733, 8, 35),
  (2432659, 9, 12),
  (2436166, 12, 4),
  (2437494, 13, 4),
  (2444315, 15, 10),
  (2444721, 11, 19),
  (2445427, 8, 35),
  (2445939, 15, 0),
  (2446639, 4, 19),
  (2448466, 4, 5),
  (2448617, 2, 1),
  (2451227, 2, 42),
  (2451431, 14, 35),
  (2457426, 3, 4),
  (2458069, 1, 0),
  (2458172, 5, 33),
  (2463714, 10, 33),
  (2465820, 8, 35),
  (2465963, 7, 35),
  (2468497, 15, 0),
  (2470674, 4, 3),
  (2470735, 0, 0),
  (2471821, 9, 35),
  (2478161, 7, 34),
  (2481238, 14, 36),
  (2481997, 0, 36),
  (2482138, 2, 4),
  (2484600, 3, 17),
  (2485406, 3, 4),
  (2485536, 12, 4),
  (2487295, 9, 35),
  (2491571, 13, 4),
  (2492854, 6, 35),
  (2493858, 0, 57),
  (2496840, 8, 9),
  (2498629, 7, 35),
  (2501045, 14, 35),
  (2502144, 7, 56),
  (2502890, 7, 35),
  (2506117, 15, 0),
  (2507004, 3, 15),
  (2507366, 14, 36),
  (2512727, 6, 35),
  (2517236, 8, 6),
  (2517348, 8, 34),
  (2517684, 11, 4),
  (2528053, 9, 35),
  (2528831, 6, 35),
  (2529628, 7, 35),
  (2530537, 8, 35),
  (2531882, 3, 4),
  (2533323, 4, 48),
  (2535408, 12, 34),
  (2540401, 9, 35),
  (2542007, 7, 35),
  (2542455, 9, 35),
  (2548858, 0, 0),
  (2550919, 5, 14),
  (2552146, 5, 15),
  (2552998, 5, 29),
  (2553473, 6, 35),
  (2556609, 7, 56),
  (2558303, 6, 60),
  (2561206, 14, 20),
  (2563282, 12, 20),
  (2565310, 2, 4),
  (2565844, 3, 4),
  (2573611, 8, 35),
  (2576473, 6, 35),
  (2576544, 10, 42),
  (2576726, 9, 35),
  (2577649, 14, 0),
  (2581053, 14, 0),
  (2581943, 4, 19),
  (2583361, 2, 33),
  (2585986, 8, 34),
  (2593884, 6, 56),
  (2593955, 3, 16),
  (2598142, 12, 33),
  (2600372, 3, 4),
  (2602696, 0, 36),
  (2604171, 14, 19),
  (2608009, 15, 36),
  (2612751, 5, 19),
  (2614368, 14, 0),
  (2614627, 4, 15),
  (2616867, 11, 18),
  (2618997, 3, 36),
  (2625781, 12, 23),
  (2628445, 4, 19),
  (2629587, 10, 14),
  (2630246, 14, 0),
  (2640129, 3, 15),
  (2647258, 6, 35),
  (2649132, 6, 35),
  (2649947, 7, 73),
  (2650174, 14, 0),
  (2652209, 11, 19),
  (2652516, 15, 0),
  (2653624, 9, 35),
  (2656031, 12, 28),
  (2656047, 13, 4),
  (2656981, 8, 35),
  (2657958, 12, 4),
  (2658773, 9, 56),
  (2659968, 14, 0),
  (2660854, 0, 73),
  (2662454, 8, 57),
  (2662480, 7, 35),
  (2662616, 3, 4),
  (2665512, 11, 16),
  (2667875, 3, 0),
  (2668282, 5, 22),
  (2670662, 8, 35),
  (2671246, 7, 56),
  (2672767, 15, 0),
  (2672993, 14, 0),
  (2673768, 15, 68),
  (2676660, 11, 15),
  (2679679, 13, 4),
  (2680839, 6, 35),
  (2681704, 4, 19),
  (2682610, 8, 35),
  (2682730, 9, 72),
  (2683240, 15, 36),
  (2683945, 2, 0),
  (2686485, 2, 47),
  (2687971, 4, 19),
  (2688890, 10, 30),
  (2692752, 10, 16),
  (2697889, 2, 15),
  (2701492, 1, 36),
  (2703028, 13, 1),
  (2705817, 12, 19),
  (2706598, 13, 19),
  (2709626, 9, 56),
  (2710520, 7, 73),
  (2711740, 2, 19),
  (2714645, 9, 56),
  (2715950, 5, 42),
  (2721123, 6, 35),
  (2721252, 0, 0),
  (2722702, 11, 36),
  (2724391, 1, 0),
  (2728409, 14, 0),
  (2735177, 8, 35),
  (2737177, 3, 34),
  (2737383, 6, 35),
  (2737678, 13, 1),
  (2738828, 13, 0),
  (2740749, 8, 35),
  (2740852, 9, 67),
  (2747542, 13, 4),
  (2749760, 9, 56),
  (2750153, 14, 56),
  (2754280, 2, 4),
  (2755393, 8, 56),
  (2755783, 1, 0),
  (2757094, 8, 35),
  (2761072, 15, 57),
  (2766213, 15, 0),
  (2768212, 9, 67),
  (2771059, 13, 4),
  (2776579, 5, 19),
  (2776588, 8, 34),
  (2777146, 10, 19),
  (2777198, 6, 35),
  (2777494, 12, 23),
  (2780822, 13, 1),
  (2784055, 8, 35),
  (2791449, 13, 19),
  (2797050, 11, 10),
  (2797521, 6, 35),
  (2798145, 3, 23),
  (2801745, 6, 35),
  (2803519, 3, 4),
  (2803886, 12, 34),
  (2805561, 7, 56),
  (2805794, 9, 60),
  (2806379, 6, 35),
  (2810761, 7, 35),
  (2810979, 0, 0),
  (2811184, 10, 31),
  (2818655, 0, 57),
  (2819392, 14, 36),
  (2820230, 4, 19),
  (2820388, 4, 1),
  (2825077, 1, 61),
  (2826281, 4, 19),
  (2827562, 11, 33),
  (2830592, 3, 37),
  (2835128, 15, 1),
  (2837204, 8, 67),
  (2839898, 13, 4),
  (2841535, 0, 36),
  (2842560, 1, 0),
  (2844765, 3, 48),
  (2846206, 10, 35),
  (2846328, 0, 0),
  (2847112, 4, 33),
  (2848105, 11, 48),
  (2850677, 12, 19),
  (2851080, 15, 36),
  (2853483, 12, 4),
  (2859559, 2, 4),
  (2862864, 9, 35),
  (2862902, 12, 26),
  (2866411, 5, 43),
  (2866830, 13, 4),
  (2868121, 13, 36),
  (2870014, 1, 0),
  (2873172, 12, 16),
  (2873552, 9, 34),
  (2875890, 13, 4),
  (2884475, 15, 0),
  (2887659, 13, 43),
  (2891411, 15, 0),
  (2892070, 9, 35),
  (2893334, 0, 0),
  (2894476, 11, 29),
  (2895145, 11, 38),
  (2899571, 6, 56),
  (2900493, 14, 0),
  (2900598, 2, 36),
  (2904501, 5, 19),
  (2907437, 15, 0),
  (2911732, 5, 47),
  (2911959, 1, 0),
  (2915366, 5, 19),
  (2915576, 14, 0),
  (2916329, 9, 73),
  (2918640, 6, 35),
  (2925697, 7, 56),
  (2931701, 14, 57),
  (2931744, 11, 42),
  (2933953, 8, 67),
  (2939062, 4, 14),
  (2943556, 15, 36),
  (2946657, 8, 35),
  (2947904, 7, 35),
  (2948519, 8, 35),
  (2948821, 6, 35),
  (2948876, 15, 59),
  (2950882, 2, 16),
  (2952567, 6, 72),
  (2953584, 7, 35),
  (2955119, 14, 0),
  (2956007, 8, 50),
  (2957995, 12, 19),
  (2958839, 1, 0),
  (2959244, 10, 15),
  (2959755, 7, 35),
  (2962142, 5, 1),
  (2963780, 13, 0),
  (2965226, 3, 4),
  (2965587, 1, 32),
  (2966580, 6, 35),
  (2967121, 1, 36),
  (2968076, 11, 30),
  (2972342, 8, 56),
  (2973769, 4, 14),
  (2974574, 8, 35),
  (2978640, 14, 0),
  (2982486, 2, 8),
  (2983345, 3, 4),
  (2985928, 3, 19),
  (2989419, 4, 46),
  (2990293, 8, 35),
  (2991135, 2, 8),
  (2995359, 2, 4),
  (2995921, 7, 35),
  (2998867, 6, 23),
  (2999225, 8, 35),
  (2999237, 2, 19),
  (2999766, 5, 33),
  (3004455, 8, 35),
  (3007173, 4, 19),
  (3007361, 1, 5),
  (3010500, 11, 19),
  (3013430, 12, 4),
  (3014010, 5, 19),
  (3014051, 4, 6),
  (3016577, 0, 0),
  (3017271, 11, 48),
  (3022341, 10, 33),
  (3025478, 5, 21),
  (3027479, 1, 0),
  (3031108, 15, 0),
  (3033668, 2, 4),
  (3034720, 13, 0),
  (3036133, 0, 0),
  (3037192, 7, 35),
  (3040498, 2, 29),
  (3044000, 1, 65),
  (3044123, 11, 23),
  (3048352, 1, 35),
  (3049948, 10, 19),
  (3050735, 15, 36),
  (3051894, 14, 0),
  (3053541, 15, 36),
  (3055683, 9, 35),
  (3056521, 10, 19),
  (3060946, 11, 19),
  (3062401, 4, 33),
  (3064509, 8, 67),
  (3070155, 5, 15),
  (3070743, 15, 0),
  (3070882, 11, 15),
  (3074725, 13, 19),
  (3076000, 4, 33),
  (3076775, 4, 19),
  (3077175, 0, 36),
  (3077882, 0, 0),
  (3082964, 15, 57),
  (3084328, 10, 33),
  (3089879, 0, 0),
  (3091323, 10, 19),
  (3094958, 5, 19),
  (3099441, 1, 6),
  (3105173, 2, 4),
  (3113497, 14, 57),
  (3114749, 8, 56),
  (3114959, 7, 35),
  (3115051, 10, 15),
  (3115377, 10, 19),
  (3122411, 11, 47),
  (3122680, 2, 30),
  (3123138, 6, 56),
  (3123950, 10, 40),
  (3124572, 12, 43),
  (3124918, 10, 19),
  (3130994, 5, 16),
  (3131274, 1, 31),
  (3131697, 4, 19),
  (3132732, 10, 3),
  (3136182, 4, 19),
  (3140505, 2, 23),
  (3142047, 0, 73),
  (3145772, 8, 35),
  (3147446, 14, 57),
  (3147473, 10, 30),
  (3147899, 11, 15),
  (3149668, 11, 14),
  (3149849, 5, 22),
  (3154883, 1, 0),
  (3158132, 11, 12),
  (3159284, 9, 35),
  (3159428, 8, 35),
  (3160688, 4, 19),
  (3160743, 14, 53),
  (3161486, 12, 4),
  (3163698, 11, 19),
  (3163784, 3, 23),
  (3165414, 13, 19),
  (3169745, 4, 29),
  (3169902, 1, 37),
  (3171132, 7, 41),
  (3176687, 14, 0),
  (3176776, 6, 35),
  (3176981, 6, 69),
  (3178125, 14, 36),
  (3178693, 8, 35),
  (3180858, 4, 15),
  (3180939, 2, 0),
  (3181334, 11, 14),
  (3182694, 7, 35),
  (3186949, 13, 13),
  (3189527, 2, 4),
  (3191854, 8, 35),
  (3192573, 13, 42),
  (3194210, 1, 0),
  (3195091, 8, 30),
  (3202203, 6, 35),
  (3207062, 1, 0),
  (3208114, 12, 0),
  (3212336, 12, 1),
  (3225100, 13, 14),
  (3229371, 5, 15),
  (3232543, 11, 33),
  (3235707, 15, 36),
  (3235834, 6, 35),
  (3241459, 4, 5),
  (3245493, 11, 29),
  (3250395, 9, 35),
  (3253656, 8, 56),
  (3254730, 15, 0),
  (3255548, 15, 0),
  (3255553, 0, 0),
  (3256342, 3, 4),
  (3256610, 7, 35),
  (3259462, 4, 19),
  (3260620, 0, 0),
  (3262278, 14, 36),
  (3262657, 1, 0),
  (3265694, 12, 4),
  (3268553, 5, 48),
  (3270113, 12, 42),
  (3272553, 9, 35),
  (3274850, 0, 0),
  (3277504, 11, 30),
  (3279157, 10, 47),
  (3279758, 12, 33),
  (3279786, 10, 19),
  (3280883, 15, 0),
  (3281099, 7, 35),
  (3282372, 7, 35),
  (3282746, 15, 0),
  (3284055, 7, 35),
  (3287402, 1, 0),
  (3289604, 5, 10),
  (3290156, 14, 52),
  (3292296, 2, 19),
  (3294594, 5, 33),
  (3297800, 8, 35),
  (3299448, 15, 36),
  (3301775, 15, 0),
  (3302314, 6, 35),
  (3302983, 12, 4),
  (3304445, 8, 35),
  (3305146, 0, 36),
  (3307469, 9, 56),
  (3309076, 14, 0),
  (3310334, 7, 67),
  (3312687, 1, 64),
  (3312893, 3, 23),
  (3314416, 7, 56),
  (3317849, 8, 35),
  (3317994, 7, 35),
  (3319051, 12, 19),
  (3321251, 13, 4),
  (3321947, 9, 23),
  (3322091, 0, 0),
  (3324655, 6, 56),
  (3327574, 12, 20),
  (3333877, 9, 56),
  (3334882, 10, 19),
  (3336782, 3, 48),
  (3338815, 13, 44),
  (3341784, 6, 35),
  (3343481, 5, 19),
  (3343736, 1, 0),
  (3344578, 9, 56),
  (3345549, 8, 35),
  (3348633, 14, 57),
  (3352027, 13, 2),
  (3353453, 14, 0),
  (3354192, 4, 19),
  (3354885, 11, 19),
  (3356974, 12, 9),
  (3364623, 8, 35),
  (3364887, 9, 56),
  (3365660, 3, 33),
  (3365683, 7, 15),
  (3369989, 1, 0),
  (3379889, 14, 0),
  (3381007, 8, 56),
  (3381807, 10, 15),
  (3384273, 10, 33),
  (3384936, 13, 45),
  (3386483, 1, 64),
  (3386924, 11, 25),
  (3390178, 11, 22),
  (3392486, 0, 0),
  (3392895, 3, 19),
  (3393534, 8, 35),
  (3394712, 13, 4),
  (3402673, 7, 35),
  (3403549, 14, 0),
  (3404083, 0, 0),
  (3404473, 13, 0),
  (3405613, 1, 0),
  (3408548, 12, 4),
  (3412786, 4, 19),
  (3416278, 2, 15),
  (3418976, 3, 4),
  (3420340, 12, 0),
  (3422144, 3, 11),
  (3424876, 6, 23),
  (3427359, 12, 8),
  (3428607, 11, 30),
  (3435109, 15, 0),
  (3436534, 2, 4),
  (3437330, 13, 27),
  (3446088, 15, 36),
  (3450163, 15, 0),
  (3451753, 10, 15),
  (3456081, 0, 0),
  (3460144, 4, 10),
  (3461783, 9, 35),
  (3463266, 4, 30),
  (3468199, 12, 4),
  (3469870, 7, 35),
  (3470981, 7, 35),
  (3474994, 11, 28),
  (3477966, 7, 62),
  (3478927, 14, 0),
  (3479370, 11, 16),
  (3481894, 9, 35),
  (3484669, 8, 35),
  (3487731, 9, 35),
  (3488436, 12, 8),
  (3489243, 13, 30),
  (3490671, 0, 0),
  (3494190, 10, 16),
  (3494207, 2, 4),
  (3499013, 4, 19),
  (3501338, 3, 4),
  (3502845, 11, 0),
  (3503005, 7, 60),
  (3503707, 0, 0),
  (3504103, 11, 14),
  (3506319, 10, 3),
  (3508086, 5, 14),
  (3509094, 14, 19),
  (3510207, 5, 19),
  (3513639, 10, 48),
  (3519829, 13, 23),
  (3520083, 15, 36),
  (3522587, 1, 0),
  (3524165, 7, 35),
  (3525301, 3, 19),
  (3527381, 14, 0),
  (3530026, 11, 15),
  (3531810, 8, 56),
  (3533699, 1, 56),
  (3533951, 4, 29),
  (3540826, 6, 1),
  (3545571, 0, 56),
  (3546741, 0, 61),
  (3548538, 7, 35),
  (3548710, 4, 48),
  (3548813, 15, 49),
  (3550021, 9, 72),
  (3553277, 8, 35),
  (3556425, 10, 6),
  (3560271, 5, 13),
  (3560970, 13, 23),
  (3566118, 2, 0),
  (3567522, 9, 35),
  (3568016, 7, 56),
  (3568133, 14, 0),
  (3571139, 4, 19),
  (3575301, 7, 56),
  (3579376, 9, 34),
  (3581266, 3, 4),
  (3588449, 7, 56),
  (3590450, 3, 0),
  (3594442, 5, 16),
  (3594783, 11, 14),
  (3595770, 6, 56),
  (3596125, 13, 12),
  (3598830, 0, 52),
  (3599047, 0, 0),
  (3599400, 8, 35),
])
