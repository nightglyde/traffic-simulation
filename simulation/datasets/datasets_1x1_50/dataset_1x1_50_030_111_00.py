from src.util import *
schedule = deque([
  (1051, 7, 0),
  (2017, 2, 4),
  (7220, 6, 7),
  (8181, 4, 6),
  (13103, 2, 1),
  (17839, 1, 5),
  (18251, 0, 4),
  (20067, 4, 7),
  (27800, 3, 7),
  (29565, 6, 2),
  (32177, 0, 2),
  (32266, 1, 0),
  (34617, 2, 6),
  (35325, 4, 3),
  (36431, 2, 6),
  (37005, 5, 3),
  (37108, 0, 0),
  (38128, 7, 0),
  (38309, 4, 0),
  (39285, 0, 0),
  (44249, 6, 0),
  (45094, 3, 2),
  (53779, 3, 3),
  (54280, 0, 0),
  (55072, 7, 0),
  (56682, 3, 7),
  (58176, 6, 3),
  (59776, 5, 3),
  (63548, 6, 0),
  (64520, 3, 3),
  (67922, 6, 0),
  (68487, 5, 3),
  (68975, 3, 5),
  (71335, 2, 6),
  (71608, 2, 3),
  (75524, 1, 3),
  (76084, 2, 3),
  (76180, 4, 4),
  (77217, 3, 3),
  (79327, 1, 2),
  (80728, 6, 0),
  (84322, 0, 4),
  (89293, 7, 0),
  (89308, 0, 3),
  (91401, 0, 2),
  (92052, 5, 3),
  (94419, 7, 7),
  (94452, 3, 4),
  (94819, 5, 2),
  (95858, 7, 6),
  (101781, 0, 0),
  (104802, 5, 7),
  (111199, 3, 3),
  (111948, 4, 3),
  (112373, 1, 0),
  (114646, 5, 3),
  (114924, 2, 6),
  (117188, 1, 0),
  (118298, 7, 0),
  (122099, 3, 3),
  (122976, 5, 2),
  (125543, 1, 4),
  (128893, 3, 6),
  (129857, 2, 2),
  (131784, 4, 3),
  (133321, 0, 7),
  (134140, 4, 2),
  (135510, 2, 0),
  (136039, 2, 3),
  (136083, 2, 3),
  (136943, 2, 2),
  (137104, 5, 3),
  (137296, 4, 7),
  (139245, 3, 2),
  (139384, 3, 3),
  (139880, 6, 2),
  (140306, 2, 0),
  (142195, 4, 3),
  (142513, 4, 3),
  (144967, 5, 3),
  (145590, 0, 7),
  (147955, 1, 1),
  (148936, 4, 5),
  (150078, 7, 5),
  (152601, 3, 5),
  (159718, 2, 3),
  (160233, 4, 5),
  (160355, 2, 6),
  (160480, 4, 2),
  (163547, 3, 2),
  (163643, 2, 4),
  (163659, 6, 7),
  (163736, 3, 3),
  (164876, 3, 6),
  (168766, 7, 5),
  (172507, 5, 4),
  (173390, 2, 0),
  (175790, 0, 0),
  (176896, 4, 6),
  (178300, 7, 0),
  (181771, 6, 4),
  (184283, 2, 3),
  (185241, 1, 2),
  (186926, 3, 6),
  (189450, 4, 7),
  (191520, 5, 6),
  (192033, 6, 4),
  (193280, 5, 3),
  (193564, 3, 3),
  (194552, 3, 0),
  (197332, 3, 6),
  (198352, 1, 4),
  (199716, 0, 0),
  (200587, 3, 3),
  (201448, 7, 6),
  (201646, 5, 3),
  (204546, 6, 0),
  (205181, 3, 6),
  (208857, 1, 0),
  (211832, 1, 3),
  (212775, 6, 0),
  (213225, 0, 4),
  (213391, 1, 2),
  (215571, 6, 5),
  (217505, 5, 2),
  (221299, 4, 1),
  (225239, 4, 7),
  (225323, 7, 4),
  (228570, 6, 4),
  (231236, 4, 6),
  (231327, 6, 0),
  (232798, 4, 3),
  (238540, 2, 3),
  (239886, 3, 7),
  (242225, 2, 1),
  (243203, 7, 4),
  (244730, 3, 4),
  (245244, 0, 7),
  (245494, 6, 5),
  (246502, 3, 7),
  (252751, 0, 0),
  (254106, 2, 7),
  (260818, 0, 7),
  (263798, 4, 3),
  (266080, 4, 3),
  (269913, 5, 3),
  (275506, 6, 7),
  (276200, 4, 0),
  (278897, 2, 3),
  (280404, 1, 0),
  (281657, 7, 4),
  (285507, 5, 7),
  (286419, 2, 3),
  (287218, 5, 3),
  (289486, 4, 2),
  (291417, 1, 4),
  (296347, 7, 1),
  (296376, 1, 4),
  (297325, 1, 4),
  (298062, 3, 3),
  (299272, 2, 3),
  (301145, 6, 7),
  (301735, 7, 3),
  (305890, 5, 6),
  (306064, 3, 3),
  (307827, 1, 7),
  (314512, 3, 5),
  (315560, 2, 7),
  (319556, 1, 4),
  (322674, 5, 3),
  (322675, 2, 1),
  (323129, 3, 3),
  (324767, 5, 0),
  (331018, 7, 5),
  (333196, 0, 2),
  (337732, 2, 3),
  (341721, 7, 6),
  (344403, 5, 7),
  (344519, 3, 3),
  (345314, 0, 3),
  (349257, 6, 0),
  (350265, 7, 0),
  (350569, 0, 0),
  (355086, 5, 6),
  (358524, 0, 0),
  (360603, 3, 3),
  (361931, 7, 0),
  (364802, 4, 2),
  (368310, 4, 7),
  (368577, 5, 2),
  (369216, 2, 6),
  (370281, 6, 0),
  (371449, 2, 2),
  (372598, 1, 4),
  (380487, 6, 0),
  (382238, 4, 3),
  (382287, 5, 7),
  (388095, 4, 2),
  (388253, 3, 3),
  (389429, 3, 3),
  (390785, 5, 1),
  (394787, 5, 3),
  (394902, 6, 2),
  (398626, 4, 1),
  (399854, 2, 7),
  (401045, 2, 3),
  (402404, 6, 0),
  (405435, 5, 3),
  (405606, 6, 7),
  (406093, 6, 0),
  (407116, 4, 2),
  (407913, 5, 3),
  (408598, 6, 4),
  (409166, 6, 6),
  (410244, 4, 2),
  (410448, 2, 3),
  (412399, 0, 2),
  (415970, 1, 7),
  (416688, 6, 1),
  (416775, 7, 4),
  (416817, 3, 3),
  (418999, 5, 7),
  (420234, 6, 7),
  (423229, 3, 6),
  (423681, 4, 2),
  (425575, 1, 7),
  (426756, 1, 0),
  (430384, 7, 1),
  (431610, 7, 7),
  (432164, 1, 3),
  (437364, 5, 2),
  (438869, 3, 2),
  (441179, 0, 0),
  (442225, 4, 3),
  (442605, 7, 4),
  (442901, 6, 1),
  (443623, 7, 2),
  (444496, 6, 0),
  (444738, 4, 3),
  (448129, 5, 5),
  (450144, 2, 5),
  (451880, 7, 7),
  (453786, 5, 7),
  (454053, 1, 0),
  (459150, 0, 2),
  (460530, 1, 0),
  (467057, 7, 5),
  (467509, 2, 3),
  (467754, 3, 3),
  (467871, 3, 7),
  (473693, 4, 3),
  (481139, 2, 7),
  (481140, 4, 3),
  (481277, 7, 4),
  (481827, 4, 3),
  (488976, 3, 3),
  (502060, 1, 0),
  (504864, 5, 7),
  (505535, 5, 7),
  (509819, 5, 0),
  (510012, 2, 3),
  (510119, 1, 0),
  (518067, 3, 3),
  (519959, 0, 4),
  (520023, 3, 5),
  (520753, 2, 3),
  (523969, 2, 7),
  (524813, 1, 5),
  (524917, 6, 0),
  (526444, 4, 4),
  (527069, 7, 4),
  (527098, 4, 0),
  (527203, 2, 2),
  (528005, 2, 3),
  (530180, 7, 2),
  (530712, 7, 6),
  (531117, 3, 0),
  (534107, 4, 7),
  (535369, 4, 2),
  (537525, 5, 3),
  (538710, 3, 3),
  (539307, 4, 2),
  (541984, 5, 3),
  (543884, 7, 0),
  (544533, 1, 7),
  (545486, 1, 2),
  (545622, 5, 1),
  (545963, 3, 7),
  (547081, 3, 6),
  (547773, 1, 2),
  (548404, 0, 0),
  (548955, 1, 7),
  (549295, 7, 7),
  (549550, 2, 5),
  (552985, 3, 0),
  (557149, 6, 4),
  (557464, 6, 0),
  (558240, 7, 1),
  (558621, 7, 0),
  (560396, 4, 2),
  (560738, 7, 0),
  (568526, 5, 3),
  (569388, 1, 7),
  (569731, 6, 5),
  (569846, 1, 7),
  (571222, 4, 0),
  (572351, 1, 4),
  (573496, 3, 6),
  (574213, 0, 0),
  (577521, 3, 2),
  (577987, 4, 5),
  (578280, 3, 3),
  (594275, 2, 7),
  (596746, 5, 3),
  (598953, 7, 4),
  (608495, 5, 4),
  (608607, 4, 3),
  (610220, 1, 0),
  (611862, 1, 2),
  (612155, 0, 0),
  (612274, 2, 5),
  (618362, 6, 0),
  (619283, 1, 2),
  (621261, 6, 0),
  (626387, 3, 2),
  (626504, 4, 6),
  (627636, 7, 3),
  (629244, 5, 3),
  (633292, 3, 2),
  (633650, 4, 3),
  (638188, 0, 0),
  (640783, 7, 0),
  (640851, 3, 3),
  (641742, 2, 3),
  (644287, 1, 0),
  (644796, 5, 2),
  (645940, 2, 3),
  (645964, 5, 7),
  (647528, 6, 0),
  (649477, 6, 7),
  (649989, 6, 0),
  (650831, 7, 0),
  (653513, 2, 2),
  (656827, 1, 7),
  (660044, 3, 3),
  (661236, 0, 1),
  (663290, 7, 6),
  (663534, 0, 0),
  (669096, 0, 3),
  (669245, 1, 6),
  (671078, 5, 5),
  (671857, 7, 7),
  (672946, 6, 2),
  (680542, 7, 3),
  (680729, 2, 4),
  (683046, 7, 0),
  (686388, 3, 1),
  (688024, 2, 3),
  (690807, 7, 4),
  (694988, 6, 0),
  (698747, 2, 3),
  (704796, 4, 6),
  (705663, 2, 3),
  (706850, 4, 7),
  (708953, 6, 3),
  (710828, 7, 0),
  (716580, 1, 7),
  (717609, 4, 7),
  (717658, 2, 4),
  (717698, 7, 4),
  (727640, 5, 3),
  (728297, 7, 5),
  (729079, 5, 2),
  (730713, 1, 0),
  (739110, 7, 6),
  (739437, 6, 0),
  (741476, 1, 0),
  (741706, 2, 3),
  (743738, 2, 3),
  (744580, 2, 3),
  (745503, 6, 0),
  (745842, 7, 7),
  (746739, 1, 3),
  (753753, 6, 3),
  (754837, 4, 6),
  (755887, 0, 6),
  (767206, 3, 2),
  (769332, 6, 3),
  (769554, 3, 3),
  (770079, 0, 0),
  (771134, 6, 4),
  (775013, 1, 0),
  (776175, 1, 0),
  (776223, 1, 0),
  (776940, 6, 5),
  (779083, 5, 2),
  (782210, 4, 6),
  (786921, 2, 3),
  (787527, 1, 0),
  (789072, 6, 0),
  (791921, 2, 3),
  (793704, 1, 3),
  (794297, 4, 4),
  (795621, 5, 4),
  (796826, 3, 2),
  (797427, 1, 0),
  (802858, 6, 0),
  (803566, 4, 1),
  (806436, 7, 4),
  (808901, 2, 7),
  (809258, 0, 0),
  (809958, 5, 7),
  (810492, 0, 4),
  (811045, 3, 4),
  (813374, 3, 7),
  (814442, 4, 3),
  (815061, 5, 6),
  (816320, 5, 2),
  (816368, 5, 7),
  (816818, 5, 1),
  (816995, 7, 3),
  (820488, 6, 4),
  (821426, 1, 0),
  (828591, 4, 3),
  (832012, 7, 4),
  (837182, 4, 2),
  (837548, 3, 7),
  (839846, 7, 0),
  (841109, 5, 3),
  (842275, 5, 3),
  (842647, 6, 6),
  (845524, 7, 2),
  (845726, 2, 6),
  (848272, 0, 4),
  (849414, 0, 0),
  (851574, 2, 6),
  (853184, 3, 3),
  (853222, 5, 2),
  (853871, 7, 7),
  (855926, 0, 0),
  (859892, 5, 3),
  (861371, 6, 0),
  (862030, 2, 7),
  (865844, 4, 7),
  (866085, 3, 3),
  (866303, 3, 3),
  (872375, 1, 7),
  (872433, 4, 7),
  (874474, 1, 3),
  (881458, 0, 0),
  (881625, 2, 3),
  (882512, 5, 6),
  (883563, 1, 0),
  (884282, 1, 7),
  (886118, 3, 4),
  (887905, 0, 7),
  (888719, 5, 7),
  (889588, 5, 2),
  (890149, 2, 3),
  (901285, 5, 1),
  (902815, 6, 3),
  (907191, 4, 7),
  (911603, 4, 6),
  (911735, 5, 0),
  (919726, 5, 7),
  (922947, 3, 3),
  (929356, 3, 7),
  (931943, 7, 0),
  (932708, 6, 0),
  (932739, 7, 3),
  (933092, 3, 7),
  (933613, 3, 3),
  (935087, 0, 0),
  (936179, 6, 5),
  (937513, 3, 6),
  (938442, 5, 6),
  (940855, 5, 3),
  (941624, 5, 2),
  (941789, 7, 6),
  (943638, 3, 6),
  (944689, 0, 0),
  (947986, 4, 5),
  (948721, 0, 3),
  (950015, 4, 3),
  (951977, 4, 1),
  (953092, 6, 7),
  (955687, 5, 1),
  (956134, 5, 3),
  (958108, 3, 7),
  (959688, 2, 7),
  (960594, 2, 6),
  (962997, 5, 7),
  (963435, 6, 2),
  (966345, 1, 4),
  (967372, 3, 3),
  (968621, 4, 7),
  (973201, 3, 2),
  (973225, 6, 6),
  (973458, 5, 3),
  (976524, 2, 1),
  (978450, 5, 3),
  (980502, 1, 7),
  (982215, 6, 6),
  (984191, 4, 3),
  (984277, 7, 5),
  (988513, 0, 0),
  (989466, 2, 1),
  (990307, 2, 3),
  (991866, 2, 6),
  (992744, 6, 7),
  (993239, 2, 7),
  (994616, 4, 4),
  (995571, 5, 3),
  (996502, 3, 3),
  (997197, 5, 1),
  (998548, 7, 2),
  (1003750, 1, 0),
  (1005601, 4, 7),
  (1005758, 4, 6),
  (1009754, 6, 0),
  (1011160, 3, 2),
  (1011278, 3, 6),
  (1018324, 7, 0),
  (1020797, 2, 2),
  (1023160, 6, 0),
  (1024502, 7, 7),
  (1024997, 7, 0),
  (1026211, 1, 0),
  (1026373, 3, 3),
  (1026423, 6, 0),
  (1028094, 5, 3),
  (1035099, 3, 6),
  (1035290, 4, 7),
  (1036595, 3, 5),
  (1040013, 2, 3),
  (1040192, 0, 0),
  (1043090, 1, 4),
  (1044872, 2, 7),
  (1045392, 5, 7),
  (1045413, 7, 5),
  (1045635, 7, 3),
  (1045802, 6, 7),
  (1046689, 7, 4),
  (1049475, 5, 5),
  (1050080, 4, 5),
  (1051984, 2, 7),
  (1054614, 4, 2),
  (1055279, 4, 6),
  (1055496, 6, 2),
  (1058601, 7, 7),
  (1063286, 3, 3),
  (1064413, 6, 4),
  (1066006, 1, 4),
  (1069366, 4, 6),
  (1070730, 4, 3),
  (1073825, 3, 3),
  (1074500, 0, 6),
  (1078867, 5, 7),
  (1079891, 2, 3),
  (1080078, 2, 7),
  (1080385, 3, 0),
  (1080926, 7, 2),
  (1081441, 4, 3),
  (1082884, 5, 5),
  (1085311, 7, 0),
  (1088095, 6, 0),
  (1093856, 3, 0),
  (1094192, 6, 4),
  (1094250, 7, 0),
  (1096426, 6, 2),
  (1100556, 7, 0),
  (1100697, 3, 0),
  (1103589, 0, 7),
  (1113249, 3, 7),
  (1113278, 1, 0),
  (1114342, 2, 2),
  (1115091, 6, 0),
  (1115568, 7, 0),
  (1115569, 5, 3),
  (1116081, 5, 3),
  (1116530, 0, 4),
  (1118832, 3, 1),
  (1121281, 6, 4),
  (1124613, 0, 5),
  (1125090, 5, 2),
  (1126656, 3, 6),
  (1127767, 3, 6),
  (1131706, 6, 3),
  (1134071, 0, 1),
  (1135836, 5, 7),
  (1137089, 0, 0),
  (1137821, 4, 3),
  (1149415, 3, 2),
  (1149939, 6, 7),
  (1150710, 3, 3),
  (1151005, 2, 3),
  (1152367, 3, 3),
  (1153376, 5, 5),
  (1156683, 6, 4),
  (1156801, 5, 6),
  (1161398, 5, 3),
  (1163903, 6, 4),
  (1168235, 7, 0),
  (1170108, 3, 6),
  (1173513, 5, 4),
  (1175535, 1, 0),
  (1175547, 2, 7),
  (1175977, 5, 3),
  (1176122, 3, 1),
  (1177736, 7, 0),
  (1178418, 6, 0),
  (1178694, 3, 7),
  (1178924, 5, 3),
  (1178974, 6, 0),
  (1181442, 5, 0),
  (1181739, 1, 0),
  (1181990, 2, 5),
  (1182630, 1, 0),
  (1184567, 0, 6),
  (1188102, 3, 6),
  (1192756, 1, 0),
  (1197117, 1, 0),
  (1199554, 5, 6),
  (1200881, 1, 0),
  (1205692, 4, 6),
  (1205745, 5, 3),
  (1206181, 0, 4),
  (1206906, 0, 3),
  (1208487, 5, 3),
  (1210968, 5, 7),
  (1214102, 7, 0),
  (1218266, 5, 6),
  (1219575, 6, 7),
  (1221773, 3, 3),
  (1221802, 6, 3),
  (1226377, 6, 3),
  (1226863, 7, 3),
  (1228839, 3, 2),
  (1238373, 7, 7),
  (1241130, 0, 6),
  (1243563, 2, 3),
  (1244998, 2, 5),
  (1245025, 2, 3),
  (1245278, 6, 0),
  (1246245, 3, 3),
  (1248179, 5, 7),
  (1249475, 6, 3),
  (1250142, 1, 0),
  (1250145, 3, 2),
  (1252589, 1, 4),
  (1254127, 1, 0),
  (1260192, 4, 3),
  (1262784, 5, 2),
  (1264050, 2, 7),
  (1266374, 1, 0),
  (1266569, 2, 3),
  (1266689, 2, 4),
  (1270125, 1, 6),
  (1274079, 6, 0),
  (1276736, 6, 0),
  (1276819, 7, 0),
  (1276898, 5, 1),
  (1284250, 4, 3),
  (1285064, 6, 4),
  (1285983, 6, 4),
  (1288142, 7, 5),
  (1290308, 2, 3),
  (1291579, 6, 7),
  (1293556, 4, 3),
  (1295508, 0, 7),
  (1295970, 7, 0),
  (1300877, 1, 6),
  (1301100, 6, 7),
  (1311571, 1, 6),
  (1311839, 6, 4),
  (1314442, 2, 3),
  (1317687, 1, 0),
  (1319766, 6, 4),
  (1321063, 5, 2),
  (1323146, 0, 1),
  (1324522, 6, 4),
  (1325958, 6, 4),
  (1326130, 1, 7),
  (1327063, 3, 5),
  (1329098, 5, 7),
  (1329191, 6, 5),
  (1330142, 1, 0),
  (1331403, 1, 3),
  (1333903, 0, 1),
  (1334676, 7, 4),
  (1337602, 3, 7),
  (1339864, 1, 3),
  (1343178, 4, 6),
  (1345090, 2, 5),
  (1346426, 6, 7),
  (1347472, 4, 7),
  (1351580, 5, 5),
  (1354110, 0, 3),
  (1356544, 0, 3),
  (1357156, 5, 3),
  (1359300, 7, 4),
  (1360480, 7, 0),
  (1363757, 6, 4),
  (1366510, 0, 2),
  (1367384, 1, 1),
  (1367587, 4, 3),
  (1369761, 6, 0),
  (1369852, 4, 6),
  (1372464, 4, 2),
  (1372809, 1, 7),
  (1374492, 0, 2),
  (1379184, 6, 4),
  (1384832, 3, 3),
  (1391065, 6, 7),
  (1391457, 2, 3),
  (1393784, 1, 0),
  (1394226, 1, 0),
  (1394722, 6, 4),
  (1399158, 1, 7),
  (1407747, 6, 4),
  (1410354, 5, 7),
  (1412273, 2, 3),
  (1415485, 5, 3),
  (1415562, 1, 0),
  (1421203, 4, 3),
  (1421965, 3, 7),
  (1422044, 5, 0),
  (1423437, 2, 3),
  (1426013, 7, 0),
  (1430359, 3, 7),
  (1434827, 6, 0),
  (1436576, 2, 6),
  (1440453, 3, 6),
  (1440997, 7, 6),
  (1442752, 2, 3),
  (1443605, 2, 7),
  (1445060, 6, 0),
  (1451509, 3, 6),
  (1452696, 3, 0),
  (1453217, 6, 7),
  (1455482, 4, 7),
  (1455572, 0, 0),
  (1459549, 6, 5),
  (1460452, 3, 3),
  (1462784, 2, 1),
  (1463192, 3, 3),
  (1466755, 4, 3),
  (1466926, 4, 3),
  (1468669, 5, 2),
  (1470313, 1, 4),
  (1471584, 1, 0),
  (1472598, 5, 7),
  (1476754, 4, 6),
  (1477105, 4, 7),
  (1479533, 0, 7),
  (1479814, 7, 4),
  (1479912, 3, 3),
  (1480904, 7, 4),
  (1481094, 6, 1),
  (1484215, 0, 4),
  (1486144, 1, 6),
  (1486724, 7, 0),
  (1489244, 1, 5),
  (1489335, 7, 3),
  (1494881, 6, 0),
  (1496483, 0, 6),
  (1499846, 0, 6),
  (1501119, 1, 4),
  (1501883, 3, 7),
  (1501892, 4, 3),
  (1509728, 6, 0),
  (1510528, 5, 7),
  (1511080, 3, 1),
  (1511210, 7, 0),
  (1511880, 6, 3),
  (1516290, 7, 0),
  (1517318, 1, 2),
  (1517426, 0, 2),
  (1518411, 3, 3),
  (1519879, 1, 4),
  (1520058, 1, 0),
  (1523961, 2, 4),
  (1524955, 5, 3),
  (1525117, 7, 7),
  (1526897, 7, 0),
  (1527369, 5, 6),
  (1528805, 7, 0),
  (1529609, 4, 5),
  (1529932, 3, 4),
  (1530781, 7, 0),
  (1532481, 6, 6),
  (1536586, 5, 6),
  (1540169, 0, 7),
  (1543962, 7, 3),
  (1545901, 7, 0),
  (1547042, 5, 3),
  (1547170, 1, 0),
  (1548561, 6, 0),
  (1548713, 5, 3),
  (1551346, 0, 4),
  (1553653, 1, 0),
  (1558454, 7, 2),
  (1558569, 1, 3),
  (1560096, 5, 5),
  (1562722, 1, 1),
  (1563175, 7, 4),
  (1563526, 7, 6),
  (1564584, 4, 3),
  (1565210, 1, 0),
  (1567215, 6, 3),
  (1572528, 5, 2),
  (1572603, 2, 1),
  (1573028, 2, 3),
  (1573167, 7, 0),
  (1575787, 7, 3),
  (1577241, 4, 4),
  (1580127, 0, 4),
  (1582256, 0, 0),
  (1583655, 6, 0),
  (1586465, 2, 2),
  (1586974, 4, 7),
  (1591650, 5, 1),
  (1593617, 3, 0),
  (1596631, 5, 7),
  (1598222, 2, 6),
  (1599739, 7, 3),
  (1600124, 7, 0),
  (1605087, 2, 6),
  (1606994, 6, 3),
  (1608454, 4, 7),
  (1610388, 7, 2),
  (1610504, 0, 4),
  (1610572, 1, 3),
  (1611311, 6, 0),
  (1612145, 4, 3),
  (1614641, 0, 0),
  (1622104, 7, 0),
  (1623682, 4, 3),
  (1624716, 1, 4),
  (1626661, 7, 7),
  (1633951, 5, 6),
  (1638946, 2, 0),
  (1640391, 0, 0),
  (1640672, 3, 3),
  (1641802, 4, 7),
  (1641981, 4, 3),
  (1642395, 4, 3),
  (1644829, 7, 0),
  (1650675, 5, 3),
  (1656172, 7, 0),
  (1659914, 7, 7),
  (1663291, 6, 0),
  (1664166, 4, 3),
  (1665898, 5, 3),
  (1666170, 0, 0),
  (1666997, 4, 3),
  (1667046, 3, 4),
  (1667429, 5, 6),
  (1667937, 7, 0),
  (1668687, 6, 4),
  (1674987, 1, 0),
  (1676409, 1, 0),
  (1681308, 3, 3),
  (1690474, 4, 2),
  (1690968, 7, 7),
  (1691943, 6, 7),
  (1695782, 5, 3),
  (1696258, 1, 3),
  (1698300, 5, 3),
  (1699461, 6, 2),
  (1699733, 7, 3),
  (1706969, 2, 1),
  (1707232, 3, 2),
  (1708115, 0, 3),
  (1708585, 2, 3),
  (1709473, 5, 3),
  (1711268, 2, 7),
  (1713353, 5, 3),
  (1718533, 4, 1),
  (1718617, 5, 3),
  (1718741, 7, 5),
  (1720988, 5, 3),
  (1723859, 1, 3),
  (1725749, 0, 3),
  (1726236, 0, 0),
  (1727288, 7, 0),
  (1729701, 3, 6),
  (1731294, 7, 0),
  (1733676, 0, 0),
  (1733759, 2, 2),
  (1739772, 2, 5),
  (1741422, 2, 5),
  (1741947, 0, 6),
  (1743085, 7, 0),
  (1745230, 6, 7),
  (1745764, 5, 3),
  (1746708, 7, 7),
  (1746984, 4, 6),
  (1748312, 1, 0),
  (1748608, 4, 3),
  (1749952, 7, 7),
  (1750077, 5, 7),
  (1754064, 5, 1),
  (1755292, 6, 2),
  (1755388, 7, 7),
  (1757048, 6, 3),
  (1757510, 7, 3),
  (1758452, 1, 0),
  (1759856, 1, 0),
  (1763385, 6, 7),
  (1767664, 7, 2),
  (1768052, 0, 7),
  (1769783, 0, 0),
  (1769923, 1, 3),
  (1770050, 5, 3),
  (1772408, 5, 3),
  (1774646, 6, 1),
  (1781339, 3, 3),
  (1782591, 1, 0),
  (1787043, 6, 4),
  (1789459, 1, 3),
  (1792342, 1, 5),
  (1793202, 2, 5),
  (1793226, 3, 7),
  (1793876, 5, 3),
  (1794711, 1, 0),
  (1795483, 6, 0),
  (1803550, 1, 0),
  (1803570, 7, 0),
  (1803700, 0, 7),
  (1806700, 2, 3),
  (1809008, 1, 3),
  (1811110, 6, 0),
  (1812542, 6, 0),
  (1813428, 3, 4),
  (1813927, 0, 0),
  (1814686, 5, 6),
  (1818247, 2, 2),
  (1820572, 5, 7),
  (1822055, 6, 0),
  (1832033, 6, 3),
  (1833848, 1, 0),
  (1835128, 6, 6),
  (1837680, 4, 3),
  (1840529, 5, 6),
  (1840803, 5, 4),
  (1843346, 2, 3),
  (1843554, 6, 0),
  (1844354, 7, 0),
  (1844381, 4, 1),
  (1846093, 4, 0),
  (1849778, 7, 4),
  (1851310, 5, 7),
  (1854934, 1, 4),
  (1855687, 2, 3),
  (1856918, 3, 7),
  (1858660, 1, 7),
  (1861026, 7, 4),
  (1863844, 2, 7),
  (1864215, 4, 7),
  (1866079, 7, 7),
  (1866704, 6, 0),
  (1868839, 4, 3),
  (1869253, 5, 7),
  (1886935, 6, 0),
  (1888185, 0, 0),
  (1888251, 1, 0),
  (1892030, 3, 7),
  (1892345, 3, 7),
  (1893844, 0, 0),
  (1894203, 3, 6),
  (1895547, 5, 6),
  (1896796, 4, 7),
  (1897012, 7, 0),
  (1899125, 1, 4),
  (1901523, 0, 0),
  (1901869, 4, 5),
  (1902485, 0, 4),
  (1902625, 1, 4),
  (1903217, 0, 4),
  (1904510, 3, 3),
  (1904916, 0, 3),
  (1909223, 7, 0),
  (1909845, 7, 0),
  (1910052, 0, 3),
  (1910526, 2, 3),
  (1912135, 1, 0),
  (1914694, 6, 0),
  (1919459, 3, 3),
  (1922042, 2, 2),
  (1925288, 6, 4),
  (1925811, 6, 4),
  (1927108, 3, 3),
  (1929792, 0, 7),
  (1935736, 2, 3),
  (1936935, 7, 7),
  (1937241, 3, 3),
  (1938588, 3, 5),
  (1938944, 4, 3),
  (1941132, 1, 3),
  (1941269, 2, 2),
  (1942007, 5, 1),
  (1944433, 5, 6),
  (1945037, 5, 3),
  (1945362, 2, 7),
  (1945833, 3, 3),
  (1947473, 6, 0),
  (1954849, 0, 0),
  (1957619, 5, 3),
  (1958287, 1, 4),
  (1959526, 6, 0),
  (1962146, 4, 4),
  (1972179, 4, 2),
  (1972598, 6, 4),
  (1973472, 2, 5),
  (1973753, 2, 5),
  (1975278, 1, 4),
  (1975689, 3, 2),
  (1978885, 6, 7),
  (1979400, 5, 2),
  (1980685, 4, 3),
  (1983970, 1, 7),
  (1987179, 5, 3),
  (1988608, 7, 6),
  (1988703, 6, 0),
  (1989498, 1, 2),
  (1991027, 2, 2),
  (1992012, 1, 1),
  (1992260, 6, 0),
  (1994506, 0, 4),
  (1998074, 4, 2),
  (1998104, 1, 0),
  (1999475, 6, 3),
  (1999708, 7, 0),
  (2000075, 6, 0),
  (2002634, 2, 0),
  (2006138, 0, 6),
  (2006686, 6, 1),
  (2007340, 2, 3),
  (2009609, 6, 0),
  (2016844, 6, 5),
  (2018625, 4, 6),
  (2021533, 7, 0),
  (2022081, 0, 0),
  (2023436, 1, 4),
  (2026403, 5, 3),
  (2030603, 5, 7),
  (2031029, 0, 7),
  (2034765, 2, 1),
  (2037906, 4, 3),
  (2038640, 4, 0),
  (2040460, 5, 5),
  (2043570, 6, 0),
  (2045858, 7, 4),
  (2046502, 6, 5),
  (2048806, 1, 4),
  (2053154, 7, 0),
  (2055245, 0, 0),
  (2058629, 6, 6),
  (2060339, 5, 2),
  (2067047, 3, 2),
  (2067104, 7, 4),
  (2070388, 6, 4),
  (2074203, 0, 5),
  (2079109, 3, 3),
  (2080471, 2, 6),
  (2080801, 6, 0),
  (2081551, 6, 3),
  (2084801, 7, 0),
  (2088058, 6, 7),
  (2089563, 6, 5),
  (2090157, 6, 4),
  (2091448, 5, 7),
  (2091767, 1, 6),
  (2097699, 1, 0),
  (2098598, 6, 6),
  (2101619, 2, 6),
  (2102395, 4, 2),
  (2102418, 3, 7),
  (2103109, 3, 7),
  (2105058, 5, 3),
  (2107786, 2, 3),
  (2110152, 4, 0),
  (2112214, 7, 4),
  (2115782, 0, 4),
  (2118919, 2, 2),
  (2121763, 2, 7),
  (2123240, 5, 3),
  (2136762, 6, 7),
  (2143587, 5, 1),
  (2144215, 4, 3),
  (2144516, 3, 3),
  (2147643, 3, 3),
  (2147762, 1, 0),
  (2152837, 2, 4),
  (2158347, 7, 4),
  (2158596, 3, 7),
  (2162195, 0, 2),
  (2166376, 7, 0),
  (2167296, 0, 4),
  (2169277, 3, 3),
  (2170353, 2, 2),
  (2172489, 4, 3),
  (2173966, 7, 3),
  (2175679, 0, 0),
  (2176651, 4, 3),
  (2176810, 1, 4),
  (2180235, 0, 0),
  (2182269, 1, 6),
  (2189224, 3, 3),
  (2190222, 2, 3),
  (2191944, 0, 0),
  (2192018, 2, 3),
  (2192907, 5, 7),
  (2194051, 1, 4),
  (2195545, 5, 6),
  (2195915, 0, 4),
  (2202500, 5, 7),
  (2206864, 3, 0),
  (2208120, 2, 3),
  (2208821, 2, 7),
  (2209223, 6, 0),
  (2214344, 6, 0),
  (2226019, 6, 0),
  (2226170, 1, 7),
  (2227922, 1, 7),
  (2228475, 7, 4),
  (2229434, 6, 0),
  (2229597, 4, 3),
  (2230364, 2, 3),
  (2237914, 2, 7),
  (2242363, 7, 2),
  (2245747, 7, 0),
  (2246148, 6, 3),
  (2248005, 7, 1),
  (2250102, 4, 6),
  (2252764, 1, 0),
  (2256431, 0, 1),
  (2261242, 4, 3),
  (2264298, 6, 0),
  (2266013, 2, 3),
  (2269809, 3, 3),
  (2271640, 3, 3),
  (2272291, 1, 0),
  (2272893, 5, 3),
  (2273976, 7, 7),
  (2274466, 2, 4),
  (2274896, 5, 6),
  (2280134, 7, 3),
  (2283476, 3, 2),
  (2284659, 4, 4),
  (2286166, 5, 6),
  (2286274, 4, 3),
  (2288193, 0, 0),
  (2289309, 6, 0),
  (2289458, 3, 3),
  (2289584, 2, 1),
  (2293339, 4, 6),
  (2294739, 6, 0),
  (2295747, 6, 3),
  (2296503, 3, 6),
  (2300322, 4, 7),
  (2305588, 2, 3),
  (2306903, 4, 7),
  (2311355, 2, 6),
  (2311384, 2, 1),
  (2316728, 6, 0),
  (2317543, 2, 2),
  (2318154, 2, 2),
  (2318896, 3, 7),
  (2321334, 4, 2),
  (2323489, 3, 6),
  (2326348, 6, 5),
  (2332260, 6, 0),
  (2332965, 6, 0),
  (2334385, 0, 0),
  (2336966, 3, 5),
  (2337136, 6, 0),
  (2337244, 6, 4),
  (2338433, 7, 7),
  (2339551, 0, 3),
  (2343316, 3, 7),
  (2344012, 6, 4),
  (2347354, 6, 2),
  (2347788, 0, 0),
  (2352056, 3, 7),
  (2353329, 0, 2),
  (2358400, 1, 0),
  (2360236, 1, 0),
  (2360900, 1, 4),
  (2364191, 6, 7),
  (2364316, 5, 3),
  (2366353, 4, 3),
  (2366668, 7, 5),
  (2366857, 3, 2),
  (2368636, 4, 2),
  (2370828, 3, 1),
  (2376762, 0, 7),
  (2378059, 7, 3),
  (2378117, 3, 5),
  (2379754, 6, 4),
  (2379754, 6, 5),
  (2380114, 6, 0),
  (2380840, 4, 7),
  (2382367, 4, 3),
  (2390841, 0, 0),
  (2394145, 3, 6),
  (2395616, 3, 4),
  (2396017, 1, 0),
  (2398786, 4, 2),
  (2402172, 0, 0),
  (2403067, 4, 3),
  (2405266, 1, 0),
  (2405676, 3, 7),
  (2413108, 3, 2),
  (2414238, 6, 4),
  (2416502, 2, 7),
  (2419467, 1, 4),
  (2422453, 7, 6),
  (2422608, 2, 3),
  (2422630, 1, 2),
  (2423250, 2, 0),
  (2425394, 4, 0),
  (2427442, 3, 4),
  (2427882, 3, 3),
  (2428102, 4, 2),
  (2428811, 6, 0),
  (2430020, 4, 7),
  (2430479, 7, 6),
  (2432053, 6, 0),
  (2437695, 1, 3),
  (2443870, 5, 6),
  (2444351, 2, 2),
  (2444702, 5, 7),
  (2444816, 7, 0),
  (2445863, 6, 3),
  (2452834, 3, 4),
  (2457059, 6, 0),
  (2457363, 2, 3),
  (2460450, 5, 2),
  (2461952, 0, 4),
  (2462612, 4, 7),
  (2463393, 7, 1),
  (2463825, 4, 3),
  (2463972, 2, 2),
  (2464039, 4, 3),
  (2464138, 4, 4),
  (2465227, 0, 2),
  (2468396, 5, 3),
  (2468660, 3, 5),
  (2469681, 6, 1),
  (2470458, 2, 3),
  (2472433, 1, 0),
  (2473316, 0, 5),
  (2475363, 3, 6),
  (2477233, 5, 2),
  (2477483, 6, 4),
  (2481696, 7, 1),
  (2482641, 7, 4),
  (2486519, 4, 6),
  (2489373, 6, 0),
  (2489868, 1, 0),
  (2491348, 1, 5),
  (2498253, 0, 3),
  (2503924, 1, 0),
  (2507944, 6, 4),
  (2512239, 2, 7),
  (2513086, 0, 7),
  (2513767, 6, 7),
  (2514585, 2, 2),
  (2518504, 5, 7),
  (2519461, 0, 0),
  (2519651, 2, 6),
  (2520216, 4, 3),
  (2522821, 3, 3),
  (2522944, 6, 3),
  (2525545, 1, 0),
  (2531039, 0, 2),
  (2531307, 1, 3),
  (2532116, 3, 2),
  (2532234, 3, 3),
  (2536329, 5, 3),
  (2536459, 0, 4),
  (2542384, 2, 5),
  (2542589, 1, 7),
  (2542818, 0, 4),
  (2542871, 2, 2),
  (2544953, 7, 0),
  (2545158, 1, 2),
  (2545685, 5, 2),
  (2545876, 7, 3),
  (2549780, 2, 3),
  (2552380, 3, 0),
  (2552667, 1, 0),
  (2556446, 7, 3),
  (2557079, 2, 0),
  (2558963, 6, 7),
  (2562556, 1, 0),
  (2564708, 0, 4),
  (2564934, 4, 3),
  (2566402, 1, 0),
  (2570362, 2, 7),
  (2570746, 6, 0),
  (2571005, 3, 3),
  (2576352, 6, 4),
  (2576835, 6, 7),
  (2576881, 7, 0),
  (2578022, 4, 6),
  (2581587, 1, 0),
  (2582087, 5, 3),
  (2583989, 1, 7),
  (2584460, 4, 7),
  (2590898, 0, 0),
  (2593005, 4, 1),
  (2597726, 3, 3),
  (2607289, 6, 0),
  (2609591, 3, 3),
  (2611491, 2, 3),
  (2617670, 3, 6),
  (2617704, 3, 2),
  (2621073, 2, 3),
  (2621558, 6, 3),
  (2625339, 2, 2),
  (2625451, 2, 3),
  (2626989, 6, 0),
  (2628239, 5, 3),
  (2628928, 2, 3),
  (2629953, 3, 2),
  (2635693, 6, 4),
  (2636548, 5, 3),
  (2636592, 7, 0),
  (2637477, 0, 0),
  (2638035, 5, 7),
  (2641000, 1, 7),
  (2641821, 4, 3),
  (2642279, 4, 0),
  (2646619, 1, 7),
  (2649890, 0, 6),
  (2651705, 1, 3),
  (2652104, 7, 0),
  (2652787, 2, 6),
  (2653587, 0, 7),
  (2657578, 2, 4),
  (2658311, 2, 6),
  (2659670, 6, 3),
  (2660069, 5, 3),
  (2660355, 7, 0),
  (2667213, 2, 3),
  (2672286, 0, 7),
  (2673651, 2, 4),
  (2679871, 3, 3),
  (2681276, 7, 7),
  (2688161, 5, 2),
  (2689703, 6, 6),
  (2691856, 7, 0),
  (2693812, 1, 3),
  (2696101, 1, 4),
  (2696614, 2, 2),
  (2700283, 7, 7),
  (2700512, 4, 2),
  (2702719, 6, 4),
  (2705344, 2, 3),
  (2707858, 4, 5),
  (2708533, 2, 7),
  (2708697, 2, 3),
  (2709225, 6, 0),
  (2712941, 7, 4),
  (2714025, 0, 7),
  (2716139, 7, 0),
  (2718508, 6, 3),
  (2719027, 0, 2),
  (2720297, 2, 3),
  (2721569, 3, 3),
  (2723905, 0, 4),
  (2727631, 7, 7),
  (2730601, 6, 0),
  (2732988, 6, 0),
  (2734944, 6, 0),
  (2739560, 2, 6),
  (2740239, 1, 0),
  (2740373, 1, 4),
  (2740540, 4, 7),
  (2740843, 5, 3),
  (2743040, 6, 0),
  (2744448, 5, 7),
  (2746620, 5, 3),
  (2750076, 6, 7),
  (2754107, 1, 3),
  (2758574, 1, 0),
  (2761458, 6, 0),
  (2766776, 0, 0),
  (2770468, 5, 3),
  (2770776, 1, 5),
  (2773325, 5, 6),
  (2773502, 2, 7),
  (2773710, 1, 4),
  (2774008, 5, 3),
  (2775167, 2, 2),
  (2782500, 3, 1),
  (2784613, 1, 0),
  (2793258, 4, 7),
  (2793482, 2, 1),
  (2796332, 1, 7),
  (2797535, 7, 0),
  (2797926, 2, 6),
  (2800738, 6, 7),
  (2804068, 7, 2),
  (2804569, 7, 0),
  (2805954, 6, 2),
  (2806671, 3, 1),
  (2809247, 3, 7),
  (2810973, 7, 0),
  (2811388, 1, 3),
  (2813131, 6, 0),
  (2816123, 6, 0),
  (2816597, 5, 3),
  (2817850, 2, 6),
  (2820660, 6, 2),
  (2822749, 6, 1),
  (2824552, 3, 0),
  (2824985, 1, 3),
  (2825234, 1, 7),
  (2825427, 4, 3),
  (2825998, 3, 5),
  (2827056, 6, 3),
  (2834043, 1, 1),
  (2836415, 2, 3),
  (2839282, 3, 6),
  (2839997, 7, 0),
  (2840818, 2, 3),
  (2844051, 1, 0),
  (2844467, 3, 3),
  (2849856, 0, 4),
  (2850290, 6, 0),
  (2851719, 0, 7),
  (2856130, 5, 2),
  (2860262, 7, 0),
  (2862888, 3, 3),
  (2863331, 0, 4),
  (2868627, 0, 0),
  (2868692, 0, 0),
  (2869125, 3, 7),
  (2872300, 0, 0),
  (2873371, 1, 3),
  (2875053, 4, 3),
  (2876213, 4, 3),
  (2877519, 1, 4),
  (2878156, 3, 3),
  (2880966, 5, 3),
  (2882892, 1, 0),
  (2883176, 5, 7),
  (2883253, 7, 4),
  (2884048, 2, 6),
  (2885565, 2, 7),
  (2886353, 6, 0),
  (2887783, 7, 0),
  (2887811, 6, 4),
  (2888040, 4, 3),
  (2888691, 0, 3),
  (2888855, 4, 3),
  (2891813, 6, 4),
  (2894129, 2, 1),
  (2898877, 3, 7),
  (2908891, 3, 3),
  (2910874, 3, 7),
  (2911778, 4, 3),
  (2915178, 5, 3),
  (2916830, 1, 1),
  (2923207, 2, 3),
  (2923480, 1, 1),
  (2924624, 1, 0),
  (2925189, 1, 0),
  (2927143, 3, 3),
  (2929934, 2, 6),
  (2932105, 7, 0),
  (2933454, 2, 6),
  (2937294, 6, 7),
  (2937517, 0, 3),
  (2940183, 7, 7),
  (2943205, 1, 4),
  (2943399, 4, 3),
  (2944162, 0, 0),
  (2944817, 4, 6),
  (2947048, 6, 3),
  (2947080, 0, 0),
  (2949006, 7, 4),
  (2954336, 5, 3),
  (2957177, 2, 3),
  (2959156, 7, 0),
  (2961253, 4, 5),
  (2964751, 0, 0),
  (2965205, 2, 7),
  (2967454, 7, 0),
  (2967974, 0, 0),
  (2968140, 5, 0),
  (2969883, 3, 7),
  (2970209, 4, 3),
  (2970334, 2, 3),
  (2970749, 1, 4),
  (2973254, 3, 3),
  (2976731, 7, 4),
  (2978902, 7, 0),
  (2980828, 3, 7),
  (2984672, 4, 3),
  (2984810, 3, 3),
  (2984836, 3, 7),
  (2988012, 4, 3),
  (2988576, 5, 5),
  (2995920, 2, 3),
  (3001368, 7, 4),
  (3005365, 3, 3),
  (3005968, 4, 3),
  (3007400, 3, 3),
  (3008536, 4, 5),
  (3009627, 3, 7),
  (3009721, 1, 0),
  (3014081, 5, 3),
  (3014278, 1, 1),
  (3015427, 3, 2),
  (3016556, 3, 3),
  (3020741, 4, 3),
  (3022710, 0, 3),
  (3027419, 6, 0),
  (3027519, 4, 3),
  (3027791, 7, 0),
  (3029226, 2, 0),
  (3035850, 3, 3),
  (3036955, 0, 3),
  (3038722, 2, 3),
  (3038985, 4, 6),
  (3039065, 6, 1),
  (3043253, 0, 4),
  (3048600, 6, 7),
  (3051338, 1, 3),
  (3051810, 2, 7),
  (3052518, 7, 2),
  (3053146, 3, 3),
  (3055234, 1, 0),
  (3059935, 2, 6),
  (3060419, 7, 4),
  (3063031, 6, 7),
  (3064209, 0, 0),
  (3070634, 6, 7),
  (3073836, 1, 4),
  (3075944, 6, 2),
  (3076671, 7, 0),
  (3077099, 2, 3),
  (3078696, 2, 5),
  (3079546, 6, 2),
  (3079628, 6, 3),
  (3079691, 7, 5),
  (3085466, 7, 7),
  (3087345, 7, 0),
  (3087760, 0, 0),
  (3092741, 5, 1),
  (3093173, 2, 1),
  (3093630, 4, 6),
  (3099220, 3, 3),
  (3099275, 4, 3),
  (3100829, 1, 0),
  (3100942, 1, 0),
  (3104161, 4, 3),
  (3105700, 5, 6),
  (3105792, 1, 6),
  (3107981, 0, 0),
  (3108864, 6, 0),
  (3109339, 6, 7),
  (3110079, 1, 7),
  (3115969, 2, 4),
  (3117009, 5, 7),
  (3121386, 3, 3),
  (3124061, 6, 7),
  (3126992, 3, 2),
  (3130601, 6, 7),
  (3130776, 3, 7),
  (3132453, 6, 6),
  (3134699, 7, 0),
  (3136025, 7, 0),
  (3136228, 2, 6),
  (3140864, 7, 0),
  (3144160, 7, 4),
  (3145749, 3, 6),
  (3147853, 5, 2),
  (3148528, 6, 0),
  (3154641, 2, 2),
  (3154952, 4, 7),
  (3155673, 5, 3),
  (3157888, 4, 6),
  (3158731, 3, 3),
  (3161468, 3, 3),
  (3164156, 5, 3),
  (3166480, 2, 6),
  (3168564, 4, 0),
  (3170506, 1, 5),
  (3173070, 5, 3),
  (3174259, 5, 3),
  (3175574, 2, 3),
  (3176170, 1, 7),
  (3177940, 7, 0),
  (3184355, 3, 2),
  (3187853, 3, 3),
  (3189672, 0, 7),
  (3191479, 2, 3),
  (3195037, 1, 7),
  (3197009, 1, 4),
  (3198454, 1, 6),
  (3198503, 6, 6),
  (3199214, 2, 6),
  (3201399, 0, 0),
  (3201976, 5, 5),
  (3206366, 7, 3),
  (3210190, 4, 3),
  (3210226, 4, 3),
  (3213343, 6, 0),
  (3214114, 7, 0),
  (3214770, 1, 0),
  (3216126, 0, 4),
  (3216856, 3, 6),
  (3221721, 5, 0),
  (3221750, 7, 0),
  (3222706, 5, 3),
  (3223374, 2, 3),
  (3223879, 7, 2),
  (3225699, 5, 3),
  (3228110, 5, 3),
  (3228229, 2, 3),
  (3235371, 0, 0),
  (3238533, 6, 0),
  (3241983, 2, 3),
  (3244375, 3, 3),
  (3245667, 6, 7),
  (3248132, 3, 4),
  (3248139, 0, 3),
  (3251142, 0, 4),
  (3251854, 7, 0),
  (3251947, 2, 3),
  (3255413, 3, 3),
  (3256979, 0, 2),
  (3259727, 6, 2),
  (3261831, 7, 7),
  (3263687, 3, 7),
  (3264137, 6, 0),
  (3264801, 1, 0),
  (3267096, 6, 0),
  (3267997, 6, 7),
  (3268417, 3, 3),
  (3268907, 7, 3),
  (3271390, 1, 0),
  (3275687, 6, 0),
  (3276041, 1, 1),
  (3280330, 5, 5),
  (3280944, 6, 7),
  (3282276, 6, 0),
  (3283182, 5, 7),
  (3285116, 0, 3),
  (3288355, 1, 3),
  (3289057, 4, 3),
  (3290180, 0, 0),
  (3291929, 6, 4),
  (3293098, 1, 1),
  (3293407, 6, 0),
  (3293444, 1, 0),
  (3294878, 1, 0),
  (3299701, 2, 3),
  (3302332, 3, 3),
  (3306459, 6, 4),
  (3311387, 6, 4),
  (3311810, 0, 2),
  (3312124, 4, 6),
  (3314705, 1, 6),
  (3316822, 2, 2),
  (3317743, 5, 6),
  (3322998, 2, 2),
  (3324051, 7, 4),
  (3327608, 4, 3),
  (3327698, 2, 3),
  (3327703, 7, 7),
  (3334948, 2, 3),
  (3336253, 7, 0),
  (3336363, 7, 0),
  (3336799, 4, 7),
  (3339469, 6, 0),
  (3339862, 1, 7),
  (3349944, 0, 0),
  (3350627, 6, 0),
  (3351377, 6, 1),
  (3351714, 4, 6),
  (3354474, 5, 7),
  (3359773, 6, 4),
  (3361309, 3, 5),
  (3365234, 2, 7),
  (3369806, 2, 7),
  (3370647, 6, 0),
  (3370674, 6, 3),
  (3371898, 7, 0),
  (3372534, 0, 0),
  (3372797, 1, 0),
  (3373041, 3, 0),
  (3375701, 6, 0),
  (3377568, 2, 2),
  (3383156, 3, 2),
  (3385777, 4, 7),
  (3389286, 1, 0),
  (3392432, 3, 3),
  (3393832, 1, 3),
  (3397103, 7, 1),
  (3405656, 6, 4),
  (3414826, 6, 0),
  (3415171, 4, 6),
  (3417825, 5, 6),
  (3418470, 6, 6),
  (3418503, 4, 7),
  (3419418, 6, 0),
  (3419676, 2, 1),
  (3422231, 2, 1),
  (3435356, 4, 2),
  (3435751, 1, 3),
  (3436222, 6, 7),
  (3437542, 0, 3),
  (3440671, 1, 0),
  (3441363, 2, 6),
  (3442977, 7, 0),
  (3444955, 3, 3),
  (3448238, 3, 0),
  (3450823, 2, 2),
  (3456546, 2, 6),
  (3457718, 2, 0),
  (3462660, 7, 2),
  (3464531, 4, 6),
  (3469555, 2, 3),
  (3469925, 0, 0),
  (3471338, 5, 2),
  (3472343, 3, 2),
  (3473333, 3, 5),
  (3473586, 3, 1),
  (3479626, 7, 6),
  (3479985, 7, 3),
  (3483506, 5, 3),
  (3486690, 3, 0),
  (3488098, 4, 3),
  (3492252, 6, 4),
  (3493432, 5, 3),
  (3493886, 4, 7),
  (3495111, 5, 7),
  (3497182, 1, 4),
  (3499431, 3, 3),
  (3501658, 3, 3),
  (3503057, 3, 3),
  (3505300, 5, 7),
  (3506396, 0, 0),
  (3508357, 0, 0),
  (3508377, 4, 3),
  (3511514, 3, 7),
  (3513310, 2, 3),
  (3514594, 4, 3),
  (3518493, 7, 3),
  (3518657, 0, 5),
  (3521392, 5, 2),
  (3522048, 2, 2),
  (3526216, 6, 3),
  (3528129, 4, 4),
  (3528527, 1, 4),
  (3531265, 3, 5),
  (3531379, 4, 6),
  (3532224, 7, 3),
  (3532465, 3, 5),
  (3535108, 7, 0),
  (3536768, 5, 3),
  (3536935, 6, 0),
  (3541036, 2, 2),
  (3544783, 2, 7),
  (3548384, 4, 3),
  (3548895, 6, 0),
  (3549062, 5, 4),
  (3558326, 5, 3),
  (3560490, 0, 0),
  (3564485, 7, 0),
  (3564601, 1, 7),
  (3564603, 1, 0),
  (3566934, 1, 7),
  (3567958, 6, 0),
  (3571163, 3, 2),
  (3575784, 2, 3),
  (3582704, 3, 3),
  (3583634, 2, 3),
  (3583808, 5, 6),
  (3585672, 4, 3),
  (3586750, 7, 0),
  (3587030, 1, 3),
  (3587741, 1, 0),
  (3588713, 4, 1),
  (3591742, 0, 0),
  (3591771, 0, 3),
  (3592446, 5, 1),
  (3593153, 0, 0),
  (3593865, 1, 0),
  (3594161, 3, 5),
  (3596776, 2, 2),
  (3598215, 0, 6),
  (3598891, 3, 7),
])
