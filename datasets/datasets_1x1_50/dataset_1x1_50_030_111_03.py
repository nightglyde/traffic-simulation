from src.util import *
schedule = deque([
  (6792, 2, 2),
  (7740, 1, 0),
  (9026, 1, 0),
  (16331, 1, 4),
  (21777, 7, 1),
  (21966, 2, 0),
  (24716, 6, 7),
  (24933, 1, 4),
  (24994, 2, 6),
  (25667, 0, 5),
  (26105, 1, 7),
  (27151, 5, 6),
  (27493, 4, 3),
  (27541, 0, 0),
  (28825, 0, 1),
  (28974, 3, 7),
  (31720, 3, 0),
  (32264, 1, 1),
  (33632, 4, 3),
  (51378, 6, 6),
  (51669, 4, 3),
  (52699, 4, 3),
  (54896, 5, 2),
  (60051, 5, 3),
  (60137, 4, 7),
  (61279, 0, 3),
  (63402, 5, 3),
  (73931, 3, 2),
  (74140, 4, 6),
  (74271, 5, 3),
  (75703, 3, 6),
  (75872, 5, 3),
  (77237, 7, 7),
  (80816, 6, 0),
  (83964, 4, 2),
  (85910, 3, 3),
  (88098, 3, 5),
  (88368, 3, 7),
  (88991, 7, 0),
  (89921, 6, 0),
  (92490, 1, 3),
  (92997, 0, 0),
  (93788, 3, 3),
  (93927, 4, 1),
  (94139, 1, 2),
  (95644, 1, 0),
  (99861, 5, 2),
  (103551, 0, 0),
  (106065, 1, 5),
  (108342, 3, 3),
  (108529, 3, 3),
  (108930, 1, 3),
  (109702, 2, 3),
  (110247, 2, 7),
  (112673, 1, 1),
  (114272, 4, 3),
  (115555, 0, 7),
  (116425, 4, 3),
  (117723, 0, 1),
  (121157, 7, 3),
  (121363, 4, 6),
  (123785, 7, 3),
  (123835, 3, 3),
  (128563, 4, 1),
  (132694, 3, 7),
  (132964, 0, 2),
  (134351, 2, 7),
  (134774, 7, 0),
  (135114, 5, 6),
  (137885, 7, 1),
  (139782, 3, 7),
  (142741, 5, 0),
  (144006, 2, 3),
  (145242, 7, 4),
  (146408, 2, 0),
  (150648, 3, 3),
  (152286, 4, 3),
  (153473, 6, 4),
  (153644, 3, 7),
  (155538, 3, 0),
  (157155, 1, 7),
  (157836, 2, 3),
  (159291, 6, 4),
  (161416, 7, 0),
  (164574, 5, 3),
  (166157, 7, 0),
  (167000, 6, 3),
  (170364, 1, 4),
  (170414, 4, 3),
  (172382, 1, 3),
  (174768, 3, 0),
  (175171, 5, 7),
  (175173, 5, 6),
  (179726, 1, 3),
  (186781, 1, 3),
  (190587, 4, 3),
  (191258, 4, 2),
  (191497, 3, 2),
  (192899, 3, 7),
  (194162, 2, 2),
  (194272, 0, 3),
  (194928, 2, 3),
  (198640, 2, 3),
  (199434, 6, 3),
  (199525, 5, 3),
  (201422, 3, 4),
  (202124, 7, 4),
  (203880, 0, 0),
  (205364, 6, 5),
  (206170, 7, 3),
  (207823, 3, 3),
  (211981, 3, 6),
  (217094, 6, 0),
  (218016, 4, 3),
  (218362, 6, 3),
  (220833, 2, 3),
  (221964, 6, 3),
  (224476, 3, 1),
  (225418, 7, 0),
  (228026, 4, 1),
  (236320, 4, 6),
  (237733, 4, 2),
  (245185, 2, 3),
  (245544, 7, 0),
  (250221, 1, 1),
  (254781, 7, 5),
  (256042, 1, 0),
  (259449, 1, 5),
  (261166, 6, 7),
  (261179, 3, 6),
  (261465, 5, 3),
  (263089, 0, 0),
  (263633, 5, 7),
  (265835, 4, 7),
  (268298, 2, 7),
  (268841, 3, 3),
  (269304, 0, 4),
  (270772, 0, 4),
  (271353, 2, 3),
  (271499, 6, 7),
  (276461, 5, 2),
  (278428, 4, 3),
  (280869, 4, 3),
  (286037, 1, 0),
  (287824, 3, 3),
  (288354, 7, 4),
  (290027, 4, 7),
  (290486, 6, 0),
  (290547, 1, 0),
  (290909, 7, 5),
  (293966, 4, 6),
  (297169, 7, 6),
  (302095, 0, 0),
  (302197, 4, 3),
  (302472, 1, 5),
  (304242, 1, 0),
  (305794, 6, 7),
  (305844, 2, 3),
  (307171, 4, 0),
  (307411, 0, 4),
  (311890, 6, 4),
  (315820, 1, 0),
  (317840, 5, 5),
  (319362, 3, 3),
  (319837, 2, 4),
  (320120, 3, 6),
  (322827, 0, 6),
  (325320, 6, 0),
  (327368, 7, 0),
  (327867, 6, 0),
  (328571, 7, 1),
  (329369, 0, 7),
  (343099, 1, 4),
  (344462, 2, 6),
  (345796, 4, 2),
  (346107, 0, 0),
  (347478, 7, 7),
  (347777, 4, 1),
  (349947, 1, 4),
  (350194, 0, 7),
  (350545, 5, 2),
  (350714, 3, 3),
  (351297, 6, 0),
  (356243, 7, 4),
  (356883, 7, 0),
  (357531, 3, 2),
  (360965, 2, 2),
  (361863, 1, 3),
  (362141, 2, 3),
  (363461, 5, 7),
  (365087, 6, 0),
  (366982, 7, 5),
  (369690, 3, 7),
  (372893, 1, 4),
  (374459, 1, 3),
  (375109, 7, 0),
  (382752, 5, 7),
  (382850, 6, 0),
  (382884, 4, 5),
  (384561, 7, 0),
  (388383, 2, 3),
  (389546, 2, 4),
  (389747, 5, 3),
  (390046, 0, 3),
  (390461, 7, 2),
  (392735, 5, 3),
  (393962, 3, 6),
  (394053, 0, 0),
  (394913, 4, 7),
  (399450, 4, 7),
  (400694, 1, 6),
  (401900, 1, 7),
  (406395, 2, 1),
  (409115, 4, 4),
  (409719, 5, 6),
  (418213, 3, 6),
  (419991, 7, 0),
  (420784, 4, 3),
  (420786, 1, 3),
  (421376, 7, 0),
  (423481, 0, 4),
  (423613, 7, 0),
  (425046, 7, 0),
  (427361, 3, 3),
  (427555, 5, 0),
  (429841, 7, 2),
  (430030, 4, 6),
  (430520, 6, 4),
  (431037, 3, 3),
  (434906, 0, 3),
  (435531, 4, 6),
  (437130, 5, 6),
  (439870, 6, 0),
  (440534, 5, 3),
  (442036, 0, 3),
  (447576, 2, 5),
  (448087, 1, 0),
  (448146, 1, 0),
  (449936, 7, 0),
  (450604, 4, 3),
  (451528, 6, 2),
  (452596, 5, 7),
  (454293, 3, 2),
  (457325, 3, 6),
  (460792, 5, 2),
  (461506, 1, 4),
  (462830, 2, 6),
  (464613, 6, 0),
  (464636, 4, 3),
  (468377, 5, 3),
  (468654, 6, 0),
  (470320, 1, 7),
  (478229, 7, 0),
  (479621, 4, 3),
  (482786, 1, 6),
  (483953, 0, 0),
  (486191, 1, 3),
  (490894, 5, 4),
  (493449, 4, 3),
  (495052, 0, 0),
  (495728, 6, 4),
  (495850, 0, 4),
  (498885, 3, 3),
  (502191, 0, 0),
  (502549, 3, 0),
  (507893, 5, 5),
  (511613, 2, 3),
  (514830, 7, 0),
  (515872, 3, 3),
  (515943, 1, 7),
  (516689, 6, 0),
  (523519, 1, 7),
  (528769, 3, 1),
  (530547, 3, 2),
  (530910, 4, 3),
  (531501, 2, 3),
  (533087, 5, 3),
  (540278, 1, 0),
  (540604, 3, 7),
  (544621, 0, 0),
  (547117, 1, 7),
  (550281, 5, 4),
  (550796, 2, 2),
  (552806, 4, 3),
  (553782, 2, 6),
  (554334, 0, 0),
  (558577, 7, 7),
  (558800, 7, 7),
  (558898, 1, 5),
  (559463, 5, 2),
  (559465, 4, 1),
  (559992, 1, 5),
  (560596, 7, 4),
  (560619, 7, 5),
  (563641, 7, 2),
  (564643, 6, 3),
  (571735, 7, 7),
  (572120, 5, 3),
  (572426, 0, 5),
  (577825, 4, 2),
  (581062, 4, 3),
  (581707, 3, 6),
  (584283, 3, 3),
  (585120, 0, 3),
  (586253, 2, 7),
  (587044, 6, 0),
  (587389, 2, 7),
  (588044, 5, 5),
  (591619, 7, 4),
  (593087, 1, 7),
  (593834, 7, 0),
  (595058, 6, 4),
  (596523, 6, 0),
  (596645, 0, 7),
  (606948, 0, 3),
  (614778, 7, 0),
  (619163, 2, 7),
  (620111, 6, 0),
  (621402, 3, 3),
  (623099, 2, 3),
  (623455, 7, 0),
  (625070, 4, 3),
  (625260, 3, 3),
  (626503, 5, 3),
  (627411, 4, 3),
  (631935, 0, 0),
  (632162, 6, 6),
  (632664, 1, 5),
  (637318, 6, 0),
  (638876, 7, 5),
  (639556, 3, 2),
  (641232, 7, 5),
  (644029, 6, 3),
  (644155, 0, 0),
  (647149, 6, 3),
  (650382, 6, 2),
  (651469, 0, 0),
  (652233, 7, 0),
  (655626, 6, 0),
  (656493, 5, 3),
  (656758, 0, 0),
  (657188, 3, 3),
  (659612, 2, 2),
  (660354, 3, 3),
  (660628, 5, 2),
  (662860, 7, 1),
  (669245, 7, 7),
  (673372, 2, 3),
  (678919, 3, 3),
  (681902, 6, 6),
  (690629, 3, 6),
  (691466, 0, 5),
  (692975, 7, 0),
  (693490, 4, 3),
  (695071, 6, 0),
  (695144, 7, 3),
  (695905, 5, 2),
  (696576, 0, 5),
  (697719, 5, 7),
  (698230, 0, 0),
  (698406, 7, 3),
  (702388, 5, 3),
  (703753, 2, 6),
  (703917, 1, 7),
  (705266, 7, 4),
  (706058, 2, 3),
  (707558, 2, 3),
  (712969, 2, 3),
  (713099, 2, 3),
  (714433, 0, 0),
  (718459, 1, 3),
  (720746, 6, 0),
  (726035, 0, 1),
  (728838, 4, 3),
  (729611, 1, 7),
  (731348, 0, 3),
  (732202, 5, 5),
  (737638, 2, 0),
  (737929, 5, 3),
  (738415, 0, 3),
  (740562, 6, 1),
  (740641, 3, 3),
  (745713, 0, 4),
  (746068, 3, 7),
  (748452, 4, 3),
  (748647, 3, 3),
  (750913, 1, 0),
  (751031, 5, 7),
  (752256, 0, 0),
  (752404, 0, 0),
  (753415, 2, 3),
  (753692, 6, 6),
  (756485, 2, 3),
  (758399, 1, 7),
  (760587, 7, 4),
  (762491, 5, 3),
  (766076, 2, 3),
  (766414, 3, 6),
  (768762, 4, 3),
  (769276, 6, 4),
  (772612, 5, 3),
  (776839, 2, 6),
  (778998, 2, 7),
  (782270, 6, 0),
  (783135, 0, 0),
  (785142, 3, 3),
  (785884, 1, 2),
  (786286, 7, 6),
  (787127, 2, 7),
  (787332, 0, 2),
  (791205, 5, 2),
  (793030, 2, 6),
  (798306, 7, 2),
  (798965, 6, 5),
  (803139, 5, 7),
  (805439, 5, 4),
  (805615, 6, 3),
  (806114, 6, 4),
  (807129, 6, 7),
  (807818, 0, 3),
  (808717, 7, 5),
  (809535, 0, 0),
  (809582, 3, 6),
  (815758, 2, 7),
  (818604, 2, 3),
  (819923, 1, 4),
  (820362, 2, 3),
  (821492, 2, 1),
  (824551, 2, 7),
  (825116, 6, 0),
  (829128, 7, 0),
  (829396, 5, 7),
  (829793, 0, 6),
  (832469, 4, 2),
  (832558, 2, 2),
  (834213, 2, 7),
  (838879, 5, 7),
  (839967, 0, 3),
  (841335, 6, 0),
  (841374, 2, 3),
  (842222, 5, 1),
  (842403, 4, 3),
  (848851, 2, 3),
  (851242, 4, 4),
  (851997, 0, 7),
  (855250, 3, 2),
  (856480, 6, 6),
  (867234, 4, 3),
  (867337, 3, 4),
  (868594, 2, 7),
  (870781, 5, 2),
  (871479, 1, 7),
  (874310, 2, 3),
  (876759, 0, 0),
  (877269, 3, 6),
  (878973, 2, 3),
  (880460, 2, 6),
  (882797, 7, 5),
  (883139, 2, 1),
  (884320, 3, 1),
  (885618, 6, 0),
  (888038, 0, 0),
  (893506, 2, 5),
  (894709, 1, 0),
  (894998, 0, 0),
  (898539, 3, 4),
  (900180, 3, 1),
  (900248, 5, 3),
  (902792, 1, 7),
  (905565, 1, 4),
  (906005, 1, 6),
  (908184, 4, 7),
  (909807, 2, 3),
  (910397, 5, 2),
  (911735, 7, 7),
  (917620, 3, 7),
  (918435, 0, 4),
  (921623, 2, 3),
  (922310, 0, 6),
  (925888, 5, 3),
  (926788, 3, 2),
  (927332, 3, 3),
  (929968, 4, 3),
  (932050, 2, 3),
  (936152, 6, 0),
  (936261, 1, 1),
  (936268, 4, 6),
  (942315, 2, 3),
  (944025, 4, 3),
  (945572, 7, 0),
  (946553, 3, 0),
  (947169, 7, 3),
  (952551, 6, 0),
  (952741, 2, 4),
  (956361, 2, 6),
  (956730, 3, 3),
  (957991, 6, 7),
  (963637, 3, 3),
  (965868, 1, 2),
  (968093, 4, 3),
  (969817, 0, 4),
  (971208, 2, 4),
  (971924, 2, 3),
  (972292, 6, 0),
  (974566, 1, 0),
  (975954, 0, 0),
  (976073, 0, 6),
  (979865, 3, 3),
  (983172, 1, 0),
  (992395, 3, 4),
  (994243, 7, 3),
  (996029, 0, 3),
  (1001345, 4, 7),
  (1001797, 1, 4),
  (1002492, 1, 0),
  (1002833, 0, 7),
  (1003987, 6, 0),
  (1006711, 0, 0),
  (1007540, 7, 0),
  (1011887, 0, 7),
  (1012129, 0, 0),
  (1012334, 4, 6),
  (1012445, 3, 3),
  (1019265, 4, 6),
  (1022329, 4, 7),
  (1024296, 4, 7),
  (1025554, 2, 3),
  (1034999, 1, 4),
  (1036428, 4, 3),
  (1038785, 6, 0),
  (1038925, 0, 4),
  (1041913, 2, 6),
  (1042024, 1, 2),
  (1043355, 5, 7),
  (1049278, 7, 0),
  (1054101, 4, 2),
  (1057075, 3, 3),
  (1060362, 6, 3),
  (1063481, 7, 3),
  (1064038, 6, 3),
  (1066682, 6, 5),
  (1068023, 3, 5),
  (1069111, 3, 3),
  (1069174, 1, 7),
  (1069762, 5, 1),
  (1070198, 3, 0),
  (1071071, 1, 0),
  (1072292, 1, 4),
  (1073041, 6, 5),
  (1074452, 0, 0),
  (1074564, 2, 3),
  (1082095, 0, 0),
  (1082607, 6, 7),
  (1082618, 4, 3),
  (1087596, 0, 0),
  (1089804, 1, 4),
  (1091461, 4, 3),
  (1093337, 5, 3),
  (1095795, 5, 6),
  (1096147, 7, 0),
  (1100676, 2, 3),
  (1102797, 7, 2),
  (1102906, 3, 2),
  (1103492, 6, 3),
  (1104135, 4, 3),
  (1104603, 5, 3),
  (1104637, 6, 4),
  (1105063, 4, 3),
  (1108034, 4, 3),
  (1108544, 7, 5),
  (1111339, 7, 6),
  (1111609, 3, 3),
  (1112363, 7, 4),
  (1112438, 6, 1),
  (1114515, 3, 3),
  (1114534, 6, 0),
  (1116346, 5, 6),
  (1117081, 2, 3),
  (1118928, 0, 4),
  (1121809, 4, 6),
  (1122828, 6, 7),
  (1124104, 3, 7),
  (1125112, 0, 0),
  (1125614, 2, 3),
  (1125958, 0, 4),
  (1130723, 6, 2),
  (1131235, 5, 7),
  (1132059, 5, 6),
  (1132593, 4, 3),
  (1140836, 4, 2),
  (1141718, 1, 0),
  (1143904, 5, 2),
  (1144460, 6, 5),
  (1147768, 6, 1),
  (1149678, 3, 3),
  (1151721, 6, 7),
  (1155748, 4, 6),
  (1158274, 3, 6),
  (1158829, 5, 5),
  (1160970, 3, 7),
  (1163325, 0, 0),
  (1163548, 7, 7),
  (1165974, 6, 4),
  (1166165, 0, 0),
  (1166780, 3, 3),
  (1167201, 1, 0),
  (1173497, 4, 5),
  (1175165, 6, 0),
  (1179517, 1, 6),
  (1182047, 1, 1),
  (1182094, 5, 1),
  (1182957, 0, 0),
  (1184153, 3, 7),
  (1185585, 4, 7),
  (1186261, 0, 4),
  (1186336, 0, 0),
  (1189646, 4, 0),
  (1192058, 6, 7),
  (1192155, 4, 7),
  (1193439, 7, 0),
  (1195540, 6, 0),
  (1197059, 0, 4),
  (1200006, 2, 5),
  (1201706, 2, 6),
  (1204597, 2, 3),
  (1209009, 4, 7),
  (1209748, 0, 0),
  (1210888, 3, 1),
  (1212321, 0, 0),
  (1213006, 4, 2),
  (1213514, 6, 7),
  (1214414, 3, 3),
  (1215478, 6, 0),
  (1215957, 6, 3),
  (1216090, 1, 7),
  (1217076, 3, 3),
  (1217279, 0, 2),
  (1217341, 0, 5),
  (1220337, 0, 0),
  (1223193, 2, 3),
  (1227859, 4, 6),
  (1229789, 3, 2),
  (1233276, 6, 0),
  (1233793, 5, 3),
  (1242409, 6, 0),
  (1243241, 2, 3),
  (1249927, 5, 3),
  (1253348, 3, 3),
  (1255258, 6, 0),
  (1256971, 0, 0),
  (1260463, 5, 0),
  (1261520, 7, 0),
  (1264760, 7, 1),
  (1266202, 1, 3),
  (1274702, 6, 0),
  (1274751, 5, 3),
  (1276748, 5, 7),
  (1278582, 7, 7),
  (1279594, 2, 7),
  (1286386, 1, 7),
  (1287062, 4, 3),
  (1288766, 0, 3),
  (1288980, 5, 3),
  (1295945, 0, 4),
  (1297580, 5, 0),
  (1297914, 1, 4),
  (1298856, 2, 7),
  (1301889, 6, 0),
  (1302005, 6, 3),
  (1304940, 3, 3),
  (1306209, 4, 3),
  (1311586, 7, 6),
  (1311834, 1, 7),
  (1313442, 5, 6),
  (1315642, 6, 7),
  (1315971, 2, 5),
  (1319131, 3, 2),
  (1319196, 7, 4),
  (1319398, 7, 2),
  (1320180, 4, 3),
  (1321472, 1, 0),
  (1322382, 3, 7),
  (1322413, 1, 0),
  (1324870, 2, 1),
  (1326190, 1, 7),
  (1326954, 0, 5),
  (1327829, 5, 6),
  (1330054, 5, 3),
  (1330328, 6, 6),
  (1331946, 1, 6),
  (1331993, 6, 4),
  (1332643, 5, 3),
  (1332702, 3, 6),
  (1335190, 4, 4),
  (1337971, 4, 2),
  (1344173, 0, 4),
  (1344984, 6, 6),
  (1346254, 6, 6),
  (1346303, 1, 4),
  (1347531, 1, 0),
  (1351735, 3, 7),
  (1352023, 2, 6),
  (1352760, 5, 3),
  (1353149, 0, 3),
  (1355418, 5, 3),
  (1359677, 5, 3),
  (1362467, 2, 3),
  (1366584, 5, 3),
  (1367859, 0, 0),
  (1369119, 4, 6),
  (1373046, 4, 6),
  (1374749, 1, 2),
  (1379992, 6, 0),
  (1382086, 6, 0),
  (1383173, 7, 3),
  (1383271, 3, 0),
  (1383374, 4, 6),
  (1383991, 3, 3),
  (1387221, 0, 7),
  (1389545, 3, 2),
  (1390288, 2, 6),
  (1391261, 0, 0),
  (1395561, 2, 7),
  (1399282, 3, 0),
  (1403371, 0, 0),
  (1405742, 2, 0),
  (1408135, 3, 6),
  (1412089, 7, 7),
  (1413315, 2, 4),
  (1418162, 6, 0),
  (1421029, 0, 5),
  (1425432, 2, 3),
  (1430242, 3, 7),
  (1430695, 0, 1),
  (1431356, 3, 3),
  (1432368, 5, 3),
  (1437462, 4, 7),
  (1441011, 5, 7),
  (1441071, 6, 4),
  (1442031, 0, 1),
  (1444091, 3, 6),
  (1444320, 3, 6),
  (1444681, 1, 4),
  (1444819, 6, 2),
  (1447132, 0, 0),
  (1447799, 6, 0),
  (1448670, 0, 0),
  (1450325, 4, 3),
  (1450386, 7, 0),
  (1452597, 4, 3),
  (1455037, 2, 6),
  (1458685, 4, 3),
  (1458747, 0, 0),
  (1465788, 6, 7),
  (1466166, 6, 0),
  (1467407, 5, 5),
  (1469637, 0, 2),
  (1470890, 6, 4),
  (1472104, 1, 3),
  (1475596, 6, 0),
  (1476395, 5, 1),
  (1476574, 7, 2),
  (1477347, 7, 7),
  (1480450, 5, 3),
  (1481000, 1, 4),
  (1485562, 7, 7),
  (1486444, 6, 3),
  (1487192, 1, 0),
  (1487494, 2, 3),
  (1489766, 3, 3),
  (1494327, 0, 3),
  (1494454, 5, 6),
  (1495100, 7, 6),
  (1496277, 1, 0),
  (1497449, 4, 3),
  (1498426, 1, 0),
  (1499165, 3, 6),
  (1501340, 1, 3),
  (1501425, 4, 2),
  (1502236, 3, 5),
  (1508420, 4, 3),
  (1509764, 4, 3),
  (1510388, 0, 2),
  (1513574, 6, 0),
  (1514158, 0, 3),
  (1515551, 1, 0),
  (1516082, 0, 4),
  (1516334, 6, 0),
  (1518148, 5, 6),
  (1518637, 3, 6),
  (1525611, 0, 0),
  (1530873, 5, 1),
  (1532403, 6, 4),
  (1535959, 6, 2),
  (1537456, 4, 6),
  (1540361, 5, 2),
  (1540692, 1, 0),
  (1542461, 3, 7),
  (1544248, 3, 3),
  (1544659, 2, 2),
  (1545176, 6, 0),
  (1545338, 4, 3),
  (1547319, 0, 2),
  (1556341, 1, 7),
  (1561819, 5, 3),
  (1563642, 6, 0),
  (1564727, 1, 4),
  (1567723, 2, 7),
  (1568097, 4, 3),
  (1569220, 6, 6),
  (1569450, 1, 7),
  (1569534, 3, 3),
  (1570337, 0, 0),
  (1572430, 5, 3),
  (1572863, 3, 3),
  (1574103, 7, 4),
  (1578007, 6, 3),
  (1580815, 1, 7),
  (1583175, 7, 2),
  (1592720, 7, 3),
  (1598410, 7, 7),
  (1599789, 1, 0),
  (1600142, 7, 3),
  (1603221, 7, 4),
  (1603329, 0, 7),
  (1606393, 2, 3),
  (1607467, 1, 0),
  (1609030, 1, 1),
  (1609868, 1, 0),
  (1611611, 6, 0),
  (1619212, 7, 7),
  (1620396, 5, 2),
  (1621681, 4, 7),
  (1624341, 6, 5),
  (1629463, 3, 2),
  (1632444, 6, 2),
  (1634480, 5, 3),
  (1635536, 4, 3),
  (1637637, 6, 7),
  (1638330, 5, 7),
  (1640842, 0, 4),
  (1640894, 3, 1),
  (1643065, 4, 4),
  (1645590, 3, 4),
  (1646894, 7, 7),
  (1650998, 3, 3),
  (1652505, 7, 0),
  (1653572, 7, 0),
  (1653612, 2, 7),
  (1655833, 1, 7),
  (1656601, 3, 7),
  (1660943, 3, 3),
  (1661367, 3, 6),
  (1662356, 3, 2),
  (1666622, 5, 3),
  (1670035, 3, 6),
  (1670343, 7, 0),
  (1673097, 6, 0),
  (1675898, 6, 0),
  (1681659, 3, 3),
  (1684707, 3, 2),
  (1689454, 6, 4),
  (1691078, 4, 3),
  (1691183, 6, 1),
  (1694559, 2, 5),
  (1694604, 0, 0),
  (1704355, 6, 4),
  (1705202, 1, 0),
  (1710933, 0, 4),
  (1713744, 2, 3),
  (1723988, 4, 6),
  (1724755, 6, 0),
  (1725340, 3, 7),
  (1726109, 0, 0),
  (1728606, 5, 3),
  (1728800, 7, 0),
  (1730047, 4, 2),
  (1731448, 6, 0),
  (1731495, 2, 3),
  (1736089, 6, 0),
  (1737933, 3, 7),
  (1738685, 6, 0),
  (1739460, 1, 3),
  (1742601, 7, 1),
  (1742972, 4, 3),
  (1746495, 7, 0),
  (1746735, 1, 6),
  (1751057, 5, 3),
  (1753550, 0, 0),
  (1756584, 1, 0),
  (1760601, 5, 3),
  (1762056, 0, 0),
  (1763132, 1, 4),
  (1763392, 7, 3),
  (1764226, 4, 3),
  (1766252, 5, 2),
  (1766287, 0, 3),
  (1769978, 7, 6),
  (1770866, 0, 3),
  (1771225, 7, 0),
  (1772643, 7, 5),
  (1775618, 7, 0),
  (1776004, 1, 0),
  (1777059, 0, 0),
  (1778184, 5, 4),
  (1778794, 3, 3),
  (1781617, 3, 3),
  (1784037, 5, 2),
  (1784657, 1, 4),
  (1785765, 6, 0),
  (1786846, 7, 5),
  (1787362, 1, 0),
  (1787773, 0, 2),
  (1791710, 0, 6),
  (1792479, 2, 1),
  (1793527, 5, 2),
  (1797302, 6, 1),
  (1798394, 0, 2),
  (1798533, 5, 3),
  (1798577, 2, 5),
  (1799122, 2, 3),
  (1802608, 3, 3),
  (1803907, 3, 3),
  (1807003, 1, 7),
  (1807940, 4, 6),
  (1815556, 7, 0),
  (1815666, 6, 3),
  (1819225, 6, 0),
  (1819263, 2, 3),
  (1819678, 2, 0),
  (1820008, 4, 7),
  (1820772, 7, 0),
  (1820877, 0, 7),
  (1821660, 6, 0),
  (1822232, 1, 0),
  (1824797, 0, 6),
  (1826334, 5, 3),
  (1831629, 6, 0),
  (1831858, 0, 5),
  (1834207, 0, 0),
  (1835995, 4, 5),
  (1837040, 1, 7),
  (1837212, 0, 0),
  (1838114, 6, 7),
  (1844150, 6, 0),
  (1845111, 2, 6),
  (1845825, 0, 0),
  (1851255, 7, 2),
  (1851449, 0, 3),
  (1853598, 3, 3),
  (1857249, 4, 3),
  (1859639, 7, 0),
  (1860286, 2, 3),
  (1863403, 5, 0),
  (1864155, 0, 7),
  (1866025, 7, 5),
  (1870216, 6, 2),
  (1870687, 0, 5),
  (1872562, 1, 3),
  (1875128, 3, 2),
  (1882936, 1, 7),
  (1885413, 5, 3),
  (1889659, 7, 7),
  (1890381, 6, 0),
  (1893142, 3, 3),
  (1895208, 4, 2),
  (1897679, 4, 6),
  (1899330, 4, 3),
  (1901862, 2, 3),
  (1904879, 6, 0),
  (1906509, 6, 7),
  (1906835, 3, 2),
  (1907654, 2, 2),
  (1910807, 3, 3),
  (1911060, 1, 4),
  (1911766, 2, 7),
  (1914028, 5, 3),
  (1922326, 4, 3),
  (1923348, 4, 3),
  (1923465, 4, 6),
  (1923528, 5, 4),
  (1924761, 6, 5),
  (1929880, 6, 0),
  (1932725, 5, 2),
  (1934216, 1, 7),
  (1934676, 7, 6),
  (1936109, 6, 1),
  (1942112, 7, 0),
  (1942239, 2, 3),
  (1943293, 0, 3),
  (1951468, 5, 2),
  (1952207, 3, 6),
  (1952277, 5, 7),
  (1954046, 2, 3),
  (1955134, 5, 3),
  (1960557, 4, 3),
  (1962700, 5, 7),
  (1964381, 0, 3),
  (1965019, 4, 5),
  (1967900, 3, 6),
  (1969550, 6, 0),
  (1973043, 2, 3),
  (1975030, 3, 0),
  (1975467, 6, 0),
  (1976967, 1, 2),
  (1979602, 4, 2),
  (1980712, 5, 0),
  (1981335, 7, 0),
  (1985270, 6, 0),
  (1988271, 0, 0),
  (1988695, 6, 0),
  (1989974, 3, 3),
  (1992928, 6, 0),
  (1993065, 1, 3),
  (2001716, 5, 3),
  (2001905, 5, 3),
  (2002447, 5, 2),
  (2006605, 7, 6),
  (2006625, 3, 6),
  (2009784, 6, 7),
  (2013857, 6, 4),
  (2014004, 5, 2),
  (2015040, 2, 2),
  (2015694, 5, 3),
  (2017354, 1, 7),
  (2018344, 7, 6),
  (2022114, 3, 2),
  (2026271, 3, 7),
  (2026795, 3, 5),
  (2028206, 5, 3),
  (2030927, 7, 0),
  (2031003, 5, 7),
  (2033245, 1, 0),
  (2034734, 3, 6),
  (2038913, 0, 6),
  (2039760, 0, 4),
  (2040419, 2, 3),
  (2041760, 3, 7),
  (2044279, 2, 3),
  (2044313, 1, 0),
  (2044934, 6, 0),
  (2045414, 0, 1),
  (2045813, 0, 0),
  (2049853, 3, 0),
  (2051262, 1, 4),
  (2052363, 5, 6),
  (2055343, 2, 7),
  (2056613, 4, 5),
  (2058557, 3, 3),
  (2059909, 4, 3),
  (2063361, 6, 4),
  (2068315, 5, 2),
  (2069329, 5, 3),
  (2070083, 4, 3),
  (2073088, 7, 0),
  (2077978, 6, 7),
  (2079512, 2, 6),
  (2080252, 5, 2),
  (2082351, 2, 3),
  (2084949, 1, 6),
  (2085220, 4, 0),
  (2088354, 4, 4),
  (2090440, 5, 3),
  (2091820, 0, 7),
  (2097329, 2, 6),
  (2097913, 5, 6),
  (2097946, 2, 7),
  (2098869, 5, 4),
  (2102843, 0, 7),
  (2105016, 3, 3),
  (2106819, 1, 0),
  (2106883, 0, 0),
  (2108540, 7, 0),
  (2109469, 7, 7),
  (2110094, 4, 7),
  (2110998, 4, 3),
  (2111403, 7, 3),
  (2113155, 0, 7),
  (2114743, 1, 0),
  (2115255, 4, 6),
  (2117365, 2, 7),
  (2122895, 6, 3),
  (2122948, 1, 1),
  (2123007, 1, 3),
  (2127522, 7, 0),
  (2128525, 5, 3),
  (2129115, 7, 1),
  (2129132, 6, 0),
  (2129648, 0, 3),
  (2131096, 0, 0),
  (2131820, 4, 3),
  (2138224, 6, 0),
  (2143957, 1, 0),
  (2145049, 7, 0),
  (2146791, 3, 3),
  (2147623, 3, 2),
  (2148268, 5, 3),
  (2148919, 2, 7),
  (2152490, 7, 0),
  (2152622, 6, 4),
  (2155550, 1, 0),
  (2156956, 3, 4),
  (2159271, 6, 0),
  (2159439, 3, 2),
  (2159761, 5, 6),
  (2161610, 7, 7),
  (2164011, 4, 3),
  (2168303, 6, 3),
  (2172046, 0, 3),
  (2175916, 7, 0),
  (2176280, 1, 0),
  (2176830, 2, 3),
  (2177550, 0, 5),
  (2184058, 1, 0),
  (2184727, 4, 7),
  (2185229, 6, 4),
  (2187005, 0, 0),
  (2187682, 7, 0),
  (2191897, 3, 7),
  (2193686, 6, 7),
  (2195654, 0, 7),
  (2196333, 1, 5),
  (2196417, 1, 0),
  (2201627, 2, 3),
  (2201742, 2, 3),
  (2203972, 2, 7),
  (2207749, 7, 5),
  (2207900, 2, 6),
  (2208039, 5, 2),
  (2208623, 3, 4),
  (2210003, 3, 3),
  (2212225, 7, 6),
  (2213434, 6, 7),
  (2213727, 3, 3),
  (2214275, 5, 1),
  (2217126, 2, 3),
  (2222479, 6, 0),
  (2223881, 1, 3),
  (2227957, 6, 0),
  (2230248, 6, 0),
  (2235188, 5, 2),
  (2235982, 2, 6),
  (2237601, 2, 3),
  (2239376, 0, 0),
  (2239692, 0, 0),
  (2244046, 7, 4),
  (2246347, 2, 0),
  (2248072, 0, 0),
  (2248873, 6, 1),
  (2250459, 3, 3),
  (2260675, 3, 2),
  (2261964, 7, 0),
  (2264592, 2, 3),
  (2264832, 2, 3),
  (2282999, 6, 7),
  (2286673, 4, 2),
  (2288325, 6, 7),
  (2289611, 5, 2),
  (2291072, 3, 7),
  (2291923, 5, 3),
  (2297586, 3, 3),
  (2301072, 3, 3),
  (2301463, 6, 2),
  (2302021, 5, 5),
  (2305775, 7, 0),
  (2305859, 0, 0),
  (2308387, 1, 3),
  (2309924, 1, 0),
  (2310927, 7, 0),
  (2314517, 1, 0),
  (2314634, 0, 3),
  (2316654, 0, 6),
  (2317230, 1, 2),
  (2317799, 7, 7),
  (2318010, 5, 3),
  (2320787, 7, 4),
  (2324580, 7, 0),
  (2328584, 0, 5),
  (2329338, 5, 7),
  (2329867, 4, 3),
  (2329889, 5, 7),
  (2331871, 5, 6),
  (2332316, 2, 2),
  (2334406, 3, 7),
  (2336280, 0, 0),
  (2339485, 0, 4),
  (2341201, 4, 0),
  (2342579, 1, 0),
  (2345916, 4, 7),
  (2348224, 0, 4),
  (2349982, 5, 6),
  (2350934, 1, 7),
  (2351559, 1, 4),
  (2352187, 7, 0),
  (2354338, 2, 3),
  (2355130, 1, 0),
  (2356829, 2, 4),
  (2357478, 0, 4),
  (2363331, 0, 4),
  (2363732, 3, 2),
  (2364987, 5, 3),
  (2365869, 3, 3),
  (2369344, 1, 0),
  (2369583, 3, 3),
  (2370044, 4, 3),
  (2372034, 2, 1),
  (2372534, 5, 3),
  (2373795, 2, 7),
  (2377366, 2, 7),
  (2379079, 4, 3),
  (2379838, 0, 0),
  (2383940, 3, 3),
  (2384322, 1, 4),
  (2385206, 7, 3),
  (2387283, 5, 2),
  (2390273, 4, 2),
  (2398212, 0, 0),
  (2398855, 4, 3),
  (2401222, 7, 7),
  (2401849, 6, 3),
  (2404235, 6, 4),
  (2404639, 0, 7),
  (2406061, 0, 5),
  (2407816, 0, 0),
  (2408341, 0, 6),
  (2415382, 0, 2),
  (2417477, 2, 7),
  (2417504, 1, 4),
  (2418512, 7, 7),
  (2421472, 1, 0),
  (2422102, 4, 2),
  (2422171, 5, 2),
  (2424105, 2, 6),
  (2427279, 0, 0),
  (2428716, 7, 0),
  (2428854, 0, 6),
  (2429841, 3, 2),
  (2431289, 7, 7),
  (2431563, 4, 3),
  (2439532, 5, 2),
  (2439627, 5, 3),
  (2441413, 5, 3),
  (2443111, 3, 3),
  (2447354, 6, 7),
  (2450252, 5, 3),
  (2450363, 5, 2),
  (2454310, 3, 3),
  (2454591, 7, 0),
  (2458910, 6, 0),
  (2459342, 4, 3),
  (2460402, 2, 3),
  (2460765, 3, 2),
  (2466051, 5, 2),
  (2466751, 3, 7),
  (2469923, 0, 0),
  (2471727, 2, 7),
  (2471979, 5, 2),
  (2473392, 7, 3),
  (2475242, 5, 5),
  (2477344, 5, 3),
  (2481644, 0, 7),
  (2482895, 1, 3),
  (2487422, 4, 2),
  (2492614, 4, 3),
  (2496960, 2, 3),
  (2498838, 6, 0),
  (2506658, 6, 0),
  (2506973, 3, 3),
  (2509149, 5, 6),
  (2509192, 4, 2),
  (2509906, 4, 3),
  (2519116, 6, 7),
  (2519152, 1, 0),
  (2519507, 4, 3),
  (2520092, 1, 3),
  (2521845, 0, 0),
  (2523983, 7, 3),
  (2528274, 1, 0),
  (2528775, 1, 7),
  (2530901, 2, 3),
  (2533220, 3, 7),
  (2533471, 0, 6),
  (2533485, 7, 0),
  (2536663, 7, 0),
  (2537262, 1, 0),
  (2542307, 6, 3),
  (2543061, 6, 4),
  (2548126, 1, 4),
  (2549071, 0, 7),
  (2554615, 7, 7),
  (2554856, 1, 3),
  (2557094, 2, 2),
  (2557124, 6, 0),
  (2557289, 5, 1),
  (2571092, 7, 0),
  (2578495, 6, 0),
  (2579506, 1, 0),
  (2580398, 3, 2),
  (2582008, 6, 1),
  (2585334, 4, 1),
  (2586458, 6, 4),
  (2590114, 0, 3),
  (2590815, 3, 3),
  (2599539, 5, 6),
  (2600757, 3, 6),
  (2601753, 3, 5),
  (2601902, 5, 4),
  (2603195, 1, 6),
  (2604083, 1, 3),
  (2606363, 3, 3),
  (2606477, 6, 7),
  (2607189, 1, 3),
  (2608278, 5, 7),
  (2609031, 6, 6),
  (2611427, 2, 3),
  (2613091, 5, 3),
  (2614192, 7, 0),
  (2616789, 7, 0),
  (2618601, 1, 0),
  (2624907, 6, 6),
  (2626410, 2, 3),
  (2626626, 6, 7),
  (2629432, 5, 3),
  (2632347, 2, 2),
  (2633234, 2, 3),
  (2633444, 3, 3),
  (2635367, 7, 1),
  (2636793, 6, 0),
  (2640333, 7, 0),
  (2646086, 5, 1),
  (2648518, 6, 0),
  (2648747, 1, 4),
  (2649020, 1, 3),
  (2650060, 4, 3),
  (2654608, 6, 0),
  (2654979, 4, 2),
  (2657402, 4, 2),
  (2658866, 6, 7),
  (2666310, 4, 0),
  (2675618, 2, 7),
  (2676072, 1, 7),
  (2679258, 3, 2),
  (2679658, 3, 2),
  (2680007, 6, 0),
  (2681587, 6, 7),
  (2682381, 5, 3),
  (2684071, 4, 3),
  (2685629, 6, 6),
  (2688602, 5, 4),
  (2691115, 6, 4),
  (2693852, 6, 3),
  (2694003, 7, 0),
  (2698045, 1, 1),
  (2699773, 3, 3),
  (2700898, 3, 3),
  (2701273, 1, 0),
  (2704475, 3, 3),
  (2704527, 1, 7),
  (2706516, 4, 0),
  (2709178, 3, 7),
  (2712706, 2, 2),
  (2715117, 7, 0),
  (2715556, 1, 0),
  (2716524, 0, 0),
  (2716608, 1, 1),
  (2716854, 0, 3),
  (2717528, 0, 7),
  (2717882, 0, 0),
  (2730181, 2, 3),
  (2733756, 0, 7),
  (2735894, 1, 7),
  (2735909, 6, 0),
  (2738475, 4, 3),
  (2743239, 2, 3),
  (2743398, 0, 0),
  (2745188, 0, 0),
  (2746685, 1, 3),
  (2747125, 7, 5),
  (2748088, 3, 3),
  (2751391, 4, 6),
  (2751526, 7, 0),
  (2754822, 0, 0),
  (2755092, 7, 4),
  (2755233, 3, 3),
  (2755974, 2, 3),
  (2759297, 6, 0),
  (2761268, 1, 0),
  (2765628, 1, 7),
  (2765843, 5, 2),
  (2768516, 3, 3),
  (2774144, 5, 3),
  (2774259, 7, 4),
  (2774443, 1, 3),
  (2777883, 1, 6),
  (2781387, 7, 7),
  (2782843, 2, 3),
  (2784019, 4, 6),
  (2785678, 5, 3),
  (2787806, 2, 2),
  (2787914, 3, 7),
  (2789712, 7, 7),
  (2791066, 2, 1),
  (2793478, 3, 4),
  (2794270, 4, 6),
  (2795827, 2, 3),
  (2796513, 6, 4),
  (2797315, 4, 7),
  (2799039, 1, 0),
  (2800014, 1, 0),
  (2800019, 2, 3),
  (2800166, 0, 3),
  (2801706, 3, 7),
  (2803362, 2, 1),
  (2805010, 6, 0),
  (2809072, 7, 7),
  (2811259, 6, 7),
  (2813203, 7, 1),
  (2814810, 0, 6),
  (2816924, 7, 0),
  (2819440, 4, 7),
  (2821101, 0, 0),
  (2821604, 4, 4),
  (2823112, 0, 4),
  (2823270, 6, 5),
  (2823998, 4, 3),
  (2824239, 3, 2),
  (2830807, 7, 5),
  (2831651, 6, 5),
  (2835777, 5, 6),
  (2837571, 0, 0),
  (2840573, 1, 7),
  (2846011, 2, 3),
  (2846013, 2, 3),
  (2846258, 5, 3),
  (2846281, 7, 0),
  (2846568, 1, 4),
  (2851026, 7, 2),
  (2851232, 5, 6),
  (2851687, 5, 7),
  (2859024, 7, 4),
  (2861624, 0, 7),
  (2863552, 2, 3),
  (2865039, 1, 0),
  (2866925, 0, 7),
  (2870271, 1, 7),
  (2870498, 6, 4),
  (2872229, 1, 4),
  (2874899, 0, 6),
  (2877440, 0, 7),
  (2878461, 2, 3),
  (2881332, 0, 0),
  (2881798, 6, 7),
  (2882986, 5, 3),
  (2885632, 0, 3),
  (2887515, 5, 1),
  (2888529, 0, 3),
  (2888895, 6, 0),
  (2891766, 7, 2),
  (2892355, 1, 3),
  (2895447, 1, 0),
  (2897884, 7, 7),
  (2904076, 3, 2),
  (2904741, 3, 6),
  (2906644, 7, 0),
  (2908532, 7, 3),
  (2910745, 1, 0),
  (2916597, 3, 3),
  (2920618, 3, 7),
  (2922748, 7, 7),
  (2923816, 4, 2),
  (2924564, 2, 3),
  (2924723, 2, 3),
  (2926990, 2, 3),
  (2928428, 2, 2),
  (2932879, 3, 3),
  (2936901, 3, 7),
  (2939370, 0, 0),
  (2941144, 6, 0),
  (2943356, 1, 4),
  (2949649, 5, 3),
  (2950801, 6, 3),
  (2953346, 2, 7),
  (2953747, 1, 4),
  (2953893, 5, 5),
  (2954110, 3, 3),
  (2956299, 7, 3),
  (2956796, 0, 0),
  (2957785, 2, 6),
  (2958115, 4, 2),
  (2958787, 2, 3),
  (2965587, 4, 7),
  (2967100, 3, 6),
  (2968080, 0, 2),
  (2969309, 4, 3),
  (2970510, 0, 7),
  (2970525, 6, 7),
  (2970613, 7, 2),
  (2970886, 7, 3),
  (2972812, 6, 5),
  (2977324, 2, 6),
  (2977428, 1, 0),
  (2977797, 4, 2),
  (2978137, 2, 3),
  (2980649, 2, 6),
  (2981124, 0, 2),
  (2981769, 2, 3),
  (2983738, 5, 3),
  (2986705, 1, 0),
  (2988629, 1, 3),
  (2991443, 1, 4),
  (2991718, 1, 0),
  (2994172, 1, 0),
  (2996718, 2, 2),
  (2997999, 0, 4),
  (3000719, 0, 3),
  (3006603, 0, 6),
  (3008321, 5, 2),
  (3010460, 4, 3),
  (3010708, 3, 2),
  (3015298, 4, 2),
  (3016476, 6, 0),
  (3020315, 4, 3),
  (3021273, 0, 7),
  (3023613, 6, 0),
  (3027323, 3, 2),
  (3027822, 1, 0),
  (3030444, 1, 0),
  (3034253, 7, 0),
  (3035058, 2, 3),
  (3037688, 0, 4),
  (3039531, 3, 1),
  (3039900, 6, 2),
  (3042732, 2, 3),
  (3043327, 6, 0),
  (3044103, 5, 3),
  (3045437, 0, 0),
  (3049049, 6, 0),
  (3050912, 2, 7),
  (3051050, 6, 3),
  (3053362, 2, 3),
  (3054968, 3, 2),
  (3063156, 6, 0),
  (3063300, 4, 6),
  (3064341, 4, 4),
  (3066263, 5, 6),
  (3068463, 6, 3),
  (3069654, 2, 6),
  (3071522, 5, 3),
  (3076991, 6, 0),
  (3079780, 4, 2),
  (3079881, 0, 3),
  (3083201, 2, 3),
  (3083306, 1, 7),
  (3085195, 2, 3),
  (3085912, 5, 2),
  (3090142, 0, 4),
  (3090515, 6, 0),
  (3091513, 0, 1),
  (3091866, 6, 4),
  (3092369, 4, 6),
  (3093136, 7, 4),
  (3093361, 7, 6),
  (3093746, 6, 0),
  (3093959, 5, 6),
  (3096344, 4, 3),
  (3096582, 1, 7),
  (3097546, 1, 0),
  (3098087, 0, 7),
  (3098759, 1, 0),
  (3098889, 2, 3),
  (3098943, 1, 7),
  (3099389, 0, 1),
  (3103745, 2, 3),
  (3103967, 0, 0),
  (3104788, 5, 6),
  (3108598, 7, 0),
  (3112971, 0, 6),
  (3117676, 7, 0),
  (3123329, 6, 3),
  (3125778, 4, 7),
  (3129760, 3, 3),
  (3133049, 6, 0),
  (3135810, 2, 0),
  (3136767, 1, 0),
  (3139323, 6, 2),
  (3141168, 2, 0),
  (3144020, 5, 3),
  (3150632, 6, 5),
  (3151628, 4, 2),
  (3152202, 7, 0),
  (3152913, 0, 7),
  (3154475, 1, 4),
  (3157326, 2, 5),
  (3160843, 1, 4),
  (3161931, 1, 0),
  (3161970, 2, 3),
  (3163442, 1, 0),
  (3164434, 4, 6),
  (3167735, 7, 4),
  (3167972, 0, 3),
  (3168148, 7, 3),
  (3169988, 5, 2),
  (3172960, 3, 1),
  (3175335, 6, 3),
  (3175738, 1, 0),
  (3176414, 0, 0),
  (3179624, 2, 1),
  (3180892, 5, 2),
  (3182628, 1, 3),
  (3183024, 3, 3),
  (3184451, 3, 7),
  (3184873, 5, 3),
  (3185173, 3, 3),
  (3185973, 2, 2),
  (3187805, 6, 4),
  (3188184, 6, 3),
  (3188665, 5, 3),
  (3190781, 1, 4),
  (3190814, 1, 4),
  (3191036, 5, 3),
  (3193952, 0, 4),
  (3195455, 6, 6),
  (3195591, 7, 7),
  (3196903, 5, 7),
  (3198336, 1, 5),
  (3201735, 1, 3),
  (3202459, 7, 0),
  (3210790, 7, 0),
  (3211590, 6, 4),
  (3213016, 0, 0),
  (3213516, 7, 3),
  (3219579, 5, 3),
  (3220427, 2, 6),
  (3222974, 1, 0),
  (3231809, 7, 6),
  (3231856, 0, 1),
  (3240394, 6, 7),
  (3242032, 3, 3),
  (3243998, 6, 4),
  (3245428, 2, 7),
  (3248463, 3, 7),
  (3251336, 4, 6),
  (3253795, 6, 0),
  (3261816, 2, 7),
  (3266956, 5, 1),
  (3266961, 5, 4),
  (3275768, 6, 7),
  (3276907, 1, 0),
  (3278241, 3, 7),
  (3279566, 2, 5),
  (3283105, 1, 0),
  (3285342, 6, 0),
  (3286735, 7, 0),
  (3287366, 0, 0),
  (3288694, 1, 3),
  (3290904, 3, 3),
  (3291959, 7, 0),
  (3292835, 4, 0),
  (3292894, 2, 3),
  (3292926, 7, 0),
  (3314314, 4, 3),
  (3317642, 2, 7),
  (3318716, 4, 4),
  (3319233, 1, 1),
  (3321127, 1, 3),
  (3323276, 4, 6),
  (3323327, 4, 4),
  (3325753, 2, 1),
  (3328965, 5, 0),
  (3329446, 5, 4),
  (3329694, 1, 1),
  (3331286, 6, 0),
  (3332852, 6, 3),
  (3338684, 0, 3),
  (3339824, 3, 3),
  (3341251, 4, 3),
  (3342218, 2, 2),
  (3348099, 3, 3),
  (3348524, 2, 5),
  (3352290, 1, 4),
  (3352760, 7, 3),
  (3359480, 3, 2),
  (3360355, 0, 7),
  (3363928, 4, 6),
  (3365235, 0, 7),
  (3367416, 1, 1),
  (3369521, 7, 3),
  (3373272, 0, 4),
  (3373456, 0, 0),
  (3376240, 2, 6),
  (3377253, 6, 6),
  (3379834, 3, 5),
  (3381756, 0, 0),
  (3382160, 1, 4),
  (3384303, 4, 7),
  (3386920, 6, 7),
  (3387067, 1, 3),
  (3387121, 4, 1),
  (3389436, 6, 3),
  (3389866, 3, 3),
  (3390180, 2, 3),
  (3393958, 7, 5),
  (3394174, 4, 1),
  (3398275, 4, 3),
  (3398726, 7, 0),
  (3400338, 7, 7),
  (3400709, 1, 7),
  (3401602, 1, 7),
  (3403000, 1, 1),
  (3404298, 0, 0),
  (3405027, 1, 0),
  (3406235, 3, 3),
  (3406267, 3, 3),
  (3407439, 6, 0),
  (3413231, 3, 2),
  (3415418, 6, 3),
  (3419113, 1, 5),
  (3427317, 0, 3),
  (3428411, 4, 6),
  (3431726, 2, 6),
  (3431853, 4, 6),
  (3434279, 1, 2),
  (3437195, 2, 2),
  (3437620, 4, 6),
  (3438865, 5, 2),
  (3441827, 6, 7),
  (3443055, 6, 0),
  (3443388, 5, 7),
  (3447402, 7, 0),
  (3447404, 1, 7),
  (3447919, 7, 4),
  (3450844, 3, 7),
  (3450940, 2, 1),
  (3453004, 6, 4),
  (3453473, 4, 6),
  (3456346, 7, 1),
  (3456432, 7, 0),
  (3460031, 0, 0),
  (3464832, 7, 3),
  (3465220, 2, 6),
  (3466185, 1, 5),
  (3466864, 5, 3),
  (3467613, 4, 3),
  (3469431, 0, 0),
  (3476726, 6, 6),
  (3478625, 1, 0),
  (3481073, 6, 0),
  (3481581, 1, 4),
  (3481689, 1, 1),
  (3483508, 1, 0),
  (3483734, 1, 6),
  (3484223, 6, 5),
  (3485693, 0, 0),
  (3487660, 6, 2),
  (3487785, 2, 7),
  (3490715, 0, 4),
  (3495652, 2, 6),
  (3495924, 3, 3),
  (3498598, 0, 4),
  (3501050, 2, 6),
  (3503706, 4, 6),
  (3507497, 7, 0),
  (3507788, 2, 5),
  (3515042, 2, 2),
  (3521640, 2, 3),
  (3522113, 4, 3),
  (3524645, 4, 3),
  (3526099, 7, 5),
  (3526403, 2, 3),
  (3531873, 5, 1),
  (3535604, 5, 3),
  (3536161, 2, 6),
  (3543562, 2, 6),
  (3549374, 0, 0),
  (3551666, 4, 3),
  (3552024, 2, 7),
  (3552066, 2, 7),
  (3552201, 0, 0),
  (3553106, 6, 0),
  (3557358, 0, 0),
  (3557896, 6, 0),
  (3557995, 3, 1),
  (3558148, 4, 6),
  (3562201, 0, 0),
  (3564442, 6, 7),
  (3568008, 1, 6),
  (3571357, 2, 1),
  (3572004, 3, 7),
  (3573310, 0, 0),
  (3574449, 3, 7),
  (3579465, 4, 6),
  (3582152, 6, 0),
  (3583805, 3, 3),
  (3586800, 4, 2),
  (3586937, 4, 3),
  (3587842, 6, 1),
  (3588497, 3, 2),
  (3589139, 0, 1),
  (3598319, 6, 0),
  (3599880, 0, 4),
])