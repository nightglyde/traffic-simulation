from util import *
schedule = deque([
  (89, 7, 5),
  (693, 3, 2),
  (1039, 5, 1),
  (1504, 1, 0),
  (2041, 1, 3),
  (3123, 3, 2),
  (5681, 3, 2),
  (5902, 4, 4),
  (6620, 7, 3),
  (10474, 3, 7),
  (11834, 5, 3),
  (13663, 7, 0),
  (15903, 0, 0),
  (16621, 3, 0),
  (20710, 5, 6),
  (21381, 3, 2),
  (25090, 0, 0),
  (26689, 1, 6),
  (28671, 4, 2),
  (31009, 1, 7),
  (32376, 5, 6),
  (32440, 0, 0),
  (33522, 4, 3),
  (33573, 6, 2),
  (33672, 6, 1),
  (35061, 6, 3),
  (36648, 1, 0),
  (37540, 0, 3),
  (38381, 1, 0),
  (42163, 4, 3),
  (48442, 1, 7),
  (49585, 7, 1),
  (49783, 2, 3),
  (52623, 6, 7),
  (53140, 4, 2),
  (55441, 6, 1),
  (56047, 2, 3),
  (62072, 7, 0),
  (63249, 4, 2),
  (64010, 3, 3),
  (71018, 1, 0),
  (76557, 4, 2),
  (78642, 5, 4),
  (79053, 1, 7),
  (79111, 1, 0),
  (80988, 6, 0),
  (82169, 5, 3),
  (83230, 7, 5),
  (83276, 6, 3),
  (83630, 3, 7),
  (85424, 5, 2),
  (87919, 4, 6),
  (88196, 6, 3),
  (91321, 3, 5),
  (93624, 0, 4),
  (94357, 6, 7),
  (94942, 5, 2),
  (99496, 1, 4),
  (99841, 7, 7),
  (100348, 7, 0),
  (101984, 0, 0),
  (103608, 3, 3),
  (105138, 2, 7),
  (111212, 6, 0),
  (111594, 7, 0),
  (115779, 6, 0),
  (118252, 3, 3),
  (118290, 4, 2),
  (122980, 6, 3),
  (129368, 1, 1),
  (129509, 5, 3),
  (129560, 6, 6),
  (131760, 6, 3),
  (132241, 1, 1),
  (133023, 5, 4),
  (136384, 0, 3),
  (136588, 3, 2),
  (137837, 1, 0),
  (139021, 2, 3),
  (139190, 2, 7),
  (140622, 5, 2),
  (141091, 5, 7),
  (145726, 7, 0),
  (146079, 4, 3),
  (146826, 0, 5),
  (154068, 5, 7),
  (155688, 1, 0),
  (156160, 1, 0),
  (161992, 2, 3),
  (163106, 4, 3),
  (163501, 3, 1),
  (163690, 1, 7),
  (164318, 5, 3),
  (165096, 4, 3),
  (165868, 6, 0),
  (166796, 6, 0),
  (166935, 6, 0),
  (169496, 7, 3),
  (174524, 7, 7),
  (176483, 7, 7),
  (179603, 4, 3),
  (184841, 3, 6),
  (184935, 4, 3),
  (187488, 1, 0),
  (188489, 7, 6),
  (188627, 0, 0),
  (197169, 0, 6),
  (197459, 2, 6),
  (197536, 3, 7),
  (199710, 6, 4),
  (201085, 0, 0),
  (202054, 0, 0),
  (202645, 1, 7),
  (206652, 6, 2),
  (208736, 3, 3),
  (212250, 1, 0),
  (216661, 5, 3),
  (224119, 2, 7),
  (227932, 6, 7),
  (231507, 7, 0),
  (235618, 3, 3),
  (236471, 3, 7),
  (238345, 2, 3),
  (238456, 5, 6),
  (238944, 2, 7),
  (242889, 7, 3),
  (243543, 2, 3),
  (246422, 7, 2),
  (250467, 6, 0),
  (252303, 0, 6),
  (254694, 0, 7),
  (256734, 4, 1),
  (258680, 0, 2),
  (258936, 2, 3),
  (258975, 5, 3),
  (262848, 0, 0),
  (262973, 7, 3),
  (263444, 2, 3),
  (263619, 7, 3),
  (263810, 5, 7),
  (264114, 1, 0),
  (264532, 2, 3),
  (266372, 0, 0),
  (267195, 6, 0),
  (269318, 7, 3),
  (273968, 1, 0),
  (275045, 5, 6),
  (276867, 4, 1),
  (280552, 5, 3),
  (281964, 7, 3),
  (283122, 6, 0),
  (286845, 3, 3),
  (290382, 7, 0),
  (292233, 2, 1),
  (292366, 3, 3),
  (295251, 5, 3),
  (296072, 3, 7),
  (297269, 4, 4),
  (298897, 4, 0),
  (299832, 7, 6),
  (300738, 3, 2),
  (301474, 4, 1),
  (303269, 5, 3),
  (303421, 5, 6),
  (305266, 3, 0),
  (306437, 3, 0),
  (312780, 3, 3),
  (312888, 3, 7),
  (312988, 5, 3),
  (316625, 1, 2),
  (319915, 2, 3),
  (322422, 2, 6),
  (322830, 3, 3),
  (324707, 4, 0),
  (325704, 3, 2),
  (330490, 0, 0),
  (331284, 1, 0),
  (334644, 6, 3),
  (337078, 4, 2),
  (338869, 4, 3),
  (339782, 4, 6),
  (339878, 0, 6),
  (340154, 6, 3),
  (341084, 4, 3),
  (342288, 3, 3),
  (342512, 2, 2),
  (343908, 7, 2),
  (344096, 6, 0),
  (350530, 0, 3),
  (351408, 3, 3),
  (354673, 3, 3),
  (357257, 3, 3),
  (358700, 7, 0),
  (362365, 0, 3),
  (365841, 5, 3),
  (366983, 6, 0),
  (367060, 4, 3),
  (367484, 6, 4),
  (369355, 2, 4),
  (370609, 7, 0),
  (373012, 5, 6),
  (373419, 0, 0),
  (375789, 3, 4),
  (377260, 7, 0),
  (378601, 7, 7),
  (380055, 7, 0),
  (384802, 5, 7),
  (386076, 0, 3),
  (386550, 7, 0),
  (388511, 4, 5),
  (390259, 0, 0),
  (394611, 7, 0),
  (397738, 5, 5),
  (399006, 7, 0),
  (400118, 7, 3),
  (400614, 7, 0),
  (401339, 1, 7),
  (406032, 7, 4),
  (406387, 5, 7),
  (406771, 4, 3),
  (408594, 6, 4),
  (410781, 2, 5),
  (412062, 1, 0),
  (419831, 3, 2),
  (420733, 2, 3),
  (420903, 5, 1),
  (421910, 4, 7),
  (423152, 6, 5),
  (423197, 2, 3),
  (423753, 5, 3),
  (426705, 1, 2),
  (427254, 2, 7),
  (428028, 4, 6),
  (428367, 4, 6),
  (429736, 3, 2),
  (430720, 0, 0),
  (432409, 3, 1),
  (433370, 2, 0),
  (433768, 2, 7),
  (435208, 0, 0),
  (436870, 2, 3),
  (441680, 7, 0),
  (441758, 1, 0),
  (442166, 6, 5),
  (443067, 7, 4),
  (444212, 6, 0),
  (445184, 2, 3),
  (445339, 2, 6),
  (446018, 2, 0),
  (446580, 6, 2),
  (451661, 0, 0),
  (452485, 1, 0),
  (455694, 3, 0),
  (457212, 1, 0),
  (457635, 4, 3),
  (457714, 4, 2),
  (463313, 6, 6),
  (464901, 5, 3),
  (466490, 4, 7),
  (476742, 0, 0),
  (478369, 3, 3),
  (479372, 6, 2),
  (479710, 1, 0),
  (481443, 3, 2),
  (489150, 5, 7),
  (489487, 1, 0),
  (489746, 5, 3),
  (491290, 7, 0),
  (492610, 7, 7),
  (496811, 5, 3),
  (497015, 1, 0),
  (498645, 5, 6),
  (500131, 3, 3),
  (501574, 1, 0),
  (505556, 0, 0),
  (508309, 6, 0),
  (510381, 6, 2),
  (510459, 0, 3),
  (510845, 7, 0),
  (515196, 7, 0),
  (515693, 0, 0),
  (518875, 5, 2),
  (521011, 7, 0),
  (525671, 3, 3),
  (527217, 3, 0),
  (527344, 4, 3),
  (529524, 2, 7),
  (530204, 1, 0),
  (532353, 7, 4),
  (536318, 4, 3),
  (537060, 1, 7),
  (544564, 5, 7),
  (548153, 1, 0),
  (549994, 4, 3),
  (550739, 6, 7),
  (551086, 3, 6),
  (551101, 5, 5),
  (551540, 0, 0),
  (551681, 2, 7),
  (552317, 2, 6),
  (553283, 6, 7),
  (553831, 0, 7),
  (554846, 4, 6),
  (556776, 6, 0),
  (559254, 4, 5),
  (562306, 1, 4),
  (562347, 4, 3),
  (568037, 7, 0),
  (568294, 3, 4),
  (568389, 4, 7),
  (568722, 3, 1),
  (569074, 2, 3),
  (569877, 7, 3),
  (572264, 6, 0),
  (572520, 1, 7),
  (573991, 1, 0),
  (575369, 7, 5),
  (578942, 3, 4),
  (580202, 4, 0),
  (581641, 7, 0),
  (581681, 6, 6),
  (582618, 3, 2),
  (584469, 6, 0),
  (587234, 1, 3),
  (589189, 3, 3),
  (589639, 6, 0),
  (592269, 5, 3),
  (594889, 1, 5),
  (595659, 5, 7),
  (596552, 6, 0),
  (597712, 5, 6),
  (599630, 2, 3),
  (601913, 7, 5),
  (610859, 2, 6),
  (613740, 3, 2),
  (617704, 7, 4),
  (617710, 7, 0),
  (619410, 4, 7),
  (621871, 5, 7),
  (623979, 7, 0),
  (627878, 4, 4),
  (629732, 3, 0),
  (633786, 7, 0),
  (636957, 3, 6),
  (639465, 5, 7),
  (639698, 1, 3),
  (642834, 7, 0),
  (643141, 4, 6),
  (648796, 7, 0),
  (649197, 3, 7),
  (649692, 3, 2),
  (650054, 4, 2),
  (651905, 0, 4),
  (655900, 7, 3),
  (656371, 5, 3),
  (658607, 6, 6),
  (659257, 7, 3),
  (661273, 6, 3),
  (662396, 5, 5),
  (663034, 6, 0),
  (669575, 7, 2),
  (671130, 6, 0),
  (671968, 7, 4),
  (672211, 2, 3),
  (674138, 1, 0),
  (677533, 7, 0),
  (678230, 2, 3),
  (678972, 7, 0),
  (680065, 4, 3),
  (683151, 2, 3),
  (689561, 7, 4),
  (690599, 2, 7),
  (691499, 0, 0),
  (694228, 7, 4),
  (696830, 6, 0),
  (699058, 7, 3),
  (700502, 0, 6),
  (700893, 5, 3),
  (705689, 0, 0),
  (706750, 1, 0),
  (707736, 1, 7),
  (708687, 5, 0),
  (709329, 1, 0),
  (710290, 2, 3),
  (715667, 5, 2),
  (717504, 1, 0),
  (722982, 4, 3),
  (726776, 1, 0),
  (728162, 3, 0),
  (728343, 6, 0),
  (728532, 5, 4),
  (730032, 1, 0),
  (732183, 2, 2),
  (733425, 6, 3),
  (735224, 7, 0),
  (735358, 2, 4),
  (737282, 4, 3),
  (740244, 2, 2),
  (743348, 4, 2),
  (746299, 2, 3),
  (753670, 5, 3),
  (755702, 4, 3),
  (758346, 6, 0),
  (758692, 7, 7),
  (761189, 0, 0),
  (763009, 1, 3),
  (766262, 7, 4),
  (767226, 7, 2),
  (770767, 6, 0),
  (770895, 1, 0),
  (770934, 1, 3),
  (774354, 4, 3),
  (779532, 6, 2),
  (783988, 1, 7),
  (784303, 0, 0),
  (785842, 4, 3),
  (787557, 6, 7),
  (787629, 3, 3),
  (788185, 4, 3),
  (790575, 1, 2),
  (791955, 4, 3),
  (792732, 0, 0),
  (799191, 1, 6),
  (803409, 7, 4),
  (804917, 5, 7),
  (806027, 4, 3),
  (808610, 7, 5),
  (813498, 0, 7),
  (815440, 5, 3),
  (819602, 6, 2),
  (821902, 3, 7),
  (821906, 5, 3),
  (822568, 2, 0),
  (823996, 4, 2),
  (826163, 2, 6),
  (827313, 2, 3),
  (828240, 1, 4),
  (829208, 2, 2),
  (829902, 2, 3),
  (830407, 4, 3),
  (831413, 6, 4),
  (831522, 4, 3),
  (832394, 2, 7),
  (836969, 5, 2),
  (838915, 0, 2),
  (842132, 7, 7),
  (846403, 0, 7),
  (850105, 1, 0),
  (855681, 6, 0),
  (857423, 7, 5),
  (857775, 0, 0),
  (860368, 7, 1),
  (862133, 2, 6),
  (866324, 1, 7),
  (869696, 0, 0),
  (872845, 1, 7),
  (874348, 0, 3),
  (876428, 2, 7),
  (876848, 3, 3),
  (880370, 4, 0),
  (880427, 7, 1),
  (881016, 7, 6),
  (886831, 4, 2),
  (888423, 6, 3),
  (890035, 2, 3),
  (893246, 0, 6),
  (893519, 3, 2),
  (893830, 4, 6),
  (898937, 4, 4),
  (899457, 6, 0),
  (901674, 0, 0),
  (905606, 3, 7),
  (906505, 7, 4),
  (909272, 5, 3),
  (912885, 7, 4),
  (916932, 2, 5),
  (918893, 0, 4),
  (919069, 4, 3),
  (921230, 7, 0),
  (922133, 2, 2),
  (926095, 5, 6),
  (928008, 0, 0),
  (928818, 6, 3),
  (928948, 7, 7),
  (930963, 7, 5),
  (934871, 7, 3),
  (938401, 5, 3),
  (938623, 4, 6),
  (940128, 3, 7),
  (940875, 3, 6),
  (942568, 0, 4),
  (946564, 3, 0),
  (946932, 5, 3),
  (949381, 4, 7),
  (949746, 6, 7),
  (950394, 7, 7),
  (953202, 2, 3),
  (962238, 6, 2),
  (965573, 3, 3),
  (968663, 0, 6),
  (968705, 2, 3),
  (969675, 3, 7),
  (970139, 5, 3),
  (971780, 2, 3),
  (973599, 1, 3),
  (973654, 3, 6),
  (976633, 5, 6),
  (978064, 6, 1),
  (978634, 4, 3),
  (979746, 2, 0),
  (980068, 5, 2),
  (980256, 7, 0),
  (982122, 7, 0),
  (986328, 4, 3),
  (986788, 7, 0),
  (992450, 0, 0),
  (993217, 1, 4),
  (994715, 1, 0),
  (995037, 5, 1),
  (995930, 2, 3),
  (1000639, 5, 7),
  (1002565, 4, 7),
  (1003689, 5, 7),
  (1004043, 6, 0),
  (1004502, 0, 3),
  (1005010, 1, 7),
  (1007623, 0, 7),
  (1009379, 5, 1),
  (1012962, 3, 3),
  (1015531, 2, 3),
  (1016830, 0, 0),
  (1017403, 4, 6),
  (1018056, 5, 3),
  (1019210, 6, 1),
  (1035169, 0, 6),
  (1038646, 0, 0),
  (1039682, 4, 6),
  (1042670, 6, 0),
  (1043544, 3, 6),
  (1046973, 7, 2),
  (1047704, 0, 7),
  (1052428, 6, 5),
  (1056304, 5, 3),
  (1058687, 6, 0),
  (1062488, 4, 1),
  (1066001, 6, 5),
  (1067074, 0, 0),
  (1071058, 1, 0),
  (1073671, 4, 3),
  (1075181, 6, 7),
  (1076335, 7, 0),
  (1077159, 3, 7),
  (1079020, 2, 2),
  (1081185, 1, 0),
  (1082651, 0, 0),
  (1085698, 6, 0),
  (1086389, 4, 3),
  (1087797, 6, 0),
  (1088978, 3, 2),
  (1092041, 4, 3),
  (1092578, 2, 1),
  (1097393, 0, 7),
  (1103709, 5, 3),
  (1108686, 5, 7),
  (1109584, 5, 7),
  (1111660, 2, 2),
  (1111749, 1, 0),
  (1112177, 7, 4),
  (1112689, 3, 2),
  (1112731, 3, 6),
  (1113556, 3, 7),
  (1117100, 5, 7),
  (1119584, 4, 1),
  (1129232, 7, 1),
  (1129352, 4, 3),
  (1133054, 5, 3),
  (1136606, 1, 1),
  (1141939, 2, 0),
  (1142165, 6, 0),
  (1149331, 0, 0),
  (1152026, 3, 3),
  (1152652, 7, 1),
  (1155095, 2, 3),
  (1155726, 2, 7),
  (1156471, 1, 0),
  (1157391, 6, 1),
  (1162220, 1, 0),
  (1163500, 0, 6),
  (1164755, 5, 0),
  (1167186, 6, 0),
  (1168648, 4, 2),
  (1175299, 1, 7),
  (1181828, 7, 0),
  (1182861, 5, 1),
  (1183203, 4, 3),
  (1187497, 5, 6),
  (1188016, 1, 1),
  (1194170, 2, 2),
  (1194405, 3, 7),
  (1195360, 4, 3),
  (1195584, 0, 3),
  (1198281, 5, 3),
  (1199497, 4, 3),
  (1200405, 6, 1),
  (1207104, 1, 0),
  (1207348, 3, 2),
  (1207757, 3, 2),
  (1207882, 6, 7),
  (1208398, 4, 7),
  (1210393, 6, 0),
  (1213164, 4, 7),
  (1214640, 4, 3),
  (1217999, 2, 3),
  (1219564, 2, 6),
  (1221471, 4, 3),
  (1224532, 6, 4),
  (1227197, 7, 4),
  (1230466, 1, 3),
  (1231031, 6, 6),
  (1234086, 6, 4),
  (1234902, 4, 3),
  (1237041, 5, 2),
  (1237096, 4, 7),
  (1239160, 4, 3),
  (1248629, 7, 7),
  (1248869, 2, 6),
  (1249462, 1, 0),
  (1249922, 6, 7),
  (1252834, 5, 2),
  (1258741, 4, 6),
  (1267992, 1, 4),
  (1270403, 1, 0),
  (1271539, 2, 3),
  (1278765, 4, 3),
  (1279062, 1, 4),
  (1281080, 4, 5),
  (1281127, 3, 3),
  (1287377, 7, 3),
  (1287983, 7, 5),
  (1287984, 3, 2),
  (1289739, 3, 3),
  (1293147, 5, 6),
  (1294030, 5, 6),
  (1296712, 5, 3),
  (1299752, 0, 4),
  (1301608, 5, 3),
  (1302382, 5, 3),
  (1303253, 7, 0),
  (1303425, 6, 0),
  (1303737, 2, 3),
  (1309687, 2, 0),
  (1309710, 3, 7),
  (1313560, 1, 0),
  (1313977, 5, 3),
  (1314112, 3, 3),
  (1315713, 3, 3),
  (1318910, 7, 6),
  (1319339, 1, 4),
  (1323863, 4, 7),
  (1329647, 6, 0),
  (1330512, 5, 6),
  (1332981, 7, 3),
  (1333900, 6, 3),
  (1335839, 2, 3),
  (1344163, 1, 0),
  (1345150, 6, 0),
  (1347732, 0, 4),
  (1359510, 1, 2),
  (1360082, 7, 0),
  (1360151, 0, 6),
  (1360932, 0, 3),
  (1368599, 2, 3),
  (1369486, 4, 6),
  (1373215, 7, 0),
  (1377252, 7, 0),
  (1380920, 5, 4),
  (1384314, 2, 2),
  (1386289, 1, 2),
  (1386991, 5, 3),
  (1390676, 3, 1),
  (1390859, 7, 7),
  (1394527, 0, 0),
  (1395345, 2, 3),
  (1395874, 3, 5),
  (1396336, 1, 1),
  (1396463, 1, 4),
  (1400611, 0, 4),
  (1400952, 2, 7),
  (1403129, 0, 0),
  (1408341, 3, 1),
  (1408805, 3, 3),
  (1410783, 4, 4),
  (1412337, 6, 3),
  (1415662, 5, 3),
  (1419797, 2, 7),
  (1424676, 3, 3),
  (1428492, 1, 0),
  (1428783, 4, 0),
  (1435267, 5, 5),
  (1437168, 4, 3),
  (1437561, 6, 1),
  (1439925, 1, 7),
  (1441349, 5, 3),
  (1450173, 6, 0),
  (1454607, 7, 6),
  (1454674, 1, 0),
  (1458707, 6, 0),
  (1459500, 4, 2),
  (1460541, 5, 3),
  (1461736, 5, 6),
  (1467306, 7, 0),
  (1476259, 0, 2),
  (1479103, 5, 3),
  (1481012, 1, 3),
  (1481901, 0, 0),
  (1486863, 2, 1),
  (1495268, 0, 4),
  (1497213, 5, 2),
  (1500458, 0, 7),
  (1501297, 4, 3),
  (1501432, 2, 3),
  (1502045, 1, 0),
  (1502871, 0, 5),
  (1503168, 5, 7),
  (1506121, 4, 6),
  (1506372, 1, 3),
  (1508915, 4, 1),
  (1509357, 3, 6),
  (1511186, 1, 0),
  (1511204, 4, 3),
  (1511403, 2, 3),
  (1511657, 6, 0),
  (1513260, 0, 1),
  (1519885, 3, 4),
  (1521826, 7, 0),
  (1522035, 2, 6),
  (1523381, 3, 2),
  (1525351, 0, 7),
  (1525651, 6, 0),
  (1528887, 1, 7),
  (1530115, 7, 0),
  (1531064, 2, 6),
  (1532183, 1, 0),
  (1535769, 7, 0),
  (1536180, 3, 3),
  (1536984, 5, 2),
  (1538137, 4, 3),
  (1542383, 5, 0),
  (1542554, 1, 0),
  (1543010, 7, 0),
  (1543457, 6, 3),
  (1548015, 0, 0),
  (1549875, 5, 6),
  (1563386, 7, 0),
  (1565137, 5, 3),
  (1570508, 2, 2),
  (1574166, 2, 7),
  (1574202, 4, 7),
  (1577698, 7, 0),
  (1578091, 1, 0),
  (1583178, 7, 2),
  (1586716, 1, 5),
  (1587945, 1, 7),
  (1588386, 3, 7),
  (1595136, 7, 4),
  (1596705, 6, 4),
  (1597502, 0, 0),
  (1604967, 7, 7),
  (1605703, 1, 3),
  (1607750, 5, 3),
  (1608433, 0, 0),
  (1611705, 3, 2),
  (1614234, 2, 1),
  (1616318, 5, 3),
  (1618897, 6, 0),
  (1620823, 6, 6),
  (1622348, 6, 5),
  (1624995, 7, 0),
  (1634484, 6, 7),
  (1641416, 2, 3),
  (1642456, 3, 7),
  (1646122, 3, 6),
  (1646295, 4, 2),
  (1646792, 6, 3),
  (1647333, 5, 6),
  (1647519, 5, 3),
  (1651334, 3, 3),
  (1652189, 5, 3),
  (1653030, 7, 2),
  (1653419, 0, 0),
  (1658785, 2, 2),
  (1662531, 2, 2),
  (1665289, 6, 0),
  (1672392, 7, 4),
  (1673320, 5, 3),
  (1673605, 2, 3),
  (1677287, 7, 0),
  (1680271, 7, 6),
  (1681766, 6, 0),
  (1687562, 3, 3),
  (1688182, 4, 1),
  (1689145, 5, 3),
  (1689315, 7, 3),
  (1691049, 7, 5),
  (1692767, 3, 3),
  (1692871, 6, 1),
  (1693062, 2, 2),
  (1694164, 5, 3),
  (1700537, 1, 0),
  (1700847, 1, 2),
  (1701583, 2, 3),
  (1705993, 0, 0),
  (1706932, 1, 0),
  (1711531, 6, 0),
  (1712416, 2, 2),
  (1712580, 2, 6),
  (1712971, 7, 3),
  (1719678, 2, 3),
  (1719775, 7, 6),
  (1722219, 5, 4),
  (1722344, 4, 2),
  (1722486, 3, 3),
  (1722866, 7, 5),
  (1723976, 2, 1),
  (1724162, 1, 0),
  (1731680, 6, 7),
  (1731691, 3, 3),
  (1735960, 6, 4),
  (1736239, 4, 7),
  (1737090, 0, 0),
  (1737133, 6, 7),
  (1738071, 0, 3),
  (1738273, 5, 3),
  (1742883, 2, 2),
  (1746308, 5, 3),
  (1750954, 7, 7),
  (1755876, 3, 5),
  (1756385, 7, 0),
  (1756862, 0, 0),
  (1758213, 0, 5),
  (1759000, 0, 0),
  (1759246, 6, 4),
  (1759253, 4, 4),
  (1761104, 1, 1),
  (1761721, 2, 3),
  (1767496, 4, 2),
  (1770272, 3, 3),
  (1772947, 5, 6),
  (1773708, 2, 3),
  (1774260, 6, 0),
  (1778002, 3, 7),
  (1783499, 6, 4),
  (1785552, 4, 3),
  (1786063, 1, 3),
  (1791444, 3, 0),
  (1792745, 3, 4),
  (1795361, 2, 7),
  (1795602, 1, 0),
  (1798769, 2, 0),
  (1799099, 3, 7),
  (1803319, 5, 4),
  (1803907, 2, 6),
  (1804329, 7, 0),
  (1805540, 6, 3),
  (1806192, 4, 4),
  (1806876, 7, 0),
  (1808120, 0, 7),
  (1811174, 3, 3),
  (1813334, 1, 5),
  (1814030, 7, 0),
  (1815059, 0, 5),
  (1818412, 7, 3),
  (1818519, 3, 5),
  (1819727, 6, 2),
  (1819963, 4, 2),
  (1820275, 5, 6),
  (1820613, 2, 3),
  (1822356, 4, 7),
  (1822421, 4, 0),
  (1826374, 0, 0),
  (1828363, 6, 0),
  (1831493, 1, 0),
  (1831865, 2, 5),
  (1832080, 1, 5),
  (1833235, 5, 3),
  (1834703, 7, 7),
  (1834973, 0, 7),
  (1836398, 7, 6),
  (1838336, 7, 0),
  (1839122, 2, 3),
  (1841627, 7, 4),
  (1841942, 4, 3),
  (1842278, 6, 4),
  (1842708, 7, 0),
  (1843237, 1, 7),
  (1843537, 7, 6),
  (1843638, 5, 3),
  (1844074, 0, 0),
  (1845156, 4, 2),
  (1850148, 4, 4),
  (1858946, 6, 0),
  (1863407, 4, 6),
  (1866631, 0, 0),
  (1870467, 2, 3),
  (1872427, 5, 5),
  (1884769, 6, 3),
  (1886819, 4, 3),
  (1887817, 5, 4),
  (1889077, 3, 3),
  (1889616, 2, 3),
  (1893794, 6, 3),
  (1894118, 7, 7),
  (1897059, 2, 6),
  (1897122, 5, 0),
  (1897547, 3, 3),
  (1900152, 6, 4),
  (1901655, 6, 0),
  (1902403, 2, 6),
  (1903806, 3, 3),
  (1905232, 0, 3),
  (1905750, 7, 0),
  (1907007, 6, 0),
  (1908491, 5, 7),
  (1909365, 5, 7),
  (1912238, 2, 5),
  (1913503, 6, 0),
  (1913907, 0, 0),
  (1915598, 1, 0),
  (1916153, 0, 0),
  (1917577, 0, 0),
  (1919269, 3, 6),
  (1925238, 7, 0),
  (1929088, 4, 3),
  (1930206, 5, 2),
  (1931124, 5, 2),
  (1932969, 2, 3),
  (1938008, 3, 6),
  (1938164, 3, 0),
  (1939005, 1, 0),
  (1945637, 1, 0),
  (1946389, 3, 0),
  (1946639, 0, 6),
  (1950053, 1, 7),
  (1953356, 2, 7),
  (1961924, 2, 3),
  (1969231, 0, 4),
  (1971483, 3, 3),
  (1971713, 2, 2),
  (1972380, 7, 3),
  (1973150, 1, 6),
  (1976763, 3, 3),
  (1977789, 2, 6),
  (1977895, 3, 3),
  (1978068, 3, 6),
  (1978257, 0, 0),
  (1979645, 7, 7),
  (1981203, 4, 1),
  (1984944, 5, 3),
  (1985331, 2, 4),
  (1994089, 7, 1),
  (1994125, 4, 3),
  (1995323, 0, 3),
  (1996021, 5, 2),
  (1996465, 1, 4),
  (2002579, 6, 3),
  (2002799, 3, 3),
  (2004056, 3, 3),
  (2005217, 0, 0),
  (2007601, 6, 1),
  (2016425, 4, 3),
  (2017889, 6, 3),
  (2019263, 3, 3),
  (2020093, 3, 6),
  (2021338, 4, 3),
  (2025781, 7, 0),
  (2028417, 1, 4),
  (2028680, 7, 7),
  (2031217, 3, 7),
  (2032094, 1, 7),
  (2033111, 2, 2),
  (2033843, 7, 0),
  (2037204, 4, 2),
  (2040013, 6, 3),
  (2040393, 7, 0),
  (2041706, 7, 2),
  (2042547, 4, 6),
  (2046110, 5, 2),
  (2046715, 7, 3),
  (2050024, 5, 3),
  (2051310, 4, 3),
  (2051994, 7, 3),
  (2053942, 6, 0),
  (2054856, 1, 0),
  (2055073, 7, 0),
  (2055396, 0, 0),
  (2061341, 5, 4),
  (2062797, 2, 6),
  (2063791, 1, 3),
  (2064547, 5, 3),
  (2065032, 4, 3),
  (2065213, 7, 7),
  (2073299, 7, 1),
  (2073483, 5, 7),
  (2075886, 0, 0),
  (2076419, 0, 5),
  (2077682, 7, 1),
  (2084512, 2, 3),
  (2085807, 7, 5),
  (2086043, 3, 2),
  (2087389, 7, 2),
  (2088749, 5, 4),
  (2089374, 7, 3),
  (2090649, 7, 3),
  (2090972, 7, 7),
  (2091097, 4, 3),
  (2094497, 4, 0),
  (2097051, 3, 1),
  (2097459, 5, 3),
  (2100524, 4, 0),
  (2100810, 7, 0),
  (2101519, 2, 5),
  (2101792, 1, 3),
  (2101828, 2, 3),
  (2103975, 1, 3),
  (2108095, 4, 5),
  (2109899, 0, 4),
  (2118149, 7, 7),
  (2118579, 5, 3),
  (2119350, 0, 7),
  (2121023, 4, 1),
  (2121219, 5, 3),
  (2124225, 5, 7),
  (2128965, 5, 4),
  (2130443, 3, 3),
  (2132940, 2, 6),
  (2133105, 5, 3),
  (2133707, 4, 4),
  (2135060, 3, 3),
  (2137313, 2, 3),
  (2137886, 4, 3),
  (2138927, 5, 3),
  (2139046, 0, 4),
  (2144294, 0, 0),
  (2151953, 7, 3),
  (2154575, 5, 0),
  (2158130, 0, 0),
  (2160216, 4, 3),
  (2162430, 7, 0),
  (2162795, 2, 2),
  (2165009, 2, 3),
  (2171810, 4, 3),
  (2172912, 1, 0),
  (2180313, 3, 6),
  (2189169, 0, 0),
  (2194098, 5, 6),
  (2194492, 5, 3),
  (2196918, 6, 0),
  (2198444, 1, 0),
  (2198546, 4, 2),
  (2199706, 4, 3),
  (2200149, 1, 0),
  (2201157, 5, 3),
  (2202096, 7, 4),
  (2204816, 0, 7),
  (2205972, 6, 7),
  (2209381, 7, 5),
  (2209994, 3, 2),
  (2210864, 6, 0),
  (2211338, 4, 7),
  (2215049, 6, 0),
  (2215595, 4, 3),
  (2219607, 4, 7),
  (2221393, 2, 7),
  (2222238, 7, 0),
  (2223586, 3, 2),
  (2224597, 7, 4),
  (2225012, 1, 2),
  (2227750, 2, 6),
  (2227979, 4, 0),
  (2229845, 3, 5),
  (2230217, 2, 7),
  (2234927, 4, 6),
  (2236074, 2, 6),
  (2237850, 2, 7),
  (2238750, 2, 0),
  (2242880, 5, 6),
  (2246581, 0, 4),
  (2250087, 5, 3),
  (2250163, 0, 7),
  (2251894, 2, 1),
  (2254779, 3, 3),
  (2259059, 0, 0),
  (2261320, 5, 7),
  (2262369, 1, 0),
  (2265056, 2, 6),
  (2265242, 7, 3),
  (2266420, 5, 7),
  (2267865, 7, 5),
  (2269479, 3, 1),
  (2272733, 1, 0),
  (2273119, 1, 5),
  (2273771, 0, 0),
  (2277104, 2, 3),
  (2279994, 5, 1),
  (2284479, 5, 3),
  (2285906, 7, 4),
  (2286035, 1, 4),
  (2286385, 5, 6),
  (2290697, 7, 4),
  (2292244, 4, 7),
  (2293537, 1, 7),
  (2294677, 7, 5),
  (2296464, 5, 3),
  (2299717, 3, 3),
  (2304017, 5, 6),
  (2307619, 1, 2),
  (2308616, 1, 2),
  (2310224, 5, 3),
  (2310566, 6, 0),
  (2310739, 7, 4),
  (2311276, 4, 3),
  (2312230, 7, 0),
  (2315041, 2, 5),
  (2315861, 4, 6),
  (2318489, 7, 6),
  (2321217, 1, 7),
  (2321454, 3, 7),
  (2324274, 1, 0),
  (2324788, 2, 3),
  (2326720, 0, 3),
  (2327098, 3, 6),
  (2327429, 0, 0),
  (2328753, 4, 2),
  (2332998, 7, 4),
  (2334903, 1, 0),
  (2337366, 1, 0),
  (2340416, 6, 6),
  (2341909, 2, 5),
  (2343200, 0, 2),
  (2343901, 5, 3),
  (2344567, 3, 3),
  (2345580, 2, 3),
  (2345668, 3, 3),
  (2351140, 6, 3),
  (2352710, 6, 7),
  (2354360, 5, 0),
  (2355382, 5, 3),
  (2356824, 5, 3),
  (2359135, 4, 7),
  (2362231, 0, 3),
  (2363192, 2, 2),
  (2364096, 0, 4),
  (2367507, 6, 6),
  (2367822, 7, 1),
  (2370741, 1, 4),
  (2372336, 6, 0),
  (2372354, 7, 0),
  (2373630, 1, 3),
  (2380573, 2, 1),
  (2381430, 2, 7),
  (2381515, 0, 0),
  (2381992, 5, 7),
  (2382928, 2, 6),
  (2384445, 7, 7),
  (2386326, 5, 2),
  (2386843, 6, 4),
  (2387529, 1, 4),
  (2388122, 0, 7),
  (2388733, 0, 1),
  (2389037, 2, 6),
  (2390136, 1, 5),
  (2392281, 7, 3),
  (2393766, 0, 7),
  (2399124, 3, 3),
  (2401595, 4, 6),
  (2401940, 4, 1),
  (2405058, 4, 6),
  (2406227, 2, 3),
  (2410379, 1, 0),
  (2410525, 7, 0),
  (2412484, 4, 2),
  (2416676, 2, 7),
  (2416758, 4, 3),
  (2416883, 0, 6),
  (2418308, 2, 7),
  (2422474, 2, 2),
  (2427079, 2, 2),
  (2427742, 6, 1),
  (2429940, 1, 7),
  (2431035, 5, 4),
  (2432771, 1, 2),
  (2433014, 6, 0),
  (2433167, 4, 3),
  (2435202, 6, 1),
  (2435722, 6, 0),
  (2436369, 4, 2),
  (2443000, 0, 0),
  (2453388, 2, 2),
  (2455046, 6, 3),
  (2455122, 3, 7),
  (2455173, 5, 3),
  (2467637, 6, 1),
  (2472330, 5, 5),
  (2473499, 6, 7),
  (2473737, 6, 5),
  (2475372, 2, 7),
  (2479422, 7, 7),
  (2480189, 7, 0),
  (2483043, 1, 7),
  (2485416, 7, 1),
  (2494106, 7, 0),
  (2499234, 5, 3),
  (2499942, 2, 3),
  (2503042, 4, 6),
  (2505241, 6, 0),
  (2508880, 3, 2),
  (2512284, 0, 0),
  (2513346, 3, 6),
  (2513636, 6, 0),
  (2514530, 2, 2),
  (2518754, 0, 0),
  (2521033, 1, 3),
  (2521608, 6, 4),
  (2521681, 4, 7),
  (2528325, 0, 0),
  (2529295, 2, 6),
  (2530981, 7, 0),
  (2534726, 2, 3),
  (2535960, 6, 0),
  (2541101, 4, 6),
  (2541675, 7, 3),
  (2542985, 3, 6),
  (2544203, 5, 3),
  (2545011, 5, 6),
  (2550731, 5, 6),
  (2551937, 0, 3),
  (2555357, 0, 3),
  (2557351, 1, 4),
  (2562366, 3, 0),
  (2563203, 4, 7),
  (2563589, 1, 7),
  (2563664, 3, 7),
  (2565122, 7, 3),
  (2572695, 3, 7),
  (2575041, 1, 4),
  (2575562, 2, 7),
  (2576757, 5, 0),
  (2577459, 0, 6),
  (2577460, 7, 3),
  (2578438, 0, 4),
  (2579835, 3, 2),
  (2580263, 6, 4),
  (2582711, 2, 3),
  (2582867, 0, 0),
  (2584868, 4, 6),
  (2585264, 5, 7),
  (2587118, 7, 3),
  (2587237, 1, 2),
  (2588552, 6, 0),
  (2588598, 4, 3),
  (2588970, 3, 6),
  (2589677, 7, 0),
  (2590161, 6, 0),
  (2592330, 0, 7),
  (2592838, 5, 3),
  (2594729, 5, 3),
  (2595380, 3, 3),
  (2596884, 3, 3),
  (2598598, 3, 3),
  (2599371, 0, 0),
  (2599765, 7, 7),
  (2600732, 4, 2),
  (2610608, 4, 3),
  (2616240, 1, 0),
  (2617034, 1, 0),
  (2618235, 3, 6),
  (2619245, 2, 3),
  (2621642, 5, 7),
  (2622650, 6, 0),
  (2623646, 4, 3),
  (2629020, 3, 3),
  (2631416, 0, 0),
  (2635186, 2, 2),
  (2636641, 2, 6),
  (2638120, 2, 1),
  (2640341, 6, 7),
  (2642283, 1, 4),
  (2645283, 1, 4),
  (2651217, 5, 3),
  (2652251, 6, 7),
  (2653078, 5, 3),
  (2653528, 2, 3),
  (2653615, 1, 4),
  (2653634, 1, 3),
  (2655440, 5, 2),
  (2659695, 2, 3),
  (2659867, 6, 6),
  (2661049, 1, 3),
  (2663570, 3, 2),
  (2665718, 2, 3),
  (2667644, 7, 4),
  (2668444, 3, 3),
  (2672145, 7, 0),
  (2673190, 7, 4),
  (2676303, 7, 0),
  (2676813, 6, 0),
  (2682158, 0, 0),
  (2682728, 5, 7),
  (2682771, 3, 3),
  (2684882, 7, 0),
  (2686128, 4, 6),
  (2687610, 7, 3),
  (2688160, 2, 3),
  (2692604, 3, 7),
  (2693394, 0, 0),
  (2694058, 7, 0),
  (2696989, 1, 2),
  (2697171, 6, 0),
  (2700675, 4, 2),
  (2701291, 4, 3),
  (2701436, 1, 4),
  (2705518, 7, 0),
  (2705592, 4, 6),
  (2708961, 2, 4),
  (2711496, 5, 3),
  (2713515, 7, 3),
  (2716139, 5, 3),
  (2719674, 7, 7),
  (2721633, 0, 1),
  (2721721, 6, 4),
  (2722376, 5, 3),
  (2723493, 0, 4),
  (2725052, 4, 3),
  (2727608, 1, 0),
  (2727809, 6, 0),
  (2728070, 1, 6),
  (2728605, 5, 3),
  (2729570, 4, 3),
  (2730649, 4, 3),
  (2730823, 5, 3),
  (2733856, 1, 1),
  (2735175, 1, 7),
  (2735935, 1, 1),
  (2737108, 5, 7),
  (2738147, 4, 2),
  (2739258, 7, 4),
  (2740054, 5, 3),
  (2745132, 7, 6),
  (2748556, 2, 3),
  (2750097, 0, 7),
  (2751096, 0, 4),
  (2751627, 6, 0),
  (2753058, 7, 1),
  (2753832, 0, 0),
  (2754737, 3, 6),
  (2755085, 3, 3),
  (2757172, 3, 3),
  (2762399, 5, 7),
  (2763837, 1, 0),
  (2764533, 1, 0),
  (2765301, 1, 6),
  (2767777, 7, 1),
  (2769842, 2, 3),
  (2771522, 2, 3),
  (2772627, 6, 2),
  (2773335, 5, 2),
  (2774520, 2, 3),
  (2774669, 2, 6),
  (2776745, 6, 7),
  (2777384, 2, 3),
  (2778614, 3, 5),
  (2778963, 4, 3),
  (2779524, 5, 3),
  (2780498, 0, 0),
  (2782920, 6, 3),
  (2786328, 6, 3),
  (2790962, 0, 6),
  (2796874, 0, 0),
  (2797580, 2, 7),
  (2799551, 2, 3),
  (2801738, 4, 2),
  (2803075, 1, 3),
  (2803712, 4, 7),
  (2804191, 0, 0),
  (2809761, 0, 4),
  (2811610, 6, 0),
  (2812388, 6, 7),
  (2816419, 4, 3),
  (2817828, 5, 3),
  (2818428, 3, 3),
  (2818826, 6, 2),
  (2822079, 5, 3),
  (2823541, 0, 0),
  (2827191, 3, 3),
  (2828934, 1, 4),
  (2830158, 2, 4),
  (2831164, 6, 3),
  (2832431, 3, 5),
  (2835879, 4, 3),
  (2836115, 1, 4),
  (2838431, 0, 0),
  (2840883, 0, 0),
  (2843607, 4, 2),
  (2844462, 4, 6),
  (2845692, 0, 1),
  (2848001, 7, 5),
  (2849527, 7, 0),
  (2855739, 1, 0),
  (2856144, 4, 1),
  (2861246, 4, 3),
  (2861496, 5, 3),
  (2863749, 3, 2),
  (2865091, 2, 2),
  (2870390, 5, 2),
  (2875675, 4, 3),
  (2876234, 2, 3),
  (2877599, 1, 3),
  (2877736, 5, 6),
  (2880297, 6, 4),
  (2881285, 2, 7),
  (2881490, 1, 4),
  (2882194, 3, 6),
  (2883254, 4, 1),
  (2883678, 5, 3),
  (2884618, 2, 3),
  (2888226, 5, 6),
  (2889885, 0, 0),
  (2891086, 0, 4),
  (2893858, 0, 4),
  (2894916, 1, 2),
  (2897471, 7, 0),
  (2897770, 0, 3),
  (2904404, 1, 0),
  (2905323, 3, 3),
  (2909189, 2, 3),
  (2915806, 5, 3),
  (2917522, 5, 7),
  (2918354, 5, 3),
  (2922730, 2, 2),
  (2926893, 5, 3),
  (2927285, 5, 7),
  (2932759, 1, 0),
  (2934843, 3, 6),
  (2938286, 4, 3),
  (2940327, 1, 3),
  (2941100, 6, 0),
  (2942923, 3, 3),
  (2946550, 4, 6),
  (2948841, 6, 7),
  (2948952, 6, 0),
  (2949834, 5, 2),
  (2955634, 0, 0),
  (2956248, 0, 3),
  (2957025, 2, 0),
  (2960629, 5, 3),
  (2961985, 5, 0),
  (2965481, 5, 3),
  (2966280, 2, 3),
  (2966516, 0, 5),
  (2967804, 2, 3),
  (2970798, 0, 7),
  (2972314, 7, 0),
  (2973146, 0, 0),
  (2975030, 0, 4),
  (2975118, 2, 2),
  (2980185, 2, 7),
  (2983791, 6, 3),
  (2985474, 2, 3),
  (2987012, 2, 4),
  (2987624, 1, 0),
  (2987864, 5, 0),
  (2989371, 0, 0),
  (2989399, 1, 6),
  (2994482, 4, 7),
  (2994992, 4, 3),
  (2997397, 5, 0),
  (2998523, 7, 0),
  (2999038, 1, 4),
  (3002595, 4, 7),
  (3006138, 0, 2),
  (3006179, 1, 0),
  (3006745, 1, 0),
  (3013637, 4, 6),
  (3014484, 0, 3),
  (3016225, 2, 3),
  (3017958, 1, 7),
  (3021896, 3, 7),
  (3024474, 3, 2),
  (3026256, 2, 7),
  (3026354, 1, 1),
  (3028716, 7, 0),
  (3030136, 6, 1),
  (3030273, 1, 0),
  (3030762, 0, 0),
  (3039830, 3, 4),
  (3040539, 5, 2),
  (3041162, 3, 6),
  (3048119, 7, 1),
  (3048231, 6, 0),
  (3052023, 4, 3),
  (3052847, 3, 3),
  (3056402, 6, 2),
  (3063053, 6, 7),
  (3063266, 0, 0),
  (3069502, 6, 4),
  (3069778, 3, 7),
  (3073425, 1, 3),
  (3074224, 1, 3),
  (3078313, 7, 0),
  (3082878, 3, 5),
  (3088922, 7, 3),
  (3089892, 4, 3),
  (3091057, 2, 6),
  (3091933, 1, 3),
  (3092193, 3, 3),
  (3093898, 5, 3),
  (3095615, 0, 5),
  (3095756, 0, 0),
  (3095895, 5, 3),
  (3096389, 3, 0),
  (3100207, 2, 3),
  (3100214, 7, 7),
  (3102690, 1, 0),
  (3105872, 1, 0),
  (3106517, 3, 3),
  (3109552, 5, 6),
  (3110973, 0, 5),
  (3111548, 6, 0),
  (3113347, 2, 2),
  (3115393, 6, 0),
  (3118700, 6, 5),
  (3118971, 1, 2),
  (3121023, 0, 4),
  (3122849, 1, 0),
  (3125648, 7, 3),
  (3126265, 7, 2),
  (3131833, 5, 1),
  (3135978, 2, 3),
  (3136365, 5, 4),
  (3142282, 7, 7),
  (3143310, 4, 3),
  (3143716, 7, 7),
  (3145398, 1, 1),
  (3148950, 5, 3),
  (3152344, 3, 3),
  (3156626, 0, 0),
  (3158854, 7, 0),
  (3159061, 2, 7),
  (3160986, 4, 3),
  (3162893, 0, 5),
  (3163240, 1, 0),
  (3165344, 1, 0),
  (3165398, 1, 3),
  (3170769, 3, 2),
  (3171077, 3, 2),
  (3174832, 5, 3),
  (3178395, 3, 6),
  (3179829, 4, 6),
  (3183112, 3, 6),
  (3183260, 3, 7),
  (3183398, 7, 4),
  (3183509, 5, 6),
  (3184184, 6, 0),
  (3184452, 1, 4),
  (3187460, 5, 7),
  (3188249, 4, 0),
  (3190327, 2, 6),
  (3190623, 2, 3),
  (3191841, 0, 4),
  (3194277, 5, 3),
  (3195583, 4, 7),
  (3196179, 6, 3),
  (3197863, 3, 3),
  (3200638, 6, 3),
  (3200658, 1, 0),
  (3202276, 1, 3),
  (3202900, 7, 0),
  (3204019, 4, 2),
  (3206543, 3, 3),
  (3208310, 1, 0),
  (3209678, 2, 3),
  (3212758, 6, 3),
  (3214591, 1, 0),
  (3216111, 6, 0),
  (3216953, 7, 0),
  (3217886, 2, 1),
  (3218990, 4, 3),
  (3219696, 5, 3),
  (3219881, 2, 1),
  (3221164, 1, 0),
  (3225626, 1, 3),
  (3232450, 0, 4),
  (3233102, 1, 4),
  (3236364, 5, 2),
  (3236634, 4, 3),
  (3237516, 4, 2),
  (3237581, 1, 7),
  (3242253, 0, 0),
  (3244162, 0, 5),
  (3244848, 7, 3),
  (3245469, 0, 0),
  (3249256, 7, 6),
  (3250231, 2, 0),
  (3251378, 3, 2),
  (3252232, 2, 6),
  (3252683, 6, 0),
  (3254500, 4, 3),
  (3257437, 7, 0),
  (3259138, 0, 2),
  (3259901, 1, 5),
  (3262442, 1, 3),
  (3263149, 6, 3),
  (3264079, 6, 7),
  (3266091, 6, 0),
  (3267148, 7, 4),
  (3268996, 5, 2),
  (3269117, 3, 7),
  (3270281, 2, 6),
  (3270506, 5, 0),
  (3271879, 7, 3),
  (3272212, 1, 0),
  (3274302, 3, 7),
  (3276927, 0, 0),
  (3277466, 0, 0),
  (3277863, 3, 7),
  (3285700, 2, 6),
  (3286416, 4, 6),
  (3289222, 3, 7),
  (3290792, 4, 3),
  (3291731, 1, 3),
  (3291980, 6, 0),
  (3292378, 5, 3),
  (3293562, 1, 0),
  (3296134, 5, 1),
  (3296197, 7, 6),
  (3296315, 2, 3),
  (3296866, 6, 0),
  (3298782, 5, 3),
  (3298963, 1, 3),
  (3303550, 3, 6),
  (3304349, 4, 7),
  (3307702, 6, 3),
  (3308448, 4, 3),
  (3309648, 3, 3),
  (3310564, 1, 4),
  (3310900, 0, 0),
  (3314521, 3, 3),
  (3315079, 1, 0),
  (3316360, 1, 0),
  (3316748, 7, 3),
  (3317075, 5, 7),
  (3318542, 7, 0),
  (3326033, 1, 3),
  (3326432, 6, 2),
  (3327026, 3, 3),
  (3328138, 1, 5),
  (3329253, 3, 3),
  (3330341, 5, 3),
  (3331246, 5, 3),
  (3332218, 5, 2),
  (3332462, 0, 7),
  (3335805, 3, 2),
  (3337524, 0, 4),
  (3339231, 6, 4),
  (3342253, 0, 0),
  (3344934, 5, 3),
  (3347734, 1, 7),
  (3351529, 0, 0),
  (3356906, 1, 0),
  (3357476, 0, 7),
  (3360324, 5, 4),
  (3361453, 3, 6),
  (3363372, 4, 2),
  (3364387, 1, 4),
  (3364388, 6, 3),
  (3364452, 7, 3),
  (3364874, 6, 6),
  (3368472, 6, 0),
  (3370450, 1, 2),
  (3370452, 1, 4),
  (3370823, 0, 0),
  (3371153, 5, 2),
  (3371309, 7, 0),
  (3372001, 5, 3),
  (3372479, 7, 0),
  (3374892, 2, 3),
  (3376836, 4, 3),
  (3378215, 4, 7),
  (3378499, 6, 0),
  (3378820, 1, 3),
  (3379627, 2, 1),
  (3382532, 2, 3),
  (3382919, 4, 7),
  (3383140, 3, 0),
  (3383288, 6, 4),
  (3388243, 1, 0),
  (3389651, 6, 0),
  (3390205, 5, 2),
  (3397016, 2, 3),
  (3397061, 1, 4),
  (3402136, 4, 2),
  (3402706, 7, 0),
  (3404314, 7, 2),
  (3404659, 0, 0),
  (3404925, 0, 0),
  (3406573, 4, 2),
  (3410639, 3, 2),
  (3412440, 2, 3),
  (3415467, 1, 3),
  (3419016, 6, 4),
  (3421591, 7, 0),
  (3422802, 5, 2),
  (3423077, 0, 7),
  (3423306, 1, 2),
  (3425145, 1, 0),
  (3425507, 5, 6),
  (3429189, 3, 6),
  (3429463, 6, 6),
  (3432135, 3, 2),
  (3433616, 0, 0),
  (3436042, 6, 5),
  (3439271, 0, 3),
  (3441720, 5, 7),
  (3441837, 3, 3),
  (3442183, 4, 7),
  (3442518, 1, 0),
  (3445317, 2, 6),
  (3448986, 0, 6),
  (3451107, 3, 3),
  (3452098, 6, 1),
  (3452218, 1, 4),
  (3454080, 2, 1),
  (3457897, 5, 6),
  (3458450, 5, 2),
  (3459346, 5, 3),
  (3460578, 2, 5),
  (3461301, 6, 0),
  (3463947, 6, 7),
  (3464523, 2, 7),
  (3468452, 6, 0),
  (3472459, 4, 4),
  (3473560, 4, 3),
  (3478058, 2, 3),
  (3480496, 0, 0),
  (3481920, 3, 6),
  (3482286, 2, 3),
  (3483032, 1, 0),
  (3484737, 6, 4),
  (3486486, 1, 1),
  (3487102, 2, 6),
  (3487210, 2, 3),
  (3492297, 3, 2),
  (3500904, 0, 0),
  (3505773, 6, 1),
  (3508610, 6, 0),
  (3520547, 0, 0),
  (3522084, 7, 4),
  (3522089, 4, 3),
  (3524779, 3, 3),
  (3526645, 5, 3),
  (3526704, 2, 7),
  (3529247, 0, 0),
  (3529985, 3, 1),
  (3532836, 0, 0),
  (3537736, 0, 4),
  (3537844, 0, 4),
  (3539471, 0, 0),
  (3540822, 6, 7),
  (3549355, 6, 4),
  (3551196, 5, 1),
  (3551852, 1, 3),
  (3551983, 1, 4),
  (3552604, 1, 3),
  (3554443, 1, 7),
  (3556511, 6, 4),
  (3559386, 2, 3),
  (3562061, 0, 0),
  (3562741, 6, 5),
  (3564061, 4, 3),
  (3566279, 5, 3),
  (3567949, 7, 3),
  (3568667, 6, 4),
  (3571025, 1, 5),
  (3571586, 2, 7),
  (3572345, 4, 3),
  (3574391, 6, 0),
  (3576261, 2, 1),
  (3584888, 2, 7),
  (3587816, 0, 0),
  (3588859, 7, 4),
  (3589780, 6, 4),
  (3590066, 3, 3),
  (3590176, 2, 3),
  (3590719, 4, 5),
  (3590905, 5, 3),
  (3591125, 0, 6),
  (3593207, 1, 4),
  (3593973, 1, 0),
  (3595940, 4, 2),
  (3599514, 2, 5),
])