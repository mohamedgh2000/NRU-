import streamlit as st
import os
import datetime
from sympy import Point, Polygon
from fpdf import FPDF
import matplotlib.pyplot as plt
import time
from io import StringIO

def_val='-5.5222321,33.8290698/-5.5175972,33.8289985/-5.5171823,33.8219555/-5.5242348,33.8200242/-5.5222178,33.829252'
def_path='C:\\Users\\Dell\\Desktop\\testnru'
with st.form("my_form"):
     
    Date_NRU = st.date_input('date nru', datetime.date(2022, 6, 1))
    Nom_du_demandeur= st.text_input('Nom_du_demandeur', '')
    Numero_du_demandeur= st.text_input('Numero_du_demandeur', '')
    Cordinates_list= st.text_input('Cordinates_list as tuples', def_val)
    Cordinates_File= st.file_uploader("upload you Cordinates ile")

    
    path_bd= st.text_input('path_bd', 'C:\\Users\\Dell\\Desktop\\testnru')
    nru= st.text_input('nru', 'C:\\Users\\Dell\\Desktop\\testnru\\rapportNRU.pdf')

    submitted = st.form_submit_button("Submit")
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

j=0
for i in ls:
    j=j+1
    globals()[f"P{j}"] = Point(i)





p5, p6, p7, p8, p9 = map(Point, [(-72.2796643, 42.9264951),(-72.2795999, 42.9259219),(-72.2785485, 42.9260633),(-72.2787255, 42.9265618),(-72.2796643, 42.9264912)])
#point de polygon zone indus
p13,p14,p15,p16,p17,p18,p19,p20,p21,p22=map(Point,[(-5.5280113,33.828355),(-5.5255222,33.8287113),(-5.5186343,33.8278205),(-5.5156088,33.82864),(-5.5148792,33.824881),(-5.5281758,33.8208897),(-5.5280614,33.8229624),(-5.527997,33.825314),(-5.5280185,33.8265967),(-5.5280399,33.8284317)])
#point de cote de route
p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41=map(Point,[(-5.5148506,33.8248556),(-5.5182409,33.823751),(-5.5172968,33.819297),(-5.5198717,33.8184418),(-5.5169535,33.8125383),(-5.5120611,33.8061235),(-5.5140352,33.8048405),(-5.5128765,33.800528),(-5.5108166,33.7970708),(-5.5094433,33.7982113),(-5.5085421,33.7995657),(-5.5024481,33.7987816),(-5.5018902,33.8004568),(-5.5069113,33.8079767),(-5.5085421,33.8112554),(-5.5123615,33.8181448),(-5.5125189,33.8208173),(-5.5138063,33.8226702),(-5.5148792,33.8248794)])
#point de cote droite de route 
p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60, p61, p62, p63, p64, p65, p66, p67, p68, p69, p70, p71, p72, p73, p74, p75, p76, p77, p78, p79, p80, p81=map(Point,[(-5.5131483,33.8228399),(-5.5127621,33.822733),(-5.5098653,33.8237485),(-5.5093718,33.8237307),(-5.5093503,33.8231606),(-5.5083847,33.8235882),(-5.5078268,33.8228043),(-5.505352,33.8235406),(-5.5048585,33.8229705),(-5.5044508,33.8227567),(-5.5040002,33.8219194),(-5.5023408,33.8174712),(-5.5012751,33.8136939),(-5.5008888,33.8123754),(-5.4996872,33.8113063),(-5.4981208,33.8103084),(-5.4973841,33.8093819),(-5.4974484,33.8085622),(-5.4958391,33.8053191),(-5.4936361,33.803745),(-5.4930496,33.8029193),(-5.4988861,33.8018323),(-5.4999161,33.8012086),(-5.4998088,33.8002107),(-5.500946,33.8007453),(-5.5011177,33.801066),(-5.5015254,33.8012086),(-5.5043507,33.8046538),(-5.5051231,33.8057943),(-5.5065107,33.8081464),(-5.5077553,33.8111578),(-5.5081201,33.8119418),(-5.5099082,33.815048),(-5.51126,33.8172455),(-5.5117321,33.8181185),(-5.5120182,33.8197458),(-5.5121899,33.8209395),(-5.5124331,33.821569),(-5.5131626,33.8228696)])
#test
p10,p11,p12 = map(Point, [(1,1),(2,2),(3,3)])

poly1 = Polygon(P1,P2,P3,P4)
poly2 = Polygon(p5, p6, p7, p8, p9)
poly3 = Polygon(p10,p11,p12)
poly4 = Polygon(p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41)
poly5 = Polygon(p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60, p61, p62, p63, p64, p65, p66, p67, p68, p69, p70, p71, p72, p73, p74, p75, p76, p77, p78, p79, p80, p81)
zone_indus = Polygon(p13,p14,p15,p16,p17,p18,p19,p20,p21,p22)
isIntersection = poly1.intersection(poly2)
pol_inter=[]
if poly1.intersection(poly2) != []:
      pol_inter.append("poly2")
if poly1.intersection(poly3) != []:
      pol_inter.append("poly3")
if poly1.intersection(poly4) != []:
      pol_inter.append("poly4")
if poly1.intersection(poly5) != []:
      pol_inter.append("poly5")
if poly1.intersection(zone_indus) != []:
      pol_inter.append("zone_indus")



coord = ls
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.figure()

plt.plot(xs,ys) 

plt.savefig('C:\\Users\\Dell\\Desktop\\testnru\\map.png')
if pol_inter !=[]:
       pdf=FPDF('P','mm','A4')
       pdf.add_page()
       #pdf.image(os.path.join(path_bd,"logo_ehtp.png"),45,17,130,32)
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
       pdf.ln(15)
       pdf.cell(0, 5,"          ")
       pdf.ln(5)
       pdf.cell(0, 5,"           ")
       pdf.ln(5)
       pdf.cell(0, 5,"           Votre teritoire a intersecter avec les polygon suivant  "+str(pol_inter))
       pdf.ln(5)
       # pdf.cell(0, 5,"           est affecte comme suit:")
       # pdf.ln(5)
       # pdf.cell(0, 5,"                  - Situe en zone :")
       pdf.ln(5)
       
       pdf.ln(10)
       pdf.cell(0, 5,"            De meme, vous trouverez ci-joint une image de votre teritoire ")
       pdf.ln(5)
       #pdf.image(os.path.join(path_bd,"map.png"),w=160, h=120)
       pdf.ln(5)
       pdf.cell(0, 5,"           Veuillez agreer, M/Mme, l'expression de mes salutations distinguees.")
       pdf.ln(25)
       pdf.cell(0, 5,"                                                                                 Signature")
       pdf.ln(5)
       #pdf.image(os.path.join(path_bd,"Moahmed-Ghalem-signature.png"), x=100, w=20, h=15)
       pdf.output(nru)

if pol_inter == []:
       pdf=FPDF('P','mm','A4')
       pdf.add_page()
       #pdf.image(os.path.join(path_bd,"logo_ehtp.png"),45,17,130,32)
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
       pdf.ln(15)
       # pdf.cell(0, 5,"           khawya da3wa")
       # pdf.ln(5)
       # pdf.cell(0, 5,"           waloo")
       pdf.ln(5)
       pdf.cell(0, 5,"          s'intersecte avec rien ")
       pdf.ln(5)
       pdf.ln(10)
       pdf.cell(0, 5,"            De meme, vous trouverez ci-joint une image de votre teritoire ")
       pdf.ln(5)
       #pdf.image(os.path.join(path_bd,"map.png"),w=160, h=120)
       pdf.ln(5)
       pdf.cell(0, 5,"           Veuillez agreer, M/Mme, lexpression de mes salutations distinguees.")
       pdf.ln(25)
       pdf.cell(0, 5,"                                                                                 Signature")
       pdf.ln(5)
       #pdf.image(os.path.join(path_bd,"Moahmed-Ghalem-signature.png"), x=100, w=20, h=15)
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
