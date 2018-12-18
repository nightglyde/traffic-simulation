from src.util import *
schedule = deque([
  (3761, 0, 1),
  (3973, 3, 2),
  (4460, 1, 2),
  (5691, 3, 0),
  (10446, 3, 2),
  (11203, 2, 1),
  (11728, 1, 0),
  (12426, 3, 0),
  (12831, 2, 2),
  (12920, 3, 0),
  (13257, 2, 1),
  (13697, 1, 1),
  (14225, 3, 2),
  (14258, 1, 2),
  (15733, 0, 2),
  (17889, 1, 2),
  (19694, 3, 2),
  (23139, 3, 2),
  (27831, 1, 0),
  (28261, 1, 2),
  (28392, 2, 1),
  (29781, 0, 1),
  (32037, 2, 1),
  (32092, 3, 2),
  (34548, 0, 1),
  (34725, 3, 2),
  (34794, 3, 1),
  (36889, 2, 2),
  (38123, 3, 2),
  (40699, 3, 2),
  (40738, 3, 0),
  (43764, 2, 0),
  (43963, 0, 0),
  (44895, 0, 0),
  (47628, 2, 1),
  (48648, 1, 1),
  (49417, 0, 2),
  (50149, 3, 1),
  (52297, 3, 0),
  (54245, 3, 1),
  (54614, 2, 2),
  (55462, 0, 0),
  (58842, 0, 1),
  (60599, 1, 0),
  (60643, 3, 0),
  (60991, 2, 2),
  (61008, 1, 1),
  (61726, 3, 0),
  (62755, 3, 2),
  (63412, 0, 1),
  (64598, 3, 2),
  (66834, 0, 0),
  (71449, 1, 0),
  (72216, 3, 0),
  (72669, 0, 1),
  (72885, 2, 2),
  (75419, 3, 2),
  (75798, 0, 2),
  (77531, 2, 2),
  (79292, 0, 0),
  (83148, 1, 2),
  (84701, 0, 0),
  (85543, 2, 2),
  (86436, 3, 2),
  (87459, 1, 1),
  (89836, 1, 0),
  (90962, 2, 2),
  (91788, 3, 0),
  (92738, 1, 2),
  (93808, 1, 2),
  (97035, 3, 0),
  (101389, 3, 0),
  (103818, 2, 2),
  (106058, 2, 2),
  (107457, 1, 2),
  (107689, 3, 2),
  (110412, 2, 2),
  (110771, 1, 0),
  (110792, 1, 2),
  (111162, 2, 0),
  (111217, 3, 1),
  (111373, 0, 0),
  (115450, 1, 1),
  (118940, 0, 1),
  (119004, 2, 1),
  (121911, 3, 1),
  (122339, 2, 1),
  (125482, 1, 0),
  (126331, 1, 1),
  (126360, 2, 0),
  (126975, 3, 2),
  (129706, 0, 2),
  (131046, 3, 0),
  (131666, 1, 0),
  (132605, 3, 2),
  (133299, 0, 2),
  (137411, 2, 0),
  (137497, 3, 2),
  (138443, 0, 0),
  (139784, 1, 0),
  (145906, 1, 1),
  (146072, 1, 1),
  (146812, 1, 0),
  (147453, 2, 1),
  (149254, 2, 2),
  (153880, 3, 2),
  (154947, 2, 2),
  (157157, 3, 2),
  (159176, 2, 1),
  (159611, 2, 0),
  (162004, 2, 0),
  (162528, 1, 1),
  (163208, 0, 1),
  (164394, 3, 2),
  (165442, 3, 1),
  (168413, 0, 1),
  (177333, 1, 1),
  (190155, 1, 2),
  (190423, 3, 1),
  (191028, 0, 2),
  (193581, 1, 2),
  (194246, 0, 2),
  (195504, 2, 0),
  (197819, 0, 2),
  (200793, 0, 2),
  (200971, 0, 2),
  (201583, 1, 2),
  (206258, 2, 1),
  (209653, 3, 2),
  (214178, 3, 2),
  (215694, 1, 0),
  (216727, 3, 1),
  (217441, 3, 0),
  (217607, 1, 2),
  (217903, 3, 0),
  (218502, 1, 1),
  (219750, 0, 0),
  (220043, 1, 0),
  (220181, 1, 1),
  (223886, 3, 2),
  (224665, 2, 2),
  (229411, 3, 1),
  (232688, 1, 0),
  (234535, 0, 2),
  (237197, 3, 2),
  (238084, 1, 2),
  (239206, 3, 0),
  (246339, 3, 2),
  (246678, 2, 2),
  (247002, 2, 1),
  (249563, 3, 2),
  (252152, 2, 0),
  (252242, 2, 1),
  (252998, 2, 2),
  (255289, 0, 1),
  (258812, 1, 1),
  (259398, 1, 0),
  (260850, 0, 0),
  (262609, 0, 1),
  (264924, 3, 2),
  (266895, 3, 2),
  (267319, 3, 0),
  (270720, 0, 0),
  (271690, 1, 2),
  (272630, 0, 2),
  (273020, 1, 2),
  (279740, 3, 1),
  (281072, 3, 1),
  (281477, 2, 2),
  (282044, 2, 0),
  (288408, 2, 2),
  (289238, 3, 2),
  (291336, 2, 0),
  (293731, 0, 0),
  (293776, 0, 1),
  (294287, 0, 0),
  (300330, 1, 1),
  (301443, 2, 0),
  (302837, 2, 0),
  (304153, 3, 2),
  (304726, 0, 1),
  (307130, 2, 0),
  (308701, 2, 0),
  (309670, 2, 1),
  (309685, 1, 1),
  (310644, 3, 2),
  (311019, 0, 1),
  (316864, 0, 2),
  (318779, 0, 0),
  (318979, 3, 2),
  (319464, 1, 0),
  (320271, 1, 2),
  (321249, 3, 0),
  (323260, 2, 1),
  (323540, 0, 1),
  (323722, 0, 2),
  (324265, 1, 2),
  (324742, 0, 0),
  (325556, 2, 0),
  (325722, 2, 1),
  (328483, 2, 1),
  (329891, 3, 0),
  (331673, 3, 0),
  (332862, 0, 0),
  (333007, 0, 0),
  (333918, 0, 1),
  (334839, 0, 0),
  (336231, 2, 1),
  (338778, 1, 2),
  (340721, 2, 2),
  (342349, 3, 2),
  (342363, 2, 1),
  (344276, 0, 1),
  (346132, 1, 0),
  (346920, 1, 0),
  (348512, 2, 0),
  (349358, 3, 0),
  (349415, 2, 1),
  (351377, 2, 0),
  (351479, 0, 2),
  (353346, 3, 1),
  (354909, 1, 1),
  (356074, 0, 2),
  (358847, 3, 0),
  (358967, 3, 0),
  (359017, 0, 0),
  (364605, 0, 1),
  (366838, 3, 2),
  (367267, 0, 2),
  (368564, 2, 2),
  (375806, 0, 2),
  (379788, 1, 0),
  (381306, 0, 2),
  (383353, 1, 0),
  (387179, 2, 2),
  (387833, 2, 0),
  (389974, 2, 2),
  (390514, 2, 1),
  (391863, 3, 2),
  (392952, 3, 0),
  (393574, 2, 0),
  (394007, 2, 1),
  (394096, 2, 0),
  (398864, 1, 2),
  (401607, 3, 2),
  (407143, 3, 0),
  (409546, 1, 0),
  (409849, 3, 1),
  (411797, 1, 2),
  (411946, 1, 2),
  (412372, 2, 1),
  (413106, 1, 2),
  (413659, 1, 1),
  (414565, 0, 0),
  (418101, 1, 2),
  (420183, 1, 1),
  (420798, 2, 0),
  (424173, 3, 1),
  (426054, 0, 2),
  (426195, 0, 2),
  (435446, 1, 2),
  (438242, 2, 0),
  (441644, 1, 0),
  (443892, 2, 0),
  (445135, 2, 0),
  (445454, 0, 2),
  (446995, 1, 1),
  (452127, 0, 2),
  (457492, 1, 2),
  (461817, 1, 2),
  (461982, 3, 2),
  (464332, 0, 2),
  (464577, 3, 2),
  (465046, 2, 2),
  (465839, 3, 0),
  (466039, 3, 2),
  (467858, 0, 0),
  (470926, 3, 2),
  (471212, 0, 2),
  (471772, 0, 1),
  (473512, 2, 0),
  (474577, 0, 2),
  (481263, 3, 1),
  (481870, 3, 1),
  (484500, 3, 2),
  (486168, 0, 0),
  (487509, 3, 0),
  (490528, 0, 0),
  (497301, 2, 0),
  (497996, 1, 2),
  (499766, 0, 2),
  (500413, 1, 2),
  (501403, 2, 1),
  (508172, 1, 2),
  (509987, 3, 0),
  (512692, 2, 1),
  (514459, 2, 1),
  (514570, 1, 1),
  (514786, 2, 1),
  (515185, 0, 0),
  (521146, 0, 0),
  (525184, 1, 2),
  (527332, 2, 0),
  (527787, 3, 0),
  (533337, 1, 1),
  (538642, 1, 1),
  (543160, 0, 1),
  (545078, 3, 0),
  (548238, 3, 1),
  (552181, 1, 1),
  (552300, 3, 1),
  (554706, 3, 1),
  (555150, 3, 2),
  (556587, 1, 1),
  (557820, 2, 2),
  (561395, 1, 1),
  (561657, 1, 2),
  (561912, 3, 0),
  (567729, 2, 1),
  (568131, 3, 2),
  (568658, 0, 1),
  (570547, 2, 0),
  (571132, 2, 0),
  (571825, 1, 1),
  (572472, 3, 0),
  (572529, 3, 1),
  (572926, 2, 0),
  (577724, 0, 2),
  (579782, 3, 1),
  (580796, 0, 0),
  (581102, 2, 2),
  (583687, 0, 2),
  (585712, 3, 2),
  (590218, 2, 2),
  (591317, 0, 1),
  (599240, 3, 0),
  (604365, 1, 0),
  (606701, 1, 2),
  (611235, 1, 1),
  (612781, 1, 1),
  (612821, 0, 1),
  (614338, 1, 1),
  (616059, 1, 2),
  (618487, 0, 1),
  (618916, 3, 2),
  (620483, 2, 2),
  (622623, 2, 1),
  (626127, 1, 1),
  (627699, 1, 1),
  (627731, 1, 2),
  (629101, 3, 0),
  (629207, 3, 1),
  (637040, 0, 0),
  (643478, 0, 0),
  (648713, 3, 0),
  (651319, 1, 2),
  (655411, 1, 1),
  (656307, 1, 0),
  (660023, 1, 2),
  (662828, 2, 1),
  (665389, 0, 1),
  (670106, 3, 1),
  (672156, 3, 0),
  (673795, 3, 1),
  (675280, 3, 0),
  (676703, 1, 2),
  (683842, 1, 1),
  (684397, 3, 2),
  (684776, 3, 1),
  (686830, 2, 2),
  (687326, 1, 1),
  (689657, 0, 2),
  (691244, 3, 0),
  (695623, 1, 2),
  (697484, 3, 2),
  (698709, 2, 1),
  (705056, 0, 1),
  (709522, 1, 2),
  (713429, 2, 1),
  (714384, 2, 1),
  (717151, 0, 2),
  (718003, 3, 0),
  (720672, 1, 2),
  (720998, 3, 0),
  (724518, 3, 0),
  (725186, 3, 0),
  (725799, 0, 2),
  (727690, 2, 1),
  (730462, 1, 0),
  (732688, 1, 1),
  (733468, 2, 1),
  (741605, 0, 0),
  (741914, 0, 0),
  (741987, 2, 1),
  (745736, 2, 0),
  (745832, 2, 1),
  (749021, 3, 2),
  (752939, 1, 0),
  (755073, 0, 1),
  (758592, 1, 2),
  (759148, 2, 0),
  (759746, 1, 2),
  (766466, 2, 1),
  (767974, 3, 2),
  (768820, 0, 2),
  (768935, 1, 0),
  (769619, 0, 1),
  (770090, 0, 0),
  (770820, 1, 0),
  (771616, 0, 1),
  (773034, 0, 1),
  (773846, 1, 0),
  (774352, 2, 1),
  (778945, 1, 0),
  (779350, 2, 2),
  (781695, 1, 2),
  (784077, 1, 0),
  (785945, 1, 0),
  (787155, 2, 2),
  (788127, 3, 2),
  (789030, 0, 1),
  (792102, 2, 1),
  (793578, 2, 0),
  (795186, 1, 1),
  (797038, 1, 2),
  (797365, 0, 2),
  (800579, 3, 1),
  (802780, 2, 2),
  (804210, 0, 0),
  (804810, 0, 0),
  (805644, 1, 0),
  (806541, 2, 0),
  (806708, 2, 0),
  (809162, 1, 1),
  (811108, 1, 2),
  (812746, 3, 1),
  (814717, 1, 2),
  (815900, 2, 0),
  (819152, 1, 1),
  (819980, 3, 1),
  (822283, 2, 2),
  (825559, 2, 0),
  (826567, 3, 2),
  (827113, 1, 0),
  (828436, 1, 0),
  (831212, 2, 2),
  (831552, 1, 0),
  (834598, 3, 2),
  (835878, 2, 2),
  (836201, 1, 1),
  (837356, 2, 2),
  (838411, 2, 2),
  (840607, 0, 0),
  (842069, 1, 0),
  (842198, 2, 2),
  (843750, 3, 0),
  (843771, 0, 0),
  (846650, 0, 0),
  (847415, 3, 1),
  (847608, 1, 1),
  (851004, 1, 1),
  (851913, 1, 0),
  (852224, 3, 2),
  (853672, 1, 2),
  (856085, 2, 0),
  (857486, 2, 0),
  (859782, 0, 1),
  (861043, 3, 0),
  (862022, 3, 0),
  (866722, 2, 2),
  (868460, 2, 0),
  (868496, 1, 1),
  (871351, 2, 1),
  (871370, 2, 2),
  (871416, 0, 2),
  (871418, 3, 2),
  (872311, 0, 2),
  (876646, 0, 0),
  (877747, 0, 2),
  (879667, 0, 2),
  (885916, 3, 2),
  (887717, 0, 2),
  (887779, 1, 0),
  (888358, 2, 2),
  (889262, 2, 0),
  (890099, 1, 1),
  (898811, 3, 0),
  (901454, 2, 0),
  (904227, 1, 0),
  (904356, 3, 2),
  (904859, 0, 0),
  (907959, 1, 0),
  (910262, 0, 2),
  (911291, 1, 2),
  (912451, 2, 0),
  (913939, 2, 1),
  (914502, 1, 2),
  (918605, 3, 2),
  (919416, 2, 1),
  (920308, 2, 1),
  (921422, 2, 0),
  (921477, 3, 2),
  (922801, 0, 2),
  (923421, 0, 1),
  (924445, 2, 0),
  (925214, 1, 2),
  (925242, 1, 2),
  (927104, 3, 2),
  (928637, 3, 0),
  (933617, 2, 1),
  (937324, 1, 2),
  (937544, 3, 0),
  (939695, 3, 1),
  (942140, 1, 1),
  (943843, 3, 2),
  (944414, 1, 2),
  (944625, 3, 1),
  (945925, 1, 2),
  (949710, 1, 2),
  (954745, 1, 1),
  (956957, 1, 0),
  (958084, 0, 1),
  (963579, 2, 2),
  (967498, 3, 1),
  (968115, 3, 0),
  (968165, 2, 0),
  (973010, 0, 2),
  (974282, 1, 2),
  (975653, 0, 0),
  (976353, 3, 2),
  (977570, 2, 1),
  (978939, 2, 0),
  (979825, 0, 1),
  (979877, 0, 2),
  (981148, 0, 1),
  (981590, 0, 0),
  (983288, 2, 2),
  (986835, 0, 2),
  (987817, 2, 2),
  (991361, 2, 0),
  (997980, 2, 1),
  (998766, 1, 1),
  (999598, 3, 2),
  (1001498, 2, 0),
  (1004457, 0, 0),
  (1004932, 3, 0),
  (1007089, 1, 2),
  (1007237, 1, 1),
  (1009244, 3, 1),
  (1009293, 1, 1),
  (1011429, 0, 0),
  (1014048, 1, 0),
  (1014987, 3, 1),
  (1016759, 0, 1),
  (1020999, 2, 0),
  (1022025, 1, 0),
  (1022419, 0, 1),
  (1024005, 2, 2),
  (1032436, 0, 0),
  (1033957, 0, 2),
  (1036230, 0, 1),
  (1036864, 3, 1),
  (1041985, 1, 1),
  (1045494, 3, 0),
  (1046687, 0, 1),
  (1047173, 1, 0),
  (1047627, 3, 1),
  (1048473, 1, 2),
  (1048488, 0, 0),
  (1049866, 0, 1),
  (1053710, 1, 2),
  (1054378, 2, 2),
  (1055539, 0, 0),
  (1057516, 0, 2),
  (1058242, 2, 2),
  (1058532, 2, 1),
  (1062310, 0, 2),
  (1064618, 2, 2),
  (1068096, 0, 2),
  (1068588, 2, 2),
  (1069534, 2, 1),
  (1069871, 2, 2),
  (1071165, 1, 0),
  (1072793, 1, 1),
  (1079083, 0, 2),
  (1079244, 3, 0),
  (1079328, 3, 2),
  (1081309, 3, 2),
  (1082609, 2, 0),
  (1084344, 0, 2),
  (1086222, 2, 0),
  (1086787, 0, 0),
  (1090371, 2, 2),
  (1092046, 2, 2),
  (1093939, 3, 0),
  (1094294, 1, 1),
  (1095121, 3, 0),
  (1095694, 3, 1),
  (1097412, 2, 1),
  (1097842, 3, 2),
  (1098037, 0, 0),
  (1098994, 2, 2),
  (1099241, 3, 0),
  (1099795, 0, 0),
  (1105254, 0, 1),
  (1106819, 2, 1),
  (1106962, 2, 2),
  (1107950, 3, 2),
  (1108117, 1, 1),
  (1109683, 2, 0),
  (1110577, 1, 2),
  (1112998, 0, 0),
  (1119856, 0, 0),
  (1121175, 2, 2),
  (1128780, 2, 2),
  (1130319, 1, 2),
  (1133693, 1, 0),
  (1135856, 2, 0),
  (1139236, 1, 1),
  (1142897, 0, 2),
  (1144733, 3, 1),
  (1145272, 0, 1),
  (1145460, 0, 0),
  (1146061, 3, 2),
  (1147386, 3, 0),
  (1148018, 0, 2),
  (1153277, 3, 1),
  (1153740, 3, 0),
  (1153967, 2, 1),
  (1155431, 0, 1),
  (1156530, 3, 1),
  (1157963, 3, 2),
  (1158329, 1, 1),
  (1168867, 1, 1),
  (1169056, 3, 2),
  (1172632, 1, 2),
  (1173388, 1, 2),
  (1174034, 3, 0),
  (1174851, 0, 1),
  (1175044, 2, 2),
  (1176331, 0, 0),
  (1176349, 1, 0),
  (1176479, 3, 2),
  (1178002, 0, 2),
  (1180176, 2, 1),
  (1181640, 3, 1),
  (1182134, 1, 1),
  (1183882, 3, 2),
  (1185030, 2, 0),
  (1186226, 0, 2),
  (1186657, 0, 2),
  (1187230, 2, 2),
  (1192706, 0, 0),
  (1197385, 0, 2),
  (1201518, 3, 2),
  (1201666, 3, 2),
  (1202369, 1, 2),
  (1205279, 2, 2),
  (1205372, 3, 0),
  (1205775, 0, 0),
  (1211142, 2, 2),
  (1212384, 1, 1),
  (1214088, 2, 1),
  (1217305, 0, 2),
  (1217502, 1, 1),
  (1217508, 2, 2),
  (1218437, 2, 1),
  (1219966, 1, 0),
  (1222262, 1, 0),
  (1223820, 2, 1),
  (1226019, 0, 2),
  (1226708, 2, 0),
  (1228210, 3, 0),
  (1229488, 2, 0),
  (1231331, 2, 2),
  (1235274, 0, 0),
  (1237226, 3, 2),
  (1241329, 3, 1),
  (1242060, 0, 0),
  (1243506, 1, 1),
  (1244773, 0, 1),
  (1246266, 1, 0),
  (1255104, 2, 2),
  (1256232, 1, 2),
  (1256503, 1, 2),
  (1258790, 2, 0),
  (1261356, 3, 2),
  (1262404, 1, 0),
  (1263908, 1, 1),
  (1266000, 3, 0),
  (1266936, 1, 0),
  (1269692, 2, 0),
  (1270270, 3, 1),
  (1271884, 1, 1),
  (1272146, 0, 1),
  (1272155, 2, 0),
  (1277083, 0, 1),
  (1278043, 2, 2),
  (1280117, 3, 2),
  (1280353, 2, 1),
  (1283341, 1, 0),
  (1285121, 3, 1),
  (1286885, 3, 1),
  (1296540, 3, 2),
  (1298322, 2, 2),
  (1299170, 3, 2),
  (1304232, 3, 1),
  (1314580, 3, 2),
  (1315766, 0, 2),
  (1320660, 0, 1),
  (1321326, 1, 0),
  (1322856, 3, 1),
  (1323886, 2, 2),
  (1323923, 3, 1),
  (1327171, 2, 0),
  (1328746, 2, 0),
  (1328999, 0, 1),
  (1330936, 3, 2),
  (1331101, 2, 2),
  (1335807, 2, 1),
  (1340767, 1, 0),
  (1342310, 2, 2),
  (1342696, 3, 1),
  (1344680, 2, 0),
  (1345535, 2, 0),
  (1345908, 3, 0),
  (1348892, 0, 0),
  (1350007, 2, 2),
  (1353101, 0, 0),
  (1355305, 2, 1),
  (1358553, 3, 2),
  (1370462, 1, 1),
  (1371826, 1, 0),
  (1379298, 1, 1),
  (1379975, 0, 0),
  (1385618, 2, 1),
  (1387246, 1, 0),
  (1387859, 3, 0),
  (1390258, 3, 2),
  (1391120, 0, 2),
  (1391132, 1, 2),
  (1391500, 2, 0),
  (1393242, 0, 2),
  (1393649, 3, 0),
  (1399606, 0, 0),
  (1400532, 0, 0),
  (1402765, 2, 2),
  (1404375, 2, 0),
  (1406741, 0, 2),
  (1407145, 2, 2),
  (1409395, 2, 1),
  (1411773, 0, 1),
  (1416923, 3, 2),
  (1418321, 2, 0),
  (1419017, 3, 0),
  (1419335, 1, 0),
  (1419382, 2, 1),
  (1420780, 1, 1),
  (1424166, 2, 1),
  (1425836, 1, 0),
  (1428618, 2, 2),
  (1428893, 2, 0),
  (1430150, 2, 2),
  (1431654, 1, 0),
  (1432147, 3, 2),
  (1433482, 1, 2),
  (1433566, 2, 1),
  (1433922, 1, 1),
  (1436669, 1, 1),
  (1437930, 2, 0),
  (1437935, 2, 2),
  (1439616, 1, 2),
  (1443380, 2, 1),
  (1444055, 1, 1),
  (1444258, 1, 1),
  (1444569, 1, 1),
  (1446566, 3, 0),
  (1448600, 3, 2),
  (1449433, 1, 1),
  (1450100, 0, 1),
  (1451506, 3, 2),
  (1453168, 0, 2),
  (1453216, 2, 1),
  (1454713, 1, 2),
  (1458413, 3, 2),
  (1459524, 3, 1),
  (1464016, 3, 2),
  (1465367, 0, 2),
  (1465551, 3, 2),
  (1466070, 1, 2),
  (1467037, 3, 0),
  (1469145, 2, 0),
  (1470397, 3, 2),
  (1477660, 0, 1),
  (1478901, 3, 1),
  (1479196, 1, 0),
  (1482532, 1, 0),
  (1483566, 1, 0),
  (1484587, 3, 0),
  (1484638, 0, 0),
  (1484734, 3, 0),
  (1485010, 2, 0),
  (1488411, 3, 1),
  (1489286, 3, 0),
  (1489458, 3, 1),
  (1489518, 0, 1),
  (1493001, 1, 0),
  (1495378, 0, 2),
  (1497308, 0, 0),
  (1497432, 1, 1),
  (1499061, 0, 1),
  (1500382, 1, 1),
  (1503391, 2, 0),
  (1503729, 0, 0),
  (1504997, 0, 1),
  (1507421, 1, 2),
  (1507904, 0, 1),
  (1508035, 3, 0),
  (1516963, 1, 2),
  (1517987, 1, 0),
  (1520040, 0, 0),
  (1522725, 1, 1),
  (1523583, 1, 0),
  (1523699, 3, 0),
  (1525581, 2, 0),
  (1528099, 3, 1),
  (1529299, 1, 1),
  (1531083, 2, 2),
  (1532881, 3, 2),
  (1536874, 2, 2),
  (1544961, 2, 0),
  (1545579, 1, 2),
  (1548116, 2, 0),
  (1548730, 1, 0),
  (1549759, 3, 0),
  (1551145, 3, 1),
  (1552943, 0, 2),
  (1554603, 2, 1),
  (1554831, 0, 2),
  (1558936, 0, 1),
  (1563177, 3, 2),
  (1563668, 1, 0),
  (1566996, 2, 2),
  (1570856, 1, 2),
  (1571522, 1, 1),
  (1575064, 3, 0),
  (1575672, 1, 2),
  (1575700, 1, 1),
  (1577391, 0, 2),
  (1582317, 0, 1),
  (1583504, 0, 2),
  (1583628, 3, 1),
  (1585578, 2, 1),
  (1586858, 1, 2),
  (1588322, 2, 1),
  (1588942, 1, 0),
  (1591758, 3, 1),
  (1592871, 1, 2),
  (1595259, 0, 0),
  (1598379, 1, 2),
  (1600661, 1, 0),
  (1607494, 0, 1),
  (1609781, 3, 2),
  (1612628, 0, 1),
  (1613410, 1, 0),
  (1613557, 3, 2),
  (1614384, 3, 1),
  (1617042, 1, 2),
  (1618240, 2, 0),
  (1621284, 1, 0),
  (1629100, 2, 0),
  (1631027, 3, 2),
  (1631863, 0, 1),
  (1635925, 2, 2),
  (1640309, 1, 2),
  (1643268, 1, 1),
  (1644559, 0, 2),
  (1646470, 0, 1),
  (1647004, 0, 1),
  (1648059, 2, 2),
  (1649810, 0, 0),
  (1657779, 3, 2),
  (1665171, 3, 2),
  (1666220, 2, 0),
  (1667239, 3, 2),
  (1667689, 1, 2),
  (1669034, 0, 2),
  (1672155, 3, 0),
  (1672414, 3, 1),
  (1675029, 2, 1),
  (1675852, 2, 1),
  (1678363, 1, 0),
  (1678973, 2, 2),
  (1680497, 1, 1),
  (1682160, 2, 2),
  (1682485, 2, 1),
  (1685650, 0, 2),
  (1686773, 3, 0),
  (1687644, 2, 1),
  (1691714, 3, 0),
  (1693162, 3, 0),
  (1694048, 3, 1),
  (1694602, 3, 2),
  (1697672, 2, 2),
  (1697876, 2, 0),
  (1700335, 1, 1),
  (1703181, 2, 2),
  (1703463, 0, 1),
  (1711576, 3, 1),
  (1713390, 3, 1),
  (1716670, 2, 1),
  (1721514, 1, 2),
  (1721917, 3, 1),
  (1723786, 0, 1),
  (1724868, 3, 2),
  (1727953, 2, 2),
  (1728976, 1, 0),
  (1729141, 1, 0),
  (1731413, 0, 2),
  (1731830, 1, 2),
  (1737802, 2, 1),
  (1739189, 1, 1),
  (1741778, 1, 2),
  (1744416, 3, 1),
  (1745202, 0, 1),
  (1746367, 2, 1),
  (1751378, 0, 1),
  (1755392, 0, 0),
  (1758191, 1, 1),
  (1758243, 1, 2),
  (1760136, 1, 1),
  (1762688, 1, 2),
  (1764431, 2, 1),
  (1765115, 1, 2),
  (1769086, 3, 2),
  (1769122, 3, 2),
  (1771337, 0, 2),
  (1775501, 0, 2),
  (1776727, 3, 0),
  (1778535, 1, 2),
  (1781239, 0, 1),
  (1783863, 3, 2),
  (1786110, 3, 0),
  (1786499, 0, 2),
  (1786833, 1, 2),
  (1786874, 1, 2),
  (1794223, 3, 2),
  (1795218, 3, 0),
  (1798831, 3, 2),
  (1800913, 3, 1),
  (1802267, 1, 2),
  (1803361, 2, 1),
  (1804214, 0, 0),
  (1804285, 0, 0),
  (1804594, 1, 1),
  (1805535, 2, 2),
  (1811012, 2, 1),
  (1816296, 1, 0),
  (1817221, 1, 0),
  (1818597, 2, 1),
  (1821822, 2, 2),
  (1822319, 2, 2),
  (1823346, 3, 0),
  (1824391, 3, 0),
  (1830038, 2, 2),
  (1830492, 1, 2),
  (1832013, 0, 0),
  (1837610, 3, 2),
  (1838349, 3, 1),
  (1839261, 3, 2),
  (1840328, 3, 2),
  (1845201, 0, 1),
  (1845340, 3, 0),
  (1849012, 0, 2),
  (1849341, 3, 0),
  (1849421, 2, 0),
  (1850330, 1, 0),
  (1850416, 0, 0),
  (1850594, 1, 0),
  (1854408, 2, 1),
  (1857426, 2, 2),
  (1862662, 2, 1),
  (1862972, 3, 2),
  (1866860, 3, 1),
  (1869614, 3, 2),
  (1878202, 2, 1),
  (1880067, 3, 0),
  (1881232, 3, 0),
  (1882637, 3, 1),
  (1886253, 1, 2),
  (1886468, 2, 0),
  (1887685, 2, 0),
  (1888344, 3, 0),
  (1889480, 0, 2),
  (1893247, 0, 2),
  (1893572, 0, 0),
  (1894210, 3, 0),
  (1899303, 0, 1),
  (1899912, 0, 2),
  (1901934, 2, 0),
  (1902198, 1, 1),
  (1905366, 2, 2),
  (1908614, 2, 0),
  (1912448, 0, 1),
  (1917212, 3, 0),
  (1917493, 2, 1),
  (1918296, 0, 1),
  (1922685, 3, 1),
  (1924264, 0, 1),
  (1930685, 1, 2),
  (1934462, 0, 0),
  (1934735, 3, 1),
  (1935348, 0, 2),
  (1937712, 0, 2),
  (1939447, 1, 2),
  (1940224, 3, 2),
  (1942181, 0, 2),
  (1942758, 2, 0),
  (1944505, 3, 1),
  (1945068, 0, 0),
  (1947308, 2, 1),
  (1950316, 3, 1),
  (1950654, 1, 2),
  (1955119, 2, 1),
  (1958859, 0, 2),
  (1966076, 2, 0),
  (1969108, 3, 1),
  (1972267, 0, 0),
  (1974600, 0, 2),
  (1977041, 1, 0),
  (1979944, 1, 1),
  (1981536, 2, 2),
  (1986734, 0, 2),
  (1987934, 2, 1),
  (1988825, 1, 1),
  (1990506, 2, 2),
  (1993356, 0, 0),
  (1994685, 0, 0),
  (1996015, 1, 1),
  (1996716, 2, 0),
  (1998445, 2, 2),
  (2001855, 1, 0),
  (2002370, 3, 2),
  (2004343, 1, 0),
  (2010199, 1, 1),
  (2011499, 3, 2),
  (2012145, 1, 0),
  (2014817, 3, 2),
  (2027377, 0, 2),
  (2028964, 1, 2),
  (2031004, 2, 2),
  (2032608, 2, 0),
  (2036065, 1, 1),
  (2040530, 1, 0),
  (2042848, 1, 1),
  (2043377, 1, 2),
  (2044907, 2, 2),
  (2045085, 1, 1),
  (2049662, 2, 0),
  (2055753, 2, 1),
  (2056765, 2, 2),
  (2060283, 1, 0),
  (2061791, 0, 0),
  (2062305, 0, 1),
  (2066979, 3, 0),
  (2067327, 1, 0),
  (2069439, 0, 0),
  (2073947, 2, 2),
  (2074218, 3, 1),
  (2074884, 3, 2),
  (2077151, 0, 1),
  (2084019, 3, 1),
  (2091543, 2, 0),
  (2094508, 3, 2),
  (2095716, 0, 2),
  (2096035, 2, 1),
  (2098815, 3, 0),
  (2100385, 2, 2),
  (2101159, 3, 0),
  (2104455, 1, 0),
  (2104768, 3, 0),
  (2106497, 3, 2),
  (2107290, 1, 0),
  (2109231, 2, 2),
  (2109993, 3, 0),
  (2111695, 1, 0),
  (2112703, 1, 1),
  (2117495, 1, 2),
  (2122949, 1, 2),
  (2123594, 1, 0),
  (2127123, 2, 2),
  (2127278, 1, 2),
  (2131295, 1, 2),
  (2133322, 3, 1),
  (2135259, 2, 1),
  (2135539, 2, 0),
  (2137199, 0, 2),
  (2137736, 2, 0),
  (2140970, 2, 2),
  (2143478, 3, 0),
  (2145577, 0, 0),
  (2146928, 1, 1),
  (2147254, 0, 1),
  (2148496, 0, 1),
  (2148656, 1, 0),
  (2150423, 0, 2),
  (2152396, 0, 0),
  (2154162, 1, 2),
  (2161038, 2, 2),
  (2162851, 0, 1),
  (2163032, 0, 2),
  (2164857, 0, 2),
  (2167245, 1, 1),
  (2169374, 2, 2),
  (2170765, 2, 1),
  (2171057, 0, 0),
  (2172134, 1, 2),
  (2172774, 1, 1),
  (2174868, 3, 0),
  (2175365, 3, 1),
  (2184514, 0, 2),
  (2185076, 2, 0),
  (2186323, 0, 0),
  (2189296, 1, 2),
  (2195767, 0, 0),
  (2198841, 1, 1),
  (2200963, 3, 2),
  (2201616, 0, 2),
  (2202168, 3, 0),
  (2202613, 3, 0),
  (2202948, 1, 1),
  (2206225, 3, 1),
  (2206427, 2, 0),
  (2209296, 3, 2),
  (2211221, 0, 1),
  (2216535, 0, 0),
  (2218118, 1, 0),
  (2218828, 3, 2),
  (2220728, 1, 0),
  (2221983, 1, 0),
  (2222406, 2, 1),
  (2234943, 1, 0),
  (2239744, 0, 2),
  (2245276, 3, 2),
  (2246032, 0, 2),
  (2246516, 3, 1),
  (2247396, 3, 1),
  (2248017, 0, 1),
  (2249423, 3, 2),
  (2250138, 3, 1),
  (2254605, 3, 1),
  (2255513, 1, 1),
  (2257727, 3, 1),
  (2258881, 1, 0),
  (2259462, 2, 1),
  (2259545, 0, 1),
  (2260182, 1, 1),
  (2266302, 0, 0),
  (2267073, 3, 1),
  (2270347, 1, 2),
  (2270422, 2, 0),
  (2270625, 3, 2),
  (2275725, 1, 1),
  (2276201, 2, 2),
  (2276946, 0, 2),
  (2277086, 1, 1),
  (2277702, 1, 0),
  (2277865, 2, 0),
  (2277877, 1, 1),
  (2279790, 1, 0),
  (2285769, 2, 2),
  (2287307, 2, 2),
  (2290996, 2, 2),
  (2293989, 3, 1),
  (2294838, 2, 2),
  (2296278, 1, 2),
  (2297073, 2, 1),
  (2297574, 2, 1),
  (2299388, 0, 2),
  (2301677, 3, 0),
  (2309193, 2, 1),
  (2309638, 1, 1),
  (2309645, 0, 0),
  (2309701, 2, 0),
  (2312863, 2, 2),
  (2313604, 2, 1),
  (2313955, 0, 0),
  (2314369, 3, 0),
  (2314389, 0, 0),
  (2317465, 2, 0),
  (2317820, 1, 2),
  (2319113, 3, 1),
  (2322078, 0, 2),
  (2324715, 0, 2),
  (2330184, 1, 0),
  (2331601, 0, 2),
  (2331752, 2, 1),
  (2335627, 2, 2),
  (2335794, 2, 1),
  (2337445, 0, 1),
  (2337625, 2, 0),
  (2339591, 0, 2),
  (2344468, 1, 1),
  (2346698, 1, 1),
  (2347539, 3, 0),
  (2347894, 2, 2),
  (2356460, 1, 0),
  (2357522, 2, 1),
  (2359859, 2, 2),
  (2359936, 0, 1),
  (2360333, 1, 0),
  (2361536, 1, 2),
  (2362084, 3, 2),
  (2362724, 1, 1),
  (2364363, 3, 2),
  (2366787, 0, 2),
  (2368989, 3, 1),
  (2373258, 3, 1),
  (2375056, 0, 0),
  (2377825, 3, 0),
  (2378629, 0, 1),
  (2379273, 0, 0),
  (2381487, 1, 1),
  (2383585, 3, 1),
  (2383796, 1, 0),
  (2383847, 2, 0),
  (2384419, 2, 2),
  (2385416, 3, 0),
  (2386817, 2, 2),
  (2390047, 0, 2),
  (2390464, 1, 1),
  (2392324, 0, 1),
  (2395954, 1, 0),
  (2396870, 3, 1),
  (2397663, 2, 1),
  (2402477, 1, 2),
  (2403642, 1, 2),
  (2405980, 0, 1),
  (2408765, 2, 1),
  (2415176, 2, 2),
  (2416757, 2, 0),
  (2417141, 0, 2),
  (2417171, 3, 1),
  (2417624, 3, 0),
  (2418515, 3, 1),
  (2418866, 2, 0),
  (2421927, 1, 2),
  (2422813, 3, 1),
  (2427090, 3, 0),
  (2431281, 0, 1),
  (2433103, 3, 1),
  (2436619, 1, 0),
  (2436825, 1, 0),
  (2436997, 3, 1),
  (2437257, 3, 0),
  (2438797, 3, 1),
  (2444373, 2, 0),
  (2446264, 0, 2),
  (2454637, 0, 0),
  (2455963, 3, 1),
  (2456324, 2, 2),
  (2457062, 1, 2),
  (2460616, 1, 2),
  (2462158, 3, 2),
  (2470151, 0, 2),
  (2470800, 1, 2),
  (2471536, 3, 1),
  (2473075, 0, 0),
  (2475985, 2, 1),
  (2477212, 2, 2),
  (2479122, 3, 0),
  (2479370, 0, 2),
  (2481241, 0, 2),
  (2490123, 3, 0),
  (2498563, 2, 2),
  (2501921, 1, 2),
  (2503498, 1, 2),
  (2503680, 2, 0),
  (2505005, 2, 1),
  (2509838, 2, 1),
  (2510475, 0, 0),
  (2511320, 3, 1),
  (2514127, 1, 2),
  (2515833, 3, 2),
  (2517596, 3, 2),
  (2517623, 2, 1),
  (2518036, 2, 0),
  (2518066, 0, 2),
  (2518189, 0, 0),
  (2518838, 0, 1),
  (2521877, 0, 2),
  (2523002, 3, 1),
  (2524809, 1, 2),
  (2526277, 3, 0),
  (2526467, 2, 1),
  (2527387, 3, 1),
  (2527999, 0, 1),
  (2531458, 2, 2),
  (2533328, 0, 2),
  (2534283, 2, 2),
  (2538326, 3, 1),
  (2539792, 3, 0),
  (2540591, 2, 1),
  (2541992, 0, 2),
  (2543581, 0, 0),
  (2543858, 1, 1),
  (2544756, 0, 1),
  (2545021, 0, 1),
  (2547122, 1, 0),
  (2547944, 3, 0),
  (2548406, 0, 0),
  (2551348, 1, 0),
  (2551790, 2, 1),
  (2552667, 1, 0),
  (2554645, 1, 1),
  (2560357, 2, 0),
  (2561451, 3, 0),
  (2561659, 3, 0),
  (2562121, 0, 0),
  (2562989, 2, 1),
  (2563141, 1, 0),
  (2563851, 2, 0),
  (2569258, 2, 0),
  (2569943, 0, 2),
  (2571035, 2, 1),
  (2575809, 0, 0),
  (2576776, 3, 2),
  (2581352, 1, 2),
  (2585036, 2, 1),
  (2587919, 0, 2),
  (2588974, 3, 2),
  (2589016, 2, 1),
  (2590823, 2, 1),
  (2595259, 2, 0),
  (2595400, 2, 0),
  (2596991, 1, 1),
  (2601329, 1, 2),
  (2602081, 2, 2),
  (2602680, 0, 2),
  (2603216, 1, 1),
  (2606782, 3, 0),
  (2607202, 0, 0),
  (2608566, 3, 2),
  (2608698, 2, 2),
  (2609338, 3, 0),
  (2614319, 3, 0),
  (2616508, 2, 1),
  (2617482, 1, 0),
  (2619106, 2, 1),
  (2621655, 2, 1),
  (2625582, 2, 0),
  (2628040, 1, 1),
  (2630922, 0, 0),
  (2631320, 1, 1),
  (2635329, 3, 1),
  (2635511, 0, 0),
  (2639645, 2, 0),
  (2640626, 3, 0),
  (2643536, 0, 2),
  (2644405, 1, 0),
  (2644689, 1, 0),
  (2645850, 3, 2),
  (2646920, 2, 2),
  (2649024, 0, 2),
  (2650535, 2, 1),
  (2653385, 0, 2),
  (2654250, 1, 2),
  (2655990, 2, 1),
  (2656674, 1, 1),
  (2665191, 0, 0),
  (2667608, 2, 0),
  (2669092, 2, 0),
  (2672525, 3, 0),
  (2672971, 0, 2),
  (2676869, 2, 2),
  (2678756, 0, 1),
  (2685133, 0, 2),
  (2686551, 2, 2),
  (2691823, 0, 0),
  (2692055, 0, 1),
  (2697820, 2, 1),
  (2698119, 1, 2),
  (2699549, 0, 0),
  (2699606, 3, 1),
  (2702048, 2, 0),
  (2702103, 1, 0),
  (2703212, 2, 0),
  (2705215, 0, 2),
  (2709894, 1, 0),
  (2710866, 0, 0),
  (2721294, 0, 2),
  (2724086, 3, 2),
  (2724525, 2, 2),
  (2727266, 1, 1),
  (2727420, 2, 0),
  (2728056, 2, 1),
  (2729797, 2, 1),
  (2730403, 3, 2),
  (2730739, 2, 1),
  (2735195, 1, 0),
  (2737479, 3, 1),
  (2738352, 2, 2),
  (2738628, 2, 1),
  (2739137, 0, 2),
  (2739733, 3, 2),
  (2740996, 0, 2),
  (2741009, 3, 0),
  (2743292, 1, 0),
  (2743496, 2, 0),
  (2750305, 3, 0),
  (2752061, 3, 1),
  (2752270, 3, 2),
  (2754292, 2, 2),
  (2754379, 1, 1),
  (2760790, 2, 1),
  (2761488, 3, 0),
  (2762336, 1, 2),
  (2765461, 2, 1),
  (2765961, 0, 0),
  (2768698, 1, 0),
  (2769291, 0, 2),
  (2769861, 1, 2),
  (2770957, 3, 2),
  (2772211, 0, 2),
  (2772976, 0, 0),
  (2774957, 1, 0),
  (2777172, 3, 2),
  (2778274, 0, 2),
  (2778856, 3, 0),
  (2782586, 0, 0),
  (2786528, 0, 0),
  (2787993, 1, 0),
  (2791814, 2, 2),
  (2794871, 0, 1),
  (2795087, 2, 2),
  (2795661, 2, 2),
  (2797151, 3, 2),
  (2798735, 2, 0),
  (2800310, 3, 2),
  (2802178, 2, 0),
  (2803040, 1, 2),
  (2803731, 1, 2),
  (2804538, 0, 0),
  (2804895, 2, 1),
  (2810593, 3, 1),
  (2812942, 0, 0),
  (2813006, 2, 1),
  (2813721, 3, 2),
  (2816452, 1, 2),
  (2819331, 1, 2),
  (2820081, 2, 2),
  (2820934, 0, 0),
  (2827733, 0, 0),
  (2828616, 2, 2),
  (2835144, 1, 0),
  (2835513, 2, 2),
  (2835937, 3, 1),
  (2836034, 0, 0),
  (2837719, 0, 2),
  (2838507, 0, 2),
  (2841077, 1, 2),
  (2842640, 1, 0),
  (2843566, 2, 2),
  (2844209, 0, 0),
  (2846368, 3, 1),
  (2848908, 0, 1),
  (2854217, 0, 1),
  (2858603, 3, 1),
  (2858750, 2, 0),
  (2860304, 0, 0),
  (2861608, 2, 2),
  (2862065, 1, 2),
  (2864746, 1, 1),
  (2866063, 1, 1),
  (2868874, 1, 2),
  (2868936, 2, 1),
  (2869607, 0, 2),
  (2872737, 1, 2),
  (2873066, 0, 0),
  (2873096, 3, 0),
  (2873541, 1, 2),
  (2883370, 1, 1),
  (2884482, 0, 2),
  (2884652, 3, 0),
  (2886671, 3, 2),
  (2886771, 0, 1),
  (2886822, 0, 2),
  (2893847, 3, 1),
  (2898107, 2, 1),
  (2899365, 3, 0),
  (2900362, 0, 2),
  (2901649, 1, 0),
  (2901706, 3, 0),
  (2905118, 0, 2),
  (2907531, 1, 0),
  (2911790, 2, 2),
  (2912496, 1, 1),
  (2914083, 2, 0),
  (2919720, 1, 2),
  (2922049, 3, 0),
  (2922455, 1, 1),
  (2923271, 3, 2),
  (2923385, 0, 0),
  (2925180, 3, 1),
  (2928029, 2, 1),
  (2929118, 3, 2),
  (2929997, 3, 1),
  (2931394, 3, 0),
  (2931726, 2, 2),
  (2931927, 0, 2),
  (2936040, 1, 2),
  (2936847, 0, 1),
  (2937412, 3, 1),
  (2939607, 2, 1),
  (2939760, 3, 1),
  (2940110, 0, 1),
  (2943611, 1, 1),
  (2943665, 1, 2),
  (2944763, 2, 2),
  (2948691, 3, 0),
  (2949366, 3, 0),
  (2954660, 2, 0),
  (2961983, 2, 0),
  (2964819, 3, 2),
  (2964994, 2, 2),
  (2971178, 1, 0),
  (2971546, 3, 1),
  (2977900, 3, 0),
  (2981342, 0, 0),
  (2984420, 2, 2),
  (2985059, 0, 0),
  (2986451, 1, 0),
  (2986546, 3, 2),
  (2988387, 3, 0),
  (2988921, 3, 2),
  (2989285, 0, 1),
  (2989839, 3, 0),
  (2994053, 3, 0),
  (2995377, 2, 1),
  (2996844, 1, 1),
  (3003103, 1, 0),
  (3004056, 0, 2),
  (3010345, 1, 0),
  (3014701, 3, 1),
  (3015328, 3, 2),
  (3017626, 2, 0),
  (3020387, 3, 2),
  (3020801, 0, 1),
  (3021703, 1, 1),
  (3027535, 0, 2),
  (3033125, 1, 0),
  (3033155, 1, 1),
  (3035013, 0, 1),
  (3037587, 2, 2),
  (3038522, 3, 1),
  (3039902, 3, 0),
  (3046876, 3, 2),
  (3048325, 3, 2),
  (3052114, 1, 0),
  (3057611, 3, 0),
  (3062725, 2, 2),
  (3063864, 0, 0),
  (3065432, 0, 0),
  (3073588, 2, 2),
  (3077740, 1, 0),
  (3077787, 0, 2),
  (3086098, 3, 2),
  (3087185, 3, 2),
  (3090474, 1, 0),
  (3093004, 0, 1),
  (3094984, 0, 2),
  (3095231, 0, 2),
  (3098779, 3, 2),
  (3103186, 3, 1),
  (3104208, 1, 2),
  (3111598, 1, 0),
  (3117002, 0, 0),
  (3118429, 1, 2),
  (3118660, 1, 0),
  (3121663, 3, 1),
  (3122776, 3, 0),
  (3127423, 3, 0),
  (3128980, 0, 0),
  (3130578, 0, 2),
  (3133911, 1, 0),
  (3135451, 0, 0),
  (3135735, 1, 2),
  (3136048, 0, 2),
  (3141286, 1, 2),
  (3141649, 2, 1),
  (3144590, 1, 0),
  (3145650, 1, 1),
  (3146580, 3, 2),
  (3146725, 0, 1),
  (3147358, 0, 0),
  (3147966, 3, 0),
  (3148392, 2, 2),
  (3151609, 3, 2),
  (3158834, 2, 0),
  (3160119, 0, 2),
  (3176176, 2, 2),
  (3177659, 1, 2),
  (3182950, 3, 0),
  (3185744, 2, 1),
  (3186209, 2, 1),
  (3189317, 3, 2),
  (3189786, 0, 0),
  (3189799, 2, 0),
  (3191029, 0, 2),
  (3197958, 2, 1),
  (3198370, 2, 2),
  (3198729, 0, 2),
  (3199272, 3, 2),
  (3203671, 3, 1),
  (3205009, 3, 2),
  (3215033, 2, 0),
  (3216639, 1, 1),
  (3219878, 1, 1),
  (3223702, 2, 2),
  (3223970, 3, 0),
  (3228561, 1, 2),
  (3230167, 3, 0),
  (3230673, 3, 2),
  (3231101, 1, 0),
  (3233321, 2, 0),
  (3234357, 2, 2),
  (3234433, 0, 0),
  (3240498, 0, 0),
  (3243549, 2, 0),
  (3243578, 0, 2),
  (3246412, 1, 0),
  (3255398, 0, 2),
  (3256913, 2, 1),
  (3256967, 0, 2),
  (3257747, 0, 1),
  (3258668, 2, 0),
  (3260477, 2, 1),
  (3267228, 1, 0),
  (3267726, 1, 1),
  (3267755, 2, 0),
  (3270771, 1, 1),
  (3278076, 2, 1),
  (3279807, 2, 1),
  (3281158, 0, 1),
  (3282306, 2, 2),
  (3282497, 2, 0),
  (3283420, 1, 1),
  (3288688, 2, 2),
  (3289009, 1, 1),
  (3293075, 3, 2),
  (3295503, 0, 0),
  (3313990, 3, 2),
  (3316468, 3, 2),
  (3319204, 1, 0),
  (3321731, 1, 0),
  (3324665, 1, 1),
  (3326576, 3, 0),
  (3328368, 2, 0),
  (3336048, 2, 1),
  (3343901, 1, 2),
  (3345689, 1, 2),
  (3346101, 0, 0),
  (3347534, 1, 0),
  (3348618, 2, 0),
  (3349661, 1, 0),
  (3350962, 2, 2),
  (3351690, 3, 0),
  (3352757, 0, 2),
  (3352969, 3, 1),
  (3353597, 0, 2),
  (3354385, 2, 1),
  (3354784, 2, 0),
  (3355185, 2, 0),
  (3359356, 0, 0),
  (3360905, 0, 2),
  (3363722, 3, 0),
  (3364680, 3, 0),
  (3366794, 2, 1),
  (3367356, 2, 1),
  (3376218, 3, 1),
  (3381815, 3, 1),
  (3384260, 1, 1),
  (3387722, 0, 2),
  (3387961, 2, 0),
  (3388772, 2, 1),
  (3390915, 2, 0),
  (3393834, 0, 1),
  (3394066, 3, 1),
  (3394428, 2, 2),
  (3394648, 3, 2),
  (3395811, 3, 0),
  (3397563, 2, 0),
  (3402403, 2, 1),
  (3404879, 0, 1),
  (3405364, 2, 0),
  (3406862, 1, 2),
  (3411696, 2, 1),
  (3413227, 1, 1),
  (3415238, 1, 2),
  (3416590, 3, 0),
  (3416717, 2, 0),
  (3417814, 3, 0),
  (3420369, 2, 2),
  (3420383, 3, 0),
  (3421008, 3, 0),
  (3423114, 0, 1),
  (3429099, 2, 0),
  (3430133, 2, 1),
  (3430239, 2, 1),
  (3431269, 3, 1),
  (3433684, 2, 1),
  (3435322, 2, 1),
  (3436441, 1, 2),
  (3440169, 0, 2),
  (3444545, 2, 1),
  (3444933, 0, 2),
  (3445095, 1, 2),
  (3449127, 2, 2),
  (3451210, 0, 2),
  (3457187, 2, 1),
  (3458208, 2, 0),
  (3458464, 3, 2),
  (3461711, 2, 1),
  (3463485, 1, 0),
  (3465456, 2, 0),
  (3465460, 3, 0),
  (3469392, 1, 1),
  (3470448, 1, 1),
  (3470766, 0, 0),
  (3470767, 1, 0),
  (3471752, 2, 0),
  (3471763, 1, 2),
  (3476884, 1, 2),
  (3478750, 3, 2),
  (3479649, 0, 2),
  (3486009, 3, 1),
  (3489112, 1, 0),
  (3490364, 0, 1),
  (3494126, 0, 2),
  (3495455, 1, 0),
  (3496104, 1, 2),
  (3497204, 1, 0),
  (3503217, 2, 0),
  (3505089, 1, 2),
  (3505468, 1, 1),
  (3507080, 0, 0),
  (3508145, 0, 2),
  (3508892, 1, 0),
  (3509619, 2, 2),
  (3510067, 1, 0),
  (3512460, 1, 2),
  (3512652, 3, 0),
  (3513422, 0, 0),
  (3514559, 1, 2),
  (3516126, 3, 0),
  (3516204, 0, 1),
  (3516571, 2, 1),
  (3518288, 2, 1),
  (3519181, 1, 0),
  (3520296, 1, 0),
  (3525491, 2, 1),
  (3526657, 3, 1),
  (3527061, 0, 2),
  (3527136, 3, 0),
  (3528012, 3, 1),
  (3528807, 2, 1),
  (3530350, 1, 0),
  (3533258, 1, 1),
  (3535187, 1, 1),
  (3535417, 2, 2),
  (3537864, 2, 2),
  (3537877, 3, 1),
  (3538683, 0, 1),
  (3539430, 0, 0),
  (3545054, 2, 2),
  (3545063, 3, 2),
  (3546248, 1, 0),
  (3547264, 3, 1),
  (3547962, 1, 2),
  (3548101, 2, 0),
  (3551859, 0, 1),
  (3554860, 1, 2),
  (3555016, 1, 2),
  (3558011, 1, 2),
  (3559053, 0, 0),
  (3560286, 2, 1),
  (3562302, 3, 0),
  (3563939, 0, 2),
  (3564112, 0, 0),
  (3573144, 0, 1),
  (3577169, 3, 0),
  (3578459, 0, 2),
  (3580650, 0, 0),
  (3581824, 3, 0),
  (3586505, 1, 2),
  (3588236, 1, 1),
  (3589607, 1, 0),
  (3591929, 2, 1),
  (3592766, 1, 1),
  (3594435, 0, 2),
])
