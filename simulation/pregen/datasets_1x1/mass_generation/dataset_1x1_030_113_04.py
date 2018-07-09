from util import *
schedule = deque([
  (3215, 1, 0),
  (5715, 2, 3),
  (11349, 3, 2),
  (11728, 6, 6),
  (12160, 3, 6),
  (12508, 0, 7),
  (15509, 3, 6),
  (18694, 1, 4),
  (27750, 4, 7),
  (29450, 2, 5),
  (30830, 7, 3),
  (35503, 4, 7),
  (37164, 2, 7),
  (37700, 0, 7),
  (44337, 7, 0),
  (50695, 5, 3),
  (56222, 0, 0),
  (57946, 0, 7),
  (60317, 1, 7),
  (61573, 5, 7),
  (66029, 6, 7),
  (67134, 2, 6),
  (70068, 0, 3),
  (70395, 2, 5),
  (73689, 7, 4),
  (78200, 2, 3),
  (78291, 4, 5),
  (80483, 3, 3),
  (84144, 6, 3),
  (84966, 1, 0),
  (87523, 3, 7),
  (87570, 4, 7),
  (89406, 7, 7),
  (94794, 5, 2),
  (95487, 1, 7),
  (96301, 3, 7),
  (97336, 7, 7),
  (98339, 4, 7),
  (98725, 2, 7),
  (99281, 6, 4),
  (101220, 7, 3),
  (103211, 3, 7),
  (104968, 6, 7),
  (105466, 5, 3),
  (106753, 4, 7),
  (107996, 7, 4),
  (109918, 2, 7),
  (110496, 7, 7),
  (111139, 7, 7),
  (119678, 2, 7),
  (128737, 1, 7),
  (132112, 2, 0),
  (133273, 0, 7),
  (134378, 2, 6),
  (134607, 7, 7),
  (136831, 5, 3),
  (139406, 2, 6),
  (142107, 7, 7),
  (143299, 0, 3),
  (143829, 6, 3),
  (150225, 6, 7),
  (152614, 0, 0),
  (158564, 1, 0),
  (170532, 3, 2),
  (173745, 7, 6),
  (175178, 2, 3),
  (175512, 5, 7),
  (178192, 1, 7),
  (178366, 4, 5),
  (178519, 6, 4),
  (179430, 0, 7),
  (179628, 6, 4),
  (180150, 5, 6),
  (181875, 1, 7),
  (182448, 5, 7),
  (183195, 5, 7),
  (183388, 6, 4),
  (183913, 7, 7),
  (186377, 7, 7),
  (186466, 3, 6),
  (186903, 6, 3),
  (187915, 7, 5),
  (188489, 0, 7),
  (189168, 2, 1),
  (193828, 7, 3),
  (198585, 0, 7),
  (201295, 6, 0),
  (205620, 6, 4),
  (210892, 7, 7),
  (211524, 7, 7),
  (213941, 4, 7),
  (216899, 4, 1),
  (217296, 5, 7),
  (219067, 7, 3),
  (220580, 7, 6),
  (222422, 4, 6),
  (226065, 4, 7),
  (227376, 7, 0),
  (228043, 7, 4),
  (229088, 2, 3),
  (232228, 4, 3),
  (233624, 5, 3),
  (235167, 5, 7),
  (238689, 3, 7),
  (239524, 0, 0),
  (240131, 0, 0),
  (248412, 4, 3),
  (249207, 5, 3),
  (252053, 2, 7),
  (252380, 6, 6),
  (253372, 6, 0),
  (254432, 0, 2),
  (255615, 3, 1),
  (256505, 3, 7),
  (261720, 1, 2),
  (262206, 0, 4),
  (263965, 6, 3),
  (266410, 5, 3),
  (267452, 4, 5),
  (270817, 6, 4),
  (271512, 4, 3),
  (272359, 3, 7),
  (273475, 3, 7),
  (280073, 5, 7),
  (285100, 5, 1),
  (285546, 5, 7),
  (288533, 0, 4),
  (289420, 4, 7),
  (295006, 7, 7),
  (295445, 3, 7),
  (305283, 1, 4),
  (305676, 4, 3),
  (305721, 5, 7),
  (306065, 0, 2),
  (307374, 3, 7),
  (307674, 3, 2),
  (308250, 1, 3),
  (311397, 1, 2),
  (312526, 6, 7),
  (314323, 5, 3),
  (318283, 7, 0),
  (318399, 2, 5),
  (322763, 1, 4),
  (327417, 6, 0),
  (331220, 5, 3),
  (332685, 3, 7),
  (333263, 3, 7),
  (334501, 6, 3),
  (336287, 5, 7),
  (337074, 2, 7),
  (341436, 0, 7),
  (347400, 1, 6),
  (349149, 5, 6),
  (350326, 4, 6),
  (351376, 6, 0),
  (352392, 2, 4),
  (352457, 1, 6),
  (352968, 2, 7),
  (353763, 7, 6),
  (354676, 3, 7),
  (358756, 1, 7),
  (363109, 1, 6),
  (364095, 5, 2),
  (365524, 7, 4),
  (368843, 7, 6),
  (369052, 2, 6),
  (369412, 4, 5),
  (370967, 3, 6),
  (372182, 7, 0),
  (372275, 7, 3),
  (373177, 3, 7),
  (373725, 4, 7),
  (376571, 0, 7),
  (379672, 7, 6),
  (380327, 0, 3),
  (383320, 5, 2),
  (385002, 3, 7),
  (386307, 3, 7),
  (387941, 1, 0),
  (388679, 4, 7),
  (389753, 2, 6),
  (389785, 2, 7),
  (390558, 5, 7),
  (396658, 7, 3),
  (399669, 2, 3),
  (401797, 6, 7),
  (409055, 0, 2),
  (410125, 5, 2),
  (411090, 1, 3),
  (411637, 7, 0),
  (420886, 1, 3),
  (422375, 4, 7),
  (425709, 5, 2),
  (426886, 7, 0),
  (427828, 0, 7),
  (428870, 6, 7),
  (433002, 2, 3),
  (433559, 1, 4),
  (435515, 7, 7),
  (438235, 5, 3),
  (438697, 4, 7),
  (443545, 1, 3),
  (445721, 0, 3),
  (447760, 6, 7),
  (450160, 2, 6),
  (450275, 2, 5),
  (450706, 0, 3),
  (451142, 2, 3),
  (457450, 5, 3),
  (469675, 0, 7),
  (471455, 4, 7),
  (472478, 3, 7),
  (473620, 1, 3),
  (475552, 0, 4),
  (477346, 0, 7),
  (477959, 3, 5),
  (479195, 7, 7),
  (479297, 4, 7),
  (479556, 5, 7),
  (479915, 3, 5),
  (483000, 0, 1),
  (483396, 6, 7),
  (486360, 1, 5),
  (487343, 2, 5),
  (493127, 3, 2),
  (494814, 0, 0),
  (495841, 1, 7),
  (498961, 1, 0),
  (500912, 5, 3),
  (501739, 4, 3),
  (504887, 1, 7),
  (505473, 3, 6),
  (506792, 5, 7),
  (510180, 3, 3),
  (516238, 5, 3),
  (520134, 3, 7),
  (521070, 3, 3),
  (524157, 0, 7),
  (525080, 5, 1),
  (528878, 1, 4),
  (529775, 5, 3),
  (530323, 0, 4),
  (530768, 4, 7),
  (531872, 7, 7),
  (535593, 0, 7),
  (536683, 4, 7),
  (539565, 5, 3),
  (539929, 4, 6),
  (540275, 3, 7),
  (541005, 0, 7),
  (542007, 3, 7),
  (543346, 7, 3),
  (545279, 0, 4),
  (550956, 4, 3),
  (551018, 0, 6),
  (551669, 3, 2),
  (552297, 1, 7),
  (555677, 0, 5),
  (555731, 3, 3),
  (556929, 7, 7),
  (557959, 7, 6),
  (559841, 2, 6),
  (560721, 1, 7),
  (561142, 5, 2),
  (563239, 2, 2),
  (563734, 6, 7),
  (564751, 1, 0),
  (567797, 4, 3),
  (569196, 3, 2),
  (571943, 5, 3),
  (574381, 5, 3),
  (576743, 5, 3),
  (578331, 6, 4),
  (578964, 7, 4),
  (580256, 7, 7),
  (582033, 5, 7),
  (584145, 1, 6),
  (586279, 2, 3),
  (586624, 0, 7),
  (586791, 7, 0),
  (590001, 0, 7),
  (593408, 5, 5),
  (594828, 3, 7),
  (599531, 3, 3),
  (599996, 3, 6),
  (601972, 5, 3),
  (602798, 2, 7),
  (603582, 5, 5),
  (604358, 4, 6),
  (605064, 5, 3),
  (606924, 4, 7),
  (607065, 0, 6),
  (607115, 2, 5),
  (608683, 3, 7),
  (608779, 2, 7),
  (611087, 1, 3),
  (612121, 3, 7),
  (614152, 4, 7),
  (615335, 5, 2),
  (615665, 1, 7),
  (618145, 4, 3),
  (619047, 3, 7),
  (623536, 6, 3),
  (625902, 0, 0),
  (626506, 7, 3),
  (633136, 7, 7),
  (633586, 1, 3),
  (636226, 4, 2),
  (640280, 0, 7),
  (642432, 2, 3),
  (643233, 5, 7),
  (643263, 6, 3),
  (644593, 6, 7),
  (645530, 0, 7),
  (646703, 3, 7),
  (647945, 6, 7),
  (648451, 0, 7),
  (648524, 6, 7),
  (651815, 4, 2),
  (651963, 1, 0),
  (653544, 6, 4),
  (654083, 7, 7),
  (656792, 7, 7),
  (656873, 3, 3),
  (658933, 4, 6),
  (661624, 5, 7),
  (665205, 2, 3),
  (667178, 0, 5),
  (668416, 7, 0),
  (668882, 0, 7),
  (669945, 3, 3),
  (671866, 6, 4),
  (672287, 4, 2),
  (674315, 4, 4),
  (674422, 4, 7),
  (674431, 2, 7),
  (675081, 1, 3),
  (675887, 2, 3),
  (680966, 0, 7),
  (682466, 3, 7),
  (682723, 6, 7),
  (684544, 3, 7),
  (684817, 7, 7),
  (688964, 1, 3),
  (689509, 3, 7),
  (689542, 1, 5),
  (689793, 5, 4),
  (692434, 7, 7),
  (694636, 5, 3),
  (695971, 2, 7),
  (699890, 5, 3),
  (700846, 1, 7),
  (700867, 6, 7),
  (702227, 1, 7),
  (702253, 6, 7),
  (702444, 1, 7),
  (703856, 1, 7),
  (710532, 5, 7),
  (711151, 0, 7),
  (723264, 2, 6),
  (726837, 0, 0),
  (727456, 2, 7),
  (727866, 7, 7),
  (728804, 2, 3),
  (729557, 2, 3),
  (729932, 1, 7),
  (732633, 3, 3),
  (733596, 7, 5),
  (735809, 5, 3),
  (736710, 6, 0),
  (737037, 0, 3),
  (738001, 2, 3),
  (742094, 5, 6),
  (744873, 1, 0),
  (745145, 5, 4),
  (749764, 0, 7),
  (751805, 7, 4),
  (755753, 2, 3),
  (756081, 4, 3),
  (758793, 5, 3),
  (763469, 4, 1),
  (764383, 1, 6),
  (765032, 0, 0),
  (767313, 6, 3),
  (768263, 7, 7),
  (770517, 1, 0),
  (770587, 1, 2),
  (771780, 5, 3),
  (773801, 3, 6),
  (774061, 6, 7),
  (774974, 5, 3),
  (775771, 6, 4),
  (779918, 1, 0),
  (780740, 1, 2),
  (781034, 3, 2),
  (782047, 5, 2),
  (788463, 1, 0),
  (788478, 0, 3),
  (792146, 4, 7),
  (792798, 1, 7),
  (793780, 2, 7),
  (794859, 5, 2),
  (796038, 1, 6),
  (796283, 4, 7),
  (796697, 0, 4),
  (797504, 3, 3),
  (800372, 3, 6),
  (801560, 5, 7),
  (802701, 5, 6),
  (804740, 6, 0),
  (805853, 6, 4),
  (806190, 7, 7),
  (811520, 0, 4),
  (811679, 4, 6),
  (813807, 3, 5),
  (817448, 7, 7),
  (817657, 4, 7),
  (818197, 7, 0),
  (818203, 4, 6),
  (818886, 2, 3),
  (819301, 0, 0),
  (822970, 2, 7),
  (825473, 1, 6),
  (828344, 5, 6),
  (828398, 2, 7),
  (829936, 1, 2),
  (831272, 3, 7),
  (831366, 4, 0),
  (831938, 2, 7),
  (832499, 0, 7),
  (832765, 4, 5),
  (834561, 4, 2),
  (835396, 6, 0),
  (837872, 1, 7),
  (839997, 0, 7),
  (840595, 2, 6),
  (841748, 4, 7),
  (843836, 7, 0),
  (844238, 0, 7),
  (849463, 1, 7),
  (851692, 2, 3),
  (851796, 2, 6),
  (853773, 0, 4),
  (853779, 1, 0),
  (856012, 7, 0),
  (858194, 5, 6),
  (859198, 3, 3),
  (860156, 2, 5),
  (864300, 2, 7),
  (866360, 7, 2),
  (867021, 4, 5),
  (867099, 1, 7),
  (868479, 0, 7),
  (868746, 0, 7),
  (871979, 6, 3),
  (872229, 3, 4),
  (872955, 4, 3),
  (877098, 5, 7),
  (877253, 3, 7),
  (877897, 3, 5),
  (878296, 1, 7),
  (886264, 0, 0),
  (886403, 0, 4),
  (893659, 6, 0),
  (895325, 1, 0),
  (896561, 7, 0),
  (896712, 7, 5),
  (897267, 6, 0),
  (900409, 6, 4),
  (900410, 3, 7),
  (901693, 6, 4),
  (909898, 3, 7),
  (911579, 6, 0),
  (913332, 0, 3),
  (913935, 5, 7),
  (914097, 0, 0),
  (916706, 3, 7),
  (918871, 5, 3),
  (919990, 4, 7),
  (920947, 0, 7),
  (924594, 6, 4),
  (925462, 2, 7),
  (930548, 1, 7),
  (932034, 6, 5),
  (933962, 3, 7),
  (934527, 5, 3),
  (935235, 7, 7),
  (946339, 5, 7),
  (948388, 3, 6),
  (949317, 6, 7),
  (953325, 7, 3),
  (953517, 1, 3),
  (953775, 4, 7),
  (954003, 5, 7),
  (954916, 1, 7),
  (954937, 6, 0),
  (958167, 3, 6),
  (962461, 3, 7),
  (962623, 4, 7),
  (963304, 2, 7),
  (967500, 3, 3),
  (968853, 0, 7),
  (969207, 4, 3),
  (974688, 1, 6),
  (975229, 0, 4),
  (976148, 1, 3),
  (976293, 6, 7),
  (976500, 5, 3),
  (980380, 7, 4),
  (981918, 4, 6),
  (984161, 6, 4),
  (987911, 3, 6),
  (991536, 7, 0),
  (992219, 0, 7),
  (992874, 2, 5),
  (995592, 6, 4),
  (999040, 5, 7),
  (1000975, 5, 3),
  (1002881, 6, 4),
  (1005488, 1, 0),
  (1005889, 1, 7),
  (1006957, 2, 6),
  (1008519, 6, 0),
  (1011460, 6, 7),
  (1015510, 6, 5),
  (1017848, 2, 6),
  (1018792, 6, 3),
  (1019525, 4, 6),
  (1019918, 0, 7),
  (1025231, 6, 3),
  (1025731, 0, 0),
  (1025898, 6, 0),
  (1033412, 4, 3),
  (1036807, 3, 2),
  (1037431, 2, 6),
  (1038610, 1, 0),
  (1043645, 7, 3),
  (1043995, 6, 0),
  (1045133, 5, 5),
  (1046510, 7, 0),
  (1046964, 7, 7),
  (1048627, 4, 7),
  (1053241, 1, 0),
  (1054304, 5, 7),
  (1054433, 5, 6),
  (1054545, 0, 2),
  (1059190, 3, 7),
  (1059860, 3, 2),
  (1063951, 7, 4),
  (1064660, 0, 0),
  (1065139, 3, 3),
  (1066890, 5, 4),
  (1069789, 3, 3),
  (1070859, 0, 7),
  (1071391, 1, 0),
  (1073345, 0, 7),
  (1074079, 6, 0),
  (1075170, 1, 7),
  (1077486, 5, 7),
  (1079848, 5, 7),
  (1082426, 2, 2),
  (1085523, 2, 5),
  (1089280, 2, 3),
  (1090241, 4, 2),
  (1091155, 4, 2),
  (1094296, 7, 3),
  (1096340, 4, 3),
  (1097552, 0, 0),
  (1097636, 0, 7),
  (1097836, 0, 7),
  (1099294, 4, 7),
  (1101655, 0, 3),
  (1102644, 0, 0),
  (1103905, 5, 2),
  (1104708, 3, 7),
  (1105370, 1, 4),
  (1107042, 5, 7),
  (1107146, 2, 7),
  (1111218, 6, 0),
  (1111453, 2, 2),
  (1112158, 1, 5),
  (1112550, 4, 7),
  (1114320, 6, 4),
  (1117354, 1, 0),
  (1119427, 1, 0),
  (1126634, 2, 7),
  (1127925, 1, 2),
  (1132389, 2, 7),
  (1138350, 0, 7),
  (1138758, 2, 7),
  (1143547, 7, 0),
  (1143718, 6, 2),
  (1146256, 3, 6),
  (1148677, 2, 3),
  (1150969, 6, 7),
  (1154480, 1, 2),
  (1155481, 4, 5),
  (1158761, 6, 7),
  (1160519, 0, 7),
  (1160632, 3, 1),
  (1160690, 2, 3),
  (1160905, 5, 6),
  (1162983, 1, 0),
  (1166316, 7, 7),
  (1168218, 5, 3),
  (1169365, 6, 7),
  (1171674, 2, 2),
  (1172530, 7, 7),
  (1174806, 1, 0),
  (1180943, 0, 4),
  (1181347, 1, 4),
  (1181451, 4, 7),
  (1183413, 6, 4),
  (1184395, 3, 7),
  (1184698, 6, 0),
  (1185362, 7, 7),
  (1185730, 5, 7),
  (1189640, 4, 6),
  (1195137, 5, 7),
  (1195593, 0, 0),
  (1200563, 3, 7),
  (1203128, 1, 0),
  (1208374, 1, 7),
  (1210161, 5, 2),
  (1210803, 5, 7),
  (1211463, 0, 1),
  (1214996, 7, 7),
  (1215448, 5, 4),
  (1216637, 1, 7),
  (1217546, 5, 5),
  (1218671, 2, 7),
  (1220490, 1, 3),
  (1220973, 0, 3),
  (1223131, 4, 5),
  (1226724, 5, 5),
  (1228310, 5, 5),
  (1233744, 3, 7),
  (1233820, 2, 2),
  (1234276, 6, 7),
  (1234904, 3, 2),
  (1235751, 2, 6),
  (1239583, 6, 7),
  (1241860, 1, 0),
  (1243132, 7, 0),
  (1248383, 5, 4),
  (1249552, 2, 7),
  (1250459, 2, 7),
  (1253379, 1, 1),
  (1255632, 1, 0),
  (1255776, 2, 2),
  (1256003, 5, 2),
  (1256791, 2, 7),
  (1259909, 2, 1),
  (1264914, 0, 4),
  (1266277, 4, 7),
  (1266857, 6, 3),
  (1272601, 3, 6),
  (1274758, 6, 6),
  (1276488, 7, 2),
  (1276630, 0, 7),
  (1277123, 7, 7),
  (1277463, 5, 7),
  (1278015, 4, 6),
  (1278310, 3, 7),
  (1281905, 4, 5),
  (1284535, 4, 7),
  (1286006, 7, 7),
  (1288799, 7, 7),
  (1288816, 0, 6),
  (1289439, 5, 7),
  (1289525, 3, 6),
  (1292946, 0, 0),
  (1293822, 0, 0),
  (1295079, 3, 7),
  (1297813, 0, 7),
  (1300740, 0, 0),
  (1301234, 1, 7),
  (1304878, 4, 2),
  (1305178, 4, 7),
  (1308108, 5, 3),
  (1308719, 5, 6),
  (1309527, 3, 3),
  (1309763, 0, 0),
  (1311533, 5, 3),
  (1312568, 6, 0),
  (1314358, 4, 7),
  (1314493, 1, 7),
  (1317310, 2, 2),
  (1318583, 1, 0),
  (1322656, 6, 4),
  (1324314, 1, 7),
  (1325541, 2, 3),
  (1326219, 2, 3),
  (1335257, 2, 7),
  (1339723, 4, 7),
  (1340049, 5, 2),
  (1344954, 0, 4),
  (1350137, 3, 0),
  (1353836, 0, 7),
  (1354576, 3, 5),
  (1360018, 0, 0),
  (1362363, 5, 7),
  (1365319, 4, 2),
  (1366609, 2, 2),
  (1369691, 4, 5),
  (1371335, 6, 7),
  (1371411, 7, 7),
  (1371878, 3, 3),
  (1372093, 1, 0),
  (1378580, 7, 7),
  (1386852, 6, 0),
  (1388586, 3, 6),
  (1394599, 5, 7),
  (1395103, 5, 2),
  (1395366, 0, 3),
  (1398933, 2, 2),
  (1399420, 1, 2),
  (1400024, 2, 7),
  (1400221, 5, 3),
  (1406570, 2, 6),
  (1408683, 6, 7),
  (1409137, 1, 7),
  (1409165, 6, 3),
  (1410129, 4, 3),
  (1411635, 6, 4),
  (1415073, 1, 4),
  (1421198, 4, 7),
  (1422980, 3, 7),
  (1424853, 7, 7),
  (1425391, 3, 3),
  (1427182, 7, 6),
  (1430382, 1, 7),
  (1431316, 5, 2),
  (1432242, 1, 6),
  (1435025, 3, 2),
  (1436103, 0, 1),
  (1437013, 7, 6),
  (1437202, 7, 0),
  (1441183, 4, 6),
  (1442640, 4, 5),
  (1442816, 1, 7),
  (1443165, 3, 3),
  (1443653, 3, 7),
  (1444889, 3, 7),
  (1446914, 0, 0),
  (1452304, 2, 2),
  (1454196, 1, 5),
  (1455761, 1, 7),
  (1461690, 7, 3),
  (1462616, 2, 3),
  (1466178, 1, 7),
  (1467786, 6, 6),
  (1470336, 3, 6),
  (1476951, 3, 3),
  (1478064, 3, 7),
  (1480017, 7, 0),
  (1480883, 2, 6),
  (1481029, 1, 3),
  (1482026, 1, 7),
  (1484996, 6, 7),
  (1487894, 5, 7),
  (1495314, 5, 3),
  (1495530, 1, 4),
  (1495915, 1, 7),
  (1498214, 4, 3),
  (1499271, 6, 7),
  (1499333, 7, 0),
  (1502488, 1, 7),
  (1513309, 2, 7),
  (1516877, 7, 2),
  (1521855, 2, 7),
  (1522218, 0, 7),
  (1522549, 7, 7),
  (1529014, 0, 7),
  (1529683, 7, 7),
  (1535773, 5, 7),
  (1535960, 7, 7),
  (1536556, 5, 5),
  (1537194, 3, 6),
  (1538045, 2, 7),
  (1538616, 4, 7),
  (1539641, 5, 7),
  (1539759, 5, 5),
  (1540579, 1, 7),
  (1540757, 5, 3),
  (1541477, 7, 4),
  (1544134, 0, 0),
  (1546810, 3, 3),
  (1548299, 3, 7),
  (1550431, 5, 7),
  (1550930, 2, 6),
  (1555673, 2, 4),
  (1556386, 3, 4),
  (1559197, 1, 3),
  (1559489, 2, 3),
  (1559642, 5, 7),
  (1562954, 4, 6),
  (1565780, 4, 6),
  (1567198, 2, 4),
  (1572437, 1, 3),
  (1573898, 5, 3),
  (1576655, 7, 7),
  (1576768, 3, 7),
  (1583468, 7, 3),
  (1586235, 5, 5),
  (1588791, 0, 0),
  (1589630, 1, 7),
  (1590057, 4, 6),
  (1590066, 5, 7),
  (1590899, 4, 7),
  (1593542, 1, 0),
  (1598308, 0, 5),
  (1598624, 5, 3),
  (1599017, 4, 6),
  (1599613, 4, 2),
  (1602242, 6, 7),
  (1602449, 6, 7),
  (1605814, 6, 0),
  (1606184, 7, 3),
  (1606190, 5, 5),
  (1606543, 4, 5),
  (1607241, 2, 7),
  (1608127, 4, 3),
  (1609285, 4, 5),
  (1610052, 3, 2),
  (1611518, 6, 7),
  (1612542, 7, 7),
  (1614792, 2, 3),
  (1617814, 3, 3),
  (1621709, 6, 7),
  (1623573, 2, 6),
  (1623960, 7, 5),
  (1625717, 4, 3),
  (1625756, 2, 6),
  (1627083, 3, 1),
  (1633026, 7, 4),
  (1634585, 4, 7),
  (1634933, 2, 2),
  (1636851, 4, 3),
  (1638313, 5, 7),
  (1638384, 0, 0),
  (1639901, 7, 7),
  (1640058, 6, 7),
  (1642839, 2, 7),
  (1644866, 3, 3),
  (1645427, 1, 4),
  (1648519, 6, 7),
  (1651225, 1, 4),
  (1655284, 3, 5),
  (1664058, 6, 7),
  (1665655, 6, 7),
  (1667651, 2, 7),
  (1668480, 1, 3),
  (1672041, 5, 3),
  (1672054, 5, 2),
  (1673749, 4, 6),
  (1677984, 2, 7),
  (1682887, 1, 0),
  (1684377, 5, 2),
  (1686380, 6, 4),
  (1686774, 2, 7),
  (1689083, 0, 0),
  (1693755, 1, 4),
  (1697089, 4, 6),
  (1698685, 3, 7),
  (1699354, 6, 2),
  (1699864, 6, 7),
  (1703011, 7, 3),
  (1704530, 0, 4),
  (1707538, 6, 3),
  (1707655, 4, 5),
  (1707894, 7, 4),
  (1708089, 3, 7),
  (1708666, 0, 0),
  (1710538, 0, 5),
  (1711957, 5, 3),
  (1714004, 1, 6),
  (1719330, 4, 3),
  (1722183, 5, 2),
  (1722598, 2, 3),
  (1723779, 7, 7),
  (1724399, 4, 3),
  (1729526, 0, 7),
  (1731056, 3, 6),
  (1732012, 5, 2),
  (1734324, 0, 3),
  (1735925, 7, 3),
  (1736091, 1, 7),
  (1737718, 2, 6),
  (1739179, 3, 3),
  (1739317, 1, 7),
  (1741391, 6, 7),
  (1744583, 3, 3),
  (1744945, 6, 0),
  (1747817, 1, 2),
  (1750030, 3, 7),
  (1750666, 7, 7),
  (1756152, 5, 6),
  (1758855, 6, 0),
  (1762205, 1, 4),
  (1765697, 2, 3),
  (1765939, 7, 4),
  (1766374, 0, 7),
  (1767955, 5, 3),
  (1770353, 3, 5),
  (1770814, 6, 7),
  (1771829, 2, 3),
  (1775766, 0, 4),
  (1779082, 1, 4),
  (1784391, 5, 3),
  (1785422, 5, 5),
  (1795771, 0, 7),
  (1796899, 1, 7),
  (1799079, 1, 6),
  (1801835, 3, 2),
  (1809438, 4, 6),
  (1810489, 0, 5),
  (1811650, 1, 7),
  (1814560, 7, 2),
  (1814727, 4, 3),
  (1818097, 7, 7),
  (1818582, 0, 7),
  (1822337, 2, 3),
  (1822438, 5, 3),
  (1823064, 6, 0),
  (1824150, 4, 3),
  (1826980, 3, 7),
  (1827847, 2, 7),
  (1829520, 3, 6),
  (1832386, 3, 7),
  (1834539, 0, 0),
  (1841991, 6, 7),
  (1844595, 1, 0),
  (1845220, 4, 7),
  (1845519, 7, 0),
  (1845769, 2, 5),
  (1848120, 0, 0),
  (1848165, 6, 7),
  (1850884, 1, 7),
  (1854088, 5, 7),
  (1855527, 6, 3),
  (1855902, 1, 6),
  (1856370, 4, 7),
  (1858418, 7, 6),
  (1861837, 7, 4),
  (1864452, 4, 2),
  (1867652, 1, 0),
  (1871000, 3, 7),
  (1873187, 7, 0),
  (1874310, 3, 4),
  (1876355, 6, 6),
  (1876410, 1, 6),
  (1876574, 5, 7),
  (1880639, 3, 3),
  (1882569, 1, 7),
  (1885173, 2, 7),
  (1885609, 3, 7),
  (1894375, 2, 2),
  (1896766, 2, 7),
  (1898533, 1, 0),
  (1898780, 6, 7),
  (1900254, 1, 0),
  (1900765, 6, 4),
  (1902438, 1, 0),
  (1907172, 3, 7),
  (1908252, 2, 3),
  (1909005, 4, 5),
  (1909669, 4, 5),
  (1911135, 3, 3),
  (1911492, 3, 2),
  (1912801, 1, 7),
  (1914402, 0, 4),
  (1915117, 3, 6),
  (1917927, 1, 6),
  (1918535, 7, 7),
  (1920304, 2, 7),
  (1920970, 2, 5),
  (1921420, 6, 7),
  (1921542, 4, 3),
  (1922138, 2, 7),
  (1925671, 6, 7),
  (1928694, 3, 6),
  (1934502, 6, 7),
  (1935392, 3, 7),
  (1939584, 3, 2),
  (1940764, 6, 7),
  (1949534, 4, 4),
  (1950955, 3, 2),
  (1951748, 3, 7),
  (1951794, 4, 3),
  (1956242, 3, 2),
  (1957720, 2, 7),
  (1958798, 5, 5),
  (1963945, 2, 3),
  (1968812, 4, 3),
  (1970474, 6, 3),
  (1971145, 5, 6),
  (1972319, 4, 1),
  (1972562, 0, 7),
  (1974560, 2, 3),
  (1975896, 2, 3),
  (1976480, 1, 6),
  (1977746, 2, 3),
  (1978890, 6, 2),
  (1980087, 2, 2),
  (1983081, 3, 3),
  (1984128, 1, 4),
  (1989762, 2, 7),
  (1990814, 1, 4),
  (1992156, 1, 4),
  (1992382, 3, 7),
  (1993736, 0, 0),
  (1998971, 1, 3),
  (2003656, 7, 4),
  (2005044, 0, 0),
  (2006112, 0, 3),
  (2008479, 2, 3),
  (2010786, 7, 4),
  (2012402, 5, 6),
  (2013143, 3, 3),
  (2017372, 3, 2),
  (2020996, 7, 3),
  (2023143, 3, 3),
  (2023326, 0, 7),
  (2029056, 0, 6),
  (2034460, 4, 1),
  (2034811, 0, 0),
  (2039410, 2, 7),
  (2039771, 4, 6),
  (2040279, 4, 7),
  (2041103, 0, 7),
  (2043444, 4, 5),
  (2045566, 4, 7),
  (2048578, 3, 4),
  (2048789, 5, 7),
  (2050205, 0, 0),
  (2054005, 7, 4),
  (2056072, 4, 3),
  (2056115, 6, 7),
  (2056316, 6, 3),
  (2059467, 5, 7),
  (2060641, 1, 2),
  (2062105, 4, 3),
  (2063340, 7, 7),
  (2065949, 0, 7),
  (2067438, 1, 2),
  (2067499, 3, 7),
  (2067845, 1, 0),
  (2072055, 5, 7),
  (2081388, 7, 4),
  (2086360, 1, 7),
  (2087897, 2, 7),
  (2091525, 7, 4),
  (2092771, 5, 7),
  (2093376, 3, 5),
  (2093849, 5, 6),
  (2094365, 7, 1),
  (2094597, 4, 7),
  (2095290, 5, 2),
  (2095880, 1, 3),
  (2096491, 7, 3),
  (2096980, 0, 0),
  (2097002, 5, 5),
  (2100503, 4, 7),
  (2100613, 0, 3),
  (2101439, 4, 7),
  (2102152, 3, 7),
  (2102600, 1, 7),
  (2104401, 5, 7),
  (2107237, 4, 2),
  (2107588, 1, 7),
  (2109540, 3, 7),
  (2109708, 4, 7),
  (2111199, 6, 3),
  (2113385, 2, 7),
  (2113445, 4, 3),
  (2117152, 5, 3),
  (2118428, 2, 3),
  (2119076, 0, 0),
  (2120303, 6, 0),
  (2122806, 0, 0),
  (2127051, 5, 3),
  (2128447, 1, 6),
  (2128892, 5, 7),
  (2131586, 1, 7),
  (2132600, 2, 7),
  (2135596, 3, 3),
  (2135976, 3, 5),
  (2136523, 6, 0),
  (2137182, 7, 6),
  (2137277, 2, 7),
  (2145110, 4, 7),
  (2146065, 0, 4),
  (2149248, 7, 3),
  (2152354, 1, 3),
  (2152514, 7, 7),
  (2152647, 2, 7),
  (2154365, 5, 3),
  (2156249, 4, 2),
  (2160642, 0, 0),
  (2169981, 6, 4),
  (2170009, 1, 3),
  (2173236, 2, 7),
  (2174446, 3, 3),
  (2175391, 6, 7),
  (2175788, 4, 3),
  (2176061, 3, 6),
  (2179783, 7, 0),
  (2181531, 5, 7),
  (2181669, 3, 3),
  (2182625, 7, 0),
  (2186064, 2, 3),
  (2193698, 6, 7),
  (2195174, 7, 0),
  (2195717, 2, 7),
  (2195723, 2, 2),
  (2196284, 2, 3),
  (2200294, 7, 0),
  (2203735, 0, 7),
  (2204002, 3, 3),
  (2205159, 5, 2),
  (2205621, 1, 7),
  (2208613, 6, 7),
  (2209217, 4, 5),
  (2216621, 3, 7),
  (2220284, 5, 7),
  (2221352, 3, 7),
  (2222208, 7, 7),
  (2224693, 2, 2),
  (2227735, 5, 3),
  (2228695, 4, 7),
  (2229162, 5, 7),
  (2232137, 3, 7),
  (2234720, 2, 7),
  (2235212, 6, 0),
  (2236704, 0, 4),
  (2236933, 0, 7),
  (2237329, 4, 2),
  (2237380, 1, 7),
  (2240105, 2, 2),
  (2243225, 6, 7),
  (2245567, 2, 7),
  (2247989, 1, 7),
  (2249651, 1, 0),
  (2250122, 0, 6),
  (2252197, 3, 5),
  (2255406, 3, 6),
  (2256627, 4, 6),
  (2259021, 4, 3),
  (2259121, 5, 6),
  (2261931, 3, 5),
  (2262975, 1, 3),
  (2263496, 7, 6),
  (2264895, 6, 7),
  (2266842, 5, 7),
  (2268728, 3, 7),
  (2271668, 4, 7),
  (2274609, 1, 7),
  (2276142, 4, 7),
  (2277787, 1, 7),
  (2281200, 3, 7),
  (2282262, 3, 5),
  (2282484, 3, 6),
  (2287940, 1, 7),
  (2289086, 6, 7),
  (2289275, 0, 4),
  (2293660, 5, 3),
  (2294160, 4, 4),
  (2295217, 3, 7),
  (2295563, 3, 2),
  (2298982, 4, 7),
  (2302383, 3, 7),
  (2302662, 3, 7),
  (2305445, 6, 0),
  (2305952, 1, 6),
  (2308994, 1, 3),
  (2309141, 5, 4),
  (2314237, 2, 7),
  (2314269, 7, 7),
  (2317291, 1, 3),
  (2317450, 2, 3),
  (2317624, 0, 3),
  (2317939, 3, 6),
  (2318250, 6, 7),
  (2318979, 7, 4),
  (2320224, 2, 5),
  (2321891, 1, 7),
  (2322351, 1, 7),
  (2326528, 6, 0),
  (2328428, 3, 3),
  (2328635, 6, 7),
  (2329970, 0, 3),
  (2334469, 0, 7),
  (2334545, 5, 7),
  (2339760, 3, 2),
  (2343878, 7, 7),
  (2344664, 6, 0),
  (2347632, 4, 2),
  (2348304, 6, 7),
  (2348406, 4, 7),
  (2349928, 3, 6),
  (2350616, 3, 7),
  (2350929, 0, 3),
  (2354999, 6, 7),
  (2360279, 3, 3),
  (2362832, 7, 0),
  (2363351, 4, 5),
  (2364248, 0, 3),
  (2364328, 0, 3),
  (2367716, 3, 2),
  (2370118, 7, 0),
  (2371072, 5, 6),
  (2376959, 6, 3),
  (2378357, 3, 5),
  (2380698, 6, 4),
  (2380926, 0, 7),
  (2382635, 7, 7),
  (2384183, 5, 7),
  (2385363, 4, 6),
  (2389187, 0, 6),
  (2392075, 6, 3),
  (2392716, 3, 5),
  (2392765, 5, 1),
  (2392813, 7, 6),
  (2395942, 5, 3),
  (2396853, 3, 6),
  (2399558, 5, 7),
  (2402689, 7, 7),
  (2402964, 0, 6),
  (2404945, 5, 3),
  (2405223, 1, 6),
  (2405263, 6, 7),
  (2406306, 0, 7),
  (2406758, 0, 7),
  (2409288, 1, 0),
  (2409677, 5, 7),
  (2414385, 4, 7),
  (2420334, 4, 6),
  (2421793, 5, 7),
  (2424209, 1, 3),
  (2424539, 0, 6),
  (2425946, 4, 4),
  (2427102, 2, 3),
  (2429033, 5, 6),
  (2430755, 1, 0),
  (2431437, 4, 3),
  (2434713, 0, 3),
  (2439717, 4, 5),
  (2439996, 7, 4),
  (2443492, 0, 7),
  (2444172, 7, 7),
  (2444379, 0, 4),
  (2444801, 1, 0),
  (2449012, 3, 7),
  (2454064, 7, 7),
  (2454637, 3, 7),
  (2455159, 5, 4),
  (2456865, 5, 7),
  (2460043, 4, 7),
  (2461264, 4, 7),
  (2464762, 7, 0),
  (2464895, 7, 7),
  (2466229, 3, 3),
  (2468653, 4, 7),
  (2476458, 3, 2),
  (2476882, 5, 2),
  (2478819, 4, 2),
  (2480776, 3, 3),
  (2480952, 2, 6),
  (2481074, 0, 7),
  (2482566, 6, 0),
  (2483034, 5, 7),
  (2483594, 0, 7),
  (2488038, 7, 0),
  (2489620, 7, 0),
  (2489862, 3, 3),
  (2490519, 0, 7),
  (2496841, 1, 7),
  (2498986, 3, 7),
  (2499584, 2, 6),
  (2505559, 5, 5),
  (2506346, 2, 3),
  (2506452, 4, 7),
  (2509374, 4, 2),
  (2510239, 5, 7),
  (2511363, 4, 7),
  (2513986, 2, 2),
  (2514983, 3, 2),
  (2515793, 2, 3),
  (2515911, 2, 7),
  (2524791, 6, 7),
  (2527193, 3, 6),
  (2527964, 2, 7),
  (2529177, 2, 7),
  (2529291, 0, 0),
  (2531809, 1, 3),
  (2536059, 3, 3),
  (2536665, 5, 2),
  (2539277, 2, 6),
  (2543560, 0, 4),
  (2544598, 2, 7),
  (2548275, 1, 4),
  (2550009, 5, 5),
  (2553032, 3, 3),
  (2553759, 5, 3),
  (2553816, 3, 2),
  (2557445, 1, 0),
  (2558064, 7, 3),
  (2558511, 5, 2),
  (2559619, 4, 3),
  (2560236, 4, 7),
  (2560731, 3, 5),
  (2561115, 7, 6),
  (2562135, 1, 2),
  (2564311, 1, 4),
  (2566888, 1, 0),
  (2571536, 0, 6),
  (2574462, 1, 7),
  (2574606, 4, 3),
  (2577361, 0, 5),
  (2581154, 3, 7),
  (2581434, 0, 6),
  (2583054, 1, 0),
  (2583363, 6, 7),
  (2588627, 3, 2),
  (2592235, 3, 6),
  (2594147, 3, 6),
  (2594965, 2, 6),
  (2596697, 2, 6),
  (2597626, 5, 6),
  (2598432, 2, 7),
  (2598987, 4, 3),
  (2602689, 1, 7),
  (2602837, 6, 0),
  (2604084, 6, 0),
  (2605136, 4, 7),
  (2606411, 7, 6),
  (2607143, 4, 7),
  (2609792, 5, 3),
  (2612242, 2, 7),
  (2614181, 3, 2),
  (2615071, 1, 6),
  (2615433, 3, 7),
  (2619355, 7, 0),
  (2620548, 4, 5),
  (2621699, 7, 0),
  (2623087, 2, 7),
  (2624064, 6, 4),
  (2624412, 5, 2),
  (2625148, 6, 7),
  (2625512, 3, 3),
  (2625584, 5, 3),
  (2632620, 0, 3),
  (2633737, 1, 7),
  (2634933, 0, 7),
  (2635151, 5, 7),
  (2638100, 6, 0),
  (2646348, 1, 7),
  (2647817, 7, 0),
  (2653108, 0, 7),
  (2658692, 4, 3),
  (2665632, 4, 2),
  (2665721, 7, 4),
  (2673318, 0, 7),
  (2674832, 2, 5),
  (2677147, 5, 7),
  (2678536, 7, 4),
  (2679248, 2, 2),
  (2682892, 0, 3),
  (2685682, 2, 3),
  (2686530, 1, 4),
  (2686553, 5, 7),
  (2690259, 1, 4),
  (2691712, 5, 3),
  (2692141, 7, 3),
  (2692143, 0, 0),
  (2692144, 7, 7),
  (2692243, 3, 7),
  (2692782, 7, 6),
  (2699490, 3, 5),
  (2700658, 7, 4),
  (2700980, 5, 7),
  (2701810, 7, 3),
  (2705419, 6, 6),
  (2706110, 1, 7),
  (2707583, 4, 3),
  (2714853, 3, 2),
  (2716339, 6, 4),
  (2717269, 1, 7),
  (2721850, 5, 7),
  (2723191, 1, 0),
  (2723464, 4, 5),
  (2731254, 3, 7),
  (2737267, 0, 4),
  (2737677, 4, 5),
  (2738060, 6, 7),
  (2741241, 6, 4),
  (2748128, 6, 0),
  (2748673, 6, 0),
  (2749330, 7, 3),
  (2749663, 6, 7),
  (2750330, 1, 3),
  (2751437, 6, 2),
  (2753802, 1, 7),
  (2756269, 7, 3),
  (2757186, 1, 4),
  (2757487, 5, 3),
  (2766481, 0, 7),
  (2767284, 0, 0),
  (2768307, 0, 0),
  (2769344, 1, 0),
  (2769358, 2, 3),
  (2769515, 1, 0),
  (2771469, 7, 0),
  (2772242, 5, 3),
  (2772815, 1, 0),
  (2776788, 5, 3),
  (2784503, 4, 3),
  (2786929, 7, 3),
  (2788023, 6, 3),
  (2809663, 6, 3),
  (2812082, 2, 3),
  (2814399, 0, 7),
  (2818706, 0, 0),
  (2821025, 4, 3),
  (2823449, 0, 6),
  (2829908, 5, 7),
  (2831097, 4, 2),
  (2831773, 0, 0),
  (2834380, 6, 7),
  (2834687, 3, 6),
  (2834938, 4, 0),
  (2835926, 0, 7),
  (2836172, 3, 2),
  (2837297, 0, 0),
  (2838269, 1, 0),
  (2840241, 0, 7),
  (2841507, 4, 5),
  (2841635, 1, 4),
  (2842982, 2, 2),
  (2844241, 6, 7),
  (2845192, 4, 7),
  (2847496, 4, 5),
  (2848583, 4, 7),
  (2849124, 2, 3),
  (2849598, 4, 0),
  (2853016, 4, 6),
  (2853055, 3, 6),
  (2853550, 4, 5),
  (2856221, 5, 7),
  (2856990, 3, 3),
  (2857399, 4, 7),
  (2860595, 1, 0),
  (2865134, 7, 4),
  (2866655, 5, 6),
  (2869678, 3, 7),
  (2869806, 5, 1),
  (2870042, 3, 6),
  (2871746, 1, 3),
  (2875135, 7, 4),
  (2880651, 3, 7),
  (2882623, 4, 6),
  (2883666, 6, 7),
  (2886807, 3, 5),
  (2890609, 3, 3),
  (2893065, 6, 0),
  (2893688, 1, 7),
  (2900137, 7, 7),
  (2900753, 5, 5),
  (2903589, 4, 2),
  (2903986, 3, 7),
  (2904457, 4, 6),
  (2904947, 0, 6),
  (2905626, 7, 0),
  (2907078, 0, 5),
  (2908859, 1, 7),
  (2909754, 4, 6),
  (2914429, 1, 7),
  (2917377, 2, 6),
  (2917511, 5, 7),
  (2918633, 3, 6),
  (2918970, 6, 0),
  (2919633, 4, 3),
  (2919801, 1, 7),
  (2920898, 1, 4),
  (2921247, 4, 7),
  (2922889, 1, 1),
  (2924792, 4, 7),
  (2926292, 5, 7),
  (2927915, 4, 3),
  (2933156, 3, 2),
  (2937144, 2, 3),
  (2938706, 7, 4),
  (2939877, 0, 3),
  (2940877, 1, 7),
  (2940998, 0, 7),
  (2941321, 1, 6),
  (2943427, 0, 7),
  (2944338, 5, 7),
  (2945330, 3, 7),
  (2948591, 5, 7),
  (2950050, 4, 5),
  (2952327, 5, 7),
  (2957312, 7, 4),
  (2958982, 0, 7),
  (2962389, 4, 3),
  (2962947, 0, 2),
  (2965560, 5, 7),
  (2966629, 0, 3),
  (2967703, 5, 7),
  (2970059, 5, 7),
  (2976692, 4, 5),
  (2977817, 7, 7),
  (2980508, 2, 3),
  (2981095, 0, 7),
  (2982306, 0, 7),
  (2982483, 3, 5),
  (2983319, 6, 7),
  (2984889, 5, 5),
  (2985427, 1, 6),
  (2985688, 1, 7),
  (2986392, 3, 2),
  (2987264, 7, 6),
  (2989609, 2, 7),
  (2992187, 2, 7),
  (2992196, 0, 3),
  (2995101, 6, 7),
  (2996986, 0, 7),
  (2997086, 0, 3),
  (3000726, 3, 2),
  (3002643, 0, 3),
  (3004074, 6, 3),
  (3004443, 4, 3),
  (3004548, 2, 2),
  (3004699, 4, 6),
  (3010028, 3, 2),
  (3010124, 7, 4),
  (3012505, 3, 7),
  (3013666, 7, 3),
  (3013907, 5, 0),
  (3019964, 4, 7),
  (3020097, 5, 7),
  (3022156, 7, 4),
  (3025093, 6, 7),
  (3026581, 1, 6),
  (3026958, 0, 7),
  (3027334, 4, 4),
  (3031088, 2, 5),
  (3035536, 1, 0),
  (3038824, 2, 5),
  (3044065, 2, 3),
  (3044684, 1, 0),
  (3047677, 7, 0),
  (3047924, 0, 0),
  (3052627, 7, 7),
  (3057093, 3, 3),
  (3066860, 2, 7),
  (3071522, 0, 4),
  (3073034, 4, 7),
  (3077296, 7, 7),
  (3080500, 5, 7),
  (3081010, 0, 0),
  (3081204, 1, 1),
  (3082340, 2, 7),
  (3083689, 1, 4),
  (3083888, 4, 7),
  (3084846, 7, 7),
  (3085723, 3, 7),
  (3089834, 7, 7),
  (3094535, 4, 6),
  (3095684, 6, 6),
  (3110187, 4, 6),
  (3113617, 5, 7),
  (3114378, 0, 7),
  (3115019, 1, 0),
  (3116235, 6, 0),
  (3117985, 2, 6),
  (3128013, 1, 7),
  (3129274, 5, 7),
  (3130672, 2, 7),
  (3131901, 5, 2),
  (3134844, 4, 2),
  (3135262, 0, 7),
  (3141077, 1, 7),
  (3145066, 7, 3),
  (3146347, 2, 5),
  (3150292, 7, 4),
  (3150829, 2, 7),
  (3152101, 4, 3),
  (3152791, 2, 7),
  (3154666, 6, 0),
  (3159181, 6, 0),
  (3159268, 4, 3),
  (3160745, 7, 7),
  (3164381, 7, 4),
  (3168735, 1, 7),
  (3176569, 1, 3),
  (3177222, 7, 7),
  (3177704, 7, 7),
  (3180152, 5, 7),
  (3182992, 4, 7),
  (3183445, 0, 4),
  (3186202, 4, 7),
  (3188721, 3, 3),
  (3200749, 7, 7),
  (3202037, 7, 7),
  (3206896, 3, 7),
  (3208093, 4, 5),
  (3210738, 5, 7),
  (3210770, 2, 2),
  (3210911, 4, 7),
  (3210946, 1, 0),
  (3220210, 6, 4),
  (3221368, 3, 3),
  (3222877, 0, 7),
  (3223119, 5, 6),
  (3223885, 7, 0),
  (3225621, 0, 0),
  (3225976, 6, 4),
  (3229828, 4, 7),
  (3231106, 6, 4),
  (3235049, 2, 7),
  (3236798, 2, 7),
  (3239200, 0, 7),
  (3239650, 3, 2),
  (3242720, 4, 7),
  (3244553, 0, 4),
  (3245732, 2, 7),
  (3246611, 2, 3),
  (3247447, 1, 0),
  (3248608, 1, 0),
  (3249942, 5, 7),
  (3250899, 2, 7),
  (3252202, 4, 3),
  (3254536, 6, 7),
  (3257759, 4, 7),
  (3261975, 7, 0),
  (3262030, 0, 4),
  (3262541, 7, 4),
  (3264476, 3, 2),
  (3264834, 1, 0),
  (3267540, 3, 3),
  (3273162, 0, 4),
  (3274132, 1, 4),
  (3276114, 2, 2),
  (3278357, 4, 7),
  (3278847, 2, 6),
  (3285480, 5, 5),
  (3285864, 6, 7),
  (3287922, 3, 7),
  (3290301, 1, 7),
  (3290864, 6, 7),
  (3293305, 6, 7),
  (3296385, 7, 0),
  (3302781, 0, 7),
  (3302846, 7, 0),
  (3309031, 6, 7),
  (3309489, 6, 4),
  (3310176, 6, 7),
  (3314659, 2, 7),
  (3314722, 4, 3),
  (3319928, 5, 6),
  (3321927, 5, 3),
  (3324889, 4, 6),
  (3326393, 6, 3),
  (3326618, 1, 4),
  (3327695, 4, 7),
  (3330601, 1, 7),
  (3332814, 3, 7),
  (3338729, 0, 4),
  (3340540, 7, 7),
  (3342849, 4, 7),
  (3343818, 4, 7),
  (3346565, 7, 3),
  (3347676, 3, 7),
  (3347951, 4, 6),
  (3350139, 1, 7),
  (3350911, 4, 7),
  (3354186, 3, 7),
  (3355560, 0, 7),
  (3359493, 3, 7),
  (3360317, 1, 7),
  (3362756, 2, 2),
  (3364686, 0, 0),
  (3366367, 6, 3),
  (3367933, 5, 3),
  (3368280, 6, 7),
  (3369993, 0, 6),
  (3372164, 3, 2),
  (3373137, 6, 7),
  (3375088, 2, 4),
  (3375335, 7, 7),
  (3377956, 2, 7),
  (3379140, 7, 0),
  (3382880, 1, 0),
  (3386548, 3, 7),
  (3389068, 5, 7),
  (3392380, 5, 7),
  (3392921, 4, 6),
  (3393114, 4, 7),
  (3400657, 0, 7),
  (3403167, 4, 7),
  (3403363, 4, 2),
  (3407092, 2, 7),
  (3409148, 0, 7),
  (3410681, 1, 5),
  (3417681, 6, 7),
  (3419268, 1, 3),
  (3420215, 2, 3),
  (3420487, 5, 7),
  (3421125, 7, 0),
  (3423871, 7, 6),
  (3427169, 4, 2),
  (3433495, 3, 2),
  (3436791, 2, 7),
  (3438015, 7, 7),
  (3438584, 4, 7),
  (3439783, 2, 3),
  (3440178, 7, 0),
  (3444307, 6, 6),
  (3445593, 1, 4),
  (3446518, 1, 0),
  (3449762, 3, 7),
  (3454063, 3, 1),
  (3455217, 5, 3),
  (3457208, 1, 3),
  (3460935, 6, 4),
  (3461550, 0, 0),
  (3462899, 2, 4),
  (3465467, 3, 3),
  (3466184, 6, 3),
  (3467256, 4, 2),
  (3467557, 3, 7),
  (3468403, 5, 5),
  (3470528, 5, 7),
  (3471660, 1, 6),
  (3474983, 4, 5),
  (3476736, 6, 7),
  (3477126, 5, 6),
  (3481126, 1, 3),
  (3484222, 6, 7),
  (3485909, 4, 7),
  (3493251, 1, 0),
  (3493576, 4, 7),
  (3497794, 0, 7),
  (3498036, 6, 0),
  (3502846, 0, 7),
  (3504994, 5, 7),
  (3507858, 4, 7),
  (3511799, 5, 7),
  (3513851, 6, 0),
  (3515436, 5, 2),
  (3518220, 3, 7),
  (3520454, 7, 0),
  (3525913, 3, 5),
  (3526742, 1, 4),
  (3527869, 6, 7),
  (3529436, 3, 7),
  (3531417, 4, 4),
  (3533279, 4, 3),
  (3534095, 7, 7),
  (3535320, 7, 7),
  (3541399, 3, 7),
  (3541402, 0, 3),
  (3552775, 5, 7),
  (3553772, 3, 6),
  (3554758, 6, 7),
  (3555202, 7, 7),
  (3555687, 2, 6),
  (3555879, 5, 3),
  (3557383, 2, 7),
  (3558405, 5, 7),
  (3559390, 2, 3),
  (3559552, 5, 3),
  (3561903, 3, 7),
  (3563791, 6, 7),
  (3564247, 2, 5),
  (3565457, 4, 7),
  (3571228, 4, 7),
  (3571765, 3, 7),
  (3571774, 0, 3),
  (3572078, 7, 4),
  (3572782, 5, 7),
  (3574059, 7, 6),
  (3574077, 1, 7),
  (3574701, 5, 3),
  (3575278, 6, 7),
  (3576115, 6, 6),
  (3579042, 1, 7),
  (3579414, 5, 7),
  (3580814, 0, 7),
  (3581448, 0, 7),
  (3583127, 3, 7),
  (3584098, 1, 0),
  (3586035, 3, 3),
  (3586794, 6, 0),
  (3588304, 3, 7),
  (3593666, 3, 7),
  (3597766, 0, 7),
  (3598571, 3, 5),
])