from src.util import *
schedule = deque([
  (350, 1, 0),
  (1766, 0, 2),
  (2967, 0, 2),
  (4886, 3, 0),
  (5869, 3, 1),
  (8979, 1, 0),
  (9702, 2, 2),
  (11020, 0, 0),
  (11447, 1, 2),
  (13191, 2, 2),
  (14322, 2, 2),
  (14347, 3, 0),
  (20158, 3, 2),
  (21729, 3, 0),
  (25533, 2, 0),
  (26573, 3, 2),
  (28999, 2, 0),
  (30166, 3, 2),
  (30706, 0, 2),
  (32690, 1, 2),
  (36477, 1, 0),
  (40036, 1, 1),
  (40078, 2, 2),
  (41037, 3, 0),
  (42601, 3, 1),
  (43710, 1, 0),
  (47983, 3, 0),
  (49072, 0, 2),
  (49669, 3, 2),
  (49822, 2, 1),
  (55352, 2, 2),
  (57891, 1, 2),
  (59183, 1, 0),
  (61336, 2, 2),
  (64438, 0, 0),
  (65650, 3, 1),
  (68668, 2, 1),
  (71202, 3, 0),
  (75966, 1, 0),
  (78508, 3, 0),
  (79425, 0, 2),
  (80409, 2, 2),
  (80867, 2, 0),
  (83694, 3, 0),
  (85125, 3, 1),
  (85142, 3, 0),
  (85625, 2, 1),
  (85839, 3, 0),
  (86365, 3, 0),
  (88340, 1, 0),
  (89131, 3, 0),
  (90097, 2, 1),
  (90597, 0, 1),
  (92204, 1, 2),
  (96495, 0, 1),
  (97887, 0, 0),
  (101635, 0, 2),
  (102254, 0, 1),
  (102351, 1, 0),
  (102906, 0, 2),
  (103463, 1, 1),
  (107907, 3, 1),
  (110868, 1, 2),
  (113192, 2, 0),
  (118658, 1, 1),
  (118830, 3, 1),
  (120092, 0, 1),
  (124684, 2, 0),
  (125579, 2, 2),
  (127055, 1, 0),
  (128312, 0, 1),
  (130916, 2, 2),
  (132683, 2, 2),
  (134071, 0, 0),
  (135097, 1, 2),
  (136935, 2, 0),
  (141021, 1, 0),
  (141681, 3, 1),
  (142732, 2, 2),
  (142793, 3, 0),
  (146488, 2, 2),
  (152001, 3, 2),
  (152376, 3, 1),
  (152739, 1, 1),
  (154597, 3, 0),
  (157248, 1, 2),
  (158180, 3, 2),
  (158603, 0, 1),
  (158713, 3, 1),
  (158767, 1, 1),
  (159783, 1, 1),
  (160537, 3, 2),
  (160695, 2, 0),
  (161460, 0, 1),
  (166649, 2, 0),
  (168440, 3, 0),
  (168682, 2, 1),
  (171551, 3, 0),
  (172260, 3, 0),
  (174751, 0, 0),
  (176478, 3, 2),
  (176540, 3, 1),
  (180291, 1, 1),
  (180772, 0, 1),
  (190785, 2, 1),
  (195579, 2, 2),
  (198882, 0, 1),
  (200119, 0, 0),
  (200239, 3, 2),
  (201119, 2, 1),
  (207734, 3, 1),
  (208589, 2, 1),
  (209531, 2, 2),
  (214565, 2, 1),
  (215691, 3, 1),
  (216873, 3, 2),
  (217883, 3, 0),
  (219890, 1, 0),
  (222913, 0, 0),
  (223661, 3, 2),
  (227255, 1, 0),
  (227348, 2, 0),
  (227515, 0, 1),
  (231239, 2, 0),
  (231355, 0, 1),
  (234559, 3, 2),
  (237502, 2, 0),
  (244819, 2, 1),
  (250477, 0, 1),
  (251180, 2, 1),
  (254467, 1, 2),
  (256489, 3, 0),
  (257054, 1, 0),
  (257087, 3, 1),
  (260716, 2, 1),
  (261723, 3, 0),
  (264000, 3, 2),
  (265386, 1, 0),
  (268095, 1, 2),
  (269368, 0, 1),
  (272637, 1, 1),
  (274030, 3, 0),
  (280044, 3, 1),
  (281083, 3, 1),
  (283335, 0, 2),
  (284675, 1, 1),
  (287510, 1, 2),
  (288575, 3, 0),
  (289459, 2, 2),
  (292344, 0, 1),
  (299900, 3, 2),
  (301337, 2, 0),
  (306166, 0, 0),
  (313151, 1, 1),
  (314254, 2, 2),
  (315809, 1, 0),
  (317104, 0, 2),
  (317678, 2, 2),
  (319525, 0, 2),
  (319730, 0, 2),
  (320951, 2, 2),
  (324652, 0, 1),
  (325819, 3, 0),
  (326741, 0, 0),
  (330429, 3, 1),
  (331360, 2, 0),
  (332228, 2, 0),
  (333832, 3, 0),
  (334992, 0, 1),
  (335950, 0, 1),
  (338713, 1, 2),
  (340344, 2, 0),
  (342496, 1, 0),
  (345180, 2, 1),
  (348645, 1, 0),
  (351952, 0, 0),
  (352400, 2, 1),
  (355401, 3, 0),
  (355466, 1, 1),
  (355810, 1, 2),
  (356433, 2, 2),
  (356705, 1, 2),
  (357413, 3, 1),
  (357820, 2, 0),
  (362330, 3, 1),
  (363180, 0, 1),
  (364213, 1, 1),
  (366087, 2, 0),
  (366465, 0, 0),
  (366587, 2, 2),
  (367667, 0, 1),
  (370259, 1, 2),
  (370817, 0, 0),
  (371261, 3, 1),
  (371299, 2, 0),
  (373718, 2, 2),
  (373783, 2, 1),
  (376549, 1, 2),
  (378405, 3, 1),
  (378431, 2, 0),
  (382918, 0, 1),
  (388758, 0, 2),
  (389753, 0, 1),
  (391731, 2, 0),
  (393894, 3, 1),
  (398960, 1, 2),
  (399364, 2, 0),
  (400161, 3, 0),
  (403413, 1, 2),
  (407464, 1, 2),
  (408479, 1, 2),
  (409593, 3, 2),
  (409758, 0, 1),
  (410070, 1, 1),
  (410747, 3, 2),
  (411077, 1, 1),
  (411707, 0, 0),
  (413478, 0, 0),
  (414438, 2, 0),
  (416058, 3, 1),
  (418253, 3, 0),
  (419876, 1, 0),
  (420091, 1, 0),
  (420252, 1, 1),
  (420535, 3, 0),
  (421148, 2, 1),
  (421507, 3, 1),
  (421613, 1, 2),
  (422090, 2, 1),
  (423164, 2, 1),
  (424908, 1, 2),
  (426112, 2, 0),
  (431736, 3, 0),
  (433976, 2, 0),
  (435248, 3, 2),
  (435836, 1, 1),
  (439293, 0, 2),
  (443082, 1, 2),
  (443915, 0, 0),
  (445072, 3, 0),
  (446207, 2, 1),
  (450671, 2, 2),
  (452385, 2, 1),
  (453366, 3, 2),
  (456116, 2, 1),
  (456836, 1, 2),
  (456937, 3, 2),
  (460126, 3, 1),
  (461873, 0, 2),
  (462640, 0, 1),
  (464949, 0, 0),
  (468245, 0, 0),
  (469288, 0, 2),
  (469766, 2, 1),
  (472957, 1, 0),
  (475223, 0, 0),
  (476892, 3, 0),
  (478244, 3, 1),
  (480524, 3, 2),
  (484100, 0, 0),
  (485199, 3, 1),
  (485201, 0, 2),
  (488738, 3, 1),
  (489932, 0, 0),
  (489935, 0, 0),
  (490645, 3, 1),
  (494383, 3, 1),
  (496714, 0, 2),
  (500129, 0, 2),
  (504822, 2, 0),
  (508659, 3, 0),
  (513196, 0, 2),
  (514135, 2, 2),
  (516186, 2, 2),
  (516489, 3, 1),
  (520142, 0, 2),
  (523991, 1, 1),
  (524363, 2, 2),
  (524922, 3, 2),
  (525655, 2, 1),
  (526748, 1, 2),
  (530910, 1, 1),
  (532088, 0, 2),
  (532496, 1, 1),
  (533525, 1, 2),
  (533683, 3, 1),
  (535525, 2, 1),
  (535957, 3, 0),
  (536821, 3, 1),
  (537200, 2, 1),
  (538312, 2, 2),
  (539062, 0, 0),
  (539412, 0, 1),
  (539557, 1, 2),
  (544919, 2, 1),
  (548111, 1, 2),
  (548818, 0, 0),
  (551832, 0, 0),
  (555282, 1, 0),
  (555381, 2, 2),
  (556015, 2, 0),
  (556097, 2, 1),
  (557880, 0, 0),
  (558649, 2, 0),
  (560883, 0, 1),
  (561381, 1, 2),
  (564286, 3, 1),
  (565223, 3, 0),
  (567053, 2, 0),
  (569335, 1, 0),
  (570227, 2, 0),
  (572668, 2, 2),
  (577221, 2, 2),
  (579404, 3, 0),
  (579513, 1, 2),
  (585205, 2, 1),
  (592893, 1, 2),
  (595609, 2, 1),
  (597463, 0, 0),
  (599241, 3, 2),
  (602247, 3, 1),
  (603112, 0, 2),
  (604060, 1, 2),
  (604705, 2, 1),
  (605563, 2, 1),
  (612297, 1, 0),
  (612449, 1, 1),
  (616716, 1, 2),
  (617817, 2, 1),
  (618950, 0, 1),
  (620823, 3, 2),
  (620915, 3, 0),
  (622187, 1, 2),
  (625227, 2, 0),
  (625342, 1, 0),
  (628552, 0, 0),
  (628735, 3, 0),
  (632867, 0, 2),
  (637374, 1, 1),
  (640772, 2, 0),
  (642317, 0, 1),
  (642666, 0, 2),
  (649716, 1, 2),
  (649777, 0, 2),
  (649820, 3, 1),
  (651678, 1, 1),
  (654920, 0, 0),
  (655998, 2, 1),
  (660535, 1, 0),
  (662936, 3, 1),
  (664946, 0, 0),
  (665970, 2, 0),
  (674750, 3, 2),
  (678041, 3, 1),
  (678702, 0, 2),
  (679251, 3, 2),
  (680570, 1, 0),
  (685607, 0, 2),
  (686909, 2, 0),
  (687979, 2, 1),
  (688525, 0, 2),
  (689189, 1, 1),
  (689418, 1, 2),
  (689827, 1, 1),
  (691065, 3, 2),
  (694331, 0, 1),
  (695957, 3, 1),
  (695985, 3, 0),
  (701424, 3, 2),
  (704842, 1, 0),
  (708823, 0, 0),
  (710336, 2, 0),
  (711577, 3, 2),
  (712691, 0, 1),
  (720068, 1, 2),
  (720162, 0, 1),
  (720680, 0, 1),
  (720724, 2, 2),
  (725555, 2, 0),
  (727274, 0, 0),
  (730981, 1, 2),
  (731102, 2, 0),
  (732397, 3, 1),
  (739274, 2, 1),
  (742821, 0, 2),
  (746128, 1, 1),
  (747264, 2, 2),
  (749535, 2, 1),
  (755082, 3, 2),
  (755562, 3, 2),
  (757975, 3, 0),
  (759373, 0, 2),
  (760350, 0, 2),
  (761946, 1, 1),
  (762979, 3, 1),
  (769771, 2, 0),
  (769916, 2, 1),
  (771606, 3, 1),
  (775583, 1, 2),
  (777715, 1, 2),
  (783793, 2, 1),
  (784199, 3, 2),
  (785711, 1, 1),
  (786421, 0, 0),
  (789691, 3, 1),
  (790156, 0, 1),
  (790763, 0, 0),
  (793004, 0, 0),
  (793291, 2, 0),
  (794556, 2, 2),
  (796964, 1, 2),
  (800727, 1, 1),
  (805802, 1, 0),
  (806306, 0, 2),
  (809080, 1, 0),
  (811115, 0, 0),
  (811117, 3, 2),
  (812285, 2, 1),
  (815509, 0, 2),
  (816006, 3, 1),
  (816639, 2, 1),
  (817569, 0, 2),
  (819147, 3, 2),
  (819266, 1, 1),
  (820145, 2, 2),
  (821506, 0, 0),
  (823525, 2, 2),
  (824303, 1, 0),
  (824330, 1, 2),
  (825128, 2, 2),
  (830605, 1, 1),
  (833774, 2, 1),
  (840064, 3, 1),
  (843797, 2, 1),
  (845982, 1, 1),
  (846168, 2, 1),
  (847982, 2, 0),
  (848457, 3, 0),
  (849811, 1, 1),
  (850344, 1, 1),
  (851099, 1, 1),
  (855153, 2, 1),
  (855432, 1, 1),
  (856088, 0, 1),
  (856783, 1, 2),
  (859882, 3, 2),
  (859907, 1, 1),
  (862145, 3, 1),
  (863609, 2, 0),
  (864403, 2, 1),
  (866511, 3, 2),
  (867807, 1, 1),
  (876454, 0, 2),
  (876489, 1, 1),
  (879621, 0, 2),
  (881604, 3, 1),
  (886461, 1, 2),
  (887543, 1, 2),
  (895700, 0, 1),
  (896093, 3, 2),
  (896844, 1, 0),
  (900608, 2, 0),
  (902866, 2, 2),
  (904065, 0, 0),
  (905134, 0, 1),
  (910566, 2, 0),
  (911375, 2, 0),
  (918911, 2, 0),
  (922320, 0, 0),
  (923809, 1, 0),
  (924585, 0, 0),
  (924950, 2, 0),
  (927301, 0, 1),
  (929024, 3, 2),
  (932740, 3, 0),
  (933189, 3, 2),
  (934912, 3, 1),
  (937004, 3, 1),
  (939289, 1, 1),
  (942110, 1, 2),
  (943412, 0, 2),
  (944604, 3, 1),
  (945924, 0, 1),
  (948605, 2, 0),
  (950049, 0, 0),
  (950222, 2, 0),
  (951987, 3, 2),
  (952078, 3, 2),
  (956862, 1, 2),
  (958381, 2, 2),
  (961438, 3, 0),
  (969582, 3, 2),
  (972359, 3, 0),
  (974036, 3, 2),
  (974232, 2, 1),
  (975741, 1, 0),
  (976823, 0, 1),
  (977284, 3, 1),
  (977387, 3, 0),
  (977742, 3, 1),
  (978032, 0, 1),
  (981922, 2, 1),
  (983631, 1, 0),
  (983853, 2, 2),
  (996976, 0, 0),
  (997598, 1, 1),
  (1000351, 0, 1),
  (1001262, 1, 2),
  (1001910, 1, 0),
  (1003102, 0, 0),
  (1003479, 1, 0),
  (1003618, 3, 1),
  (1004391, 3, 2),
  (1005029, 2, 1),
  (1006696, 2, 1),
  (1010915, 0, 1),
  (1012830, 2, 1),
  (1013709, 3, 1),
  (1015991, 1, 0),
  (1019565, 0, 0),
  (1024477, 0, 1),
  (1025419, 1, 1),
  (1026021, 0, 2),
  (1032437, 2, 1),
  (1033173, 1, 2),
  (1035825, 0, 0),
  (1037063, 0, 0),
  (1040276, 3, 2),
  (1043540, 0, 1),
  (1046859, 3, 0),
  (1050691, 0, 2),
  (1052951, 2, 0),
  (1054532, 2, 2),
  (1055731, 2, 0),
  (1056284, 2, 2),
  (1056501, 3, 2),
  (1056648, 0, 0),
  (1057251, 3, 1),
  (1058217, 2, 0),
  (1061441, 1, 1),
  (1065999, 1, 2),
  (1068024, 3, 2),
  (1070186, 1, 0),
  (1074128, 3, 0),
  (1080560, 2, 0),
  (1082903, 2, 2),
  (1085063, 0, 1),
  (1087736, 3, 1),
  (1087936, 2, 2),
  (1091264, 2, 0),
  (1092968, 3, 0),
  (1097692, 1, 1),
  (1097812, 1, 2),
  (1099688, 2, 0),
  (1101451, 3, 1),
  (1101901, 0, 2),
  (1102222, 0, 2),
  (1109195, 0, 1),
  (1110767, 0, 2),
  (1110855, 0, 1),
  (1112539, 1, 2),
  (1116271, 2, 2),
  (1116755, 3, 1),
  (1120948, 3, 1),
  (1123352, 2, 1),
  (1132476, 2, 0),
  (1133010, 1, 0),
  (1137520, 1, 2),
  (1139306, 3, 2),
  (1141284, 0, 1),
  (1141767, 3, 1),
  (1142223, 0, 0),
  (1142367, 1, 0),
  (1146469, 0, 1),
  (1149592, 2, 1),
  (1152523, 3, 2),
  (1153707, 1, 1),
  (1154330, 2, 2),
  (1154434, 2, 1),
  (1157647, 2, 1),
  (1158829, 3, 0),
  (1159410, 2, 1),
  (1164274, 3, 0),
  (1165977, 1, 1),
  (1166544, 3, 0),
  (1167007, 2, 2),
  (1167313, 2, 0),
  (1171661, 0, 0),
  (1171713, 3, 0),
  (1173915, 3, 1),
  (1174781, 2, 1),
  (1175158, 1, 2),
  (1176233, 1, 0),
  (1176569, 2, 1),
  (1179767, 3, 1),
  (1183851, 2, 2),
  (1187753, 2, 0),
  (1188527, 1, 0),
  (1188588, 3, 2),
  (1190055, 2, 1),
  (1191542, 2, 0),
  (1193467, 3, 0),
  (1193529, 3, 0),
  (1193859, 0, 2),
  (1194914, 3, 0),
  (1195850, 2, 2),
  (1196988, 0, 1),
  (1198824, 3, 0),
  (1199256, 3, 1),
  (1199770, 0, 1),
  (1202006, 0, 0),
  (1202706, 2, 1),
  (1208195, 0, 0),
  (1211089, 0, 0),
  (1211748, 1, 2),
  (1212105, 1, 0),
  (1212629, 3, 2),
  (1214709, 0, 2),
  (1217312, 2, 1),
  (1224002, 2, 1),
  (1225166, 2, 2),
  (1227336, 0, 0),
  (1228264, 2, 2),
  (1229721, 1, 2),
  (1231150, 1, 0),
  (1234240, 1, 1),
  (1235056, 0, 2),
  (1236254, 2, 1),
  (1236803, 3, 1),
  (1237808, 1, 1),
  (1241685, 0, 2),
  (1241745, 1, 1),
  (1242478, 3, 2),
  (1243618, 0, 1),
  (1244467, 3, 1),
  (1247432, 3, 1),
  (1251150, 1, 1),
  (1251816, 2, 1),
  (1257117, 1, 1),
  (1257240, 3, 0),
  (1257734, 3, 0),
  (1258121, 2, 1),
  (1260106, 2, 2),
  (1260910, 1, 2),
  (1261165, 0, 2),
  (1261725, 3, 0),
  (1262077, 1, 0),
  (1263046, 0, 1),
  (1263345, 3, 0),
  (1267475, 3, 0),
  (1268751, 3, 1),
  (1270188, 0, 1),
  (1271896, 3, 0),
  (1274883, 1, 1),
  (1275528, 2, 1),
  (1279095, 0, 2),
  (1281144, 3, 1),
  (1286009, 0, 1),
  (1289930, 1, 0),
  (1290199, 1, 0),
  (1291131, 0, 2),
  (1293288, 1, 1),
  (1297878, 0, 1),
  (1304099, 1, 0),
  (1304256, 2, 2),
  (1307173, 0, 1),
  (1308888, 0, 0),
  (1309629, 1, 2),
  (1311492, 2, 1),
  (1314258, 1, 0),
  (1320205, 1, 2),
  (1323347, 0, 2),
  (1326348, 1, 2),
  (1328258, 3, 2),
  (1329089, 2, 0),
  (1330607, 0, 1),
  (1330903, 0, 0),
  (1331805, 2, 1),
  (1332592, 2, 1),
  (1333493, 3, 1),
  (1333913, 1, 0),
  (1334027, 1, 2),
  (1334127, 2, 2),
  (1334464, 1, 2),
  (1336217, 3, 1),
  (1340640, 1, 2),
  (1344689, 0, 1),
  (1346213, 1, 0),
  (1351078, 2, 0),
  (1351913, 2, 2),
  (1352557, 0, 1),
  (1353021, 1, 1),
  (1353125, 1, 2),
  (1354132, 2, 1),
  (1354855, 1, 1),
  (1360242, 0, 2),
  (1363797, 1, 0),
  (1366675, 3, 2),
  (1368167, 2, 1),
  (1369475, 0, 2),
  (1374502, 3, 1),
  (1375515, 1, 2),
  (1377720, 2, 0),
  (1378067, 3, 2),
  (1379854, 3, 0),
  (1381342, 2, 0),
  (1382426, 0, 2),
  (1384389, 3, 2),
  (1387390, 2, 2),
  (1387865, 2, 2),
  (1390865, 0, 1),
  (1394519, 3, 1),
  (1394851, 1, 0),
  (1395700, 1, 2),
  (1401252, 3, 2),
  (1402239, 3, 2),
  (1405412, 1, 2),
  (1407254, 2, 0),
  (1407667, 3, 2),
  (1407763, 2, 1),
  (1412140, 0, 2),
  (1417634, 3, 1),
  (1418495, 0, 1),
  (1420159, 2, 1),
  (1423858, 0, 0),
  (1436074, 3, 2),
  (1437624, 3, 0),
  (1442207, 2, 2),
  (1448255, 3, 2),
  (1452637, 0, 2),
  (1455560, 3, 2),
  (1455743, 2, 2),
  (1456281, 1, 2),
  (1457290, 2, 1),
  (1459525, 2, 0),
  (1459777, 3, 0),
  (1460192, 2, 0),
  (1462541, 2, 1),
  (1463312, 2, 0),
  (1466040, 3, 0),
  (1470478, 2, 2),
  (1472971, 1, 2),
  (1473276, 3, 1),
  (1474031, 2, 2),
  (1474383, 3, 2),
  (1474856, 1, 0),
  (1480327, 1, 0),
  (1481019, 3, 1),
  (1481329, 1, 1),
  (1483204, 0, 0),
  (1483718, 2, 2),
  (1483894, 2, 2),
  (1484370, 0, 2),
  (1486689, 0, 0),
  (1487318, 2, 2),
  (1495443, 3, 1),
  (1497496, 3, 1),
  (1497627, 0, 1),
  (1503335, 2, 1),
  (1505104, 2, 1),
  (1508127, 3, 1),
  (1513267, 0, 2),
  (1513726, 1, 0),
  (1514389, 3, 1),
  (1516101, 0, 0),
  (1517902, 2, 0),
  (1519847, 3, 1),
  (1520875, 2, 1),
  (1522108, 2, 0),
  (1524574, 3, 1),
  (1527157, 1, 0),
  (1529457, 1, 0),
  (1548851, 2, 2),
  (1549455, 3, 0),
  (1549571, 0, 2),
  (1553158, 0, 0),
  (1554052, 2, 0),
  (1555867, 3, 1),
  (1559328, 2, 1),
  (1562621, 1, 1),
  (1563103, 2, 1),
  (1564661, 2, 1),
  (1564959, 3, 2),
  (1565676, 1, 0),
  (1569586, 1, 2),
  (1571176, 2, 0),
  (1573313, 3, 1),
  (1574215, 0, 1),
  (1574375, 2, 1),
  (1576334, 3, 1),
  (1580505, 0, 2),
  (1583238, 3, 1),
  (1585911, 3, 0),
  (1587056, 3, 2),
  (1588313, 3, 0),
  (1589070, 0, 1),
  (1589694, 2, 1),
  (1592409, 2, 2),
  (1592700, 3, 1),
  (1593988, 1, 1),
  (1594302, 3, 2),
  (1594714, 0, 2),
  (1595829, 1, 0),
  (1597215, 2, 1),
  (1601439, 2, 1),
  (1602718, 3, 0),
  (1604229, 0, 0),
  (1604292, 2, 0),
  (1604888, 2, 0),
  (1605719, 1, 0),
  (1606040, 0, 2),
  (1607608, 1, 0),
  (1610846, 0, 2),
  (1613432, 1, 2),
  (1615710, 0, 1),
  (1616219, 0, 0),
  (1618842, 1, 2),
  (1619711, 2, 0),
  (1620354, 2, 0),
  (1623368, 0, 1),
  (1623409, 2, 2),
  (1625976, 3, 1),
  (1629034, 3, 1),
  (1629365, 0, 0),
  (1629837, 0, 0),
  (1633450, 0, 1),
  (1637276, 1, 2),
  (1637823, 3, 1),
  (1638492, 3, 1),
  (1639359, 2, 1),
  (1642637, 2, 0),
  (1645396, 2, 2),
  (1645514, 0, 2),
  (1651485, 1, 1),
  (1651538, 2, 2),
  (1651652, 0, 1),
  (1656165, 0, 0),
  (1661545, 2, 2),
  (1663895, 3, 2),
  (1663899, 1, 1),
  (1667503, 0, 1),
  (1668703, 1, 1),
  (1672003, 1, 0),
  (1673522, 1, 0),
  (1675084, 3, 0),
  (1681291, 3, 0),
  (1682138, 0, 2),
  (1682310, 1, 0),
  (1683393, 1, 2),
  (1683806, 1, 0),
  (1688232, 3, 1),
  (1689925, 2, 0),
  (1692124, 1, 2),
  (1692806, 2, 1),
  (1693099, 0, 0),
  (1695161, 1, 1),
  (1695314, 2, 2),
  (1698314, 1, 1),
  (1699023, 0, 0),
  (1701996, 1, 0),
  (1704854, 1, 1),
  (1706916, 2, 1),
  (1717684, 3, 2),
  (1721457, 1, 0),
  (1729388, 0, 0),
  (1729998, 0, 1),
  (1732654, 3, 0),
  (1734025, 3, 2),
  (1735546, 0, 0),
  (1736526, 1, 0),
  (1736779, 2, 2),
  (1736782, 3, 2),
  (1740304, 0, 1),
  (1743476, 0, 2),
  (1744335, 2, 0),
  (1748448, 2, 1),
  (1748454, 0, 0),
  (1750665, 1, 2),
  (1753098, 0, 1),
  (1757907, 2, 0),
  (1758754, 3, 1),
  (1762155, 2, 0),
  (1765697, 0, 0),
  (1768228, 2, 1),
  (1769555, 1, 1),
  (1771324, 1, 1),
  (1774479, 1, 0),
  (1776304, 1, 2),
  (1777493, 3, 1),
  (1777743, 2, 1),
  (1780062, 3, 0),
  (1786362, 3, 2),
  (1786550, 1, 0),
  (1788448, 3, 0),
  (1793588, 3, 2),
  (1794316, 3, 1),
  (1795275, 1, 0),
  (1799973, 1, 2),
  (1800492, 2, 2),
  (1802191, 0, 0),
  (1802451, 2, 2),
  (1808337, 2, 1),
  (1816488, 0, 2),
  (1817271, 2, 2),
  (1817702, 1, 0),
  (1821162, 0, 0),
  (1821557, 2, 0),
  (1821708, 2, 1),
  (1821952, 0, 1),
  (1822405, 3, 1),
  (1824998, 2, 2),
  (1827656, 0, 1),
  (1828024, 3, 0),
  (1828266, 2, 2),
  (1829194, 3, 1),
  (1829420, 0, 0),
  (1833107, 3, 2),
  (1833220, 2, 2),
  (1833503, 2, 1),
  (1833934, 0, 2),
  (1834105, 3, 1),
  (1835640, 2, 2),
  (1838014, 2, 0),
  (1839210, 2, 0),
  (1841075, 1, 0),
  (1841757, 3, 1),
  (1843416, 2, 1),
  (1843588, 2, 2),
  (1844416, 1, 0),
  (1844742, 1, 2),
  (1853633, 1, 2),
  (1854600, 1, 2),
  (1857554, 2, 2),
  (1859424, 0, 2),
  (1860810, 1, 2),
  (1864067, 2, 2),
  (1867873, 1, 0),
  (1869665, 3, 0),
  (1869845, 2, 1),
  (1869889, 2, 2),
  (1874728, 2, 0),
  (1874736, 3, 2),
  (1875126, 1, 2),
  (1875658, 3, 0),
  (1875706, 1, 1),
  (1884838, 1, 1),
  (1886194, 0, 1),
  (1886259, 0, 2),
  (1888011, 1, 1),
  (1890178, 3, 1),
  (1893234, 2, 2),
  (1893495, 2, 0),
  (1893699, 1, 1),
  (1899322, 1, 0),
  (1901310, 2, 0),
  (1902511, 0, 2),
  (1904007, 0, 1),
  (1905242, 0, 0),
  (1908034, 0, 2),
  (1908719, 0, 2),
  (1909402, 0, 2),
  (1912506, 3, 1),
  (1913053, 2, 0),
  (1913504, 0, 0),
  (1915430, 2, 1),
  (1917666, 1, 1),
  (1919492, 2, 1),
  (1919844, 2, 2),
  (1921673, 2, 1),
  (1923689, 2, 1),
  (1927323, 3, 0),
  (1931382, 0, 0),
  (1935255, 1, 0),
  (1937080, 0, 1),
  (1938467, 3, 2),
  (1940998, 1, 0),
  (1941916, 1, 2),
  (1943493, 2, 2),
  (1944006, 3, 2),
  (1945403, 1, 2),
  (1947165, 1, 1),
  (1948782, 0, 2),
  (1951959, 0, 2),
  (1953550, 3, 2),
  (1954919, 3, 2),
  (1958393, 2, 0),
  (1960533, 2, 0),
  (1960936, 2, 2),
  (1965696, 3, 0),
  (1967339, 3, 0),
  (1972002, 2, 2),
  (1972038, 2, 0),
  (1977281, 3, 1),
  (1982998, 2, 1),
  (1987225, 3, 1),
  (1987786, 0, 1),
  (1991936, 1, 2),
  (1994437, 3, 0),
  (1994453, 0, 2),
  (1995039, 1, 2),
  (1995923, 3, 1),
  (1996421, 1, 1),
  (1998790, 0, 2),
  (1998799, 1, 1),
  (2000523, 0, 0),
  (2001072, 1, 0),
  (2007847, 2, 1),
  (2011996, 0, 0),
  (2014295, 0, 1),
  (2014892, 3, 2),
  (2015454, 2, 1),
  (2017235, 1, 2),
  (2017348, 0, 1),
  (2018722, 0, 2),
  (2022732, 3, 1),
  (2026024, 1, 0),
  (2026229, 3, 0),
  (2028856, 1, 1),
  (2030094, 0, 0),
  (2033171, 1, 2),
  (2037732, 3, 0),
  (2039847, 0, 2),
  (2040356, 0, 1),
  (2040784, 2, 1),
  (2041598, 1, 1),
  (2041943, 2, 0),
  (2042082, 2, 1),
  (2042799, 1, 2),
  (2046497, 2, 1),
  (2047680, 3, 1),
  (2051238, 0, 1),
  (2052987, 2, 2),
  (2054091, 3, 1),
  (2054868, 0, 0),
  (2055976, 2, 1),
  (2057508, 2, 0),
  (2059108, 3, 0),
  (2061586, 2, 2),
  (2061943, 0, 0),
  (2064605, 2, 1),
  (2064652, 2, 2),
  (2065221, 0, 2),
  (2065297, 2, 2),
  (2073299, 3, 2),
  (2074092, 3, 0),
  (2079875, 1, 0),
  (2084792, 2, 2),
  (2085758, 3, 2),
  (2086714, 3, 1),
  (2086960, 1, 0),
  (2089252, 1, 0),
  (2091884, 2, 0),
  (2092558, 2, 2),
  (2093276, 0, 2),
  (2093430, 1, 1),
  (2098242, 1, 1),
  (2098699, 2, 2),
  (2101634, 3, 1),
  (2102280, 0, 0),
  (2102631, 3, 2),
  (2102706, 0, 2),
  (2105780, 1, 1),
  (2106754, 0, 0),
  (2107630, 0, 1),
  (2110126, 1, 0),
  (2112155, 0, 2),
  (2113379, 2, 2),
  (2115046, 2, 0),
  (2115658, 1, 2),
  (2117120, 1, 1),
  (2120111, 3, 2),
  (2122684, 2, 0),
  (2123467, 2, 2),
  (2124651, 1, 0),
  (2125963, 1, 2),
  (2135343, 0, 2),
  (2139498, 1, 0),
  (2139915, 1, 2),
  (2140588, 2, 1),
  (2140936, 0, 0),
  (2141228, 1, 2),
  (2143096, 3, 1),
  (2151640, 2, 2),
  (2153618, 2, 2),
  (2156401, 2, 0),
  (2159548, 2, 2),
  (2159665, 2, 1),
  (2165841, 3, 1),
  (2167337, 1, 1),
  (2168921, 1, 2),
  (2169061, 0, 1),
  (2169584, 0, 0),
  (2169755, 1, 0),
  (2170585, 0, 0),
  (2175023, 0, 1),
  (2176187, 3, 1),
  (2180004, 1, 1),
  (2180573, 3, 2),
  (2184338, 3, 2),
  (2190533, 2, 0),
  (2191366, 1, 1),
  (2192254, 3, 2),
  (2193823, 2, 1),
  (2193974, 0, 0),
  (2195809, 3, 2),
  (2196750, 1, 2),
  (2197789, 3, 0),
  (2199501, 2, 0),
  (2202129, 0, 1),
  (2205168, 1, 1),
  (2205340, 0, 0),
  (2207103, 1, 2),
  (2207494, 1, 0),
  (2209261, 2, 0),
  (2209827, 0, 2),
  (2210245, 2, 0),
  (2215458, 1, 0),
  (2223948, 0, 2),
  (2225704, 0, 0),
  (2234028, 3, 1),
  (2234213, 0, 2),
  (2238344, 3, 0),
  (2239170, 0, 1),
  (2240099, 3, 1),
  (2244147, 1, 2),
  (2245405, 2, 1),
  (2245548, 3, 1),
  (2248142, 0, 0),
  (2249710, 2, 1),
  (2250367, 2, 1),
  (2253444, 2, 2),
  (2255772, 3, 2),
  (2262759, 2, 2),
  (2263595, 1, 0),
  (2263989, 2, 2),
  (2269868, 0, 2),
  (2271420, 0, 2),
  (2272615, 0, 0),
  (2273699, 1, 2),
  (2274786, 1, 0),
  (2282332, 1, 1),
  (2285870, 1, 0),
  (2287913, 2, 0),
  (2289397, 1, 2),
  (2293182, 2, 2),
  (2294093, 2, 1),
  (2294662, 1, 1),
  (2295483, 2, 2),
  (2296196, 3, 2),
  (2300429, 3, 2),
  (2307498, 2, 1),
  (2308469, 1, 1),
  (2309840, 2, 1),
  (2313666, 0, 0),
  (2318052, 3, 0),
  (2322016, 1, 1),
  (2324046, 3, 0),
  (2324536, 3, 0),
  (2331261, 3, 0),
  (2331549, 2, 1),
  (2337345, 1, 1),
  (2337469, 1, 2),
  (2338323, 3, 2),
  (2340320, 0, 2),
  (2341012, 1, 1),
  (2343202, 2, 2),
  (2346060, 1, 0),
  (2346091, 3, 0),
  (2355946, 3, 0),
  (2356104, 0, 1),
  (2357489, 1, 1),
  (2357644, 3, 0),
  (2361523, 3, 1),
  (2363374, 3, 1),
  (2363846, 0, 2),
  (2365144, 2, 0),
  (2365217, 0, 1),
  (2365533, 1, 1),
  (2365784, 3, 1),
  (2366315, 3, 0),
  (2366748, 0, 2),
  (2368192, 3, 1),
  (2369586, 2, 2),
  (2374804, 3, 2),
  (2380861, 1, 2),
  (2381653, 0, 0),
  (2382897, 3, 0),
  (2386574, 3, 1),
  (2388323, 3, 2),
  (2391230, 3, 2),
  (2391260, 0, 0),
  (2394372, 3, 0),
  (2394881, 3, 2),
  (2395946, 2, 1),
  (2396991, 1, 0),
  (2398018, 1, 0),
  (2403168, 3, 1),
  (2403822, 1, 1),
  (2406690, 3, 2),
  (2408757, 3, 2),
  (2409081, 3, 0),
  (2411502, 0, 2),
  (2412351, 1, 2),
  (2413870, 1, 0),
  (2415832, 3, 0),
  (2418010, 0, 1),
  (2422175, 3, 2),
  (2424595, 0, 2),
  (2427413, 3, 2),
  (2429686, 0, 0),
  (2435085, 2, 1),
  (2438924, 1, 2),
  (2439340, 0, 2),
  (2440425, 2, 1),
  (2444107, 3, 2),
  (2447351, 1, 2),
  (2447730, 1, 2),
  (2447953, 1, 1),
  (2449940, 0, 2),
  (2453897, 2, 2),
  (2454858, 0, 1),
  (2457254, 2, 1),
  (2458163, 2, 0),
  (2459159, 3, 1),
  (2461438, 3, 2),
  (2464054, 1, 2),
  (2465747, 3, 2),
  (2468660, 3, 1),
  (2469514, 1, 0),
  (2471678, 3, 0),
  (2473517, 1, 2),
  (2474493, 2, 1),
  (2475109, 1, 2),
  (2475434, 1, 1),
  (2475721, 1, 2),
  (2476502, 0, 1),
  (2477478, 0, 1),
  (2477662, 2, 1),
  (2480332, 2, 1),
  (2481520, 1, 0),
  (2482821, 3, 1),
  (2484288, 1, 1),
  (2490937, 2, 1),
  (2497151, 3, 0),
  (2497424, 2, 0),
  (2499687, 1, 2),
  (2500596, 3, 1),
  (2501733, 0, 1),
  (2511944, 3, 2),
  (2513387, 0, 0),
  (2513880, 2, 0),
  (2514664, 3, 1),
  (2515208, 0, 1),
  (2517742, 1, 2),
  (2521337, 0, 1),
  (2521400, 1, 1),
  (2522928, 1, 1),
  (2527863, 2, 2),
  (2527869, 2, 2),
  (2530482, 1, 1),
  (2531547, 3, 1),
  (2535986, 2, 2),
  (2536167, 3, 2),
  (2536876, 2, 2),
  (2538145, 2, 0),
  (2538400, 2, 2),
  (2543196, 2, 0),
  (2548273, 2, 1),
  (2551237, 2, 1),
  (2551384, 3, 2),
  (2552103, 1, 0),
  (2557443, 2, 0),
  (2559032, 0, 1),
  (2559155, 1, 0),
  (2560240, 0, 1),
  (2562415, 2, 1),
  (2562622, 1, 2),
  (2564769, 1, 0),
  (2565200, 2, 0),
  (2565211, 3, 0),
  (2567320, 1, 0),
  (2569440, 3, 1),
  (2569758, 3, 0),
  (2570354, 2, 0),
  (2571243, 0, 0),
  (2571888, 1, 1),
  (2573982, 0, 1),
  (2574158, 1, 2),
  (2575852, 0, 1),
  (2578293, 3, 2),
  (2579330, 0, 2),
  (2579937, 1, 2),
  (2582860, 0, 0),
  (2586208, 1, 1),
  (2588308, 1, 1),
  (2590008, 3, 0),
  (2590076, 3, 2),
  (2590978, 2, 2),
  (2592370, 3, 2),
  (2592887, 0, 1),
  (2594038, 2, 2),
  (2596335, 1, 1),
  (2600985, 0, 1),
  (2601068, 3, 0),
  (2602171, 2, 1),
  (2602573, 1, 1),
  (2604763, 2, 2),
  (2605058, 2, 2),
  (2606926, 0, 1),
  (2607062, 2, 0),
  (2608694, 1, 1),
  (2608757, 1, 1),
  (2609405, 2, 0),
  (2611703, 0, 1),
  (2615319, 1, 0),
  (2617291, 1, 1),
  (2617548, 0, 0),
  (2618929, 0, 0),
  (2619051, 2, 1),
  (2619936, 3, 2),
  (2622370, 1, 1),
  (2624399, 0, 1),
  (2625585, 3, 0),
  (2626455, 0, 0),
  (2629171, 0, 1),
  (2631404, 3, 2),
  (2633147, 1, 2),
  (2633466, 1, 0),
  (2633542, 1, 2),
  (2634929, 0, 1),
  (2639621, 1, 0),
  (2639927, 2, 2),
  (2646605, 3, 2),
  (2646693, 1, 0),
  (2646964, 0, 0),
  (2648374, 2, 1),
  (2652879, 1, 0),
  (2653039, 1, 2),
  (2655204, 3, 1),
  (2658753, 3, 2),
  (2659586, 1, 2),
  (2662116, 1, 0),
  (2662124, 3, 1),
  (2662349, 2, 1),
  (2664131, 2, 1),
  (2664398, 2, 0),
  (2665793, 0, 1),
  (2667344, 0, 1),
  (2675903, 1, 0),
  (2676872, 3, 1),
  (2679064, 2, 0),
  (2679731, 2, 2),
  (2683792, 2, 1),
  (2687156, 0, 1),
  (2694762, 1, 2),
  (2702047, 1, 1),
  (2703309, 1, 2),
  (2706154, 0, 2),
  (2707944, 2, 2),
  (2708740, 1, 0),
  (2711090, 3, 2),
  (2711655, 3, 1),
  (2716368, 0, 1),
  (2721255, 0, 2),
  (2721467, 2, 2),
  (2722111, 0, 0),
  (2723503, 3, 2),
  (2726797, 0, 1),
  (2729467, 1, 0),
  (2732581, 1, 1),
  (2733346, 2, 2),
  (2738023, 1, 2),
  (2739278, 1, 2),
  (2740202, 1, 2),
  (2741627, 3, 1),
  (2743022, 0, 2),
  (2743105, 1, 0),
  (2743883, 3, 2),
  (2745677, 1, 0),
  (2747162, 1, 2),
  (2750972, 0, 2),
  (2751296, 1, 1),
  (2753577, 3, 2),
  (2761169, 3, 0),
  (2763473, 0, 2),
  (2764258, 1, 0),
  (2765306, 2, 1),
  (2769506, 2, 0),
  (2770928, 1, 1),
  (2772568, 1, 0),
  (2773695, 3, 0),
  (2775461, 0, 1),
  (2775965, 1, 1),
  (2777446, 1, 0),
  (2778926, 3, 1),
  (2780155, 0, 2),
  (2780675, 0, 1),
  (2783173, 0, 0),
  (2784116, 2, 1),
  (2784623, 2, 1),
  (2791061, 2, 2),
  (2791484, 2, 0),
  (2792380, 2, 1),
  (2792437, 1, 0),
  (2793998, 1, 0),
  (2795016, 1, 0),
  (2796418, 1, 2),
  (2797092, 1, 0),
  (2799353, 0, 0),
  (2799662, 3, 1),
  (2803659, 2, 0),
  (2803844, 2, 2),
  (2806393, 0, 2),
  (2810835, 2, 1),
  (2812880, 2, 2),
  (2815769, 2, 2),
  (2815954, 3, 1),
  (2816835, 1, 0),
  (2821117, 1, 1),
  (2824258, 0, 0),
  (2824262, 3, 2),
  (2824734, 3, 0),
  (2825368, 2, 0),
  (2825849, 1, 1),
  (2826380, 1, 2),
  (2826409, 0, 1),
  (2827960, 2, 2),
  (2828131, 2, 0),
  (2829314, 0, 2),
  (2829691, 0, 1),
  (2832852, 2, 0),
  (2833452, 3, 0),
  (2834429, 0, 0),
  (2836218, 1, 1),
  (2836422, 0, 1),
  (2837025, 3, 0),
  (2837190, 0, 1),
  (2837304, 3, 2),
  (2839161, 2, 2),
  (2842168, 3, 0),
  (2845597, 2, 2),
  (2849154, 1, 1),
  (2851014, 1, 0),
  (2851660, 0, 1),
  (2853578, 3, 0),
  (2853950, 2, 0),
  (2855473, 2, 1),
  (2856744, 3, 0),
  (2857571, 2, 1),
  (2858139, 2, 1),
  (2859508, 2, 2),
  (2859755, 2, 1),
  (2859921, 0, 1),
  (2860477, 1, 2),
  (2860918, 0, 0),
  (2863868, 2, 1),
  (2864834, 2, 2),
  (2866229, 1, 2),
  (2869651, 2, 1),
  (2872595, 0, 1),
  (2873797, 0, 0),
  (2873825, 0, 2),
  (2874682, 2, 0),
  (2876099, 2, 0),
  (2881333, 3, 1),
  (2885326, 3, 0),
  (2889664, 2, 1),
  (2891202, 1, 0),
  (2891909, 3, 2),
  (2892582, 1, 2),
  (2892681, 1, 2),
  (2893594, 1, 1),
  (2895005, 1, 2),
  (2896856, 1, 2),
  (2898978, 1, 0),
  (2905473, 2, 1),
  (2906935, 0, 1),
  (2907609, 0, 0),
  (2911108, 2, 2),
  (2912541, 2, 2),
  (2912796, 3, 1),
  (2915734, 0, 2),
  (2918759, 1, 1),
  (2919695, 3, 0),
  (2920903, 2, 2),
  (2922217, 3, 1),
  (2922863, 3, 1),
  (2923408, 1, 2),
  (2924724, 3, 1),
  (2929878, 0, 1),
  (2937233, 1, 0),
  (2937646, 3, 0),
  (2937758, 1, 1),
  (2939611, 0, 1),
  (2940296, 1, 0),
  (2941518, 2, 0),
  (2944352, 0, 2),
  (2944895, 3, 2),
  (2945805, 3, 2),
  (2945907, 0, 1),
  (2947240, 2, 1),
  (2950700, 0, 1),
  (2952134, 2, 0),
  (2952384, 0, 1),
  (2954653, 0, 1),
  (2957461, 1, 0),
  (2958594, 2, 0),
  (2960776, 2, 1),
  (2961238, 2, 1),
  (2962075, 0, 0),
  (2962527, 1, 2),
  (2962542, 3, 2),
  (2968942, 2, 1),
  (2970601, 0, 2),
  (2970890, 3, 2),
  (2972247, 2, 1),
  (2974583, 2, 2),
  (2974649, 2, 2),
  (2979532, 2, 2),
  (2981430, 1, 2),
  (2981916, 2, 2),
  (2982894, 0, 2),
  (2983588, 2, 0),
  (2987242, 2, 0),
  (2987682, 0, 1),
  (2989722, 1, 1),
  (2990319, 2, 2),
  (2991108, 2, 2),
  (2991473, 0, 0),
  (2993737, 3, 2),
  (2995272, 2, 0),
  (2996471, 0, 1),
  (3000920, 1, 1),
  (3003149, 2, 1),
  (3005111, 1, 0),
  (3007301, 0, 0),
  (3008362, 3, 1),
  (3014466, 2, 2),
  (3015916, 0, 0),
  (3015948, 0, 0),
  (3016735, 1, 1),
  (3020035, 3, 0),
  (3020666, 3, 2),
  (3021245, 3, 1),
  (3023077, 0, 1),
  (3025887, 3, 2),
  (3027093, 1, 1),
  (3027752, 3, 2),
  (3029085, 2, 1),
  (3029959, 1, 0),
  (3036410, 0, 2),
  (3037223, 3, 0),
  (3043537, 2, 0),
  (3045778, 2, 0),
  (3050284, 3, 2),
  (3052765, 0, 0),
  (3053901, 3, 1),
  (3058848, 1, 1),
  (3059413, 3, 2),
  (3060236, 1, 0),
  (3063411, 0, 0),
  (3064574, 0, 2),
  (3066964, 1, 2),
  (3068964, 3, 0),
  (3072671, 2, 1),
  (3074549, 2, 1),
  (3074727, 2, 2),
  (3077706, 2, 0),
  (3078180, 1, 2),
  (3078894, 1, 2),
  (3079268, 1, 2),
  (3080137, 3, 1),
  (3080303, 3, 2),
  (3082542, 1, 2),
  (3083668, 1, 0),
  (3085388, 2, 2),
  (3086327, 2, 1),
  (3086339, 0, 0),
  (3086958, 3, 2),
  (3089298, 3, 1),
  (3093737, 3, 2),
  (3095692, 2, 1),
  (3097761, 0, 2),
  (3099923, 3, 1),
  (3102394, 2, 0),
  (3103292, 0, 1),
  (3104828, 3, 2),
  (3105265, 2, 0),
  (3107388, 0, 1),
  (3107496, 3, 2),
  (3109715, 0, 2),
  (3114337, 0, 2),
  (3116032, 1, 1),
  (3121422, 1, 0),
  (3123579, 1, 0),
  (3126200, 2, 0),
  (3126842, 0, 1),
  (3128270, 3, 0),
  (3129159, 2, 0),
  (3130788, 3, 0),
  (3131128, 0, 2),
  (3131971, 2, 0),
  (3133748, 0, 2),
  (3133954, 0, 0),
  (3138877, 3, 1),
  (3140701, 0, 2),
  (3141130, 0, 2),
  (3145540, 0, 0),
  (3151175, 1, 0),
  (3154939, 1, 0),
  (3158211, 2, 1),
  (3159095, 0, 1),
  (3159096, 2, 2),
  (3162919, 1, 2),
  (3167485, 2, 1),
  (3169655, 2, 2),
  (3173070, 1, 0),
  (3173710, 0, 1),
  (3177661, 3, 1),
  (3178577, 3, 2),
  (3180456, 3, 0),
  (3180996, 1, 0),
  (3182995, 3, 1),
  (3183061, 1, 1),
  (3188874, 3, 2),
  (3189382, 2, 2),
  (3190089, 3, 0),
  (3190433, 0, 0),
  (3191238, 0, 2),
  (3193245, 0, 0),
  (3193516, 3, 1),
  (3196411, 2, 1),
  (3199221, 2, 2),
  (3203786, 0, 1),
  (3207481, 1, 0),
  (3209541, 0, 0),
  (3210038, 0, 1),
  (3217272, 1, 0),
  (3218050, 2, 0),
  (3218907, 2, 0),
  (3220342, 2, 1),
  (3220581, 2, 1),
  (3221201, 3, 2),
  (3221326, 0, 0),
  (3225762, 0, 2),
  (3226493, 3, 1),
  (3227168, 0, 0),
  (3232406, 0, 2),
  (3239083, 0, 0),
  (3241227, 2, 2),
  (3242667, 3, 0),
  (3245628, 3, 0),
  (3248012, 2, 2),
  (3248769, 1, 0),
  (3255546, 2, 2),
  (3259194, 2, 0),
  (3263260, 0, 1),
  (3263746, 2, 1),
  (3264339, 1, 1),
  (3265059, 0, 0),
  (3272422, 2, 0),
  (3274042, 3, 0),
  (3274440, 0, 1),
  (3277373, 3, 0),
  (3279902, 1, 0),
  (3280578, 2, 2),
  (3281808, 1, 0),
  (3281859, 1, 0),
  (3284899, 0, 0),
  (3285093, 0, 2),
  (3289561, 2, 0),
  (3293962, 0, 2),
  (3297674, 1, 2),
  (3297701, 2, 0),
  (3307813, 1, 0),
  (3307858, 2, 0),
  (3310460, 2, 2),
  (3313024, 0, 0),
  (3317478, 1, 2),
  (3321553, 3, 0),
  (3323890, 0, 1),
  (3326961, 0, 0),
  (3327401, 1, 0),
  (3328991, 1, 0),
  (3333644, 1, 0),
  (3334931, 1, 2),
  (3340942, 1, 2),
  (3342943, 3, 1),
  (3345316, 3, 0),
  (3348614, 0, 2),
  (3349909, 2, 2),
  (3350584, 2, 2),
  (3354566, 1, 1),
  (3363093, 1, 0),
  (3363744, 1, 2),
  (3364835, 0, 0),
  (3365456, 2, 2),
  (3367957, 0, 2),
  (3374013, 1, 0),
  (3378342, 3, 1),
  (3380785, 1, 0),
  (3381585, 2, 1),
  (3382505, 0, 0),
  (3386384, 3, 2),
  (3388032, 2, 0),
  (3389894, 3, 1),
  (3390382, 3, 0),
  (3396293, 2, 1),
  (3397291, 0, 0),
  (3412534, 1, 2),
  (3412750, 1, 1),
  (3412762, 2, 0),
  (3413161, 1, 1),
  (3414090, 1, 0),
  (3414712, 1, 0),
  (3417196, 3, 1),
  (3420425, 0, 2),
  (3422453, 1, 0),
  (3424007, 1, 0),
  (3426539, 1, 1),
  (3427922, 3, 0),
  (3429711, 0, 1),
  (3431140, 0, 1),
  (3434584, 0, 0),
  (3435078, 0, 2),
  (3437981, 3, 1),
  (3438017, 3, 0),
  (3442793, 3, 0),
  (3443689, 2, 0),
  (3444044, 0, 1),
  (3446463, 0, 1),
  (3449816, 0, 1),
  (3450572, 1, 0),
  (3452357, 2, 0),
  (3455048, 3, 1),
  (3456299, 3, 2),
  (3458577, 1, 0),
  (3459103, 3, 0),
  (3460514, 2, 1),
  (3463481, 3, 1),
  (3464640, 2, 2),
  (3464818, 2, 0),
  (3467335, 0, 2),
  (3467768, 2, 1),
  (3471176, 0, 1),
  (3473081, 2, 2),
  (3478436, 0, 1),
  (3480400, 2, 2),
  (3482728, 1, 1),
  (3482806, 1, 1),
  (3485643, 0, 2),
  (3486304, 2, 2),
  (3487850, 3, 1),
  (3488563, 1, 1),
  (3493205, 1, 1),
  (3495866, 1, 2),
  (3496145, 3, 1),
  (3496829, 1, 2),
  (3499772, 0, 0),
  (3500940, 1, 1),
  (3506644, 0, 0),
  (3509609, 2, 0),
  (3511973, 0, 0),
  (3512055, 3, 2),
  (3513920, 1, 0),
  (3514097, 1, 2),
  (3519811, 1, 2),
  (3522296, 2, 1),
  (3526559, 0, 0),
  (3527132, 2, 0),
  (3529104, 0, 0),
  (3530951, 0, 2),
  (3530952, 0, 2),
  (3531381, 2, 1),
  (3531496, 0, 1),
  (3533378, 1, 2),
  (3535215, 0, 2),
  (3535949, 2, 2),
  (3536537, 1, 0),
  (3541180, 2, 0),
  (3541597, 1, 1),
  (3541841, 2, 0),
  (3547316, 3, 1),
  (3548014, 1, 2),
  (3548052, 2, 1),
  (3551717, 1, 1),
  (3552839, 1, 1),
  (3556709, 0, 0),
  (3557312, 0, 0),
  (3560556, 3, 2),
  (3565610, 2, 1),
  (3567078, 3, 1),
  (3567600, 0, 1),
  (3571891, 3, 1),
  (3573211, 3, 1),
  (3575080, 2, 0),
  (3576945, 1, 0),
  (3579938, 3, 2),
  (3582991, 2, 2),
  (3586427, 1, 0),
])