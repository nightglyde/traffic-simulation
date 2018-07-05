from util import *
schedule = deque([
  (5287, 7, 0),
  (9950, 4, 1),
  (10221, 3, 7),
  (12106, 5, 3),
  (12985, 7, 4),
  (13387, 2, 4),
  (14546, 7, 0),
  (16212, 6, 0),
  (17387, 2, 3),
  (19773, 5, 0),
  (21016, 2, 4),
  (21635, 7, 0),
  (22963, 6, 0),
  (25362, 5, 7),
  (26353, 4, 7),
  (30465, 5, 3),
  (30753, 5, 7),
  (31289, 2, 7),
  (31555, 7, 7),
  (31705, 2, 7),
  (32036, 7, 0),
  (32537, 0, 0),
  (36097, 3, 6),
  (36354, 0, 0),
  (36497, 1, 6),
  (37834, 3, 7),
  (38091, 6, 3),
  (53633, 6, 0),
  (54734, 2, 2),
  (56376, 2, 6),
  (60857, 6, 2),
  (61707, 1, 0),
  (61736, 0, 7),
  (62295, 1, 0),
  (62941, 4, 3),
  (63829, 4, 2),
  (69047, 6, 7),
  (70284, 0, 7),
  (71863, 1, 0),
  (72674, 4, 3),
  (75218, 0, 1),
  (78467, 3, 3),
  (78557, 2, 7),
  (80838, 1, 7),
  (81162, 6, 7),
  (81842, 2, 7),
  (81927, 4, 6),
  (83663, 0, 4),
  (84681, 0, 4),
  (85632, 5, 3),
  (88611, 1, 7),
  (91248, 1, 7),
  (93246, 2, 7),
  (93517, 5, 3),
  (96415, 6, 7),
  (96902, 2, 7),
  (98240, 0, 0),
  (99678, 6, 4),
  (103253, 2, 2),
  (109619, 0, 7),
  (112331, 4, 3),
  (113672, 4, 7),
  (114183, 6, 4),
  (114352, 2, 3),
  (118726, 1, 0),
  (119536, 6, 0),
  (119745, 6, 7),
  (120018, 0, 7),
  (121624, 1, 3),
  (122808, 0, 6),
  (123403, 5, 3),
  (124555, 4, 3),
  (124865, 3, 3),
  (125519, 3, 6),
  (125858, 5, 7),
  (126949, 0, 4),
  (127045, 6, 7),
  (129699, 2, 7),
  (131490, 6, 0),
  (133964, 5, 3),
  (133970, 4, 7),
  (135752, 0, 0),
  (143246, 3, 3),
  (145685, 2, 7),
  (145722, 6, 6),
  (147487, 4, 7),
  (153445, 1, 3),
  (157215, 3, 7),
  (159963, 6, 4),
  (160215, 2, 3),
  (162275, 3, 3),
  (164036, 5, 5),
  (168355, 3, 7),
  (168942, 0, 3),
  (170112, 3, 6),
  (170146, 4, 7),
  (173572, 0, 6),
  (175384, 6, 4),
  (178516, 7, 1),
  (179381, 6, 3),
  (179588, 3, 6),
  (184307, 0, 2),
  (185284, 4, 2),
  (185344, 4, 7),
  (186423, 3, 7),
  (186788, 1, 7),
  (187670, 5, 7),
  (188647, 4, 5),
  (189077, 3, 6),
  (189221, 0, 4),
  (195468, 2, 5),
  (195560, 4, 2),
  (197109, 6, 3),
  (203722, 5, 3),
  (204172, 2, 5),
  (205347, 0, 4),
  (206148, 6, 4),
  (206486, 0, 7),
  (207918, 6, 0),
  (210125, 5, 2),
  (211213, 3, 5),
  (212851, 1, 0),
  (213216, 0, 4),
  (214291, 6, 3),
  (214365, 4, 3),
  (215114, 6, 0),
  (215634, 3, 6),
  (216589, 3, 7),
  (217828, 7, 0),
  (218013, 3, 2),
  (221124, 3, 5),
  (222810, 7, 6),
  (222959, 6, 7),
  (224551, 0, 3),
  (226810, 1, 0),
  (227347, 4, 6),
  (228945, 1, 3),
  (229597, 4, 7),
  (230084, 6, 7),
  (233661, 5, 7),
  (234325, 2, 3),
  (235546, 0, 0),
  (236512, 1, 7),
  (237239, 7, 7),
  (237263, 1, 0),
  (238548, 4, 5),
  (241420, 4, 2),
  (242523, 3, 7),
  (243795, 0, 7),
  (246371, 5, 7),
  (247729, 5, 6),
  (247904, 0, 7),
  (250569, 1, 0),
  (251244, 7, 4),
  (255317, 3, 3),
  (255459, 6, 3),
  (255480, 2, 2),
  (255902, 6, 3),
  (258690, 6, 2),
  (260411, 3, 6),
  (261011, 6, 0),
  (263676, 7, 4),
  (264407, 7, 3),
  (272437, 6, 0),
  (273046, 7, 3),
  (275827, 1, 0),
  (279200, 0, 7),
  (280222, 3, 7),
  (280888, 0, 4),
  (280942, 1, 3),
  (283844, 1, 0),
  (285005, 2, 1),
  (286534, 0, 3),
  (289838, 3, 7),
  (289856, 5, 0),
  (290318, 4, 7),
  (291038, 0, 6),
  (291303, 6, 7),
  (293135, 3, 7),
  (295498, 7, 0),
  (298690, 7, 7),
  (300696, 1, 0),
  (302646, 4, 3),
  (303145, 6, 4),
  (303989, 1, 7),
  (304129, 0, 4),
  (306030, 7, 5),
  (306966, 0, 0),
  (310288, 2, 3),
  (310664, 7, 0),
  (314706, 0, 3),
  (322664, 2, 7),
  (324867, 7, 6),
  (325922, 2, 3),
  (327178, 2, 5),
  (327636, 1, 4),
  (327910, 7, 0),
  (328074, 2, 3),
  (328950, 6, 7),
  (330602, 7, 4),
  (332528, 2, 5),
  (332667, 7, 0),
  (333392, 4, 2),
  (335040, 0, 4),
  (335225, 7, 5),
  (338413, 5, 2),
  (339834, 6, 2),
  (341757, 0, 0),
  (343437, 5, 1),
  (346494, 0, 5),
  (346917, 0, 4),
  (347028, 7, 7),
  (348631, 5, 7),
  (356801, 2, 3),
  (357209, 4, 5),
  (358400, 2, 7),
  (363755, 1, 0),
  (364589, 0, 7),
  (369214, 2, 5),
  (380677, 1, 6),
  (382976, 0, 0),
  (383301, 7, 0),
  (389052, 4, 6),
  (391996, 4, 2),
  (393198, 2, 7),
  (396333, 7, 0),
  (398661, 7, 7),
  (399050, 4, 6),
  (406166, 5, 7),
  (408644, 0, 4),
  (410492, 5, 4),
  (410667, 4, 2),
  (411180, 5, 7),
  (418069, 4, 3),
  (419627, 7, 7),
  (420028, 4, 2),
  (420679, 7, 4),
  (420888, 5, 7),
  (421175, 3, 2),
  (425495, 4, 3),
  (425715, 0, 1),
  (427142, 7, 4),
  (429184, 3, 3),
  (429749, 2, 3),
  (430871, 0, 4),
  (433769, 2, 3),
  (435778, 6, 0),
  (435947, 4, 3),
  (438698, 4, 4),
  (438741, 7, 0),
  (439496, 5, 7),
  (440271, 0, 0),
  (442268, 0, 0),
  (442999, 3, 3),
  (444109, 4, 7),
  (444521, 3, 7),
  (444689, 3, 6),
  (445323, 0, 7),
  (448227, 6, 7),
  (448477, 0, 7),
  (452810, 5, 3),
  (453022, 7, 0),
  (458708, 6, 4),
  (463985, 0, 3),
  (465236, 1, 7),
  (466704, 1, 7),
  (467127, 1, 4),
  (468426, 3, 3),
  (470205, 1, 3),
  (471496, 4, 3),
  (471967, 4, 2),
  (472625, 5, 7),
  (472703, 5, 3),
  (473240, 2, 2),
  (473847, 5, 7),
  (474376, 1, 0),
  (474631, 5, 3),
  (478467, 5, 2),
  (480609, 5, 7),
  (482098, 4, 6),
  (485011, 5, 3),
  (486773, 4, 6),
  (488319, 7, 7),
  (491031, 6, 7),
  (492139, 0, 4),
  (496433, 5, 2),
  (499991, 1, 4),
  (501603, 7, 0),
  (506097, 0, 0),
  (509192, 2, 6),
  (509379, 2, 7),
  (510799, 7, 0),
  (510948, 3, 6),
  (511557, 2, 7),
  (513366, 7, 7),
  (514626, 1, 3),
  (515208, 5, 3),
  (517693, 6, 0),
  (518423, 1, 7),
  (518848, 7, 0),
  (524721, 7, 7),
  (528846, 5, 3),
  (528948, 2, 7),
  (529888, 4, 0),
  (532508, 0, 3),
  (534896, 7, 6),
  (538232, 4, 1),
  (539755, 1, 7),
  (540213, 5, 3),
  (540220, 4, 6),
  (541274, 4, 6),
  (542848, 7, 7),
  (546940, 6, 5),
  (551075, 7, 0),
  (552231, 4, 4),
  (552594, 5, 3),
  (552810, 0, 7),
  (556609, 3, 3),
  (556883, 7, 0),
  (559822, 3, 7),
  (560500, 4, 5),
  (561899, 3, 7),
  (564942, 6, 7),
  (565572, 0, 4),
  (566829, 5, 2),
  (567592, 1, 4),
  (570526, 7, 0),
  (574665, 6, 2),
  (576658, 3, 3),
  (577583, 3, 7),
  (578629, 6, 3),
  (578791, 5, 7),
  (579893, 6, 6),
  (581918, 5, 6),
  (591187, 7, 7),
  (593928, 2, 3),
  (594873, 7, 3),
  (594937, 3, 7),
  (597120, 4, 5),
  (598567, 4, 3),
  (599305, 0, 4),
  (600438, 5, 6),
  (600737, 7, 3),
  (602673, 3, 3),
  (604578, 5, 7),
  (610842, 5, 7),
  (611441, 5, 3),
  (616207, 6, 0),
  (619020, 5, 3),
  (619788, 4, 5),
  (619836, 4, 3),
  (622793, 7, 0),
  (623859, 5, 2),
  (624437, 4, 7),
  (626235, 7, 7),
  (630585, 3, 7),
  (631530, 7, 7),
  (633197, 1, 0),
  (635453, 7, 6),
  (636402, 0, 5),
  (636408, 0, 5),
  (638266, 5, 2),
  (638328, 6, 7),
  (639233, 0, 6),
  (639419, 6, 3),
  (640841, 6, 7),
  (641575, 3, 3),
  (641593, 7, 0),
  (641911, 0, 7),
  (642111, 1, 3),
  (643064, 5, 3),
  (643177, 3, 6),
  (643283, 7, 0),
  (643424, 4, 2),
  (649721, 2, 1),
  (652259, 3, 7),
  (653008, 6, 4),
  (654264, 4, 6),
  (657660, 4, 3),
  (659669, 0, 0),
  (661522, 6, 7),
  (664125, 5, 5),
  (664982, 4, 7),
  (665378, 5, 3),
  (666260, 5, 2),
  (667178, 4, 2),
  (667588, 5, 7),
  (670376, 1, 7),
  (670789, 3, 7),
  (676387, 4, 6),
  (680388, 5, 4),
  (681383, 2, 2),
  (682994, 2, 3),
  (683828, 5, 3),
  (687152, 5, 6),
  (687607, 0, 4),
  (690152, 3, 7),
  (692605, 5, 2),
  (694058, 0, 2),
  (694480, 1, 7),
  (695312, 6, 0),
  (695661, 5, 7),
  (697874, 4, 7),
  (698638, 2, 7),
  (700774, 6, 0),
  (701432, 7, 0),
  (702510, 1, 2),
  (706113, 2, 5),
  (707838, 0, 0),
  (707964, 0, 4),
  (709757, 5, 7),
  (714636, 4, 3),
  (714752, 5, 1),
  (714961, 3, 6),
  (716191, 4, 2),
  (717012, 2, 0),
  (719651, 0, 7),
  (721043, 6, 3),
  (721327, 5, 7),
  (723815, 3, 3),
  (726428, 5, 1),
  (728033, 6, 0),
  (729691, 2, 7),
  (730960, 1, 7),
  (735404, 3, 7),
  (735910, 3, 7),
  (736101, 5, 2),
  (736968, 6, 7),
  (738647, 5, 7),
  (742448, 5, 2),
  (742925, 6, 4),
  (745099, 5, 3),
  (745433, 0, 6),
  (750594, 7, 4),
  (753510, 7, 7),
  (754621, 3, 6),
  (756253, 1, 7),
  (756756, 4, 3),
  (757135, 1, 3),
  (759778, 6, 3),
  (765092, 7, 7),
  (765738, 7, 0),
  (770473, 3, 3),
  (770863, 4, 3),
  (775188, 4, 6),
  (776049, 0, 4),
  (778720, 4, 4),
  (781394, 2, 3),
  (783434, 7, 7),
  (785625, 6, 3),
  (786439, 6, 5),
  (787199, 4, 6),
  (788126, 6, 4),
  (790576, 6, 4),
  (799298, 4, 3),
  (802143, 3, 0),
  (805836, 0, 0),
  (806417, 7, 7),
  (806865, 3, 7),
  (807485, 0, 0),
  (807989, 2, 2),
  (808247, 2, 3),
  (809049, 2, 3),
  (813173, 6, 7),
  (815813, 4, 2),
  (816647, 7, 6),
  (817047, 0, 0),
  (818325, 5, 7),
  (818575, 3, 3),
  (819056, 2, 7),
  (820655, 7, 0),
  (823945, 5, 4),
  (829917, 4, 7),
  (830459, 4, 2),
  (830770, 7, 0),
  (835813, 4, 7),
  (836530, 0, 7),
  (838141, 5, 2),
  (838852, 3, 3),
  (838970, 4, 0),
  (840971, 6, 7),
  (842105, 7, 3),
  (845023, 3, 7),
  (846313, 5, 3),
  (849572, 1, 7),
  (850503, 7, 7),
  (850513, 0, 3),
  (852506, 2, 2),
  (853194, 4, 4),
  (853337, 5, 1),
  (854302, 2, 7),
  (855771, 5, 3),
  (857305, 3, 7),
  (858302, 7, 6),
  (859373, 2, 7),
  (863898, 3, 2),
  (864697, 5, 7),
  (865305, 0, 0),
  (868423, 5, 2),
  (868498, 7, 0),
  (869419, 7, 7),
  (870983, 4, 3),
  (873302, 3, 6),
  (873938, 7, 7),
  (875997, 5, 2),
  (882279, 7, 7),
  (883690, 7, 0),
  (884083, 6, 7),
  (884390, 0, 4),
  (884459, 7, 0),
  (884558, 3, 4),
  (884799, 3, 5),
  (887644, 7, 3),
  (888839, 5, 7),
  (892306, 6, 7),
  (892866, 1, 3),
  (895374, 0, 0),
  (896382, 6, 0),
  (900787, 4, 2),
  (903337, 0, 7),
  (903425, 3, 7),
  (905677, 2, 7),
  (906855, 5, 2),
  (908463, 7, 4),
  (908561, 0, 7),
  (911223, 4, 3),
  (915160, 2, 6),
  (922205, 7, 0),
  (922490, 5, 3),
  (924402, 2, 3),
  (928615, 2, 2),
  (929801, 5, 2),
  (931230, 3, 5),
  (932557, 0, 7),
  (932640, 0, 7),
  (933176, 0, 4),
  (934577, 7, 0),
  (935499, 4, 5),
  (935585, 2, 7),
  (942694, 7, 3),
  (947956, 0, 0),
  (949552, 1, 7),
  (950273, 2, 6),
  (954530, 3, 3),
  (955805, 6, 4),
  (957340, 0, 0),
  (958320, 2, 2),
  (960021, 3, 1),
  (968281, 6, 7),
  (968403, 4, 1),
  (973486, 6, 4),
  (973736, 2, 7),
  (986318, 6, 0),
  (989352, 6, 0),
  (992917, 4, 3),
  (995611, 6, 1),
  (995951, 4, 3),
  (999674, 2, 3),
  (1000052, 5, 6),
  (1001518, 3, 6),
  (1002590, 0, 6),
  (1003211, 5, 2),
  (1007274, 2, 7),
  (1007996, 3, 2),
  (1013448, 7, 3),
  (1014047, 4, 0),
  (1015486, 4, 2),
  (1017639, 5, 7),
  (1022004, 7, 0),
  (1022836, 0, 6),
  (1028265, 5, 4),
  (1029302, 0, 0),
  (1034392, 4, 3),
  (1034911, 1, 7),
  (1035229, 3, 7),
  (1038162, 0, 7),
  (1038214, 6, 3),
  (1038386, 4, 1),
  (1039821, 5, 3),
  (1041035, 7, 0),
  (1045281, 3, 2),
  (1046769, 0, 4),
  (1047056, 3, 7),
  (1048129, 5, 7),
  (1051503, 7, 3),
  (1052741, 3, 3),
  (1054646, 4, 3),
  (1055760, 4, 7),
  (1064113, 6, 0),
  (1065373, 4, 6),
  (1066481, 0, 6),
  (1067560, 6, 0),
  (1068038, 2, 7),
  (1068179, 5, 3),
  (1068209, 0, 4),
  (1069426, 0, 7),
  (1071786, 1, 7),
  (1072791, 1, 0),
  (1073697, 0, 3),
  (1075216, 6, 4),
  (1075451, 6, 0),
  (1077098, 1, 0),
  (1078807, 2, 2),
  (1080648, 1, 2),
  (1081860, 0, 3),
  (1083676, 5, 4),
  (1084200, 1, 0),
  (1085529, 0, 4),
  (1086919, 0, 0),
  (1088339, 0, 3),
  (1094484, 7, 4),
  (1096239, 5, 7),
  (1097388, 3, 7),
  (1101028, 1, 0),
  (1103638, 4, 7),
  (1104050, 1, 4),
  (1104242, 2, 2),
  (1106109, 0, 4),
  (1106411, 1, 7),
  (1107037, 7, 3),
  (1108613, 0, 7),
  (1109178, 5, 6),
  (1109890, 4, 6),
  (1110669, 5, 3),
  (1112223, 7, 4),
  (1112384, 0, 2),
  (1112606, 7, 7),
  (1114837, 0, 0),
  (1118235, 3, 7),
  (1119520, 0, 3),
  (1120894, 6, 7),
  (1125263, 3, 2),
  (1125460, 2, 3),
  (1129550, 7, 0),
  (1129729, 2, 2),
  (1130501, 5, 4),
  (1132013, 0, 7),
  (1133449, 7, 2),
  (1133453, 5, 2),
  (1133573, 1, 0),
  (1134469, 7, 4),
  (1135215, 0, 0),
  (1139317, 3, 1),
  (1140107, 2, 3),
  (1140858, 1, 1),
  (1145185, 7, 0),
  (1146276, 1, 4),
  (1148282, 7, 0),
  (1150527, 0, 0),
  (1154832, 5, 3),
  (1155155, 5, 7),
  (1159216, 0, 0),
  (1159589, 4, 6),
  (1160551, 4, 2),
  (1161723, 6, 0),
  (1161726, 3, 7),
  (1161966, 7, 4),
  (1166490, 4, 6),
  (1167035, 0, 5),
  (1171695, 3, 7),
  (1173704, 5, 2),
  (1174040, 4, 5),
  (1174162, 1, 7),
  (1174248, 5, 2),
  (1175109, 3, 2),
  (1177794, 6, 6),
  (1179297, 1, 7),
  (1180155, 7, 0),
  (1180507, 6, 3),
  (1184303, 2, 3),
  (1185313, 5, 6),
  (1187060, 1, 7),
  (1189760, 7, 7),
  (1192074, 7, 0),
  (1193187, 6, 7),
  (1193907, 0, 7),
  (1194990, 0, 7),
  (1196519, 1, 0),
  (1198260, 5, 7),
  (1200807, 3, 3),
  (1201382, 6, 7),
  (1203313, 5, 6),
  (1205061, 2, 7),
  (1209232, 3, 4),
  (1217178, 7, 7),
  (1217415, 1, 6),
  (1218116, 5, 3),
  (1219791, 6, 0),
  (1222497, 2, 6),
  (1224951, 4, 3),
  (1227328, 2, 7),
  (1227792, 6, 0),
  (1228532, 4, 2),
  (1237280, 1, 0),
  (1238574, 5, 5),
  (1240878, 7, 4),
  (1242822, 6, 5),
  (1242823, 0, 0),
  (1248160, 5, 7),
  (1249255, 2, 3),
  (1253242, 1, 2),
  (1258204, 6, 2),
  (1258519, 2, 6),
  (1262073, 4, 3),
  (1263219, 1, 0),
  (1263755, 3, 4),
  (1264316, 6, 7),
  (1264851, 0, 7),
  (1266718, 1, 7),
  (1269906, 2, 2),
  (1271540, 1, 4),
  (1271638, 6, 3),
  (1274235, 1, 4),
  (1275245, 7, 4),
  (1276475, 5, 7),
  (1277381, 0, 3),
  (1278361, 6, 0),
  (1279920, 0, 0),
  (1280759, 1, 4),
  (1281881, 5, 3),
  (1282033, 5, 6),
  (1284186, 5, 2),
  (1287718, 7, 7),
  (1290895, 5, 3),
  (1292055, 6, 5),
  (1292939, 3, 2),
  (1293107, 1, 7),
  (1293535, 4, 7),
  (1293870, 6, 0),
  (1294323, 6, 4),
  (1296335, 7, 0),
  (1297649, 3, 1),
  (1298547, 3, 6),
  (1300480, 6, 4),
  (1300695, 0, 5),
  (1306933, 4, 4),
  (1307229, 3, 3),
  (1309122, 2, 7),
  (1310749, 2, 2),
  (1313208, 5, 2),
  (1313286, 2, 3),
  (1313765, 1, 0),
  (1314305, 7, 0),
  (1316055, 5, 0),
  (1318103, 3, 0),
  (1319449, 2, 5),
  (1320485, 1, 0),
  (1322040, 3, 1),
  (1328380, 2, 1),
  (1331086, 2, 7),
  (1332891, 3, 6),
  (1334723, 3, 7),
  (1336020, 2, 3),
  (1336199, 7, 4),
  (1336424, 3, 7),
  (1336532, 4, 7),
  (1337761, 0, 6),
  (1338999, 1, 0),
  (1343331, 6, 0),
  (1343611, 2, 6),
  (1344520, 1, 3),
  (1352791, 3, 4),
  (1355322, 5, 7),
  (1358796, 5, 3),
  (1364102, 5, 1),
  (1364550, 3, 5),
  (1365457, 3, 7),
  (1366943, 7, 6),
  (1374327, 4, 2),
  (1378206, 1, 7),
  (1378519, 7, 6),
  (1381317, 1, 0),
  (1384305, 7, 4),
  (1386178, 6, 6),
  (1386495, 5, 6),
  (1387958, 5, 6),
  (1388949, 1, 3),
  (1389115, 7, 5),
  (1390557, 1, 7),
  (1391029, 0, 3),
  (1393419, 5, 3),
  (1396694, 1, 0),
  (1404837, 4, 5),
  (1405561, 1, 3),
  (1405738, 7, 7),
  (1410336, 4, 7),
  (1411552, 4, 6),
  (1416700, 5, 2),
  (1419126, 2, 5),
  (1422800, 0, 3),
  (1425408, 1, 3),
  (1428686, 5, 7),
  (1428936, 0, 7),
  (1429653, 2, 7),
  (1430556, 4, 5),
  (1430687, 2, 6),
  (1432734, 4, 3),
  (1434657, 1, 7),
  (1435988, 4, 2),
  (1444038, 7, 0),
  (1446541, 3, 2),
  (1450923, 1, 6),
  (1451423, 1, 7),
  (1451520, 0, 0),
  (1451931, 2, 2),
  (1453070, 4, 7),
  (1456339, 2, 3),
  (1461366, 3, 3),
  (1463215, 2, 3),
  (1464868, 5, 0),
  (1465516, 1, 7),
  (1466722, 5, 7),
  (1467039, 3, 6),
  (1470011, 4, 3),
  (1470801, 1, 4),
  (1474532, 5, 2),
  (1474633, 0, 3),
  (1475442, 4, 6),
  (1476696, 3, 6),
  (1482486, 3, 7),
  (1487583, 4, 3),
  (1487802, 0, 4),
  (1491101, 2, 3),
  (1492468, 4, 3),
  (1493389, 0, 3),
  (1496669, 5, 0),
  (1496706, 0, 6),
  (1499527, 4, 3),
  (1501883, 4, 7),
  (1503912, 3, 3),
  (1503955, 0, 0),
  (1506846, 3, 5),
  (1507084, 5, 7),
  (1507458, 2, 6),
  (1510841, 3, 3),
  (1513571, 1, 7),
  (1515967, 7, 0),
  (1520733, 4, 6),
  (1521732, 6, 3),
  (1521799, 0, 7),
  (1525120, 3, 6),
  (1525268, 7, 2),
  (1526004, 1, 4),
  (1526007, 7, 0),
  (1526958, 1, 7),
  (1527192, 2, 6),
  (1527780, 2, 4),
  (1533442, 7, 0),
  (1534859, 1, 0),
  (1535576, 7, 3),
  (1537703, 4, 7),
  (1539462, 1, 3),
  (1542991, 5, 6),
  (1543941, 2, 3),
  (1545939, 2, 3),
  (1546524, 4, 3),
  (1548069, 5, 7),
  (1549058, 4, 3),
  (1550918, 3, 6),
  (1551692, 0, 5),
  (1554218, 4, 6),
  (1556072, 4, 2),
  (1561410, 5, 3),
  (1563177, 1, 7),
  (1566097, 2, 2),
  (1569043, 3, 1),
  (1574404, 6, 5),
  (1579085, 6, 4),
  (1579862, 2, 1),
  (1580056, 5, 7),
  (1583021, 4, 3),
  (1584812, 6, 2),
  (1589585, 3, 2),
  (1589621, 2, 3),
  (1590555, 1, 7),
  (1592723, 2, 6),
  (1593020, 0, 7),
  (1594430, 1, 7),
  (1596095, 7, 0),
  (1597685, 2, 3),
  (1597839, 4, 7),
  (1598941, 6, 0),
  (1601312, 1, 0),
  (1601646, 6, 0),
  (1602947, 7, 3),
  (1602955, 3, 3),
  (1603529, 0, 7),
  (1604032, 6, 7),
  (1614285, 5, 3),
  (1615404, 5, 5),
  (1615470, 5, 3),
  (1617281, 5, 5),
  (1617622, 3, 2),
  (1618809, 1, 4),
  (1621389, 4, 5),
  (1622627, 1, 7),
  (1623822, 5, 3),
  (1628769, 0, 0),
  (1628897, 6, 0),
  (1629109, 3, 6),
  (1630871, 3, 5),
  (1631976, 6, 1),
  (1632931, 6, 4),
  (1633358, 7, 3),
  (1633754, 7, 7),
  (1634803, 6, 0),
  (1635126, 7, 7),
  (1637166, 7, 0),
  (1637968, 4, 2),
  (1639048, 1, 4),
  (1643334, 5, 7),
  (1644035, 6, 3),
  (1646388, 3, 3),
  (1647625, 0, 4),
  (1647819, 5, 3),
  (1651207, 7, 0),
  (1655926, 2, 3),
  (1658197, 0, 3),
  (1659037, 7, 3),
  (1662783, 7, 7),
  (1663655, 5, 2),
  (1664622, 2, 6),
  (1665939, 0, 5),
  (1666952, 2, 3),
  (1667131, 6, 5),
  (1672990, 2, 4),
  (1675080, 0, 4),
  (1676619, 4, 6),
  (1676722, 2, 6),
  (1678207, 1, 4),
  (1678388, 0, 3),
  (1681781, 0, 0),
  (1682921, 0, 7),
  (1686052, 4, 3),
  (1686660, 7, 0),
  (1688797, 4, 1),
  (1694139, 7, 6),
  (1697819, 6, 7),
  (1699240, 3, 3),
  (1699732, 3, 7),
  (1703546, 1, 7),
  (1710137, 7, 7),
  (1710361, 7, 2),
  (1711077, 6, 3),
  (1712802, 1, 4),
  (1714191, 6, 3),
  (1714329, 6, 7),
  (1714785, 7, 7),
  (1726125, 4, 7),
  (1726591, 0, 3),
  (1726676, 5, 3),
  (1728896, 0, 7),
  (1733918, 1, 7),
  (1735495, 0, 7),
  (1736349, 2, 3),
  (1736953, 0, 3),
  (1737949, 4, 2),
  (1740073, 6, 4),
  (1740143, 0, 7),
  (1742989, 7, 4),
  (1744018, 2, 2),
  (1746444, 2, 3),
  (1747186, 0, 0),
  (1747336, 2, 4),
  (1750227, 4, 7),
  (1756033, 5, 7),
  (1758393, 6, 0),
  (1761177, 6, 6),
  (1765078, 2, 5),
  (1766179, 4, 2),
  (1773163, 6, 7),
  (1776463, 3, 4),
  (1777580, 2, 6),
  (1781384, 5, 7),
  (1781762, 5, 2),
  (1784276, 6, 0),
  (1785289, 0, 7),
  (1791103, 6, 7),
  (1792219, 0, 7),
  (1793123, 2, 7),
  (1793282, 5, 3),
  (1795529, 1, 4),
  (1795594, 6, 5),
  (1796111, 7, 7),
  (1801437, 6, 3),
  (1802545, 4, 6),
  (1802693, 1, 4),
  (1804163, 4, 7),
  (1804288, 0, 0),
  (1812703, 6, 2),
  (1814958, 1, 0),
  (1816390, 4, 3),
  (1818036, 4, 3),
  (1818295, 7, 2),
  (1818399, 5, 0),
  (1820300, 4, 3),
  (1824306, 1, 7),
  (1825587, 3, 7),
  (1828489, 0, 0),
  (1829856, 3, 2),
  (1833111, 4, 2),
  (1833551, 2, 3),
  (1835433, 2, 3),
  (1838783, 7, 7),
  (1842719, 6, 0),
  (1844306, 5, 2),
  (1845419, 0, 3),
  (1845611, 1, 0),
  (1846990, 4, 3),
  (1847533, 2, 5),
  (1849282, 6, 4),
  (1850145, 5, 6),
  (1850430, 6, 3),
  (1850475, 1, 0),
  (1853991, 5, 2),
  (1855623, 3, 3),
  (1858950, 3, 2),
  (1863312, 1, 0),
  (1864824, 0, 0),
  (1867666, 3, 7),
  (1867862, 0, 4),
  (1868347, 4, 7),
  (1871173, 5, 7),
  (1874451, 7, 7),
  (1878335, 0, 0),
  (1879084, 4, 7),
  (1880245, 1, 4),
  (1881964, 6, 7),
  (1882982, 2, 6),
  (1885584, 4, 6),
  (1886085, 0, 5),
  (1886283, 3, 3),
  (1892072, 4, 2),
  (1892325, 2, 3),
  (1895775, 1, 4),
  (1901555, 2, 6),
  (1902059, 2, 2),
  (1909622, 4, 3),
  (1911940, 3, 7),
  (1916424, 1, 7),
  (1916535, 0, 4),
  (1917512, 6, 0),
  (1920097, 0, 7),
  (1929314, 1, 4),
  (1937549, 5, 2),
  (1937982, 7, 6),
  (1943042, 1, 0),
  (1943366, 5, 3),
  (1945494, 2, 6),
  (1946612, 0, 0),
  (1949810, 3, 3),
  (1950838, 1, 7),
  (1952161, 7, 2),
  (1953344, 4, 7),
  (1953885, 1, 0),
  (1957749, 6, 0),
  (1967707, 3, 3),
  (1971124, 2, 4),
  (1975970, 1, 7),
  (1976423, 7, 3),
  (1977156, 1, 4),
  (1982436, 4, 2),
  (1984306, 6, 0),
  (1984850, 2, 7),
  (1988003, 4, 7),
  (1988672, 2, 6),
  (1989516, 4, 3),
  (1989530, 1, 0),
  (1991462, 4, 7),
  (1997806, 0, 7),
  (1998033, 6, 5),
  (1998967, 7, 2),
  (2000596, 4, 7),
  (2001292, 3, 5),
  (2002821, 7, 0),
  (2003682, 3, 7),
  (2007272, 6, 3),
  (2007927, 6, 7),
  (2012450, 7, 4),
  (2012544, 2, 2),
  (2015165, 2, 7),
  (2018545, 7, 4),
  (2021400, 5, 2),
  (2022936, 2, 2),
  (2028432, 4, 3),
  (2032848, 6, 7),
  (2035788, 6, 0),
  (2036354, 0, 3),
  (2038067, 5, 2),
  (2038565, 3, 4),
  (2043207, 0, 4),
  (2045347, 0, 3),
  (2046419, 2, 3),
  (2055086, 1, 0),
  (2058060, 0, 3),
  (2059852, 6, 0),
  (2062879, 6, 3),
  (2065576, 7, 5),
  (2065886, 0, 7),
  (2067091, 3, 2),
  (2075793, 1, 0),
  (2075946, 5, 3),
  (2078080, 1, 7),
  (2081357, 2, 3),
  (2081590, 1, 7),
  (2081661, 7, 7),
  (2085211, 5, 6),
  (2086354, 2, 4),
  (2087253, 3, 6),
  (2087757, 4, 2),
  (2088190, 7, 0),
  (2088301, 4, 2),
  (2089690, 6, 5),
  (2095010, 4, 3),
  (2097675, 7, 0),
  (2099086, 6, 4),
  (2103251, 0, 4),
  (2103389, 6, 7),
  (2104173, 0, 7),
  (2106675, 6, 7),
  (2106798, 4, 2),
  (2111728, 5, 3),
  (2113128, 4, 7),
  (2113240, 0, 3),
  (2114973, 6, 3),
  (2118072, 0, 0),
  (2120426, 3, 6),
  (2122267, 5, 3),
  (2122651, 1, 3),
  (2123025, 5, 2),
  (2124044, 0, 7),
  (2125329, 3, 7),
  (2127968, 2, 7),
  (2129496, 0, 4),
  (2129759, 1, 4),
  (2132324, 2, 7),
  (2137779, 7, 4),
  (2137880, 6, 4),
  (2140100, 6, 1),
  (2141227, 3, 2),
  (2141748, 6, 2),
  (2144385, 2, 3),
  (2146162, 4, 7),
  (2147633, 0, 0),
  (2149481, 4, 7),
  (2149941, 3, 2),
  (2150152, 5, 7),
  (2150648, 2, 7),
  (2151060, 0, 4),
  (2152037, 3, 3),
  (2155782, 4, 6),
  (2158763, 1, 7),
  (2159252, 5, 3),
  (2159414, 3, 7),
  (2159999, 0, 5),
  (2160802, 3, 7),
  (2162407, 2, 3),
  (2172396, 2, 3),
  (2174227, 7, 2),
  (2175995, 4, 6),
  (2178813, 2, 6),
  (2179844, 5, 3),
  (2183873, 4, 5),
  (2184631, 3, 6),
  (2186794, 5, 2),
  (2188734, 3, 3),
  (2189589, 1, 3),
  (2189664, 6, 7),
  (2192237, 1, 7),
  (2194070, 6, 6),
  (2196967, 0, 0),
  (2205705, 5, 2),
  (2208656, 1, 0),
  (2214617, 0, 0),
  (2216406, 2, 3),
  (2217664, 7, 4),
  (2220568, 7, 7),
  (2220681, 0, 6),
  (2227758, 3, 3),
  (2230058, 4, 7),
  (2230433, 6, 4),
  (2231196, 6, 0),
  (2232935, 5, 6),
  (2233373, 4, 7),
  (2233451, 4, 7),
  (2236554, 5, 3),
  (2240540, 2, 6),
  (2245458, 7, 0),
  (2249648, 0, 4),
  (2252964, 6, 6),
  (2253726, 3, 2),
  (2257082, 2, 0),
  (2258898, 2, 3),
  (2259558, 1, 7),
  (2260818, 4, 7),
  (2263742, 0, 5),
  (2265467, 6, 3),
  (2266991, 4, 1),
  (2268633, 5, 0),
  (2269125, 6, 3),
  (2272031, 4, 3),
  (2278315, 3, 7),
  (2278827, 7, 7),
  (2282421, 4, 3),
  (2282894, 4, 3),
  (2283480, 2, 3),
  (2286183, 3, 7),
  (2286688, 7, 3),
  (2286998, 2, 7),
  (2289451, 2, 7),
  (2290139, 7, 3),
  (2292956, 6, 0),
  (2304169, 3, 3),
  (2304263, 2, 5),
  (2304879, 7, 3),
  (2306938, 3, 1),
  (2308002, 7, 0),
  (2311938, 0, 3),
  (2315223, 6, 0),
  (2318587, 1, 7),
  (2321198, 3, 7),
  (2322079, 1, 0),
  (2323190, 5, 7),
  (2324118, 1, 0),
  (2324836, 1, 6),
  (2325290, 4, 7),
  (2336442, 6, 4),
  (2337894, 4, 2),
  (2339055, 0, 4),
  (2339117, 7, 6),
  (2340114, 1, 2),
  (2340551, 5, 3),
  (2341411, 5, 5),
  (2341887, 6, 7),
  (2346845, 0, 0),
  (2347495, 3, 4),
  (2348552, 4, 6),
  (2351479, 3, 7),
  (2352165, 7, 7),
  (2354982, 7, 0),
  (2356981, 3, 7),
  (2357109, 2, 2),
  (2359466, 0, 0),
  (2366046, 3, 2),
  (2366953, 4, 4),
  (2370153, 0, 7),
  (2374895, 1, 0),
  (2377535, 3, 6),
  (2377704, 6, 3),
  (2381957, 4, 3),
  (2382187, 5, 7),
  (2383220, 2, 7),
  (2383822, 6, 5),
  (2386777, 3, 2),
  (2388802, 7, 1),
  (2390978, 5, 6),
  (2392698, 1, 6),
  (2396670, 2, 5),
  (2397373, 4, 7),
  (2400199, 5, 6),
  (2401992, 5, 3),
  (2402123, 7, 3),
  (2405821, 7, 6),
  (2407038, 3, 3),
  (2407187, 0, 0),
  (2409318, 5, 7),
  (2412057, 1, 7),
  (2417871, 0, 7),
  (2422844, 5, 7),
  (2425384, 2, 3),
  (2426000, 6, 7),
  (2426910, 0, 4),
  (2427876, 5, 6),
  (2429679, 5, 3),
  (2432010, 3, 7),
  (2434153, 1, 0),
  (2434500, 6, 0),
  (2437237, 4, 3),
  (2438308, 6, 3),
  (2443504, 5, 7),
  (2445114, 4, 6),
  (2446917, 4, 1),
  (2447079, 0, 7),
  (2451048, 6, 6),
  (2453055, 4, 6),
  (2453702, 3, 2),
  (2454381, 6, 7),
  (2459165, 0, 3),
  (2459401, 5, 3),
  (2461447, 1, 7),
  (2464961, 0, 7),
  (2467760, 5, 0),
  (2468905, 3, 4),
  (2472391, 7, 0),
  (2474995, 5, 3),
  (2483923, 4, 3),
  (2495100, 4, 3),
  (2504877, 6, 0),
  (2506360, 4, 0),
  (2506977, 2, 2),
  (2507958, 1, 7),
  (2508525, 0, 7),
  (2512055, 1, 4),
  (2513849, 7, 0),
  (2516560, 4, 7),
  (2518128, 4, 5),
  (2519190, 5, 2),
  (2521979, 0, 0),
  (2524050, 3, 6),
  (2527056, 4, 7),
  (2531247, 3, 6),
  (2533071, 4, 5),
  (2534306, 6, 0),
  (2534706, 2, 7),
  (2537777, 0, 2),
  (2542400, 5, 5),
  (2549971, 2, 3),
  (2551155, 3, 3),
  (2552174, 1, 3),
  (2552902, 6, 0),
  (2555363, 5, 7),
  (2556389, 7, 7),
  (2556508, 1, 4),
  (2556828, 0, 0),
  (2557430, 6, 3),
  (2557485, 3, 0),
  (2557757, 4, 5),
  (2558568, 5, 7),
  (2558878, 4, 1),
  (2559379, 7, 2),
  (2561562, 0, 0),
  (2566019, 3, 3),
  (2567689, 1, 0),
  (2567809, 7, 7),
  (2567876, 1, 0),
  (2569039, 7, 4),
  (2571370, 6, 7),
  (2573753, 6, 7),
  (2576418, 0, 7),
  (2576857, 2, 7),
  (2578490, 3, 7),
  (2580165, 4, 2),
  (2583706, 7, 3),
  (2583749, 3, 6),
  (2585050, 0, 0),
  (2587692, 5, 2),
  (2589855, 1, 7),
  (2592532, 5, 3),
  (2594150, 1, 2),
  (2600767, 1, 6),
  (2602564, 3, 7),
  (2602937, 1, 0),
  (2603100, 7, 3),
  (2603898, 3, 7),
  (2603914, 2, 2),
  (2611614, 6, 7),
  (2611877, 7, 3),
  (2614842, 2, 7),
  (2615262, 2, 7),
  (2617106, 1, 7),
  (2617618, 1, 7),
  (2618877, 6, 3),
  (2620807, 1, 5),
  (2633038, 0, 0),
  (2633316, 1, 7),
  (2633437, 0, 2),
  (2635332, 1, 6),
  (2637001, 7, 7),
  (2638855, 1, 7),
  (2641862, 6, 4),
  (2642757, 4, 3),
  (2643627, 6, 7),
  (2652499, 3, 7),
  (2656493, 2, 3),
  (2658493, 0, 1),
  (2664841, 4, 7),
  (2667342, 1, 6),
  (2670116, 0, 5),
  (2670293, 3, 7),
  (2671036, 7, 7),
  (2672469, 0, 0),
  (2673811, 2, 3),
  (2675860, 7, 7),
  (2677917, 4, 7),
  (2678187, 2, 6),
  (2678574, 3, 6),
  (2682232, 0, 0),
  (2682332, 4, 3),
  (2684461, 5, 7),
  (2685832, 5, 6),
  (2686610, 5, 3),
  (2687740, 2, 3),
  (2690880, 5, 7),
  (2693318, 2, 6),
  (2696125, 4, 1),
  (2700442, 5, 2),
  (2704709, 0, 3),
  (2706730, 2, 7),
  (2706952, 2, 2),
  (2707154, 4, 2),
  (2708865, 0, 3),
  (2711722, 6, 3),
  (2715527, 7, 4),
  (2715854, 1, 0),
  (2720108, 7, 0),
  (2721984, 0, 4),
  (2725725, 3, 2),
  (2729573, 7, 6),
  (2731856, 5, 7),
  (2733477, 6, 4),
  (2735092, 3, 5),
  (2737443, 6, 0),
  (2738529, 0, 7),
  (2739015, 0, 3),
  (2753948, 0, 4),
  (2763562, 1, 0),
  (2765087, 2, 2),
  (2765181, 1, 7),
  (2766641, 1, 7),
  (2772378, 4, 2),
  (2774386, 7, 0),
  (2776680, 7, 7),
  (2777540, 7, 7),
  (2781924, 0, 0),
  (2783337, 2, 2),
  (2789293, 6, 0),
  (2797714, 5, 6),
  (2800722, 3, 2),
  (2802233, 3, 7),
  (2802349, 1, 7),
  (2805802, 3, 1),
  (2808119, 5, 7),
  (2808221, 1, 5),
  (2809455, 7, 7),
  (2811672, 7, 7),
  (2814059, 6, 0),
  (2814282, 1, 0),
  (2816973, 2, 7),
  (2818282, 6, 0),
  (2819970, 0, 3),
  (2822588, 2, 3),
  (2825462, 2, 3),
  (2825905, 0, 4),
  (2826589, 2, 7),
  (2831982, 6, 7),
  (2834017, 5, 3),
  (2834980, 1, 2),
  (2836924, 5, 4),
  (2839696, 5, 2),
  (2839972, 0, 3),
  (2840056, 2, 6),
  (2841290, 2, 3),
  (2844649, 7, 7),
  (2845300, 0, 7),
  (2847927, 6, 7),
  (2848796, 2, 0),
  (2849396, 1, 7),
  (2857588, 0, 7),
  (2859270, 2, 2),
  (2861069, 5, 7),
  (2862711, 7, 2),
  (2869755, 1, 0),
  (2870176, 1, 6),
  (2874125, 0, 2),
  (2875636, 6, 7),
  (2875749, 7, 4),
  (2876115, 7, 7),
  (2876406, 5, 7),
  (2876870, 0, 6),
  (2878682, 0, 4),
  (2884429, 0, 3),
  (2889317, 3, 7),
  (2890839, 1, 2),
  (2891695, 2, 7),
  (2892701, 1, 0),
  (2892781, 1, 7),
  (2893352, 1, 0),
  (2894394, 4, 5),
  (2901602, 7, 0),
  (2901835, 3, 5),
  (2907878, 4, 3),
  (2909113, 7, 0),
  (2909989, 0, 0),
  (2910108, 2, 6),
  (2913648, 2, 3),
  (2915432, 0, 4),
  (2922724, 5, 7),
  (2927792, 6, 4),
  (2933082, 3, 3),
  (2935453, 6, 7),
  (2935493, 0, 0),
  (2935731, 4, 3),
  (2936028, 6, 7),
  (2936813, 3, 7),
  (2936837, 5, 5),
  (2937793, 6, 7),
  (2942532, 7, 7),
  (2944981, 5, 7),
  (2946776, 0, 7),
  (2947068, 7, 4),
  (2947796, 5, 6),
  (2948449, 1, 0),
  (2948636, 5, 3),
  (2950929, 7, 3),
  (2951430, 4, 3),
  (2955082, 3, 2),
  (2955708, 5, 6),
  (2959919, 3, 7),
  (2960015, 1, 3),
  (2960329, 6, 0),
  (2963645, 4, 3),
  (2964675, 1, 0),
  (2966620, 7, 4),
  (2967590, 7, 4),
  (2967607, 7, 7),
  (2970001, 4, 5),
  (2970381, 7, 7),
  (2970519, 0, 0),
  (2970566, 5, 7),
  (2970818, 1, 7),
  (2972060, 0, 5),
  (2972114, 2, 7),
  (2973419, 2, 3),
  (2975600, 4, 3),
  (2984838, 0, 2),
  (2985271, 0, 0),
  (2986113, 7, 7),
  (2987161, 0, 0),
  (2999846, 4, 3),
  (3001399, 5, 6),
  (3006894, 6, 0),
  (3012373, 2, 6),
  (3012662, 5, 5),
  (3012981, 6, 3),
  (3013127, 5, 3),
  (3014497, 7, 6),
  (3014818, 6, 3),
  (3016066, 2, 7),
  (3016641, 2, 7),
  (3018061, 1, 4),
  (3019794, 1, 0),
  (3024943, 4, 3),
  (3029177, 0, 1),
  (3030058, 3, 7),
  (3030794, 6, 5),
  (3035301, 6, 4),
  (3036704, 3, 2),
  (3037226, 2, 3),
  (3037705, 3, 4),
  (3037999, 5, 2),
  (3040411, 6, 7),
  (3041018, 5, 6),
  (3042412, 1, 3),
  (3044897, 6, 4),
  (3045323, 4, 3),
  (3047276, 6, 4),
  (3050395, 6, 4),
  (3050503, 3, 7),
  (3052403, 7, 1),
  (3053432, 3, 7),
  (3054229, 5, 7),
  (3054468, 6, 7),
  (3055940, 5, 2),
  (3058379, 7, 7),
  (3058802, 5, 3),
  (3058883, 7, 0),
  (3060967, 7, 2),
  (3063359, 0, 0),
  (3065013, 3, 3),
  (3068315, 0, 4),
  (3068679, 1, 7),
  (3072069, 4, 7),
  (3074433, 7, 0),
  (3078803, 3, 6),
  (3082444, 1, 3),
  (3086321, 5, 7),
  (3089093, 2, 6),
  (3089409, 6, 7),
  (3092247, 3, 2),
  (3094562, 1, 7),
  (3098657, 6, 7),
  (3099668, 6, 4),
  (3104674, 3, 6),
  (3108976, 6, 4),
  (3109103, 7, 7),
  (3109710, 2, 0),
  (3112080, 4, 3),
  (3112396, 7, 3),
  (3112828, 7, 7),
  (3113601, 7, 6),
  (3117610, 7, 3),
  (3117727, 1, 3),
  (3119789, 5, 3),
  (3122400, 3, 7),
  (3129239, 5, 6),
  (3129297, 3, 0),
  (3131629, 2, 3),
  (3132446, 1, 7),
  (3134581, 5, 2),
  (3136829, 5, 1),
  (3137095, 2, 7),
  (3138460, 3, 6),
  (3142109, 5, 2),
  (3144424, 0, 7),
  (3144946, 4, 3),
  (3145903, 3, 2),
  (3146143, 2, 3),
  (3153493, 5, 7),
  (3156825, 6, 6),
  (3160759, 0, 4),
  (3161517, 1, 3),
  (3167654, 4, 6),
  (3168236, 3, 7),
  (3169420, 6, 3),
  (3170076, 0, 0),
  (3170526, 1, 7),
  (3180627, 4, 3),
  (3182867, 3, 7),
  (3183121, 4, 3),
  (3184271, 0, 6),
  (3186409, 1, 5),
  (3187474, 0, 6),
  (3187962, 6, 7),
  (3188759, 1, 7),
  (3189252, 6, 3),
  (3192874, 1, 0),
  (3193471, 6, 7),
  (3195176, 3, 5),
  (3196372, 4, 4),
  (3198100, 7, 0),
  (3198139, 2, 3),
  (3200371, 4, 6),
  (3201013, 6, 6),
  (3201176, 6, 3),
  (3202862, 2, 7),
  (3203511, 5, 3),
  (3206629, 4, 7),
  (3208643, 0, 2),
  (3210491, 1, 1),
  (3210911, 3, 7),
  (3212013, 0, 4),
  (3215730, 6, 7),
  (3217637, 2, 3),
  (3220496, 3, 7),
  (3221717, 5, 3),
  (3221980, 7, 3),
  (3222332, 0, 0),
  (3224171, 7, 0),
  (3228192, 4, 3),
  (3228393, 6, 7),
  (3228851, 5, 3),
  (3229000, 2, 3),
  (3229090, 1, 4),
  (3241013, 2, 4),
  (3241863, 3, 3),
  (3242544, 7, 7),
  (3244260, 5, 6),
  (3250096, 3, 7),
  (3252431, 2, 6),
  (3252624, 3, 7),
  (3257209, 4, 2),
  (3258343, 5, 3),
  (3262078, 7, 3),
  (3263695, 7, 0),
  (3265061, 7, 0),
  (3266348, 1, 3),
  (3267218, 2, 6),
  (3268702, 4, 7),
  (3272527, 2, 6),
  (3272893, 4, 3),
  (3276305, 2, 5),
  (3284015, 5, 3),
  (3286431, 1, 0),
  (3288454, 0, 7),
  (3290018, 1, 4),
  (3294494, 5, 3),
  (3294989, 0, 0),
  (3297250, 3, 3),
  (3297922, 4, 3),
  (3297934, 3, 7),
  (3305632, 5, 7),
  (3306556, 5, 7),
  (3308362, 1, 6),
  (3313540, 2, 7),
  (3313623, 2, 6),
  (3316143, 1, 7),
  (3320212, 0, 7),
  (3321225, 3, 2),
  (3322874, 1, 4),
  (3323511, 5, 4),
  (3323901, 2, 3),
  (3332430, 2, 3),
  (3333783, 1, 4),
  (3338794, 2, 7),
  (3342898, 1, 0),
  (3344042, 7, 4),
  (3348047, 3, 2),
  (3349793, 6, 7),
  (3350310, 2, 2),
  (3351203, 3, 3),
  (3356977, 0, 0),
  (3357678, 7, 0),
  (3358438, 4, 2),
  (3359253, 1, 2),
  (3365913, 5, 7),
  (3370306, 4, 7),
  (3373820, 3, 3),
  (3373910, 2, 7),
  (3375152, 7, 7),
  (3379971, 1, 3),
  (3381068, 6, 7),
  (3381894, 2, 7),
  (3382195, 6, 0),
  (3382755, 5, 2),
  (3384276, 3, 2),
  (3385844, 4, 4),
  (3389472, 1, 6),
  (3390279, 7, 7),
  (3390395, 3, 7),
  (3393298, 4, 2),
  (3394659, 3, 5),
  (3395920, 2, 2),
  (3396945, 0, 7),
  (3397362, 3, 2),
  (3397949, 6, 7),
  (3400194, 7, 5),
  (3402500, 4, 3),
  (3403039, 0, 2),
  (3403301, 4, 7),
  (3404638, 4, 5),
  (3404977, 7, 0),
  (3413050, 4, 3),
  (3413192, 1, 0),
  (3416295, 0, 6),
  (3416748, 0, 4),
  (3417001, 6, 7),
  (3419509, 7, 4),
  (3420527, 3, 0),
  (3421097, 1, 0),
  (3421512, 7, 0),
  (3426010, 1, 7),
  (3428491, 2, 3),
  (3429381, 1, 4),
  (3429705, 3, 7),
  (3430995, 4, 6),
  (3432983, 6, 3),
  (3433648, 5, 7),
  (3434054, 3, 7),
  (3441426, 2, 5),
  (3448771, 4, 7),
  (3456824, 3, 2),
  (3458268, 4, 2),
  (3461093, 5, 2),
  (3465291, 6, 0),
  (3473058, 3, 6),
  (3473154, 0, 4),
  (3475047, 0, 7),
  (3479898, 4, 7),
  (3481086, 4, 3),
  (3481621, 6, 6),
  (3483588, 3, 6),
  (3486802, 6, 6),
  (3489610, 7, 4),
  (3492508, 6, 0),
  (3499097, 2, 2),
  (3501005, 0, 0),
  (3505496, 2, 2),
  (3506783, 0, 7),
  (3510677, 4, 2),
  (3511957, 7, 2),
  (3512121, 3, 7),
  (3513656, 3, 3),
  (3516370, 7, 3),
  (3524041, 4, 2),
  (3525454, 6, 7),
  (3529623, 4, 7),
  (3531818, 6, 0),
  (3531820, 5, 7),
  (3536730, 2, 2),
  (3539247, 6, 4),
  (3544052, 1, 6),
  (3550414, 4, 3),
  (3556997, 1, 3),
  (3560103, 7, 0),
  (3572590, 0, 0),
  (3572627, 3, 3),
  (3575586, 0, 7),
  (3584080, 2, 2),
  (3584698, 2, 5),
  (3584758, 4, 7),
  (3586386, 4, 2),
  (3586716, 2, 7),
  (3588004, 5, 3),
  (3589755, 1, 5),
  (3590106, 3, 3),
  (3590597, 3, 3),
  (3590730, 0, 4),
  (3596456, 0, 4),
  (3598508, 4, 3),
  (3598568, 2, 7),
])
