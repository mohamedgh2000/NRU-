import streamlit as st
import os
import datetime
from sympy import Point, Polygon, Line
from fpdf import FPDF
import matplotlib.pyplot as plt
import time
from io import StringIO
from PIL import Image

def_val='-5.5222321,33.8290698/-5.5175972,33.8289985/-5.5171823,33.8219555/-5.5242348,33.8200242/-5.5222178,33.829252'
def_path='C:\\Users\\Dell\\Desktop\\testnru'
image = Image.open('image.png')

st.image(image, caption='')
with st.form("my_form"):
     
    Date_NRU = st.date_input('date nru', datetime.date(2022, 6, 1))
    Nom_du_demandeur= st.text_input('Nom_du_demandeur', '')
    Numero_du_demandeur= st.text_input('Numero_du_demandeur', '')
    Cordinates_list= st.text_input('Cordinates_list as tuples', def_val)
    Cordinates_File= st.file_uploader("upload you Cordinates ile")

    
    #path_bd= st.text_input('path_bd', 'C:\\Users\\Dell\\Desktop\\testnru')
    #nru= st.text_input('nru', 'C:\\Users\\Dell\\Desktop\\testnru\\rapportNRU.pdf')

    submitted = st.form_submit_button("Submit")
path_bd= 'C:\\Users\\Dell\\Desktop\\testnru'
nru= 'C:\\Users\\Dell\\Desktop\\testnru\\rapportNRU.pdf'

x=""
if Cordinates_File is not None:
     # To read file as string:
     bytes_data = Cordinates_File.getvalue()
     

     # To convert to a string based IO:
     stringio = StringIO(Cordinates_File.getvalue().decode("utf-8"))
          # To read file as string:
     string_data = stringio.read()
     x=string_data
     
if Cordinates_list == "":
	Cordinates_list=x

l=Cordinates_list.split('/')

ls=[]
for i in l:
	ls.append((i.split(',')))
for i in range(len(ls)):
	for j in range(len(ls[i])):
		ls[i][j]=float(ls[i][j])
		
listply=[]
j=0
for i in ls:
    j=j+1
    globals()[f"P{j}"] = Point(i)
    listply.append(Point(i))
lnn=tuple(listply)





p5, p6, p7, p8, p9 = map(Point, [(-72.2796643, 42.9264951),(-72.2795999, 42.9259219),(-72.2785485, 42.9260633),(-72.2787255, 42.9265618),(-72.2796643, 42.9264912)])
#point de polygon zone indus
p13,p14,p15,p16,p17,p18,p19,p20,p21,p22=map(Point,[(-5.5280113,33.828355),(-5.5255222,33.8287113),(-5.5186343,33.8278205),(-5.5156088,33.82864),(-5.5148792,33.824881),(-5.5281758,33.8208897),(-5.5280614,33.8229624),(-5.527997,33.825314),(-5.5280185,33.8265967),(-5.5280399,33.8284317)])
#point de cote de route
p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41=map(Point,[(-5.5148506,33.8248556),(-5.5182409,33.823751),(-5.5172968,33.819297),(-5.5198717,33.8184418),(-5.5169535,33.8125383),(-5.5120611,33.8061235),(-5.5140352,33.8048405),(-5.5128765,33.800528),(-5.5108166,33.7970708),(-5.5094433,33.7982113),(-5.5085421,33.7995657),(-5.5024481,33.7987816),(-5.5018902,33.8004568),(-5.5069113,33.8079767),(-5.5085421,33.8112554),(-5.5123615,33.8181448),(-5.5125189,33.8208173),(-5.5138063,33.8226702),(-5.5148792,33.8248794)])
#point de cote droite de route 
p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60, p61, p62, p63, p64, p65, p66, p67, p68, p69, p70, p71, p72, p73, p74, p75, p76, p77, p78, p79, p80, p81=map(Point,[(-5.5131483,33.8228399),(-5.5127621,33.822733),(-5.5098653,33.8237485),(-5.5093718,33.8237307),(-5.5093503,33.8231606),(-5.5083847,33.8235882),(-5.5078268,33.8228043),(-5.505352,33.8235406),(-5.5048585,33.8229705),(-5.5044508,33.8227567),(-5.5040002,33.8219194),(-5.5023408,33.8174712),(-5.5012751,33.8136939),(-5.5008888,33.8123754),(-5.4996872,33.8113063),(-5.4981208,33.8103084),(-5.4973841,33.8093819),(-5.4974484,33.8085622),(-5.4958391,33.8053191),(-5.4936361,33.803745),(-5.4930496,33.8029193),(-5.4988861,33.8018323),(-5.4999161,33.8012086),(-5.4998088,33.8002107),(-5.500946,33.8007453),(-5.5011177,33.801066),(-5.5015254,33.8012086),(-5.5043507,33.8046538),(-5.5051231,33.8057943),(-5.5065107,33.8081464),(-5.5077553,33.8111578),(-5.5081201,33.8119418),(-5.5099082,33.815048),(-5.51126,33.8172455),(-5.5117321,33.8181185),(-5.5120182,33.8197458),(-5.5121899,33.8209395),(-5.5124331,33.821569),(-5.5131626,33.8228696)])
#test
p10,p11,p12 = map(Point, [(1,1),(2,2),(3,3)])
#zone_verte 1
p81,p82,p83,p84,p85,p86,p87,p88,p89,p90=map(Point, [(-5.5068004,33.8080847),(-5.5092627,33.8071665),(-5.51149,33.8063606),(-5.5140113,33.8050368),(-5.5137001,33.8039768),(-5.5096983,33.8056474),(-5.5077016,33.8064935),(-5.5066824,33.8069124),(-5.5064152,33.8072236),(-5.5067908,33.8080847)])
#zone verte 2
p92,p93,p94,p95,p96,p97,p98,p99,p100,p101,p102,p103,p104,p105,p106,p107,p108,p109,P110=map(Point, [(-5.5071137,33.80501),(-5.510268,33.8024157),(-5.509989,33.8018451),(-5.508208,33.8031824),(-5.5079505,33.8027723),(-5.5096457,33.8013994),(-5.5093238,33.800704),(-5.5117593,33.7989833),(-5.510843,33.7975621),(-5.5091908,33.7988371),(-5.5086758,33.7997554),(-5.508944,33.8003884),(-5.5084398,33.8000407),(-5.5069914,33.8010749),(-5.5074763,33.8015991),(-5.5071974,33.8018487),(-5.5072618,33.8020359),(-5.5062318,33.802874),(-5.5073154,33.8043182)])
#zone verte 3
p110,p111,p112,p113,p114,p115,p116,p117,p118=map(Point, [(-5.5034208,33.8029988),(-5.5041826,33.8025173),(-5.5034745,33.8014386),(-5.5038822,33.801189),(-5.5035925,33.8008858),(-5.5032277,33.8011355),(-5.5029166,33.8008056),(-5.5021119,33.8012425),(-5.5034101,33.8029899)])
#zone verte 4
p119,p120,p121,p122,p123,p124,p125,p126,p127=map(Point, [(-5.5110598,33.7976317),(-5.512594,33.7968025),(-5.5121434,33.795688),(-5.5108345,33.7960001),(-5.510577,33.7952244),(-5.5105662,33.7946092),(-5.5101049,33.7946716),(-5.5107701,33.7972572),(-5.511049,33.7976227)])
#zone verte 5
p127,p128,p129,p130,p131,p132,p133,p134=map(Point,[(-5.5101907,33.8275833),(-5.514493,33.8258453),(-5.5145252,33.8255512),(-5.5143106,33.8251145),(-5.5116928,33.8262197),(-5.5118752,33.8265494),(-5.5100513,33.8273694),(-5.5101907,33.8275655)])
#zone verte 6 
p135,p136,p137,p138,p139,p140,p141,p142=map(Point,[(-5.518158,33.8347702),(-5.520014,33.8339948),(-5.5177717,33.8309023),(-5.5159478,33.8310003),(-5.5175786,33.8335492),(-5.5177395,33.8337185),(-5.5178039,33.834182),(-5.5181687,33.8347612)])
#zone verte 7
p144,p145,p146,p147,p148,p149,p150=map(Point,[(-5.5224216,33.8336793),(-5.5214131,33.8327257),(-5.524621,33.830462),(-5.5237627,33.829856),(-5.5280221,33.8291074),(-5.5281508,33.8296778),(-5.5224216,33.8336972)])
#zone indus1
p151,p152,p153,p154,p155,p156,p157,p158,p159,p160,p161=map(Point,[(-5.5278997,33.8282446),(-5.5279427,33.8258917),(-5.5281572,33.8239665),(-5.528286,33.8206865),(-5.5148535,33.8248578),(-5.5153685,33.8263195),(-5.5156689,33.8267473),(-5.515583,33.8285655),(-5.5187159,33.8276029),(-5.5260115,33.8287081),(-5.5278997,33.8283159)])
#zone indus2 
p163,p164,p165,p166,p167,p168,p169,p170,p171,p172=map(Point,[(-5.5252218,33.8499243),(-5.5216598,33.8421899),(-5.5169392,33.8438651),(-5.5188274,33.8474294),(-5.5187416,33.8478571),(-5.5192137,33.8479284),(-5.5198574,33.8492828),(-5.5211878,33.8489977),(-5.5223465,33.8507084),(-5.5252647,33.84996)])
#zone indus 3
p174,p175,p176,p177,p178,p179,p180,p181=map(Point,[(-5.5220461,33.841477),(-5.5242348,33.8406571),(-5.525651,33.8425107),(-5.527668,33.844079),(-5.5280113,33.8448988),(-5.5248785,33.8442928),(-5.5236769,33.8442928),(-5.5220461,33.8415126)])
#zone indus 4
p182,p183,p184,p185,p186,p187,p188,p189,p190,p191,p192=map(Point,[(-5.5263805,33.8507084),(-5.5237198,33.8451126),(-5.5240631,33.8449344),(-5.5273247,33.8452909),(-5.5286551,33.8459681),(-5.5334616,33.8481779),(-5.5329895,33.8491402),(-5.5274105,33.8462889),(-5.5263805,33.8473938),(-5.5277538,33.8502807),(-5.5263376,33.8507084)])

A1,A2,A3,A4,A5 = map(Point,[(-5.5278740,33.8286144),(-5.5149565,33.8302909),(-5.5140553,33.8255467),(-5.5279169,33.8209094),(-5.5279169,33.8286144)])

poly1 = Polygon(P1,P2,P3,P4)
poly2 = Polygon(p5, p6, p7, p8, p9)
poly3 = Polygon(p10,p11,p12)
poly4 = Polygon(p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41)
poly5 = Polygon(p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60, p61, p62, p63, p64, p65, p66, p67, p68, p69, p70, p71, p72, p73, p74, p75, p76, p77, p78, p79, p80, p81)

zone_indus = Polygon(p13,p14,p15,p16,p17,p18,p19,p20,p21,p22)
zone_indus1 = Polygon((-5.5278997,33.8282446),(-5.5279427,33.8258917),(-5.5281572,33.8239665),(-5.528286,33.8206865),(-5.5148535,33.8248578),(-5.5153685,33.8263195),(-5.5156689,33.8267473),(-5.515583,33.8285655),(-5.5187159,33.8276029),(-5.5260115,33.8287081),(-5.5278997,33.8283159))
zone_indus2 = Polygon((-5.5252218,33.8499243),(-5.5216598,33.8421899),(-5.5169392,33.8438651),(-5.5188274,33.8474294),(-5.5187416,33.8478571),(-5.5192137,33.8479284),(-5.5198574,33.8492828),(-5.5211878,33.8489977),(-5.5223465,33.8507084),(-5.5252647,33.84996))
zone_indus3 = Polygon((-5.5220461,33.841477),(-5.5242348,33.8406571),(-5.525651,33.8425107),(-5.527668,33.844079),(-5.5280113,33.8448988),(-5.5248785,33.8442928),(-5.5236769,33.8442928),(-5.5220461,33.8415126))
zone_indus4 = Polygon((-5.5263805,33.8507084),(-5.5237198,33.8451126),(-5.5240631,33.8449344),(-5.5273247,33.8452909),(-5.5286551,33.8459681),(-5.5334616,33.8481779),(-5.5329895,33.8491402),(-5.5274105,33.8462889),(-5.5263805,33.8473938),(-5.5277538,33.8502807),(-5.5263376,33.8507084))
zone_indus5= Polygon((-5.5279684,33.8501239),(-5.5317879,33.8490547),(-5.5275822,33.8464885),(-5.5267239,33.8473795),(-5.5280113,33.8500883))

zone_verte1=Polygon((-5.5068004,33.8080847),(-5.5092627,33.8071665),(-5.51149,33.8063606),(-5.5140113,33.8050368),(-5.5137001,33.8039768),(-5.5096983,33.8056474),(-5.5077016,33.8064935),(-5.5066824,33.8069124),(-5.5064152,33.8072236),(-5.5067908,33.8080847))
zone_verte2 = Polygon((-5.5071137,33.80501),(-5.510268,33.8024157),(-5.509989,33.8018451),(-5.508208,33.8031824),(-5.5079505,33.8027723),(-5.5096457,33.8013994),(-5.5093238,33.800704),(-5.5117593,33.7989833),(-5.510843,33.7975621),(-5.5091908,33.7988371),(-5.5086758,33.7997554),(-5.508944,33.8003884),(-5.5084398,33.8000407),(-5.5069914,33.8010749),(-5.5074763,33.8015991),(-5.5071974,33.8018487),(-5.5072618,33.8020359),(-5.5062318,33.802874),(-5.5073154,33.8043182))
zone_verte3 = Polygon((-5.5034208,33.8029988),(-5.5041826,33.8025173),(-5.5034745,33.8014386),(-5.5038822,33.801189),(-5.5035925,33.8008858),(-5.5032277,33.8011355),(-5.5029166,33.8008056),(-5.5021119,33.8012425),(-5.5034101,33.8029899))
zone_verte4 = Polygon((-5.5110598,33.7976317),(-5.512594,33.7968025),(-5.5121434,33.795688),(-5.5108345,33.7960001),(-5.510577,33.7952244),(-5.5105662,33.7946092),(-5.5101049,33.7946716),(-5.5107701,33.7972572),(-5.511049,33.7976227))
zone_verte5 = Polygon((-5.5101907,33.8275833),(-5.514493,33.8258453),(-5.5145252,33.8255512),(-5.5143106,33.8251145),(-5.5116928,33.8262197),(-5.5118752,33.8265494),(-5.5100513,33.8273694),(-5.5101907,33.8275655))
zone_verte6 = Polygon((-5.518158,33.8347702),(-5.520014,33.8339948),(-5.5177717,33.8309023),(-5.5159478,33.8310003),(-5.5175786,33.8335492),(-5.5177395,33.8337185),(-5.5178039,33.834182),(-5.5181687,33.8347612))
zone_verte7 = Polygon((-5.5224216,33.8336793),(-5.5214131,33.8327257),(-5.524621,33.830462),(-5.5237627,33.829856),(-5.5280221,33.8291074),(-5.5281508,33.8296778),(-5.5224216,33.8336972))

road=Line((-5.5085707,33.812484),(-5.5111241,33.8167449),(-5.511843,33.818139),(-5.5122185,33.8204208),(-5.5130231,33.8224495),(-5.51386,33.8237686),(-5.5148363,33.8265227),(-5.5149672,33.8282232),(-5.5154285,33.8303533))
highway = Line((-5.5211127,33.830061),(-5.5200398,33.8302392),(-5.5193102,33.8303818),(-5.5187953,33.8304264),(-5.5175078,33.8305066),(-5.5149221,33.8305066),(-5.5137527,33.8304264),(-5.5118966,33.8301858),(-5.5075729,33.8291519))

isIntersection = poly1.intersection(poly2)
pol_inter=[]
pol_inside=[]
# if poly1.intersection(poly2) != []:
#       pol_inter.append("poly2")
# if poly1.intersection(poly3) != []:
#       pol_inter.append("poly3")
# if poly1.intersection(poly4) != []:
#       pol_inter.append("poly4")
# if poly1.intersection(poly5) != []:
#       pol_inter.append("poly5")
# if poly1.intersection(zone_indus) != []:
#       pol_inter.append("zone_indus")
###############################################################
if poly1.intersection(zone_indus1) != []:
      pol_inter.append("zone_indus1")
if poly1.intersection(zone_indus2) != []:
      pol_inter.append("zone_indus2")
if poly1.intersection(zone_indus3) != []:
      pol_inter.append("zone_indus3")
if poly1.intersection(zone_indus4) != []:
      pol_inter.append("zone_indus4")
if poly1.intersection(zone_indus5) != []:
      pol_inter.append("zone_indus5")
#####################################################################################
if poly1.intersection(zone_verte1) != []:
      pol_inter.append("zone_verte1")
if poly1.intersection(zone_verte2) != []:
      pol_inter.append("zone_verte2")
if poly1.intersection(zone_verte3) != []:
      pol_inter.append("zone_vert3")
if poly1.intersection(zone_verte4) != []:
      pol_inter.append("zone_verte4")
if poly1.intersection(zone_verte5) != []:
      pol_inter.append("zone_verte5")
if poly1.intersection(zone_verte6) != []:
      pol_inter.append("zone_verte6")
if poly1.intersection(zone_verte7) != []:
      pol_inter.append("zone_verte7")
if poly1.intersection(road) != []:
	pol_inter.append("road")
if poly1.intersection(highway) != []:
	pol_inter.append("highway")	
if poly1.encloses_point(p81) and poly1.encloses_point(p82) and poly1.encloses_point(p83) and poly1.encloses_point(p84) and poly1.encloses_point(p85) and poly1.encloses_point(p86) and poly1.encloses_point(p87) and poly1.encloses_point(p88) and poly1.encloses_point(p89) and poly1.encloses_point(p90):
	pol_inside.append("zone_verte1")
if poly1.encloses_point(p92) and poly1.encloses_point(p93) and poly1.encloses_point(p94) and poly1.encloses_point(p95) and poly1.encloses_point(p96) and poly1.encloses_point(p97) and poly1.encloses_point(p98) and poly1.encloses_point(p99) and poly1.encloses_point(p100) and poly1.encloses_point(p101) and poly1.encloses_point(p102) and poly1.encloses_point(p103) and poly1.encloses_point(p104) and poly1.encloses_point(p105) and poly1.encloses_point(p106) and poly1.encloses_point(p107) and poly1.encloses_point(p108) and poly1.encloses_point(p109) and poly1.encloses_point(P110):
	pol_inside.append("zone_verte2")
if poly1.encloses_point(p110) and poly1.encloses_point(p111) and poly1.encloses_point(p112) and poly1.encloses_point(p113) and poly1.encloses_point(p114) and poly1.encloses_point(p115) and poly1.encloses_point(p116) and poly1.encloses_point(p117) and poly1.encloses_point(p118):
    pol_inside.append("zone_vert3")
if poly1.encloses_point(p119) and poly1.encloses_point(p120) and poly1.encloses_point(p121) and poly1.encloses_point(p122) and poly1.encloses_point(p123) and poly1.encloses_point(p124) and poly1.encloses_point(p125) and poly1.encloses_point(p126) and poly1.encloses_point(p127):
	pol_inside.append("zone_verte4")
if poly1.encloses_point(p127) and poly1.encloses_point(p128) and poly1.encloses_point(p129) and poly1.encloses_point(p130) and poly1.encloses_point(p131) and poly1.encloses_point(p132) and poly1.encloses_point(p133) and poly1.encloses_point(p134):
	pol_inside.append("zone_verte5")
if poly1.encloses_point(p135) and poly1.encloses_point(p136) and poly1.encloses_point(p137) and poly1.encloses_point(p138) and poly1.encloses_point(p139) and poly1.encloses_point(p140) and poly1.encloses_point(p141) and poly1.encloses_point(p142):
	pol_inside.append("zone_verte6")
if poly1.encloses_point(p144) and poly1.encloses_point(p145) and poly1.encloses_point(p146) and poly1.encloses_point(p147) and poly1.encloses_point(p148) and poly1.encloses_point(p149) and poly1.encloses_point(p150):
	pol_inside.append("zone_verte7")
if poly1.encloses_point(p151) and poly1.encloses_point(p152) and poly1.encloses_point(p153) and poly1.encloses_point(p154) and poly1.encloses_point(p155) and poly1.encloses_point(p156) and poly1.encloses_point(p157) and poly1.encloses_point(p158) and poly1.encloses_point(p159) and poly1.encloses_point(p160) and poly1.encloses_point(p161):
	pol_inside.append("zone_indus1")
if poly1.encloses_point(p163) and poly1.encloses_point(p164) and poly1.encloses_point(p165) and poly1.encloses_point(p166) and poly1.encloses_point(p167) and poly1.encloses_point(p168) and poly1.encloses_point(p169) and poly1.encloses_point(p170) and poly1.encloses_point(p171) and poly1.encloses_point(p172):
	pol_inside.append("zone_indus2")
if poly1.encloses_point(p174) and poly1.encloses_point(p175) and poly1.encloses_point(p176) and poly1.encloses_point(p177) and poly1.encloses_point(p178) and poly1.encloses_point(p179) and poly1.encloses_point(p180) and poly1.encloses_point(p181):
	pol_inside.append("zone_indus3")
if poly1.encloses_point(p182) and poly1.encloses_point(p183) and poly1.encloses_point(p184) and poly1.encloses_point(p185) and poly1.encloses_point(p186) and poly1.encloses_point(p187) and poly1.encloses_point(p188) and poly1.encloses_point(p189) and poly1.encloses_point(p190) and poly1.encloses_point(p191) and poly1.encloses_point(p192):
	pol_inside.append("zone_indus4")



coord = ls
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.figure()

fig=plt.plot(xs,ys) 
#fig = io.BytesIO()
plt.savefig('map.png')
if pol_inter !=[] or pol_inside !=[]:
       pdf=FPDF('P','mm','A4')
       pdf.add_page()
       pdf.image("logo_ehtp.png",45,17,130,32)
       pdf.set_font('arial','', 12)
       pdf.set_text_color(170,0,0)
       var= "                                                                                                             "+str(Date_NRU)
       pdf.ln(45)
       pdf.cell(0, 5, var )
       pdf.set_font('arial','', 12)
       pdf.set_text_color(0,0,0)
       pdf.ln(10)
       pdf.cell(0, 5, '                                                                                    A' )
       pdf.ln(8)
       pdf.cell(0, 5, '                                                              M/Mme '+Nom_du_demandeur)
       pdf.ln(15)
       pdf.cell(0, 5,"          Objet : Note de renseignements urbanistiques indicative relative a votre demande N")
       pdf.ln(5)
       pdf.cell(0, 5,"          "+Numero_du_demandeur)
#        pdf.ln(15)
#        pdf.cell(0, 5,"          ")
#        pdf.ln(5)
#        pdf.cell(0, 5,"           ")
       pdf.ln(5)
       pdf.cell(0, 5,"           Votre teritoire a intersecter avec les zones suivantes  "+str(pol_inter))
       pdf.ln(5)
       pdf.cell(0, 5,"           et il contient les zones suivantes "+str(pol_inside))
       # pdf.ln(5)
       # pdf.cell(0, 5,"                  - Situe en zone :")
       pdf.ln(5)
       
       pdf.ln(10)
       pdf.cell(0, 5,"            De meme, vous trouverez ci-joint une image de votre teritoire ")
       pdf.ln(5)
       pdf.image("map.png",w=100, h=80)
       pdf.ln(5)
       pdf.cell(0, 5,"           Veuillez agreer, M/Mme, l'expression de mes salutations distinguees.")
       pdf.ln(25)
       pdf.cell(0, 5,"                                                                                 Signature")
       pdf.ln(5)
       pdf.image("Moahmed-Ghalem-signature.png", x=100, w=20, h=15)
       pdf.output(nru)

if pol_inter == []  and pol_inside ==[] :
       pdf=FPDF('P','mm','A4')
       pdf.add_page()
       pdf.image("logo_ehtp.png",45,17,130,32)
       pdf.set_font('arial','', 12)
       pdf.set_text_color(170,0,0)
       var= "                                                                                                             "+str(Date_NRU)
       pdf.ln(45)
       pdf.cell(0, 5, var )
       pdf.set_font('arial','', 12)
       pdf.set_text_color(0,0,0)
       pdf.ln(10)
       pdf.cell(0, 5, '                                                                                    A' )
       pdf.ln(8)
       pdf.cell(0, 5, '                                                              M/Mme '+Nom_du_demandeur)
       pdf.ln(15)
       pdf.cell(0, 5,"          Objet : Note de renseignements urbanistiques indicative relative a votre demande N")
       pdf.ln(5)
       pdf.cell(0, 5,"          "+Numero_du_demandeur)
#        pdf.ln(15)
#        # pdf.cell(0, 5,"           khawya da3wa")
#        # pdf.ln(5)
#        # pdf.cell(0, 5,"           waloo")
       pdf.ln(5)
       pdf.cell(0, 5,"          Votre Teritoire n'intersecte avec aucune Zone ")
       pdf.ln(5)
       pdf.ln(10)
       pdf.cell(0, 5,"            De meme, vous trouverez ci-joint une image de votre teritoire ")
       pdf.ln(5)
       pdf.image("map.png",w=100, h=80)
       pdf.ln(5)
       pdf.cell(0, 5,"           Veuillez agreer, M/Mme, lexpression de mes salutations distinguees.")
       pdf.ln(25)
       pdf.cell(0, 5,"                                                                                 Signature")
       pdf.ln(5)
       pdf.image("Moahmed-Ghalem-signature.png", x=100, w=20, h=15)
       pdf.output(nru)

# st.download_button(
#      label="Download PDF",
#      data=pdf,
#      file_name='nru.pdf',
#      mime='text/pdf',
#  )

with open(nru, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    
    st.download_button(label="Telecharger Votre Nru",
                    data=PDFbyte,
                    file_name="rapportNRU.pdf",
                    mime='application/octet-stream')







# [[   "x1",  "y1"],[  "x2",  "y2"],[  "x3",  "x2"]]
