from src.util import *
schedule = deque([
  (2721, 0, 0),
  (2880, 0, 0),
  (4820, 3, 7),
  (7650, 6, 3),
  (9066, 1, 7),
  (10424, 0, 0),
  (13341, 2, 7),
  (15791, 5, 7),
  (15911, 0, 7),
  (20201, 6, 3),
  (21274, 2, 3),
  (24032, 5, 3),
  (26313, 4, 4),
  (27717, 0, 1),
  (29412, 7, 7),
  (30791, 1, 0),
  (34100, 4, 7),
  (36023, 2, 3),
  (36449, 7, 3),
  (41329, 7, 7),
  (45576, 1, 4),
  (51504, 7, 4),
  (51650, 4, 3),
  (55080, 6, 0),
  (56354, 7, 0),
  (57640, 3, 5),
  (58966, 1, 0),
  (65214, 3, 3),
  (65973, 6, 0),
  (67986, 7, 0),
  (69499, 2, 3),
  (71705, 3, 6),
  (73135, 3, 7),
  (74805, 1, 0),
  (78220, 3, 7),
  (80176, 2, 3),
  (80282, 6, 3),
  (85865, 2, 3),
  (85946, 1, 2),
  (86435, 2, 6),
  (89460, 7, 5),
  (92745, 7, 0),
  (96558, 1, 3),
  (99665, 2, 3),
  (100203, 5, 6),
  (100634, 2, 6),
  (101198, 0, 6),
  (102565, 0, 4),
  (102776, 3, 3),
  (102874, 5, 7),
  (103854, 0, 0),
  (104974, 0, 3),
  (106624, 2, 3),
  (107503, 5, 7),
  (107620, 4, 2),
  (115352, 6, 0),
  (120950, 1, 4),
  (121960, 1, 0),
  (122589, 4, 2),
  (123148, 5, 5),
  (126354, 0, 3),
  (126383, 6, 7),
  (126920, 4, 3),
  (127775, 2, 3),
  (130568, 6, 4),
  (130678, 5, 2),
  (135918, 6, 3),
  (136104, 1, 3),
  (136121, 2, 3),
  (136665, 4, 7),
  (145466, 4, 3),
  (145605, 0, 1),
  (148128, 1, 4),
  (148133, 3, 7),
  (155059, 5, 6),
  (156153, 1, 7),
  (156759, 6, 3),
  (157151, 4, 7),
  (158440, 2, 7),
  (163933, 3, 7),
  (164441, 6, 0),
  (166953, 5, 3),
  (171580, 5, 6),
  (172577, 2, 3),
  (176076, 7, 6),
  (180215, 2, 7),
  (182656, 6, 5),
  (183311, 3, 2),
  (183496, 7, 0),
  (185215, 2, 6),
  (186247, 3, 1),
  (187576, 3, 3),
  (187814, 2, 3),
  (188694, 4, 0),
  (190265, 1, 3),
  (196682, 7, 6),
  (198139, 5, 3),
  (203262, 1, 0),
  (203799, 6, 0),
  (204951, 5, 3),
  (206699, 0, 4),
  (207225, 5, 6),
  (209199, 4, 3),
  (209581, 0, 7),
  (211195, 1, 0),
  (212494, 2, 3),
  (212792, 0, 0),
  (216802, 7, 0),
  (220704, 3, 3),
  (225067, 6, 4),
  (225427, 5, 5),
  (225969, 7, 4),
  (227905, 1, 4),
  (234438, 4, 7),
  (236763, 3, 7),
  (237336, 4, 2),
  (237515, 1, 1),
  (245162, 6, 1),
  (245990, 2, 3),
  (247310, 4, 7),
  (248816, 5, 6),
  (251926, 1, 0),
  (251987, 2, 3),
  (253349, 4, 2),
  (255993, 2, 2),
  (259870, 6, 0),
  (262726, 1, 0),
  (266036, 5, 2),
  (266870, 5, 2),
  (267764, 1, 7),
  (270675, 1, 3),
  (270912, 0, 0),
  (272315, 2, 7),
  (273639, 0, 0),
  (274397, 4, 3),
  (274957, 1, 4),
  (276263, 2, 3),
  (276422, 5, 2),
  (279238, 4, 6),
  (279563, 2, 3),
  (285826, 2, 2),
  (286447, 3, 3),
  (289962, 2, 3),
  (290749, 2, 3),
  (291549, 1, 3),
  (293693, 6, 0),
  (295335, 7, 7),
  (296145, 1, 0),
  (296948, 1, 7),
  (299588, 2, 6),
  (301257, 7, 4),
  (303260, 2, 3),
  (306666, 2, 3),
  (307836, 2, 6),
  (310208, 4, 6),
  (310802, 0, 0),
  (317963, 6, 3),
  (320409, 6, 6),
  (321155, 4, 3),
  (321399, 5, 3),
  (323659, 0, 0),
  (326214, 3, 3),
  (329389, 1, 1),
  (332946, 7, 3),
  (339183, 1, 0),
  (339861, 5, 1),
  (345440, 7, 7),
  (345519, 6, 5),
  (350160, 7, 7),
  (351701, 7, 0),
  (352195, 3, 3),
  (354649, 2, 3),
  (357351, 0, 4),
  (359981, 1, 0),
  (361449, 1, 3),
  (361969, 7, 7),
  (365311, 5, 7),
  (368198, 3, 7),
  (368422, 2, 3),
  (371503, 7, 1),
  (371566, 6, 0),
  (375770, 0, 3),
  (376462, 7, 0),
  (377774, 4, 3),
  (380467, 6, 5),
  (380909, 1, 4),
  (383075, 3, 3),
  (385476, 5, 2),
  (387407, 4, 7),
  (387841, 4, 3),
  (388454, 5, 2),
  (389424, 4, 7),
  (398278, 2, 4),
  (398500, 4, 6),
  (401340, 5, 6),
  (411499, 1, 4),
  (416582, 0, 7),
  (418208, 4, 2),
  (420350, 4, 3),
  (421211, 6, 6),
  (422839, 4, 3),
  (424114, 6, 5),
  (426261, 2, 7),
  (432797, 7, 2),
  (433982, 0, 3),
  (437185, 1, 0),
  (442667, 6, 0),
  (442812, 6, 4),
  (442886, 2, 3),
  (445581, 4, 3),
  (445629, 0, 4),
  (447458, 4, 1),
  (448666, 0, 3),
  (449844, 4, 2),
  (454420, 3, 3),
  (454617, 0, 0),
  (455387, 1, 0),
  (455759, 0, 2),
  (460613, 6, 7),
  (462103, 3, 3),
  (464418, 1, 0),
  (464750, 7, 0),
  (465445, 6, 7),
  (465638, 3, 1),
  (466433, 5, 3),
  (468306, 2, 2),
  (471976, 4, 1),
  (472907, 1, 1),
  (474879, 6, 0),
  (477363, 1, 3),
  (479134, 1, 1),
  (480806, 6, 5),
  (481281, 3, 6),
  (481853, 1, 0),
  (484370, 1, 0),
  (484430, 0, 3),
  (484611, 4, 6),
  (484774, 4, 7),
  (485377, 0, 1),
  (485415, 1, 1),
  (485777, 1, 0),
  (488717, 0, 7),
  (489315, 6, 7),
  (490043, 7, 0),
  (490127, 2, 3),
  (490217, 5, 4),
  (493998, 1, 0),
  (494110, 7, 2),
  (494664, 4, 3),
  (495746, 1, 4),
  (497035, 2, 3),
  (499175, 3, 7),
  (503218, 3, 3),
  (506122, 3, 5),
  (506579, 1, 3),
  (507097, 7, 0),
  (512471, 1, 6),
  (512891, 2, 3),
  (513000, 5, 3),
  (515407, 3, 7),
  (515671, 0, 6),
  (516643, 4, 3),
  (517597, 3, 2),
  (520861, 2, 3),
  (520935, 6, 5),
  (521927, 2, 3),
  (524118, 1, 0),
  (525260, 3, 0),
  (526535, 3, 3),
  (526862, 1, 7),
  (526983, 6, 0),
  (529381, 0, 0),
  (533766, 4, 6),
  (533846, 2, 1),
  (535557, 3, 4),
  (538383, 4, 5),
  (539491, 5, 0),
  (539544, 5, 6),
  (539759, 5, 3),
  (539838, 5, 2),
  (544063, 1, 0),
  (546857, 1, 4),
  (548252, 0, 7),
  (548297, 2, 2),
  (553146, 0, 4),
  (555162, 5, 3),
  (556468, 2, 3),
  (559284, 0, 7),
  (562175, 4, 6),
  (565671, 1, 0),
  (567069, 5, 3),
  (569723, 1, 0),
  (570086, 1, 4),
  (573463, 2, 3),
  (573870, 0, 4),
  (576389, 2, 7),
  (578641, 3, 3),
  (581821, 7, 6),
  (582626, 3, 2),
  (583881, 4, 3),
  (589032, 4, 7),
  (591019, 5, 6),
  (592723, 1, 3),
  (600103, 0, 3),
  (602292, 5, 6),
  (603359, 7, 0),
  (606338, 0, 5),
  (611125, 1, 4),
  (612285, 0, 4),
  (617229, 5, 3),
  (618194, 4, 3),
  (618981, 2, 1),
  (619642, 4, 6),
  (620792, 0, 4),
  (624590, 7, 0),
  (627112, 5, 2),
  (627940, 0, 4),
  (630454, 3, 3),
  (630701, 4, 3),
  (633507, 0, 0),
  (633740, 6, 7),
  (638331, 1, 4),
  (644836, 0, 3),
  (646459, 6, 0),
  (652292, 4, 7),
  (662007, 3, 6),
  (662584, 6, 0),
  (665005, 7, 3),
  (665081, 6, 4),
  (666992, 1, 0),
  (667436, 5, 2),
  (670155, 6, 2),
  (676175, 3, 3),
  (677808, 7, 3),
  (678226, 7, 0),
  (680872, 1, 4),
  (681060, 2, 2),
  (682578, 5, 2),
  (684827, 7, 4),
  (686122, 1, 0),
  (689621, 1, 1),
  (689884, 5, 2),
  (690685, 2, 3),
  (692866, 0, 7),
  (696820, 4, 6),
  (697043, 1, 3),
  (697466, 7, 3),
  (700205, 5, 6),
  (703192, 3, 3),
  (703659, 4, 7),
  (705752, 3, 6),
  (706009, 6, 0),
  (706784, 2, 3),
  (709361, 0, 7),
  (714510, 6, 3),
  (715022, 5, 7),
  (715734, 6, 0),
  (726561, 0, 0),
  (727082, 4, 4),
  (728493, 7, 7),
  (730848, 1, 4),
  (735628, 1, 0),
  (739779, 6, 0),
  (741008, 6, 7),
  (741648, 1, 5),
  (743877, 2, 7),
  (746983, 7, 0),
  (751381, 3, 3),
  (754032, 6, 0),
  (756367, 3, 3),
  (756598, 3, 7),
  (757056, 2, 3),
  (762138, 0, 0),
  (764145, 5, 3),
  (764232, 2, 5),
  (765804, 6, 3),
  (767629, 5, 3),
  (768141, 2, 3),
  (768565, 5, 3),
  (770230, 6, 2),
  (772419, 1, 6),
  (774214, 1, 0),
  (776977, 6, 3),
  (779397, 1, 3),
  (783011, 7, 0),
  (784631, 5, 6),
  (784756, 5, 2),
  (787924, 6, 3),
  (789574, 3, 3),
  (790304, 2, 6),
  (790367, 3, 3),
  (790848, 7, 0),
  (791477, 1, 0),
  (794732, 7, 7),
  (795773, 1, 0),
  (798351, 3, 6),
  (803672, 4, 0),
  (803676, 6, 0),
  (803763, 4, 3),
  (804433, 3, 3),
  (806741, 6, 7),
  (808724, 0, 3),
  (811214, 0, 0),
  (813609, 5, 2),
  (816480, 3, 3),
  (817014, 3, 1),
  (819098, 7, 5),
  (829534, 1, 0),
  (831425, 6, 3),
  (831532, 6, 6),
  (832409, 2, 3),
  (836070, 3, 3),
  (836450, 7, 3),
  (838577, 0, 0),
  (841538, 6, 1),
  (845860, 7, 3),
  (850074, 0, 0),
  (850649, 4, 7),
  (855244, 7, 3),
  (856454, 2, 7),
  (856567, 5, 7),
  (863981, 3, 2),
  (864030, 2, 7),
  (870339, 0, 7),
  (874345, 7, 0),
  (875334, 3, 3),
  (875616, 4, 3),
  (875719, 7, 0),
  (878558, 2, 0),
  (887638, 6, 4),
  (887901, 7, 7),
  (889114, 0, 3),
  (890245, 7, 0),
  (891883, 2, 2),
  (892008, 4, 1),
  (896108, 6, 0),
  (899473, 7, 7),
  (901950, 1, 0),
  (902110, 7, 0),
  (903394, 7, 2),
  (906966, 0, 4),
  (909200, 0, 4),
  (909557, 4, 3),
  (912407, 7, 4),
  (912973, 6, 5),
  (913731, 6, 7),
  (920533, 5, 2),
  (922604, 4, 3),
  (926077, 5, 6),
  (927504, 3, 7),
  (930666, 6, 3),
  (931742, 6, 0),
  (935519, 3, 6),
  (936175, 2, 3),
  (936787, 4, 3),
  (938997, 2, 3),
  (941356, 1, 4),
  (945340, 5, 4),
  (947382, 3, 7),
  (952826, 5, 3),
  (958456, 7, 7),
  (961560, 2, 4),
  (963607, 2, 3),
  (969567, 5, 0),
  (970261, 3, 7),
  (972421, 3, 5),
  (973083, 3, 2),
  (974602, 1, 6),
  (974619, 6, 0),
  (978201, 6, 2),
  (982081, 7, 0),
  (982657, 5, 2),
  (985495, 6, 7),
  (991296, 0, 0),
  (996072, 5, 3),
  (996446, 4, 2),
  (1002106, 1, 0),
  (1006749, 5, 0),
  (1008533, 4, 3),
  (1010802, 7, 3),
  (1011365, 3, 7),
  (1012920, 5, 3),
  (1013169, 2, 3),
  (1015910, 5, 3),
  (1016449, 7, 3),
  (1020640, 0, 0),
  (1024176, 6, 3),
  (1024622, 1, 2),
  (1026874, 4, 3),
  (1028609, 5, 5),
  (1031227, 2, 3),
  (1033475, 2, 3),
  (1033731, 7, 0),
  (1040597, 1, 6),
  (1043746, 3, 0),
  (1046261, 7, 0),
  (1047533, 4, 2),
  (1047777, 6, 0),
  (1050433, 1, 4),
  (1050917, 2, 7),
  (1051107, 4, 3),
  (1052110, 3, 2),
  (1054563, 5, 2),
  (1058571, 0, 0),
  (1058583, 1, 4),
  (1059250, 6, 7),
  (1062546, 7, 0),
  (1067392, 4, 3),
  (1068985, 1, 0),
  (1070832, 3, 4),
  (1071362, 1, 1),
  (1073283, 6, 0),
  (1074555, 1, 3),
  (1074978, 5, 4),
  (1075805, 7, 0),
  (1077580, 5, 3),
  (1081941, 0, 0),
  (1081989, 1, 0),
  (1082727, 3, 6),
  (1083807, 0, 0),
  (1085222, 6, 0),
  (1087746, 6, 0),
  (1088293, 0, 0),
  (1096120, 0, 5),
  (1096678, 6, 7),
  (1097382, 2, 3),
  (1098049, 0, 3),
  (1100166, 0, 3),
  (1100276, 3, 2),
  (1100337, 2, 3),
  (1105074, 1, 0),
  (1105732, 4, 3),
  (1107214, 3, 3),
  (1108303, 7, 0),
  (1112774, 7, 7),
  (1113361, 5, 3),
  (1113736, 1, 5),
  (1117822, 2, 6),
  (1118535, 4, 3),
  (1119997, 0, 6),
  (1120883, 0, 4),
  (1121583, 0, 7),
  (1122352, 7, 0),
  (1125587, 4, 7),
  (1127990, 4, 2),
  (1128193, 1, 0),
  (1131440, 3, 7),
  (1135533, 3, 5),
  (1137968, 7, 7),
  (1148161, 1, 3),
  (1149516, 6, 3),
  (1150330, 2, 3),
  (1150599, 7, 0),
  (1156522, 5, 3),
  (1156729, 3, 6),
  (1156946, 1, 0),
  (1159436, 1, 0),
  (1164643, 6, 2),
  (1166168, 0, 7),
  (1167553, 0, 0),
  (1167653, 1, 0),
  (1170013, 0, 0),
  (1171423, 0, 1),
  (1181153, 0, 0),
  (1181824, 0, 3),
  (1182533, 0, 1),
  (1183476, 5, 2),
  (1187513, 1, 7),
  (1189109, 6, 3),
  (1191282, 3, 3),
  (1194546, 1, 7),
  (1194788, 2, 3),
  (1198574, 5, 3),
  (1199679, 3, 3),
  (1200916, 5, 3),
  (1209250, 1, 7),
  (1210595, 2, 3),
  (1213368, 4, 3),
  (1214122, 4, 6),
  (1214880, 7, 0),
  (1215924, 5, 2),
  (1216614, 1, 0),
  (1221194, 2, 0),
  (1222979, 4, 6),
  (1223293, 2, 3),
  (1223513, 5, 0),
  (1226422, 0, 0),
  (1229070, 7, 0),
  (1229906, 3, 3),
  (1231541, 1, 7),
  (1232254, 4, 7),
  (1233870, 5, 3),
  (1238458, 4, 7),
  (1239623, 1, 0),
  (1240706, 5, 7),
  (1240891, 0, 4),
  (1242973, 4, 3),
  (1245701, 0, 7),
  (1252742, 2, 7),
  (1254308, 7, 7),
  (1254546, 5, 3),
  (1257242, 2, 3),
  (1258527, 6, 0),
  (1258986, 3, 3),
  (1259861, 1, 4),
  (1260456, 0, 4),
  (1262262, 2, 3),
  (1262708, 7, 2),
  (1264242, 7, 1),
  (1264996, 6, 0),
  (1265212, 2, 1),
  (1266595, 1, 2),
  (1266670, 7, 0),
  (1267739, 4, 3),
  (1268477, 1, 0),
  (1268600, 6, 1),
  (1269843, 1, 4),
  (1272847, 1, 3),
  (1273500, 5, 3),
  (1276874, 4, 3),
  (1282845, 5, 3),
  (1283649, 4, 1),
  (1284540, 3, 1),
  (1284774, 2, 6),
  (1287313, 3, 7),
  (1288574, 2, 6),
  (1289504, 5, 3),
  (1296238, 5, 3),
  (1298177, 4, 3),
  (1299734, 4, 1),
  (1304677, 2, 7),
  (1308648, 6, 0),
  (1309020, 0, 5),
  (1309240, 2, 2),
  (1311393, 6, 5),
  (1312004, 7, 7),
  (1315486, 5, 1),
  (1315803, 4, 6),
  (1317644, 0, 4),
  (1317661, 3, 7),
  (1319780, 1, 3),
  (1320785, 6, 0),
  (1322971, 1, 5),
  (1324949, 1, 0),
  (1328564, 6, 0),
  (1329893, 5, 1),
  (1331693, 1, 0),
  (1331762, 6, 7),
  (1332580, 1, 0),
  (1333318, 6, 0),
  (1333407, 6, 5),
  (1339721, 4, 2),
  (1340621, 7, 5),
  (1346300, 7, 7),
  (1347606, 3, 6),
  (1349954, 3, 2),
  (1354439, 6, 7),
  (1362672, 1, 3),
  (1365148, 7, 4),
  (1365551, 6, 0),
  (1366473, 0, 0),
  (1367391, 0, 0),
  (1370231, 7, 0),
  (1376548, 4, 2),
  (1376855, 1, 0),
  (1377885, 1, 3),
  (1378811, 3, 3),
  (1381900, 6, 0),
  (1383213, 4, 6),
  (1386389, 4, 6),
  (1386760, 7, 0),
  (1387443, 1, 0),
  (1390598, 0, 0),
  (1393218, 5, 7),
  (1396889, 1, 0),
  (1398918, 1, 0),
  (1400718, 6, 4),
  (1402135, 0, 4),
  (1404225, 2, 0),
  (1404421, 1, 0),
  (1407234, 1, 0),
  (1408677, 0, 0),
  (1410326, 7, 4),
  (1411095, 1, 0),
  (1414915, 6, 3),
  (1415134, 4, 3),
  (1415777, 6, 0),
  (1418640, 2, 2),
  (1419284, 3, 7),
  (1420480, 0, 0),
  (1423131, 0, 3),
  (1425208, 2, 2),
  (1425607, 2, 2),
  (1426273, 2, 6),
  (1427134, 2, 5),
  (1430501, 4, 7),
  (1432056, 2, 0),
  (1433296, 1, 3),
  (1434628, 6, 0),
  (1440863, 6, 3),
  (1443876, 0, 3),
  (1444422, 6, 0),
  (1444790, 1, 3),
  (1450333, 0, 6),
  (1450565, 7, 3),
  (1456661, 3, 0),
  (1456693, 3, 3),
  (1457210, 5, 6),
  (1457294, 4, 3),
  (1458535, 3, 1),
  (1461271, 6, 0),
  (1461314, 3, 2),
  (1462565, 2, 5),
  (1463599, 3, 3),
  (1465056, 6, 0),
  (1473910, 6, 1),
  (1475219, 5, 3),
  (1476424, 2, 7),
  (1476971, 7, 0),
  (1482440, 2, 3),
  (1485243, 5, 6),
  (1486473, 4, 1),
  (1487933, 3, 7),
  (1489959, 0, 0),
  (1491105, 5, 2),
  (1491313, 5, 3),
  (1493278, 2, 3),
  (1497406, 2, 6),
  (1499850, 6, 0),
  (1500102, 2, 0),
  (1502457, 0, 0),
  (1503146, 1, 3),
  (1507001, 3, 6),
  (1507866, 5, 3),
  (1510135, 2, 3),
  (1510152, 3, 3),
  (1512758, 4, 4),
  (1513737, 5, 3),
  (1515162, 5, 7),
  (1515548, 1, 0),
  (1521785, 2, 2),
  (1524176, 3, 1),
  (1525182, 0, 7),
  (1526008, 6, 0),
  (1528116, 1, 4),
  (1531162, 2, 7),
  (1531735, 2, 6),
  (1532685, 4, 4),
  (1533296, 2, 3),
  (1540460, 4, 1),
  (1541239, 2, 2),
  (1543657, 7, 6),
  (1544259, 5, 1),
  (1545526, 0, 0),
  (1545996, 2, 6),
  (1546553, 5, 3),
  (1547783, 4, 0),
  (1548835, 5, 2),
  (1550091, 7, 4),
  (1552142, 2, 3),
  (1554099, 4, 1),
  (1555037, 0, 2),
  (1556833, 2, 6),
  (1557711, 2, 6),
  (1561800, 1, 6),
  (1563638, 0, 4),
  (1567853, 1, 0),
  (1567881, 0, 4),
  (1568757, 2, 1),
  (1570282, 7, 0),
  (1576417, 0, 0),
  (1577770, 6, 7),
  (1580261, 4, 2),
  (1582740, 1, 4),
  (1591283, 1, 3),
  (1593325, 4, 3),
  (1594277, 0, 0),
  (1595156, 3, 3),
  (1595209, 2, 1),
  (1596695, 7, 3),
  (1598359, 2, 3),
  (1606489, 0, 7),
  (1609751, 5, 7),
  (1611659, 4, 7),
  (1613042, 7, 0),
  (1613566, 2, 2),
  (1614612, 0, 2),
  (1614846, 1, 0),
  (1616031, 1, 3),
  (1619654, 1, 0),
  (1621592, 0, 0),
  (1625051, 5, 3),
  (1625948, 5, 2),
  (1626157, 7, 0),
  (1628395, 4, 1),
  (1633513, 0, 0),
  (1635553, 5, 2),
  (1635891, 5, 2),
  (1637279, 3, 2),
  (1637481, 6, 0),
  (1639456, 4, 3),
  (1639573, 0, 4),
  (1640854, 0, 0),
  (1641883, 6, 0),
  (1642467, 1, 0),
  (1642478, 5, 1),
  (1647270, 0, 4),
  (1647646, 1, 6),
  (1648707, 7, 0),
  (1649306, 1, 7),
  (1650983, 0, 0),
  (1652908, 6, 7),
  (1655520, 6, 5),
  (1656312, 6, 0),
  (1662206, 1, 4),
  (1665985, 5, 6),
  (1666845, 6, 6),
  (1675572, 7, 0),
  (1675953, 5, 7),
  (1677520, 6, 0),
  (1679176, 7, 6),
  (1680195, 4, 6),
  (1680692, 7, 4),
  (1682559, 3, 0),
  (1684166, 3, 3),
  (1687211, 4, 3),
  (1689617, 4, 3),
  (1690073, 5, 3),
  (1690338, 2, 7),
  (1696384, 5, 2),
  (1696813, 3, 6),
  (1697115, 5, 3),
  (1698864, 6, 0),
  (1708426, 2, 3),
  (1714652, 2, 3),
  (1716624, 2, 3),
  (1717711, 7, 0),
  (1718601, 2, 3),
  (1719264, 5, 4),
  (1719285, 4, 7),
  (1723946, 7, 0),
  (1723964, 2, 3),
  (1724110, 1, 4),
  (1724874, 5, 3),
  (1725093, 1, 1),
  (1726658, 4, 5),
  (1729931, 6, 4),
  (1733624, 0, 4),
  (1736448, 7, 2),
  (1736975, 4, 2),
  (1740834, 2, 3),
  (1741362, 7, 0),
  (1747157, 2, 3),
  (1759838, 2, 7),
  (1761637, 1, 3),
  (1764315, 4, 2),
  (1766327, 1, 7),
  (1766838, 0, 0),
  (1769551, 2, 5),
  (1773002, 0, 7),
  (1774213, 0, 7),
  (1776781, 4, 3),
  (1777037, 5, 3),
  (1778496, 7, 0),
  (1778788, 4, 3),
  (1780807, 5, 0),
  (1782175, 6, 4),
  (1783723, 2, 2),
  (1788214, 7, 3),
  (1789900, 1, 0),
  (1790523, 2, 2),
  (1792559, 1, 4),
  (1793748, 4, 1),
  (1793991, 2, 3),
  (1794399, 3, 3),
  (1795262, 4, 2),
  (1796799, 3, 3),
  (1801402, 1, 7),
  (1801739, 5, 1),
  (1803195, 4, 2),
  (1803301, 0, 1),
  (1805322, 1, 0),
  (1806808, 1, 0),
  (1808495, 3, 3),
  (1808790, 2, 3),
  (1810276, 5, 3),
  (1811782, 7, 0),
  (1812894, 4, 1),
  (1815582, 3, 3),
  (1816865, 2, 3),
  (1818005, 0, 0),
  (1819710, 6, 0),
  (1819740, 3, 5),
  (1821991, 4, 3),
  (1823951, 1, 0),
  (1825681, 3, 3),
  (1826676, 1, 0),
  (1826948, 3, 3),
  (1829813, 5, 2),
  (1830306, 0, 6),
  (1830399, 7, 3),
  (1830960, 4, 5),
  (1836041, 2, 3),
  (1837758, 1, 7),
  (1837874, 0, 4),
  (1840502, 6, 0),
  (1846419, 0, 3),
  (1847212, 7, 0),
  (1847382, 2, 3),
  (1849981, 1, 4),
  (1850111, 7, 7),
  (1851143, 0, 5),
  (1851614, 5, 7),
  (1851670, 0, 0),
  (1856779, 1, 6),
  (1857852, 0, 0),
  (1859699, 0, 2),
  (1863267, 7, 1),
  (1863780, 0, 0),
  (1868635, 6, 7),
  (1871938, 5, 3),
  (1873918, 3, 7),
  (1879792, 4, 2),
  (1880231, 6, 7),
  (1880284, 7, 0),
  (1880982, 7, 3),
  (1882631, 7, 0),
  (1883208, 7, 7),
  (1883368, 4, 3),
  (1885805, 4, 2),
  (1887416, 5, 1),
  (1887856, 4, 3),
  (1890401, 7, 1),
  (1891103, 1, 5),
  (1894431, 4, 2),
  (1894486, 5, 4),
  (1901094, 0, 6),
  (1902522, 0, 3),
  (1904473, 6, 0),
  (1907579, 0, 3),
  (1907807, 6, 0),
  (1909125, 1, 4),
  (1913453, 0, 0),
  (1913814, 7, 0),
  (1916047, 1, 0),
  (1916879, 0, 0),
  (1918017, 4, 3),
  (1923209, 1, 2),
  (1923514, 4, 7),
  (1924471, 3, 2),
  (1929701, 4, 1),
  (1932722, 6, 0),
  (1933486, 5, 7),
  (1936845, 5, 3),
  (1941878, 4, 2),
  (1942852, 6, 7),
  (1942953, 4, 2),
  (1943542, 0, 5),
  (1944584, 5, 3),
  (1951091, 5, 4),
  (1951254, 3, 3),
  (1954004, 4, 0),
  (1954339, 5, 3),
  (1956298, 0, 7),
  (1957796, 3, 3),
  (1958306, 7, 7),
  (1960490, 2, 3),
  (1963089, 1, 3),
  (1963324, 1, 0),
  (1972284, 2, 6),
  (1972542, 4, 2),
  (1974216, 1, 0),
  (1977109, 5, 3),
  (1977769, 5, 7),
  (1980205, 6, 0),
  (1982566, 7, 3),
  (1983664, 3, 6),
  (1985886, 1, 0),
  (1985987, 4, 7),
  (1987556, 1, 7),
  (1994415, 2, 7),
  (1995146, 3, 4),
  (1997697, 6, 4),
  (1999373, 2, 3),
  (2001256, 6, 4),
  (2003729, 1, 0),
  (2006668, 2, 5),
  (2007712, 6, 0),
  (2010594, 2, 2),
  (2011325, 2, 3),
  (2013490, 0, 3),
  (2016108, 6, 3),
  (2016271, 1, 0),
  (2019020, 0, 0),
  (2021626, 5, 3),
  (2027549, 7, 0),
  (2029376, 2, 1),
  (2030195, 7, 3),
  (2032490, 0, 0),
  (2035346, 5, 2),
  (2038682, 3, 6),
  (2041785, 1, 3),
  (2042645, 5, 3),
  (2047002, 2, 1),
  (2049940, 4, 2),
  (2050790, 1, 6),
  (2051064, 6, 7),
  (2058665, 2, 6),
  (2066654, 0, 0),
  (2069873, 6, 5),
  (2072064, 7, 0),
  (2074525, 0, 7),
  (2075250, 5, 7),
  (2076300, 7, 0),
  (2077411, 5, 3),
  (2078532, 3, 3),
  (2079980, 2, 2),
  (2081814, 3, 3),
  (2088129, 5, 2),
  (2090454, 1, 4),
  (2093874, 4, 4),
  (2095181, 4, 7),
  (2102789, 6, 0),
  (2103275, 6, 3),
  (2108305, 5, 1),
  (2111903, 1, 3),
  (2114896, 5, 3),
  (2116547, 2, 7),
  (2117575, 4, 0),
  (2117840, 1, 3),
  (2120357, 3, 3),
  (2121544, 1, 4),
  (2123802, 6, 4),
  (2124995, 4, 6),
  (2128694, 1, 1),
  (2130026, 6, 6),
  (2132670, 2, 0),
  (2133194, 7, 0),
  (2144215, 4, 3),
  (2144669, 0, 5),
  (2146087, 4, 3),
  (2146140, 5, 2),
  (2146528, 1, 2),
  (2154469, 1, 3),
  (2157532, 1, 4),
  (2162923, 0, 0),
  (2163650, 4, 3),
  (2164530, 5, 3),
  (2166102, 0, 4),
  (2167313, 3, 6),
  (2167350, 5, 5),
  (2168352, 3, 3),
  (2170516, 6, 0),
  (2170798, 5, 3),
  (2171958, 5, 5),
  (2175838, 5, 3),
  (2176796, 7, 0),
  (2177256, 3, 5),
  (2177530, 1, 0),
  (2179625, 7, 1),
  (2179997, 5, 6),
  (2181696, 4, 3),
  (2183551, 6, 4),
  (2184681, 0, 0),
  (2190424, 3, 3),
  (2191725, 3, 4),
  (2191902, 4, 5),
  (2193263, 5, 2),
  (2196216, 3, 3),
  (2197400, 4, 6),
  (2200537, 5, 3),
  (2202052, 7, 7),
  (2203045, 0, 0),
  (2204028, 3, 3),
  (2206025, 2, 7),
  (2207484, 7, 0),
  (2209552, 2, 4),
  (2212700, 6, 4),
  (2213591, 7, 0),
  (2213861, 3, 3),
  (2213871, 7, 3),
  (2216022, 0, 0),
  (2219073, 6, 2),
  (2223342, 1, 2),
  (2225083, 7, 0),
  (2232664, 6, 0),
  (2242688, 2, 3),
  (2243796, 3, 3),
  (2246067, 5, 3),
  (2246477, 2, 2),
  (2249506, 1, 0),
  (2251578, 2, 7),
  (2254600, 3, 7),
  (2256650, 1, 5),
  (2258133, 6, 5),
  (2258710, 0, 3),
  (2260331, 7, 0),
  (2263126, 7, 1),
  (2263655, 1, 4),
  (2264861, 3, 7),
  (2267718, 3, 6),
  (2269631, 2, 3),
  (2273790, 0, 0),
  (2278351, 2, 2),
  (2279103, 4, 7),
  (2279683, 7, 7),
  (2281951, 3, 3),
  (2282516, 0, 7),
  (2282665, 1, 3),
  (2283493, 7, 4),
  (2283571, 2, 2),
  (2286316, 5, 3),
  (2286377, 7, 0),
  (2287635, 5, 3),
  (2289553, 5, 2),
  (2298034, 4, 2),
  (2299231, 2, 3),
  (2299807, 2, 0),
  (2300309, 1, 2),
  (2306344, 6, 0),
  (2307960, 6, 0),
  (2308178, 1, 0),
  (2310483, 4, 3),
  (2312214, 0, 0),
  (2312917, 5, 7),
  (2313618, 1, 5),
  (2315098, 3, 3),
  (2316816, 7, 3),
  (2319609, 5, 6),
  (2319948, 3, 1),
  (2320690, 3, 2),
  (2322543, 2, 4),
  (2322831, 2, 3),
  (2327206, 5, 3),
  (2327490, 1, 0),
  (2328147, 6, 6),
  (2329697, 0, 4),
  (2331273, 5, 3),
  (2334685, 5, 1),
  (2335989, 6, 3),
  (2340068, 3, 3),
  (2342076, 5, 6),
  (2343764, 5, 3),
  (2349869, 5, 6),
  (2352175, 1, 0),
  (2354896, 2, 7),
  (2355011, 7, 7),
  (2356584, 4, 3),
  (2358853, 6, 4),
  (2359997, 4, 7),
  (2360302, 0, 4),
  (2364499, 5, 2),
  (2365467, 2, 2),
  (2369234, 2, 7),
  (2371139, 2, 3),
  (2371842, 7, 0),
  (2372009, 2, 2),
  (2373614, 3, 6),
  (2379511, 2, 2),
  (2385049, 5, 2),
  (2387782, 0, 0),
  (2388157, 4, 6),
  (2391077, 1, 4),
  (2394168, 4, 2),
  (2395232, 2, 6),
  (2396135, 5, 3),
  (2398731, 4, 7),
  (2400150, 7, 0),
  (2403323, 6, 1),
  (2408209, 7, 3),
  (2408601, 1, 0),
  (2408822, 1, 4),
  (2411082, 5, 3),
  (2413470, 1, 1),
  (2415778, 3, 7),
  (2417065, 6, 3),
  (2418199, 7, 7),
  (2419147, 3, 6),
  (2422051, 0, 0),
  (2425023, 1, 0),
  (2425716, 4, 3),
  (2427743, 2, 1),
  (2428051, 1, 7),
  (2429090, 0, 7),
  (2429432, 4, 3),
  (2430759, 0, 7),
  (2431633, 6, 1),
  (2436322, 3, 1),
  (2436639, 5, 3),
  (2438908, 1, 0),
  (2440726, 6, 0),
  (2441916, 4, 7),
  (2445141, 5, 3),
  (2445559, 4, 7),
  (2445984, 1, 3),
  (2446788, 6, 0),
  (2451622, 3, 3),
  (2452990, 4, 3),
  (2454807, 5, 6),
  (2455349, 3, 3),
  (2458992, 0, 7),
  (2465585, 1, 0),
  (2466188, 3, 0),
  (2467812, 4, 0),
  (2468248, 4, 3),
  (2468953, 2, 3),
  (2470748, 5, 1),
  (2474139, 0, 4),
  (2474584, 0, 2),
  (2479844, 1, 1),
  (2480663, 3, 2),
  (2481023, 2, 5),
  (2481799, 6, 0),
  (2483863, 3, 3),
  (2485727, 4, 7),
  (2485741, 6, 3),
  (2485947, 4, 7),
  (2489888, 5, 3),
  (2490747, 1, 4),
  (2497019, 7, 0),
  (2502898, 4, 3),
  (2511895, 0, 1),
  (2515619, 0, 3),
  (2515681, 3, 7),
  (2522791, 0, 4),
  (2524634, 3, 2),
  (2525203, 4, 3),
  (2526415, 2, 2),
  (2527345, 5, 2),
  (2530863, 3, 7),
  (2530977, 1, 0),
  (2532250, 6, 7),
  (2536650, 7, 7),
  (2537391, 2, 2),
  (2537905, 4, 3),
  (2538137, 4, 6),
  (2541073, 2, 7),
  (2547597, 5, 2),
  (2550139, 4, 2),
  (2551143, 2, 1),
  (2554242, 4, 3),
  (2554620, 3, 2),
  (2555060, 1, 0),
  (2555512, 6, 0),
  (2556679, 5, 3),
  (2556937, 7, 4),
  (2558598, 3, 2),
  (2559667, 7, 3),
  (2559774, 7, 0),
  (2563942, 7, 1),
  (2566134, 6, 2),
  (2568209, 5, 3),
  (2573351, 3, 3),
  (2575289, 4, 3),
  (2577457, 5, 3),
  (2578371, 0, 7),
  (2584704, 5, 2),
  (2585753, 6, 5),
  (2589485, 0, 3),
  (2590162, 6, 7),
  (2592798, 2, 3),
  (2596497, 4, 3),
  (2598248, 4, 6),
  (2598625, 6, 0),
  (2599463, 5, 3),
  (2600731, 5, 3),
  (2602961, 6, 3),
  (2605594, 7, 0),
  (2605859, 4, 3),
  (2606039, 6, 0),
  (2610262, 2, 3),
  (2610948, 3, 5),
  (2613089, 0, 7),
  (2613891, 7, 7),
  (2616246, 1, 0),
  (2624524, 4, 3),
  (2625838, 4, 3),
  (2626153, 3, 3),
  (2628007, 3, 3),
  (2631146, 1, 4),
  (2634929, 2, 3),
  (2637001, 6, 7),
  (2645368, 6, 7),
  (2645740, 3, 2),
  (2645769, 4, 7),
  (2646999, 4, 5),
  (2647331, 2, 3),
  (2648663, 6, 4),
  (2649072, 5, 3),
  (2651181, 6, 0),
  (2655512, 3, 6),
  (2657916, 5, 1),
  (2663002, 6, 0),
  (2663311, 1, 7),
  (2664404, 1, 4),
  (2665189, 3, 6),
  (2665592, 7, 0),
  (2666301, 3, 3),
  (2667932, 3, 2),
  (2670399, 2, 7),
  (2670649, 0, 3),
  (2671586, 7, 0),
  (2674554, 1, 0),
  (2676197, 1, 4),
  (2679620, 6, 0),
  (2679627, 3, 6),
  (2682557, 5, 6),
  (2685538, 4, 7),
  (2686012, 3, 0),
  (2687152, 7, 1),
  (2688033, 0, 7),
  (2690418, 2, 7),
  (2695717, 3, 3),
  (2697188, 3, 6),
  (2699221, 1, 0),
  (2699513, 4, 6),
  (2703206, 4, 3),
  (2704756, 3, 3),
  (2708211, 0, 2),
  (2709116, 1, 7),
  (2709379, 2, 3),
  (2713219, 0, 5),
  (2713354, 2, 6),
  (2721661, 5, 2),
  (2721826, 6, 0),
  (2721979, 3, 3),
  (2723422, 6, 0),
  (2724239, 4, 3),
  (2726625, 4, 4),
  (2729273, 7, 0),
  (2734039, 6, 6),
  (2736797, 6, 0),
  (2737177, 4, 1),
  (2738192, 5, 7),
  (2738537, 1, 3),
  (2741944, 4, 1),
  (2743066, 7, 0),
  (2743291, 5, 3),
  (2743756, 1, 4),
  (2747559, 6, 0),
  (2748187, 3, 2),
  (2748791, 6, 0),
  (2756354, 5, 7),
  (2757643, 2, 2),
  (2758053, 4, 0),
  (2758121, 2, 3),
  (2764765, 1, 0),
  (2769542, 6, 0),
  (2770775, 1, 0),
  (2774601, 3, 4),
  (2775386, 3, 3),
  (2775608, 7, 3),
  (2776007, 5, 7),
  (2777652, 5, 6),
  (2777952, 2, 3),
  (2780255, 7, 1),
  (2780439, 7, 0),
  (2780843, 2, 3),
  (2780975, 7, 5),
  (2781649, 3, 2),
  (2782394, 3, 3),
  (2787003, 1, 4),
  (2788705, 0, 6),
  (2790785, 3, 3),
  (2794504, 4, 3),
  (2796255, 3, 7),
  (2797861, 1, 3),
  (2803542, 1, 4),
  (2808523, 2, 2),
  (2808953, 7, 3),
  (2809376, 1, 0),
  (2809507, 1, 7),
  (2811532, 1, 0),
  (2812064, 7, 0),
  (2814684, 3, 3),
  (2816722, 0, 1),
  (2816955, 6, 0),
  (2817604, 4, 3),
  (2818620, 2, 3),
  (2823601, 4, 3),
  (2824331, 1, 1),
  (2825563, 5, 0),
  (2825901, 1, 0),
  (2826216, 1, 3),
  (2826420, 0, 4),
  (2834516, 2, 5),
  (2835874, 0, 2),
  (2841725, 7, 4),
  (2841913, 0, 4),
  (2842492, 3, 3),
  (2844569, 6, 7),
  (2844643, 1, 7),
  (2849274, 7, 0),
  (2849521, 3, 7),
  (2849549, 3, 3),
  (2850500, 4, 3),
  (2850937, 1, 0),
  (2852878, 5, 2),
  (2854145, 3, 3),
  (2854705, 2, 3),
  (2854710, 6, 4),
  (2857913, 0, 3),
  (2859282, 2, 2),
  (2861447, 7, 0),
  (2864828, 4, 6),
  (2866813, 6, 2),
  (2867863, 0, 0),
  (2868151, 3, 2),
  (2869844, 5, 3),
  (2870189, 3, 4),
  (2871950, 7, 2),
  (2873835, 7, 0),
  (2875621, 1, 3),
  (2877137, 1, 3),
  (2878030, 1, 3),
  (2881612, 7, 3),
  (2884556, 7, 6),
  (2885489, 7, 0),
  (2886562, 4, 2),
  (2887997, 0, 7),
  (2888433, 4, 2),
  (2888634, 1, 0),
  (2889620, 0, 7),
  (2890356, 3, 7),
  (2891188, 3, 7),
  (2892591, 7, 7),
  (2896669, 6, 6),
  (2900360, 1, 7),
  (2900442, 6, 1),
  (2900834, 7, 0),
  (2902634, 5, 0),
  (2903717, 5, 3),
  (2905914, 6, 4),
  (2906334, 1, 0),
  (2908455, 7, 0),
  (2910470, 4, 6),
  (2910694, 2, 3),
  (2911614, 0, 0),
  (2914221, 4, 1),
  (2916134, 1, 7),
  (2924777, 6, 4),
  (2927578, 6, 7),
  (2929084, 1, 0),
  (2929908, 7, 4),
  (2930018, 3, 3),
  (2931037, 2, 3),
  (2933588, 0, 7),
  (2934186, 4, 4),
  (2935140, 4, 7),
  (2937099, 1, 1),
  (2939297, 6, 0),
  (2944190, 7, 0),
  (2945331, 1, 3),
  (2950361, 6, 0),
  (2951451, 5, 3),
  (2952196, 0, 0),
  (2952507, 7, 2),
  (2952626, 0, 3),
  (2954036, 2, 7),
  (2956676, 3, 6),
  (2960541, 0, 0),
  (2961576, 7, 1),
  (2963804, 5, 7),
  (2964462, 5, 7),
  (2965961, 2, 6),
  (2972150, 1, 7),
  (2974302, 7, 0),
  (2976445, 1, 2),
  (2977692, 0, 7),
  (2978777, 5, 2),
  (2980777, 4, 7),
  (2986412, 5, 3),
  (2988717, 4, 2),
  (2992002, 3, 2),
  (2993105, 5, 7),
  (2994778, 7, 3),
  (2995268, 0, 0),
  (2995291, 7, 7),
  (2995857, 6, 0),
  (2996924, 6, 7),
  (2998979, 4, 3),
  (3005554, 7, 3),
  (3006074, 1, 2),
  (3009374, 0, 0),
  (3011290, 5, 3),
  (3012061, 6, 1),
  (3012372, 2, 5),
  (3017262, 3, 7),
  (3018542, 6, 3),
  (3020816, 5, 7),
  (3028707, 7, 0),
  (3029534, 4, 3),
  (3032451, 0, 7),
  (3037573, 7, 0),
  (3038864, 5, 6),
  (3039172, 6, 0),
  (3045176, 3, 7),
  (3046852, 6, 6),
  (3047628, 1, 3),
  (3048991, 6, 0),
  (3049054, 3, 3),
  (3049337, 3, 3),
  (3049459, 0, 5),
  (3049660, 0, 4),
  (3050709, 2, 6),
  (3051503, 2, 3),
  (3054153, 6, 0),
  (3055116, 4, 3),
  (3057650, 4, 7),
  (3060557, 4, 3),
  (3062150, 5, 1),
  (3067126, 4, 3),
  (3069145, 6, 0),
  (3073970, 4, 3),
  (3074192, 4, 3),
  (3074784, 1, 3),
  (3075042, 3, 3),
  (3075519, 7, 4),
  (3076459, 3, 2),
  (3080998, 4, 7),
  (3081102, 5, 3),
  (3081320, 5, 3),
  (3081914, 6, 0),
  (3082055, 3, 2),
  (3086259, 6, 0),
  (3091650, 5, 5),
  (3093556, 7, 3),
  (3094174, 2, 2),
  (3094225, 0, 1),
  (3095752, 0, 0),
  (3096679, 5, 7),
  (3097542, 2, 3),
  (3098377, 3, 5),
  (3099809, 4, 3),
  (3100404, 3, 3),
  (3101039, 0, 0),
  (3103112, 1, 0),
  (3105630, 6, 0),
  (3108370, 5, 3),
  (3108595, 3, 6),
  (3108925, 3, 3),
  (3109120, 7, 4),
  (3109892, 4, 6),
  (3110072, 0, 4),
  (3110879, 0, 3),
  (3112459, 6, 7),
  (3113824, 0, 7),
  (3115592, 3, 3),
  (3116954, 5, 7),
  (3117796, 7, 2),
  (3119815, 1, 0),
  (3119923, 4, 7),
  (3119926, 7, 0),
  (3121431, 1, 0),
  (3122325, 7, 4),
  (3124565, 7, 0),
  (3125472, 5, 2),
  (3126511, 0, 3),
  (3128117, 5, 3),
  (3129773, 7, 3),
  (3131130, 7, 7),
  (3135915, 4, 3),
  (3138759, 5, 3),
  (3142847, 5, 6),
  (3143690, 5, 6),
  (3145469, 3, 7),
  (3146350, 0, 6),
  (3147479, 1, 4),
  (3148196, 1, 0),
  (3159044, 3, 2),
  (3159685, 6, 1),
  (3159812, 2, 2),
  (3159844, 3, 7),
  (3161142, 0, 0),
  (3161312, 1, 3),
  (3162875, 3, 4),
  (3165572, 1, 4),
  (3165648, 4, 7),
  (3168370, 2, 4),
  (3171691, 7, 2),
  (3174930, 7, 0),
  (3177022, 3, 2),
  (3177277, 2, 3),
  (3178386, 1, 0),
  (3178901, 3, 2),
  (3179406, 1, 0),
  (3180443, 2, 2),
  (3182412, 6, 2),
  (3185579, 4, 6),
  (3191687, 4, 7),
  (3195679, 6, 3),
  (3201768, 1, 0),
  (3201893, 1, 4),
  (3206522, 5, 3),
  (3207611, 2, 6),
  (3210879, 5, 3),
  (3211341, 2, 3),
  (3213129, 0, 6),
  (3215774, 3, 7),
  (3219524, 4, 6),
  (3220024, 4, 1),
  (3220287, 5, 7),
  (3221199, 0, 3),
  (3227426, 5, 4),
  (3228050, 3, 7),
  (3228079, 4, 5),
  (3229551, 3, 6),
  (3237099, 4, 2),
  (3239975, 7, 4),
  (3241464, 7, 4),
  (3242275, 1, 0),
  (3242650, 3, 6),
  (3245710, 1, 0),
  (3246044, 7, 0),
  (3249324, 5, 3),
  (3254339, 2, 3),
  (3255077, 7, 0),
  (3256559, 2, 7),
  (3259347, 2, 3),
  (3263026, 2, 3),
  (3263121, 2, 3),
  (3264110, 6, 0),
  (3266913, 7, 3),
  (3267531, 3, 5),
  (3267869, 3, 6),
  (3275498, 3, 3),
  (3276337, 6, 7),
  (3277450, 0, 0),
  (3278639, 3, 3),
  (3282567, 5, 3),
  (3286994, 4, 3),
  (3288226, 3, 2),
  (3289723, 7, 0),
  (3289725, 2, 5),
  (3292917, 4, 3),
  (3295580, 4, 3),
  (3297221, 7, 0),
  (3299038, 7, 2),
  (3299891, 5, 7),
  (3301423, 2, 3),
  (3304759, 2, 2),
  (3306867, 7, 3),
  (3311321, 7, 3),
  (3314274, 5, 7),
  (3314287, 3, 3),
  (3314713, 5, 2),
  (3315535, 7, 0),
  (3318826, 3, 2),
  (3319223, 4, 3),
  (3323730, 2, 6),
  (3326266, 1, 1),
  (3326325, 2, 6),
  (3327526, 4, 3),
  (3327891, 0, 0),
  (3328876, 4, 3),
  (3330328, 2, 6),
  (3330932, 7, 2),
  (3333266, 1, 0),
  (3335330, 3, 6),
  (3337632, 2, 4),
  (3341524, 4, 3),
  (3342285, 4, 3),
  (3343180, 0, 3),
  (3347700, 2, 3),
  (3349110, 1, 7),
  (3349365, 0, 5),
  (3353178, 3, 2),
  (3353183, 7, 0),
  (3353506, 2, 3),
  (3354079, 3, 3),
  (3355439, 1, 0),
  (3360374, 6, 0),
  (3360508, 3, 7),
  (3365033, 5, 0),
  (3365538, 5, 1),
  (3366090, 0, 0),
  (3368512, 1, 4),
  (3371055, 6, 3),
  (3373361, 3, 1),
  (3375649, 7, 7),
  (3376761, 0, 2),
  (3379911, 1, 0),
  (3380316, 6, 3),
  (3380401, 1, 3),
  (3381245, 4, 3),
  (3381252, 7, 0),
  (3382204, 2, 3),
  (3382329, 5, 7),
  (3382838, 1, 3),
  (3385617, 5, 3),
  (3386630, 6, 3),
  (3386910, 5, 3),
  (3387683, 0, 0),
  (3391543, 2, 3),
  (3391937, 6, 4),
  (3392377, 5, 3),
  (3398397, 5, 3),
  (3400952, 5, 3),
  (3401900, 2, 3),
  (3402665, 3, 3),
  (3407789, 7, 7),
  (3408578, 2, 6),
  (3412985, 7, 4),
  (3415113, 4, 3),
  (3415991, 7, 5),
  (3417675, 4, 6),
  (3421106, 7, 7),
  (3421514, 7, 5),
  (3423748, 6, 0),
  (3426389, 6, 0),
  (3430182, 2, 1),
  (3431767, 0, 0),
  (3433210, 4, 2),
  (3433837, 1, 0),
  (3434986, 0, 6),
  (3436922, 5, 3),
  (3438730, 4, 2),
  (3439219, 3, 1),
  (3441097, 4, 5),
  (3444340, 1, 0),
  (3444470, 5, 3),
  (3446069, 2, 3),
  (3448224, 6, 1),
  (3452151, 5, 2),
  (3455360, 4, 2),
  (3457435, 2, 3),
  (3459452, 6, 0),
  (3460117, 0, 0),
  (3462486, 2, 3),
  (3463899, 7, 3),
  (3463904, 5, 2),
  (3464417, 0, 1),
  (3466707, 5, 3),
  (3467047, 5, 4),
  (3470557, 2, 3),
  (3471748, 3, 0),
  (3474806, 5, 2),
  (3476284, 3, 7),
  (3477321, 2, 3),
  (3477951, 1, 7),
  (3478900, 5, 6),
  (3481672, 6, 4),
  (3482059, 4, 3),
  (3482874, 5, 6),
  (3483143, 3, 3),
  (3483687, 7, 4),
  (3483883, 2, 7),
  (3492837, 6, 0),
  (3494130, 3, 5),
  (3495068, 7, 3),
  (3495357, 3, 5),
  (3498531, 2, 0),
  (3501861, 0, 3),
  (3504137, 2, 4),
  (3511141, 5, 2),
  (3515023, 0, 0),
  (3524338, 4, 4),
  (3527161, 6, 4),
  (3528202, 5, 3),
  (3529942, 7, 0),
  (3530249, 1, 1),
  (3530985, 0, 0),
  (3531741, 5, 3),
  (3534637, 5, 3),
  (3535268, 0, 0),
  (3537117, 5, 3),
  (3538380, 6, 0),
  (3539402, 1, 4),
  (3540409, 2, 3),
  (3541485, 3, 2),
  (3550066, 4, 6),
  (3551533, 2, 3),
  (3553234, 0, 0),
  (3553467, 3, 2),
  (3555242, 0, 6),
  (3555704, 0, 3),
  (3558470, 0, 7),
  (3559583, 7, 0),
  (3560329, 2, 5),
  (3560729, 1, 0),
  (3560938, 4, 2),
  (3563742, 5, 2),
  (3565880, 5, 0),
  (3566104, 0, 6),
  (3571640, 1, 0),
  (3571650, 6, 7),
  (3572538, 5, 3),
  (3579440, 4, 3),
  (3582774, 5, 2),
  (3583831, 1, 3),
  (3586547, 2, 4),
  (3589685, 1, 5),
  (3590749, 1, 6),
  (3591994, 3, 3),
  (3594933, 3, 7),
  (3596023, 1, 0),
  (3596759, 3, 0),
  (3597766, 6, 1),
  (3597839, 5, 6),
  (3598561, 2, 3),
])
