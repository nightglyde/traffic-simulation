from util import *
schedule = deque([
  (304, 2, 4),
  (4363, 7, 0),
  (5142, 3, 3),
  (5962, 6, 7),
  (7083, 3, 3),
  (7425, 2, 0),
  (9322, 0, 2),
  (10790, 5, 7),
  (11758, 1, 0),
  (12248, 2, 7),
  (18989, 6, 0),
  (22250, 2, 3),
  (22950, 5, 3),
  (23118, 5, 5),
  (23614, 2, 5),
  (24986, 0, 3),
  (25885, 2, 7),
  (26672, 4, 6),
  (27719, 6, 0),
  (29685, 3, 3),
  (30521, 4, 6),
  (32263, 0, 0),
  (39821, 7, 0),
  (40497, 2, 7),
  (43756, 4, 5),
  (44834, 2, 2),
  (47249, 7, 7),
  (47497, 1, 3),
  (47705, 3, 6),
  (49159, 0, 1),
  (53365, 2, 7),
  (54023, 2, 3),
  (55141, 2, 3),
  (57724, 3, 5),
  (59026, 2, 7),
  (61106, 1, 0),
  (64014, 6, 3),
  (65701, 4, 3),
  (66778, 5, 3),
  (68472, 0, 7),
  (72140, 5, 3),
  (73003, 6, 0),
  (74895, 2, 3),
  (79033, 7, 0),
  (79706, 0, 2),
  (79753, 3, 7),
  (82133, 2, 2),
  (82591, 3, 4),
  (85912, 4, 6),
  (86896, 4, 3),
  (87341, 7, 4),
  (88587, 0, 7),
  (89775, 6, 0),
  (90617, 5, 3),
  (91928, 7, 7),
  (93088, 6, 6),
  (94235, 2, 3),
  (94657, 0, 7),
  (98052, 1, 4),
  (98395, 7, 4),
  (98837, 2, 6),
  (99239, 5, 2),
  (99891, 7, 7),
  (102167, 3, 4),
  (104468, 0, 0),
  (104513, 5, 3),
  (111993, 5, 3),
  (112019, 0, 0),
  (112698, 6, 0),
  (117158, 5, 3),
  (117181, 7, 4),
  (120237, 2, 2),
  (125474, 3, 3),
  (126673, 5, 5),
  (127323, 5, 3),
  (129947, 0, 4),
  (132485, 1, 7),
  (134507, 5, 3),
  (136244, 5, 2),
  (137685, 6, 0),
  (139311, 5, 6),
  (140216, 6, 0),
  (140258, 0, 0),
  (140460, 5, 6),
  (143908, 3, 3),
  (145981, 0, 0),
  (146365, 4, 3),
  (150319, 3, 3),
  (152128, 5, 7),
  (153661, 0, 3),
  (155253, 1, 5),
  (155299, 6, 3),
  (157025, 1, 7),
  (157885, 0, 0),
  (157988, 0, 0),
  (160887, 7, 7),
  (164138, 2, 3),
  (164489, 3, 7),
  (165470, 2, 6),
  (165887, 1, 3),
  (167354, 0, 3),
  (167930, 6, 0),
  (168628, 6, 4),
  (172426, 1, 3),
  (173614, 4, 7),
  (175408, 4, 0),
  (180719, 7, 0),
  (185283, 3, 3),
  (186357, 0, 0),
  (186461, 6, 4),
  (186744, 2, 4),
  (188342, 1, 4),
  (190948, 2, 6),
  (191230, 2, 7),
  (191837, 6, 0),
  (193774, 0, 0),
  (194069, 2, 3),
  (200290, 1, 6),
  (202838, 7, 0),
  (204018, 6, 7),
  (204840, 3, 2),
  (205506, 7, 1),
  (208406, 2, 3),
  (210669, 4, 0),
  (211403, 1, 7),
  (216424, 3, 6),
  (218764, 0, 1),
  (220248, 0, 7),
  (220375, 6, 0),
  (221645, 5, 2),
  (224138, 2, 7),
  (224963, 6, 0),
  (226613, 4, 3),
  (228285, 7, 6),
  (229737, 2, 6),
  (230696, 1, 7),
  (231217, 2, 3),
  (232796, 2, 5),
  (234272, 0, 1),
  (236876, 5, 2),
  (238378, 1, 0),
  (238805, 1, 7),
  (240977, 4, 0),
  (241141, 6, 0),
  (243021, 0, 0),
  (244787, 1, 0),
  (248336, 1, 7),
  (249626, 7, 1),
  (249934, 2, 3),
  (250144, 2, 7),
  (252792, 3, 3),
  (252959, 7, 7),
  (253049, 3, 3),
  (253423, 0, 0),
  (254113, 4, 2),
  (254477, 5, 4),
  (259603, 6, 2),
  (263069, 3, 3),
  (264916, 2, 3),
  (267526, 7, 0),
  (267604, 4, 2),
  (269269, 2, 2),
  (271666, 6, 0),
  (273125, 0, 3),
  (278988, 7, 0),
  (281153, 2, 1),
  (284695, 4, 5),
  (286821, 0, 0),
  (288132, 6, 0),
  (289449, 7, 4),
  (290832, 0, 0),
  (294818, 7, 0),
  (299246, 6, 6),
  (310046, 5, 2),
  (311797, 1, 1),
  (313531, 1, 3),
  (315042, 3, 3),
  (315656, 5, 3),
  (316216, 3, 3),
  (318558, 7, 0),
  (321941, 0, 3),
  (331582, 0, 2),
  (332629, 0, 4),
  (332840, 6, 7),
  (333219, 0, 0),
  (340073, 7, 4),
  (343819, 0, 0),
  (343925, 7, 0),
  (344528, 1, 3),
  (345761, 4, 3),
  (348221, 1, 2),
  (348966, 0, 2),
  (349930, 3, 6),
  (350026, 3, 3),
  (353633, 7, 0),
  (354121, 7, 0),
  (354158, 4, 7),
  (356885, 5, 0),
  (358612, 7, 7),
  (359218, 4, 5),
  (362841, 5, 7),
  (363977, 3, 3),
  (367086, 1, 0),
  (369120, 3, 3),
  (370993, 5, 1),
  (371222, 2, 5),
  (373202, 2, 3),
  (375927, 4, 0),
  (379985, 3, 6),
  (380072, 0, 4),
  (383762, 0, 0),
  (386015, 0, 4),
  (389116, 2, 3),
  (390128, 5, 2),
  (393543, 3, 5),
  (394764, 6, 5),
  (395110, 0, 0),
  (395213, 1, 7),
  (397420, 5, 2),
  (399821, 2, 3),
  (400951, 2, 2),
  (402561, 6, 6),
  (403567, 4, 3),
  (410908, 3, 3),
  (412719, 0, 5),
  (416312, 7, 0),
  (416666, 6, 0),
  (417118, 2, 6),
  (417192, 2, 3),
  (418738, 1, 4),
  (419222, 3, 6),
  (419627, 1, 1),
  (421124, 2, 0),
  (432655, 7, 0),
  (433477, 1, 3),
  (435270, 6, 0),
  (436450, 3, 3),
  (436944, 0, 0),
  (441593, 3, 7),
  (442408, 2, 3),
  (445598, 7, 0),
  (445631, 5, 4),
  (447080, 5, 3),
  (447096, 6, 7),
  (455734, 5, 2),
  (457778, 3, 7),
  (458783, 7, 0),
  (460487, 2, 7),
  (461405, 5, 7),
  (462210, 2, 3),
  (462293, 0, 0),
  (465319, 6, 7),
  (466493, 5, 7),
  (466786, 7, 0),
  (467053, 5, 6),
  (468537, 4, 7),
  (469643, 3, 3),
  (472612, 7, 2),
  (474023, 1, 0),
  (476644, 2, 6),
  (477099, 6, 0),
  (479088, 7, 1),
  (485240, 3, 3),
  (486216, 0, 1),
  (486876, 0, 2),
  (489063, 0, 2),
  (490624, 2, 3),
  (491129, 4, 7),
  (491689, 0, 3),
  (493636, 5, 3),
  (496704, 0, 6),
  (497464, 3, 2),
  (497788, 5, 3),
  (498440, 6, 0),
  (500122, 7, 0),
  (501041, 0, 0),
  (502737, 1, 0),
  (502771, 1, 1),
  (503747, 7, 7),
  (504918, 0, 5),
  (505409, 7, 7),
  (508492, 2, 1),
  (513667, 1, 0),
  (513708, 3, 2),
  (516367, 6, 3),
  (516929, 6, 0),
  (517977, 7, 0),
  (518213, 3, 1),
  (524086, 7, 0),
  (526425, 7, 7),
  (528697, 4, 7),
  (529520, 2, 3),
  (529917, 3, 3),
  (530344, 1, 0),
  (531357, 3, 7),
  (531506, 7, 7),
  (534497, 0, 2),
  (535941, 7, 7),
  (541414, 6, 0),
  (541474, 0, 0),
  (545092, 4, 3),
  (553070, 2, 3),
  (553070, 2, 6),
  (553157, 6, 4),
  (556585, 3, 7),
  (556871, 3, 3),
  (557964, 4, 3),
  (561002, 4, 7),
  (562026, 2, 2),
  (565815, 6, 0),
  (570111, 0, 0),
  (570564, 1, 0),
  (574902, 1, 0),
  (576486, 4, 3),
  (581716, 0, 4),
  (583084, 2, 3),
  (584094, 4, 3),
  (586013, 4, 3),
  (587865, 7, 0),
  (588259, 6, 4),
  (589135, 4, 3),
  (591742, 0, 4),
  (594877, 3, 0),
  (597759, 4, 7),
  (605351, 3, 3),
  (605861, 3, 3),
  (607609, 4, 2),
  (608491, 3, 4),
  (609019, 1, 3),
  (609417, 7, 5),
  (610468, 1, 3),
  (611299, 3, 3),
  (613974, 6, 3),
  (619481, 5, 3),
  (619837, 0, 0),
  (621689, 6, 7),
  (623259, 7, 0),
  (626818, 4, 3),
  (628418, 1, 3),
  (629822, 0, 0),
  (633660, 2, 0),
  (636874, 5, 6),
  (636895, 4, 3),
  (637100, 6, 7),
  (638081, 5, 7),
  (639083, 2, 7),
  (644251, 0, 4),
  (647604, 5, 3),
  (648132, 3, 3),
  (648949, 0, 3),
  (650788, 3, 6),
  (651885, 6, 3),
  (656182, 1, 4),
  (656313, 0, 4),
  (657010, 1, 3),
  (657545, 1, 0),
  (658689, 4, 7),
  (660114, 4, 6),
  (660741, 5, 6),
  (661052, 3, 3),
  (663296, 2, 3),
  (664432, 7, 7),
  (666693, 5, 1),
  (669920, 2, 2),
  (671434, 2, 5),
  (672315, 6, 0),
  (675598, 4, 7),
  (677975, 5, 3),
  (682274, 3, 3),
  (682764, 1, 4),
  (688556, 1, 4),
  (688821, 5, 6),
  (689073, 1, 6),
  (690155, 6, 7),
  (692799, 7, 1),
  (698713, 4, 3),
  (702444, 2, 0),
  (705301, 0, 5),
  (705838, 2, 1),
  (706468, 6, 3),
  (717810, 3, 2),
  (718707, 0, 3),
  (723527, 2, 7),
  (727525, 3, 4),
  (728078, 0, 0),
  (730555, 4, 1),
  (734354, 0, 0),
  (736475, 1, 7),
  (740617, 2, 3),
  (740984, 0, 3),
  (742992, 1, 0),
  (745318, 4, 3),
  (748124, 3, 5),
  (748416, 2, 3),
  (748733, 5, 3),
  (748885, 5, 2),
  (749789, 7, 7),
  (749894, 3, 4),
  (751778, 6, 4),
  (753583, 2, 2),
  (755476, 3, 3),
  (757471, 6, 3),
  (760252, 5, 4),
  (761480, 5, 2),
  (764665, 0, 1),
  (769917, 0, 7),
  (772848, 1, 0),
  (779069, 2, 3),
  (780175, 4, 3),
  (782222, 6, 0),
  (783661, 4, 2),
  (784740, 5, 6),
  (788742, 5, 3),
  (790653, 2, 7),
  (792800, 3, 5),
  (793373, 2, 1),
  (800632, 0, 1),
  (801009, 0, 0),
  (802459, 7, 5),
  (808562, 4, 3),
  (809109, 3, 3),
  (809148, 1, 0),
  (812348, 6, 0),
  (815434, 7, 7),
  (818495, 6, 4),
  (819221, 3, 1),
  (821278, 5, 7),
  (822260, 6, 0),
  (822436, 3, 7),
  (824114, 1, 0),
  (826397, 7, 0),
  (827559, 1, 0),
  (828978, 0, 6),
  (830614, 1, 0),
  (833075, 7, 0),
  (836159, 1, 0),
  (838911, 6, 4),
  (839980, 5, 3),
  (844872, 4, 7),
  (847809, 1, 4),
  (851443, 7, 4),
  (856795, 0, 0),
  (862820, 6, 0),
  (862974, 1, 3),
  (867136, 2, 2),
  (867525, 4, 3),
  (870070, 6, 0),
  (870325, 6, 0),
  (873234, 3, 3),
  (873821, 1, 0),
  (875404, 6, 0),
  (875907, 7, 4),
  (878143, 3, 3),
  (882055, 6, 2),
  (882633, 7, 0),
  (884588, 5, 2),
  (886840, 2, 6),
  (887067, 0, 3),
  (890185, 5, 5),
  (892044, 6, 1),
  (896780, 3, 6),
  (898937, 0, 0),
  (902786, 0, 1),
  (902880, 0, 4),
  (907403, 7, 3),
  (909534, 2, 3),
  (913967, 4, 3),
  (914245, 4, 3),
  (916498, 1, 2),
  (917533, 7, 0),
  (919732, 4, 3),
  (919863, 1, 0),
  (920637, 2, 3),
  (922050, 3, 3),
  (923265, 6, 0),
  (923413, 6, 0),
  (923536, 3, 3),
  (924366, 4, 3),
  (924990, 3, 3),
  (925142, 2, 7),
  (926075, 2, 5),
  (927251, 3, 2),
  (928802, 3, 3),
  (929387, 6, 4),
  (930784, 3, 3),
  (930836, 4, 2),
  (931079, 1, 6),
  (931330, 3, 3),
  (935226, 0, 4),
  (936762, 0, 1),
  (936945, 1, 0),
  (937565, 5, 3),
  (939291, 6, 1),
  (943983, 4, 2),
  (947539, 7, 0),
  (951089, 6, 3),
  (952719, 7, 5),
  (952912, 4, 3),
  (953851, 5, 2),
  (954577, 5, 2),
  (956251, 5, 3),
  (958444, 1, 3),
  (959247, 3, 3),
  (960618, 4, 2),
  (960900, 1, 0),
  (961521, 0, 0),
  (961941, 3, 2),
  (963604, 1, 7),
  (963724, 6, 0),
  (963727, 2, 3),
  (966055, 1, 4),
  (966675, 2, 1),
  (967660, 1, 4),
  (969597, 6, 0),
  (971880, 4, 3),
  (973026, 1, 7),
  (974441, 0, 7),
  (976254, 4, 2),
  (976256, 6, 0),
  (977784, 7, 3),
  (984504, 2, 5),
  (986835, 3, 1),
  (987518, 4, 1),
  (988820, 7, 4),
  (989066, 1, 0),
  (989521, 7, 7),
  (989869, 5, 6),
  (991070, 1, 7),
  (995318, 3, 2),
  (995929, 4, 6),
  (996121, 0, 3),
  (997689, 2, 7),
  (1001662, 0, 5),
  (1002227, 2, 3),
  (1006307, 2, 3),
  (1008696, 6, 4),
  (1009084, 6, 4),
  (1010452, 2, 4),
  (1014241, 7, 5),
  (1016809, 0, 0),
  (1020752, 5, 6),
  (1023397, 1, 7),
  (1026086, 0, 6),
  (1028415, 7, 0),
  (1029121, 7, 0),
  (1040573, 6, 7),
  (1040740, 3, 6),
  (1042315, 0, 0),
  (1042975, 3, 2),
  (1045704, 1, 6),
  (1045946, 4, 7),
  (1049416, 0, 0),
  (1054265, 3, 3),
  (1055377, 4, 4),
  (1055568, 1, 0),
  (1059148, 3, 3),
  (1060131, 1, 3),
  (1061257, 6, 5),
  (1061695, 1, 0),
  (1066238, 0, 7),
  (1067470, 0, 0),
  (1069220, 5, 7),
  (1070043, 0, 7),
  (1070909, 4, 3),
  (1071488, 5, 3),
  (1072673, 0, 0),
  (1075771, 2, 4),
  (1077023, 7, 4),
  (1077405, 4, 6),
  (1082116, 1, 6),
  (1086559, 3, 3),
  (1090303, 7, 5),
  (1091679, 2, 3),
  (1093612, 2, 4),
  (1094365, 1, 1),
  (1096746, 4, 3),
  (1099187, 5, 7),
  (1099498, 6, 2),
  (1101649, 4, 3),
  (1108563, 3, 3),
  (1110299, 0, 2),
  (1110379, 4, 3),
  (1115300, 0, 7),
  (1116735, 4, 3),
  (1118860, 0, 3),
  (1118898, 0, 0),
  (1121031, 0, 0),
  (1126999, 5, 3),
  (1129151, 6, 0),
  (1129457, 0, 0),
  (1132372, 4, 3),
  (1132963, 1, 0),
  (1134155, 7, 0),
  (1137718, 7, 7),
  (1138821, 3, 7),
  (1141994, 1, 0),
  (1143548, 1, 0),
  (1143591, 7, 4),
  (1147444, 5, 7),
  (1149143, 7, 0),
  (1150260, 3, 2),
  (1156951, 0, 3),
  (1161285, 7, 0),
  (1161809, 4, 1),
  (1161929, 6, 3),
  (1162804, 5, 3),
  (1164904, 3, 2),
  (1165416, 1, 5),
  (1165710, 6, 0),
  (1170592, 3, 3),
  (1171420, 0, 0),
  (1171881, 6, 0),
  (1173183, 3, 3),
  (1173753, 2, 2),
  (1174007, 3, 3),
  (1179448, 4, 3),
  (1180878, 5, 3),
  (1183669, 6, 0),
  (1185829, 3, 3),
  (1188494, 0, 3),
  (1192266, 7, 6),
  (1194397, 1, 3),
  (1197631, 5, 6),
  (1197663, 6, 0),
  (1198534, 7, 2),
  (1201158, 5, 3),
  (1203835, 2, 3),
  (1204462, 7, 4),
  (1205197, 6, 0),
  (1207711, 1, 0),
  (1208618, 5, 3),
  (1209018, 3, 3),
  (1212119, 2, 7),
  (1212477, 6, 4),
  (1213745, 3, 1),
  (1215274, 2, 3),
  (1219038, 6, 0),
  (1220689, 3, 2),
  (1222154, 5, 3),
  (1222171, 3, 6),
  (1222956, 5, 5),
  (1224031, 1, 0),
  (1224484, 1, 0),
  (1225034, 6, 2),
  (1226982, 2, 3),
  (1229236, 7, 0),
  (1231254, 6, 3),
  (1231471, 0, 5),
  (1231964, 1, 0),
  (1234253, 1, 2),
  (1235823, 1, 6),
  (1237193, 3, 3),
  (1238676, 2, 7),
  (1239815, 6, 0),
  (1242383, 3, 3),
  (1243684, 7, 0),
  (1244503, 4, 2),
  (1246904, 6, 4),
  (1247049, 2, 3),
  (1250057, 7, 1),
  (1250374, 2, 3),
  (1250960, 4, 6),
  (1251822, 1, 1),
  (1252305, 2, 6),
  (1258946, 2, 7),
  (1263637, 6, 0),
  (1264570, 4, 3),
  (1271123, 7, 0),
  (1272326, 0, 1),
  (1274283, 6, 5),
  (1275066, 7, 7),
  (1276842, 6, 0),
  (1278520, 3, 6),
  (1278970, 2, 3),
  (1279528, 4, 6),
  (1281039, 0, 0),
  (1283832, 4, 6),
  (1289846, 1, 1),
  (1290972, 3, 4),
  (1293217, 4, 2),
  (1293735, 2, 3),
  (1295172, 3, 5),
  (1295716, 3, 7),
  (1296992, 1, 0),
  (1302227, 7, 3),
  (1317182, 0, 2),
  (1317373, 0, 7),
  (1318279, 7, 0),
  (1322618, 3, 0),
  (1324810, 3, 7),
  (1326241, 2, 3),
  (1329329, 6, 5),
  (1330635, 7, 1),
  (1331050, 4, 6),
  (1332090, 3, 3),
  (1334111, 0, 0),
  (1337031, 4, 6),
  (1338219, 2, 3),
  (1338604, 6, 7),
  (1341042, 2, 3),
  (1343648, 7, 0),
  (1344092, 0, 0),
  (1344098, 7, 3),
  (1344804, 6, 0),
  (1346086, 1, 7),
  (1347888, 3, 7),
  (1349647, 3, 6),
  (1349711, 4, 5),
  (1354161, 2, 3),
  (1356346, 5, 3),
  (1362226, 7, 0),
  (1363238, 5, 3),
  (1365199, 7, 0),
  (1365202, 2, 6),
  (1367621, 5, 3),
  (1369323, 5, 3),
  (1372403, 6, 5),
  (1374408, 1, 7),
  (1378348, 7, 0),
  (1379721, 6, 7),
  (1380513, 0, 0),
  (1380877, 1, 3),
  (1381649, 1, 0),
  (1382229, 3, 2),
  (1383820, 6, 4),
  (1384274, 4, 1),
  (1385854, 6, 3),
  (1391746, 0, 6),
  (1392420, 0, 3),
  (1394174, 5, 3),
  (1396811, 4, 5),
  (1397663, 6, 1),
  (1399285, 1, 4),
  (1400386, 0, 7),
  (1406506, 2, 3),
  (1407835, 5, 6),
  (1409292, 0, 0),
  (1411265, 3, 6),
  (1418766, 2, 3),
  (1422316, 1, 7),
  (1423460, 3, 3),
  (1428419, 4, 7),
  (1428935, 2, 4),
  (1435366, 6, 3),
  (1435830, 0, 3),
  (1435852, 6, 3),
  (1439782, 6, 3),
  (1442767, 2, 7),
  (1442856, 3, 3),
  (1443639, 0, 3),
  (1444151, 4, 3),
  (1445428, 1, 6),
  (1445834, 1, 2),
  (1447665, 6, 0),
  (1448938, 0, 1),
  (1451588, 1, 1),
  (1454119, 6, 1),
  (1456027, 1, 0),
  (1457809, 0, 0),
  (1458292, 2, 0),
  (1462132, 2, 3),
  (1462604, 2, 3),
  (1464380, 7, 7),
  (1464635, 2, 3),
  (1466006, 0, 6),
  (1466722, 0, 0),
  (1468221, 0, 4),
  (1475655, 2, 3),
  (1477241, 1, 2),
  (1481192, 2, 3),
  (1482625, 1, 0),
  (1483454, 6, 0),
  (1484292, 4, 2),
  (1484988, 1, 2),
  (1486759, 7, 6),
  (1488146, 5, 7),
  (1488896, 7, 3),
  (1492617, 7, 0),
  (1493913, 6, 7),
  (1496074, 0, 0),
  (1496743, 4, 3),
  (1500366, 4, 5),
  (1501440, 0, 0),
  (1502756, 3, 3),
  (1505728, 6, 6),
  (1508152, 3, 5),
  (1509447, 4, 0),
  (1513155, 2, 3),
  (1513469, 5, 6),
  (1513662, 2, 5),
  (1514187, 7, 3),
  (1515588, 5, 3),
  (1521374, 1, 0),
  (1521458, 6, 6),
  (1523205, 1, 0),
  (1525739, 3, 3),
  (1528660, 5, 6),
  (1528699, 3, 3),
  (1531754, 7, 0),
  (1533610, 0, 0),
  (1536082, 1, 2),
  (1537461, 6, 4),
  (1537562, 4, 7),
  (1540127, 3, 3),
  (1542740, 7, 1),
  (1543732, 0, 0),
  (1546187, 2, 3),
  (1549127, 0, 2),
  (1549987, 7, 7),
  (1554271, 4, 2),
  (1554562, 3, 3),
  (1559515, 1, 0),
  (1559679, 3, 7),
  (1560532, 6, 7),
  (1561164, 7, 7),
  (1564088, 3, 3),
  (1568714, 1, 0),
  (1572231, 0, 7),
  (1577119, 7, 0),
  (1577716, 0, 6),
  (1579089, 3, 3),
  (1580494, 7, 0),
  (1582100, 1, 5),
  (1583445, 5, 3),
  (1584403, 5, 6),
  (1588754, 1, 7),
  (1589149, 7, 0),
  (1591247, 4, 3),
  (1591455, 7, 0),
  (1594463, 0, 3),
  (1595151, 2, 7),
  (1596884, 5, 3),
  (1598293, 0, 4),
  (1598884, 6, 4),
  (1599197, 3, 2),
  (1601373, 3, 2),
  (1602399, 6, 4),
  (1603458, 5, 1),
  (1604979, 7, 0),
  (1606510, 7, 3),
  (1607486, 4, 2),
  (1607617, 2, 7),
  (1613382, 7, 0),
  (1613590, 7, 7),
  (1615244, 1, 5),
  (1616591, 7, 6),
  (1617017, 0, 4),
  (1618298, 0, 0),
  (1618861, 7, 7),
  (1622902, 7, 5),
  (1623425, 2, 3),
  (1624934, 2, 3),
  (1624971, 7, 0),
  (1625814, 4, 3),
  (1630383, 7, 4),
  (1630436, 4, 7),
  (1630689, 1, 3),
  (1632273, 6, 7),
  (1632329, 1, 3),
  (1632756, 3, 6),
  (1632969, 3, 0),
  (1634712, 0, 7),
  (1634985, 2, 2),
  (1635476, 6, 4),
  (1639026, 7, 0),
  (1639162, 0, 0),
  (1639416, 3, 3),
  (1640250, 5, 3),
  (1641251, 6, 1),
  (1643054, 5, 4),
  (1643990, 4, 3),
  (1648553, 4, 2),
  (1654727, 0, 4),
  (1654740, 2, 6),
  (1660517, 6, 3),
  (1665661, 6, 0),
  (1665886, 1, 0),
  (1669703, 6, 6),
  (1671476, 2, 6),
  (1673627, 4, 3),
  (1682436, 3, 3),
  (1683857, 6, 2),
  (1686356, 3, 2),
  (1687350, 4, 5),
  (1694822, 6, 3),
  (1697641, 2, 7),
  (1698115, 4, 2),
  (1698295, 3, 0),
  (1699934, 7, 0),
  (1702866, 5, 6),
  (1704651, 6, 0),
  (1708515, 5, 0),
  (1712174, 2, 3),
  (1712572, 2, 3),
  (1713842, 5, 3),
  (1713850, 0, 3),
  (1714598, 0, 6),
  (1717440, 1, 0),
  (1717926, 2, 3),
  (1719011, 1, 0),
  (1721210, 2, 1),
  (1724936, 6, 0),
  (1726733, 2, 2),
  (1729015, 7, 7),
  (1736575, 4, 7),
  (1738104, 5, 2),
  (1741752, 0, 7),
  (1741858, 4, 3),
  (1749256, 1, 0),
  (1749968, 7, 3),
  (1756366, 0, 0),
  (1756812, 0, 0),
  (1762561, 3, 6),
  (1766516, 7, 0),
  (1767274, 0, 7),
  (1767471, 6, 4),
  (1769538, 0, 3),
  (1770019, 4, 3),
  (1772436, 3, 3),
  (1773409, 6, 0),
  (1774568, 0, 4),
  (1776004, 5, 1),
  (1780734, 3, 3),
  (1780746, 6, 7),
  (1784664, 5, 5),
  (1788709, 6, 3),
  (1788896, 5, 0),
  (1792532, 3, 1),
  (1793758, 4, 7),
  (1795897, 7, 7),
  (1796439, 0, 3),
  (1799529, 0, 0),
  (1799585, 1, 0),
  (1802346, 5, 3),
  (1803936, 6, 0),
  (1805823, 5, 3),
  (1810244, 3, 3),
  (1810409, 2, 6),
  (1811601, 6, 3),
  (1811738, 0, 3),
  (1812662, 2, 3),
  (1818609, 5, 0),
  (1818621, 4, 3),
  (1819609, 7, 4),
  (1822052, 2, 6),
  (1822779, 5, 0),
  (1826027, 1, 0),
  (1826941, 2, 2),
  (1828138, 4, 1),
  (1833341, 7, 2),
  (1836897, 1, 7),
  (1838863, 6, 0),
  (1840163, 1, 5),
  (1842224, 1, 7),
  (1849904, 1, 0),
  (1850041, 4, 5),
  (1850158, 6, 0),
  (1854100, 0, 0),
  (1859741, 1, 0),
  (1861629, 3, 5),
  (1861846, 4, 6),
  (1862634, 3, 6),
  (1864544, 2, 7),
  (1869957, 1, 5),
  (1871044, 6, 0),
  (1878082, 5, 3),
  (1878877, 0, 3),
  (1882529, 2, 7),
  (1883949, 1, 3),
  (1893322, 3, 7),
  (1895306, 4, 5),
  (1895986, 7, 7),
  (1897491, 1, 4),
  (1899577, 2, 1),
  (1902176, 7, 4),
  (1902442, 7, 0),
  (1904928, 4, 2),
  (1905193, 7, 5),
  (1906213, 5, 3),
  (1909350, 3, 5),
  (1912954, 2, 7),
  (1914946, 6, 3),
  (1915870, 2, 2),
  (1916043, 7, 0),
  (1917824, 0, 1),
  (1918387, 3, 7),
  (1920282, 5, 3),
  (1921014, 1, 4),
  (1921343, 2, 6),
  (1921932, 2, 7),
  (1929666, 6, 7),
  (1930065, 6, 1),
  (1932347, 0, 7),
  (1933064, 4, 3),
  (1939219, 3, 3),
  (1942851, 0, 0),
  (1943533, 1, 3),
  (1945101, 1, 0),
  (1945371, 4, 3),
  (1945945, 6, 0),
  (1946646, 2, 3),
  (1946663, 4, 3),
  (1947518, 5, 1),
  (1951631, 1, 0),
  (1955826, 7, 4),
  (1956338, 6, 0),
  (1956730, 3, 1),
  (1959673, 7, 0),
  (1959787, 7, 3),
  (1963132, 3, 3),
  (1963852, 6, 7),
  (1966531, 1, 0),
  (1969223, 5, 5),
  (1971441, 2, 5),
  (1971610, 5, 7),
  (1977540, 1, 0),
  (1977594, 2, 2),
  (1978563, 1, 3),
  (1982269, 1, 7),
  (1982565, 7, 4),
  (1983446, 7, 0),
  (1984359, 6, 4),
  (1985845, 6, 0),
  (1986540, 4, 6),
  (1988634, 0, 1),
  (1989287, 0, 4),
  (1990491, 2, 3),
  (1992017, 7, 0),
  (1993149, 7, 3),
  (1994428, 5, 3),
  (1996988, 6, 0),
  (1998362, 1, 5),
  (1999446, 3, 0),
  (1999852, 3, 1),
  (2000961, 0, 0),
  (2004691, 4, 2),
  (2006721, 5, 7),
  (2007417, 6, 7),
  (2007548, 1, 3),
  (2007721, 3, 4),
  (2007942, 6, 1),
  (2009539, 4, 6),
  (2009862, 3, 3),
  (2010623, 6, 1),
  (2010634, 6, 0),
  (2011252, 5, 2),
  (2013042, 7, 4),
  (2014115, 2, 2),
  (2018824, 0, 0),
  (2022763, 6, 3),
  (2024238, 6, 0),
  (2025343, 7, 0),
  (2029138, 3, 3),
  (2029193, 0, 5),
  (2030176, 6, 3),
  (2032052, 5, 6),
  (2034645, 3, 3),
  (2039046, 7, 3),
  (2044970, 6, 0),
  (2050729, 7, 3),
  (2051793, 7, 0),
  (2055772, 5, 6),
  (2057836, 1, 7),
  (2058395, 1, 0),
  (2060210, 1, 6),
  (2060255, 7, 0),
  (2060942, 6, 0),
  (2063069, 6, 0),
  (2063796, 5, 1),
  (2068163, 7, 6),
  (2068215, 1, 1),
  (2070261, 2, 2),
  (2072639, 4, 3),
  (2073485, 0, 4),
  (2074352, 0, 0),
  (2078579, 5, 3),
  (2084589, 4, 3),
  (2085622, 5, 7),
  (2085640, 2, 4),
  (2087041, 3, 7),
  (2088047, 7, 3),
  (2089666, 6, 0),
  (2090109, 1, 7),
  (2090356, 7, 4),
  (2091108, 1, 3),
  (2091528, 0, 7),
  (2092026, 0, 4),
  (2092414, 3, 7),
  (2094276, 4, 2),
  (2095134, 7, 0),
  (2096340, 6, 3),
  (2096790, 1, 7),
  (2098819, 5, 3),
  (2103186, 6, 0),
  (2104552, 5, 0),
  (2106726, 7, 0),
  (2107882, 7, 0),
  (2113365, 4, 3),
  (2114750, 4, 3),
  (2115983, 2, 3),
  (2121155, 6, 0),
  (2122426, 6, 0),
  (2122946, 3, 3),
  (2125113, 4, 4),
  (2127311, 3, 3),
  (2132035, 7, 4),
  (2134580, 5, 2),
  (2135922, 0, 0),
  (2137752, 0, 4),
  (2138398, 1, 5),
  (2140722, 4, 2),
  (2140731, 4, 6),
  (2141028, 2, 3),
  (2143766, 2, 3),
  (2144641, 1, 0),
  (2145833, 1, 2),
  (2154074, 3, 3),
  (2154839, 6, 3),
  (2155263, 7, 0),
  (2157568, 7, 0),
  (2160423, 0, 0),
  (2162552, 6, 7),
  (2167209, 0, 4),
  (2168308, 2, 4),
  (2170355, 3, 2),
  (2171654, 7, 0),
  (2172584, 2, 3),
  (2177492, 3, 6),
  (2179277, 3, 3),
  (2179999, 7, 3),
  (2182544, 2, 7),
  (2186035, 7, 0),
  (2188523, 0, 0),
  (2188894, 0, 0),
  (2189132, 7, 7),
  (2192578, 7, 0),
  (2196930, 5, 5),
  (2199948, 3, 6),
  (2201121, 0, 6),
  (2203088, 3, 2),
  (2209970, 3, 2),
  (2211470, 5, 2),
  (2211570, 1, 4),
  (2212714, 7, 2),
  (2214015, 7, 0),
  (2214315, 4, 3),
  (2215134, 4, 3),
  (2217992, 7, 2),
  (2218048, 3, 3),
  (2220554, 5, 2),
  (2221661, 6, 0),
  (2223805, 1, 0),
  (2226859, 5, 3),
  (2228387, 7, 0),
  (2229072, 7, 3),
  (2229340, 6, 0),
  (2229782, 4, 7),
  (2230923, 1, 0),
  (2232476, 5, 7),
  (2234483, 6, 0),
  (2236777, 5, 3),
  (2239322, 2, 3),
  (2242474, 7, 7),
  (2243682, 3, 6),
  (2250449, 7, 7),
  (2251669, 5, 2),
  (2253249, 4, 4),
  (2254889, 3, 3),
  (2256687, 7, 7),
  (2259099, 1, 3),
  (2263386, 2, 6),
  (2263664, 2, 1),
  (2267293, 6, 0),
  (2270509, 1, 7),
  (2270809, 5, 3),
  (2271559, 2, 3),
  (2274250, 1, 0),
  (2274317, 0, 4),
  (2275464, 7, 0),
  (2279091, 2, 0),
  (2283329, 7, 0),
  (2285245, 6, 0),
  (2285405, 4, 2),
  (2286721, 1, 3),
  (2288255, 0, 2),
  (2290149, 7, 0),
  (2291778, 4, 7),
  (2293080, 7, 0),
  (2294622, 7, 0),
  (2299583, 4, 3),
  (2302884, 2, 6),
  (2302917, 4, 7),
  (2305793, 0, 4),
  (2309086, 6, 5),
  (2309213, 5, 3),
  (2310497, 5, 3),
  (2310551, 0, 4),
  (2311793, 6, 3),
  (2313310, 2, 4),
  (2314696, 0, 5),
  (2318614, 4, 0),
  (2320229, 6, 1),
  (2321205, 1, 7),
  (2322943, 0, 4),
  (2326456, 4, 0),
  (2328924, 2, 6),
  (2332311, 3, 2),
  (2334374, 3, 6),
  (2335518, 7, 7),
  (2335986, 0, 0),
  (2338909, 7, 3),
  (2342167, 0, 7),
  (2343384, 2, 3),
  (2343652, 7, 3),
  (2344777, 1, 0),
  (2344876, 4, 2),
  (2350146, 4, 7),
  (2353199, 4, 3),
  (2359685, 0, 0),
  (2359981, 0, 4),
  (2360416, 0, 7),
  (2362759, 7, 7),
  (2364790, 1, 0),
  (2365489, 7, 5),
  (2368440, 2, 3),
  (2370701, 7, 4),
  (2373032, 6, 7),
  (2373809, 5, 2),
  (2374343, 7, 0),
  (2375220, 4, 2),
  (2376807, 7, 4),
  (2380136, 1, 0),
  (2385270, 4, 5),
  (2386246, 7, 0),
  (2387908, 5, 3),
  (2391070, 1, 0),
  (2397502, 7, 0),
  (2397761, 5, 2),
  (2399503, 2, 7),
  (2399782, 5, 7),
  (2401865, 2, 3),
  (2413951, 6, 7),
  (2416101, 0, 7),
  (2424222, 0, 3),
  (2424713, 5, 3),
  (2425257, 5, 5),
  (2427767, 1, 0),
  (2428676, 7, 7),
  (2429279, 1, 0),
  (2432577, 2, 3),
  (2437262, 7, 3),
  (2437443, 7, 7),
  (2437650, 2, 4),
  (2438442, 6, 5),
  (2441097, 1, 0),
  (2441645, 1, 7),
  (2442569, 0, 0),
  (2445226, 3, 3),
  (2450342, 1, 7),
  (2452577, 5, 2),
  (2453164, 7, 0),
  (2456119, 0, 2),
  (2456859, 6, 1),
  (2459129, 0, 4),
  (2459374, 5, 5),
  (2460178, 4, 3),
  (2462070, 6, 7),
  (2465364, 6, 3),
  (2468148, 4, 3),
  (2471028, 5, 3),
  (2472311, 5, 7),
  (2474024, 0, 1),
  (2482059, 7, 0),
  (2483256, 7, 0),
  (2483379, 1, 2),
  (2487034, 6, 0),
  (2488400, 1, 3),
  (2490673, 7, 0),
  (2492727, 6, 7),
  (2493087, 3, 3),
  (2493521, 5, 2),
  (2493895, 5, 7),
  (2495314, 0, 7),
  (2504370, 1, 3),
  (2507786, 5, 3),
  (2509342, 7, 6),
  (2509768, 1, 0),
  (2510749, 3, 2),
  (2511668, 3, 3),
  (2513523, 4, 5),
  (2513672, 4, 6),
  (2514917, 1, 7),
  (2518123, 7, 0),
  (2521025, 2, 3),
  (2522351, 4, 6),
  (2522434, 3, 2),
  (2525901, 2, 3),
  (2526036, 0, 0),
  (2530073, 0, 1),
  (2531234, 3, 2),
  (2533414, 1, 7),
  (2535062, 5, 4),
  (2536339, 2, 2),
  (2539783, 6, 0),
  (2542093, 2, 6),
  (2542469, 0, 2),
  (2546716, 0, 4),
  (2549691, 2, 2),
  (2551622, 1, 2),
  (2553973, 1, 4),
  (2554347, 5, 6),
  (2557232, 2, 7),
  (2564224, 5, 2),
  (2564397, 6, 1),
  (2564972, 7, 1),
  (2566709, 6, 0),
  (2567876, 4, 3),
  (2570791, 2, 7),
  (2574443, 1, 3),
  (2575065, 5, 6),
  (2575584, 2, 4),
  (2576419, 0, 3),
  (2577277, 1, 7),
  (2578779, 1, 7),
  (2580383, 3, 7),
  (2580642, 4, 7),
  (2587362, 5, 3),
  (2590670, 1, 4),
  (2591481, 0, 7),
  (2591905, 2, 3),
  (2592660, 5, 2),
  (2595122, 2, 6),
  (2599471, 3, 5),
  (2600685, 7, 3),
  (2602134, 1, 3),
  (2602750, 4, 6),
  (2609644, 0, 2),
  (2610724, 6, 4),
  (2611510, 0, 0),
  (2612706, 7, 0),
  (2614743, 0, 7),
  (2619957, 2, 4),
  (2620214, 5, 1),
  (2623569, 7, 0),
  (2627440, 3, 5),
  (2628707, 6, 1),
  (2631773, 6, 6),
  (2633516, 1, 0),
  (2637638, 4, 2),
  (2643271, 3, 2),
  (2646331, 4, 3),
  (2646541, 0, 0),
  (2647753, 1, 4),
  (2648409, 0, 7),
  (2648512, 0, 4),
  (2650986, 6, 7),
  (2651162, 5, 7),
  (2653068, 7, 5),
  (2654982, 3, 3),
  (2656116, 1, 3),
  (2658360, 1, 7),
  (2660676, 5, 4),
  (2664871, 7, 7),
  (2667236, 6, 7),
  (2667466, 2, 3),
  (2671731, 4, 2),
  (2673651, 5, 3),
  (2677090, 7, 7),
  (2679737, 7, 4),
  (2680843, 0, 0),
  (2682433, 6, 0),
  (2683510, 4, 2),
  (2684543, 3, 0),
  (2686922, 4, 7),
  (2687119, 1, 0),
  (2688555, 4, 3),
  (2688862, 1, 4),
  (2693740, 3, 2),
  (2693793, 2, 6),
  (2697819, 5, 7),
  (2705921, 6, 7),
  (2706673, 0, 3),
  (2709722, 5, 2),
  (2710389, 7, 0),
  (2711877, 0, 5),
  (2714816, 2, 5),
  (2714949, 0, 6),
  (2715580, 4, 3),
  (2718954, 1, 3),
  (2719119, 3, 7),
  (2719791, 4, 0),
  (2721408, 1, 3),
  (2722280, 0, 3),
  (2722702, 7, 3),
  (2728871, 5, 3),
  (2731466, 0, 6),
  (2735273, 6, 3),
  (2736960, 6, 3),
  (2737186, 0, 2),
  (2738893, 3, 1),
  (2741435, 2, 4),
  (2741759, 2, 3),
  (2743171, 2, 6),
  (2747751, 6, 1),
  (2747898, 4, 2),
  (2748239, 1, 0),
  (2749209, 6, 4),
  (2751600, 0, 4),
  (2764127, 0, 0),
  (2764456, 3, 3),
  (2765931, 2, 3),
  (2769199, 5, 6),
  (2772128, 7, 0),
  (2779845, 1, 0),
  (2782158, 3, 2),
  (2782969, 0, 0),
  (2791763, 1, 0),
  (2794394, 2, 3),
  (2796546, 3, 2),
  (2796619, 7, 5),
  (2797939, 6, 0),
  (2798694, 7, 0),
  (2798699, 1, 0),
  (2798939, 1, 7),
  (2802989, 3, 5),
  (2804031, 4, 2),
  (2805417, 6, 0),
  (2808827, 2, 3),
  (2809761, 2, 3),
  (2811361, 0, 0),
  (2811521, 4, 6),
  (2821056, 7, 7),
  (2821211, 4, 4),
  (2822955, 0, 4),
  (2823946, 4, 6),
  (2825563, 0, 4),
  (2828385, 4, 4),
  (2828638, 6, 4),
  (2832722, 2, 6),
  (2833715, 2, 3),
  (2834371, 0, 0),
  (2836910, 3, 3),
  (2837625, 1, 0),
  (2841137, 4, 7),
  (2841731, 1, 0),
  (2841849, 7, 2),
  (2842193, 7, 4),
  (2845426, 6, 7),
  (2847291, 3, 1),
  (2852258, 3, 3),
  (2852624, 1, 1),
  (2854115, 6, 0),
  (2859049, 5, 7),
  (2860749, 6, 0),
  (2863056, 4, 6),
  (2864221, 6, 3),
  (2865829, 2, 3),
  (2865891, 1, 3),
  (2873368, 7, 5),
  (2875029, 6, 4),
  (2875693, 4, 6),
  (2875903, 5, 7),
  (2876573, 3, 3),
  (2877039, 1, 0),
  (2877475, 0, 0),
  (2881453, 4, 7),
  (2882895, 0, 0),
  (2883411, 0, 3),
  (2888454, 3, 3),
  (2889656, 0, 0),
  (2890637, 0, 0),
  (2891374, 1, 4),
  (2893059, 4, 3),
  (2893709, 2, 2),
  (2893825, 1, 0),
  (2897803, 6, 4),
  (2899171, 3, 2),
  (2901331, 5, 5),
  (2901783, 3, 3),
  (2902315, 7, 0),
  (2902609, 5, 0),
  (2914267, 3, 7),
  (2914492, 6, 4),
  (2917123, 6, 5),
  (2921384, 3, 3),
  (2926141, 3, 2),
  (2927403, 2, 3),
  (2929117, 0, 4),
  (2929740, 1, 0),
  (2933324, 6, 0),
  (2935153, 0, 0),
  (2941182, 6, 0),
  (2948246, 7, 3),
  (2954710, 5, 6),
  (2960612, 2, 3),
  (2960865, 5, 2),
  (2962805, 5, 2),
  (2963748, 4, 3),
  (2964579, 6, 0),
  (2964734, 4, 4),
  (2965051, 2, 3),
  (2965943, 2, 3),
  (2966933, 4, 3),
  (2968157, 1, 4),
  (2968838, 0, 4),
  (2969177, 0, 0),
  (2969526, 6, 0),
  (2969710, 4, 2),
  (2974635, 6, 3),
  (2976567, 7, 0),
  (2976727, 6, 6),
  (2977856, 6, 0),
  (2979172, 0, 3),
  (2980237, 6, 0),
  (2981725, 1, 7),
  (2985227, 1, 0),
  (2987250, 2, 2),
  (2988058, 7, 4),
  (2989529, 3, 5),
  (2993148, 1, 7),
  (2993394, 1, 3),
  (2994610, 7, 0),
  (2997495, 1, 0),
  (2999408, 2, 3),
  (2999742, 1, 4),
  (3000450, 4, 2),
  (3001420, 2, 3),
  (3003591, 6, 3),
  (3003869, 0, 6),
  (3006212, 7, 0),
  (3010124, 5, 3),
  (3012159, 1, 0),
  (3013019, 2, 3),
  (3013048, 2, 3),
  (3016218, 6, 0),
  (3016679, 5, 2),
  (3018908, 6, 0),
  (3019424, 6, 0),
  (3021245, 3, 7),
  (3021292, 3, 1),
  (3024604, 7, 0),
  (3025328, 5, 3),
  (3025608, 0, 0),
  (3027351, 4, 2),
  (3028961, 4, 6),
  (3032459, 4, 7),
  (3032794, 3, 6),
  (3033701, 5, 3),
  (3034668, 3, 3),
  (3038351, 5, 3),
  (3038513, 7, 0),
  (3039553, 6, 7),
  (3039870, 6, 4),
  (3040993, 2, 3),
  (3041140, 1, 7),
  (3042616, 4, 2),
  (3048955, 2, 4),
  (3050840, 1, 0),
  (3051614, 6, 4),
  (3054879, 1, 0),
  (3055372, 2, 3),
  (3056436, 0, 5),
  (3057207, 1, 2),
  (3057541, 3, 7),
  (3060221, 4, 2),
  (3065426, 4, 3),
  (3067796, 7, 0),
  (3072749, 4, 4),
  (3074204, 6, 4),
  (3074419, 3, 3),
  (3076015, 0, 0),
  (3077453, 7, 2),
  (3077482, 0, 0),
  (3078850, 5, 3),
  (3081794, 5, 4),
  (3085509, 0, 5),
  (3087315, 2, 3),
  (3088577, 6, 1),
  (3089364, 3, 2),
  (3090345, 6, 0),
  (3090630, 3, 3),
  (3093238, 2, 3),
  (3093379, 5, 5),
  (3093831, 6, 0),
  (3096299, 7, 7),
  (3101024, 6, 1),
  (3106106, 4, 6),
  (3110027, 6, 4),
  (3117874, 0, 0),
  (3118706, 3, 3),
  (3120662, 0, 7),
  (3123649, 4, 6),
  (3127394, 7, 2),
  (3127786, 0, 3),
  (3129311, 2, 0),
  (3132506, 5, 3),
  (3134927, 4, 3),
  (3136621, 6, 3),
  (3141236, 0, 0),
  (3141666, 0, 4),
  (3143053, 7, 3),
  (3143309, 2, 4),
  (3145565, 5, 4),
  (3146994, 6, 2),
  (3147716, 3, 6),
  (3153999, 0, 0),
  (3158745, 7, 3),
  (3163016, 3, 6),
  (3166317, 3, 7),
  (3170139, 4, 2),
  (3174902, 6, 0),
  (3176879, 5, 3),
  (3180451, 4, 7),
  (3184693, 6, 0),
  (3185069, 2, 2),
  (3185106, 2, 6),
  (3188256, 3, 7),
  (3189637, 0, 0),
  (3189733, 1, 0),
  (3189973, 7, 0),
  (3190041, 4, 3),
  (3190350, 1, 0),
  (3204627, 4, 6),
  (3209395, 1, 0),
  (3211826, 7, 4),
  (3212209, 1, 0),
  (3213258, 0, 5),
  (3213794, 6, 7),
  (3214221, 5, 3),
  (3215668, 4, 1),
  (3216850, 5, 3),
  (3219360, 6, 0),
  (3221630, 1, 2),
  (3222062, 5, 5),
  (3224612, 4, 3),
  (3228120, 6, 0),
  (3228435, 4, 0),
  (3229548, 7, 0),
  (3230844, 0, 4),
  (3232240, 3, 6),
  (3232759, 0, 0),
  (3234357, 3, 3),
  (3242422, 4, 2),
  (3245751, 7, 4),
  (3249486, 6, 0),
  (3250448, 5, 3),
  (3251902, 1, 0),
  (3253419, 1, 0),
  (3253514, 1, 0),
  (3254338, 5, 3),
  (3256968, 4, 4),
  (3257228, 2, 4),
  (3258854, 3, 3),
  (3260690, 0, 7),
  (3261341, 3, 0),
  (3261844, 2, 3),
  (3262396, 6, 1),
  (3263779, 4, 3),
  (3267040, 1, 0),
  (3267698, 2, 3),
  (3268767, 2, 3),
  (3272804, 6, 2),
  (3276289, 7, 7),
  (3279779, 3, 3),
  (3281246, 6, 5),
  (3282311, 5, 2),
  (3284256, 7, 3),
  (3284413, 3, 4),
  (3284475, 6, 0),
  (3285424, 1, 0),
  (3286267, 5, 7),
  (3289037, 4, 3),
  (3296761, 1, 3),
  (3299000, 0, 7),
  (3300958, 0, 4),
  (3302250, 3, 1),
  (3303520, 3, 3),
  (3308245, 3, 0),
  (3311896, 0, 4),
  (3312602, 6, 0),
  (3316748, 5, 3),
  (3316772, 6, 4),
  (3316948, 1, 0),
  (3318309, 1, 5),
  (3319464, 6, 3),
  (3324840, 6, 0),
  (3325273, 6, 7),
  (3327978, 7, 0),
  (3329197, 4, 6),
  (3333630, 6, 3),
  (3334842, 4, 3),
  (3337959, 4, 3),
  (3338548, 2, 3),
  (3339277, 2, 5),
  (3340376, 3, 3),
  (3340562, 6, 7),
  (3341490, 0, 0),
  (3342705, 4, 7),
  (3343780, 1, 0),
  (3344430, 4, 4),
  (3350087, 7, 3),
  (3351421, 2, 3),
  (3351741, 3, 2),
  (3352955, 4, 3),
  (3353657, 2, 3),
  (3354595, 5, 3),
  (3357727, 6, 4),
  (3359974, 2, 3),
  (3360408, 6, 1),
  (3365747, 0, 0),
  (3367673, 1, 1),
  (3370398, 5, 3),
  (3370451, 0, 4),
  (3373711, 7, 0),
  (3375513, 0, 2),
  (3379692, 2, 3),
  (3384854, 2, 3),
  (3386004, 0, 3),
  (3387517, 6, 0),
  (3390416, 0, 0),
  (3391127, 2, 7),
  (3391631, 4, 1),
  (3393223, 6, 0),
  (3395035, 4, 3),
  (3397020, 5, 3),
  (3398593, 2, 3),
  (3398697, 4, 7),
  (3399434, 3, 2),
  (3403083, 7, 0),
  (3406379, 5, 0),
  (3406502, 7, 2),
  (3407838, 6, 7),
  (3407905, 6, 0),
  (3409139, 1, 0),
  (3411517, 7, 0),
  (3414051, 4, 2),
  (3419168, 6, 1),
  (3421281, 2, 3),
  (3424359, 6, 6),
  (3433967, 1, 0),
  (3436364, 5, 6),
  (3439212, 5, 4),
  (3439231, 1, 0),
  (3444292, 4, 3),
  (3445613, 6, 6),
  (3457444, 5, 7),
  (3461257, 0, 3),
  (3470563, 0, 3),
  (3471067, 6, 0),
  (3472779, 3, 5),
  (3474848, 2, 3),
  (3476051, 3, 3),
  (3485695, 1, 4),
  (3485964, 4, 3),
  (3488133, 1, 3),
  (3489017, 2, 3),
  (3489273, 2, 7),
  (3498136, 6, 6),
  (3501313, 0, 5),
  (3501481, 5, 3),
  (3504557, 3, 6),
  (3505263, 1, 4),
  (3506352, 6, 1),
  (3508151, 0, 0),
  (3512403, 4, 3),
  (3513835, 3, 6),
  (3514448, 2, 2),
  (3515613, 7, 0),
  (3516259, 2, 7),
  (3518294, 4, 0),
  (3519587, 3, 1),
  (3523340, 7, 0),
  (3528027, 1, 7),
  (3530431, 0, 0),
  (3530549, 3, 7),
  (3530959, 0, 3),
  (3538199, 4, 6),
  (3538675, 3, 6),
  (3541606, 7, 0),
  (3542716, 0, 4),
  (3543203, 4, 7),
  (3545386, 1, 3),
  (3547678, 4, 3),
  (3553288, 4, 3),
  (3553609, 2, 3),
  (3554436, 0, 3),
  (3554447, 2, 7),
  (3557116, 1, 4),
  (3559155, 3, 7),
  (3559785, 2, 2),
  (3561156, 0, 4),
  (3567816, 5, 3),
  (3568885, 0, 3),
  (3573254, 5, 3),
  (3573898, 1, 4),
  (3584790, 4, 7),
  (3588580, 5, 2),
  (3588622, 3, 7),
  (3590993, 3, 1),
  (3591068, 7, 0),
])
